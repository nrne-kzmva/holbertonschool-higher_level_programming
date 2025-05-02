#!/usr/bin/python3
import importlib.util
import sys
if __name__ == "__main__":
    # Fayl yolunu müəyyən et
    file_path = "/tmp/hidden_4.pyc"
    # Modulun adını təyin et
    module_name = "hidden_4"
    # Spec yarat və modul yüklə
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)
    # Moduldan bütün adları tap
    names = dir(hidden_module)
    # __ ilə BAŞLAMAYAN adları süz və çap et
    for name in sorted(name for name in names if not name.startswith("__")):
        print(name)
