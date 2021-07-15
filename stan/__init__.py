from stan.model import build  # noqa

try:
    from importlib.metadata import version

    __version__ = version("pystan")
except ModuleNotFoundError:
    pass

try:
    ipython_shell = get_ipython().__class__.__name__
    if ipython_shell == 'ZMQInteractiveShell':
        import nest_asyncio
        nest_asyncio.apply()
except NameError:
    pass
