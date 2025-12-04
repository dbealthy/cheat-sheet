``` python
def _module_path_from_path(path: str, root: str | None = None) -> str:

	module_path = pathlib.Path(path)
	if root:
		module_path = module_path.relative_to(root)
	return ".".join(module_path.with_suffix("").parts)

  
  

def _load_module_from_path(module_path: str, root=None):

	module_name = _module_path_from_path(module_path, root)

	spec = importlib.util.spec_from_file_location(module_name, module_path)

	module = importlib.util.module_from_spec(spec)

	sys.modules[module_name] = module

	spec.loader.exec_module(module)

	return module
```