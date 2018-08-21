def do_pass(value):
    return 'PASS SUBSTITUTION'


def add_filters(env):
    env.filters['pass'] = do_pass
    return env
