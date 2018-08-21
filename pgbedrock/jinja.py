import subprocess
import os

def do_pass(value):
    pass_path = os.environ.get('PASS_PATH', '/usr/local/bin/pass')

    result = subprocess.run([pass_path, value], check=True, stdout=subprocess.PIPE)
    return result.stdout.decode('utf8')


def add_filters(env):
    env.filters['pass'] = do_pass
    return env
