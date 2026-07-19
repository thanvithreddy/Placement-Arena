import requests

PISTON_URL = 'https://emkc.org/api/v2/piston/execute'

LANGUAGE_MAP = {
    'python': {'language': 'python', 'version': '3.10.0'},
    'java': {'language': 'java', 'version': '15.0.2'},
    'cpp': {'language': 'c++', 'version': '10.2.0'},
    'c': {'language': 'c', 'version': '10.2.0'},
}

def execute_code(language, code, stdin='', timeout=10):
    lang_config = LANGUAGE_MAP.get(language)
    if not lang_config:
        return {'error': 'Unsupported language', 'stdout': '', 'stderr': '', 'exit_code': 1, 'status': 'runtime_error'}
    
    payload = {
        'language': lang_config['language'],
        'version': lang_config['version'],
        'files': [{'name': 'main', 'content': code}],
        'stdin': stdin,
        'args': [],
        'compile_timeout': 10000,
        'run_timeout': timeout * 1000,
        'compile_memory_limit': -1,
        'run_memory_limit': -1
    }
    
    try:
        response = requests.post(PISTON_URL, json=payload, timeout=timeout + 5)
        data = response.json()
        run = data.get('run', {})
        compile_info = data.get('compile', {})
        
        if compile_info.get('code', 0) != 0:
            return {
                'stdout': '',
                'stderr': compile_info.get('stderr', '') or compile_info.get('output', ''),
                'exit_code': compile_info.get('code', 1),
                'status': 'compilation_error'
            }
        
        return {
            'stdout': run.get('stdout', '') or run.get('output', ''),
            'stderr': run.get('stderr', ''),
            'exit_code': run.get('code', 0),
            'status': 'ok'
        }
    except requests.Timeout:
        return {'stdout': '', 'stderr': 'Time Limit Exceeded', 'exit_code': 1, 'status': 'time_limit_exceeded'}
    except Exception as e:
        return {'stdout': '', 'stderr': str(e), 'exit_code': 1, 'status': 'runtime_error'}
