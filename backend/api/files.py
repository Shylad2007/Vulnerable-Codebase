from pathlib import Path

ALLOWED_LOG_ROOT = Path('/var/log/app').resolve()

def read_log_file(filename: str):
    # Resolve the requested path and confirm it stays within the allowed root
    safe_path = (ALLOWED_LOG_ROOT / Path(filename).name).resolve()
    if not str(safe_path).startswith(str(ALLOWED_LOG_ROOT)):
        raise PermissionError('Path traversal attempt blocked.')
    with open(safe_path, 'r') as f:
        return f.read()