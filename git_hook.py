#!/usr/bin/python3
import pathlib
import platform
import urllib.request


def get_platform_data() -> dict:
    platform_data = platform.uname()
    return {"OS": platform_data.system, "CPU": platform_data.machine}


def replace_os_type(os_type: str, name:str) -> str:
    if os_type.upper() in ("WINDOWS", "WIN"):
        name = name.replace("os", "windows")
        name = f"{name}.zip"
    elif  os_type.upper() in ("LINUX", "UBUNTU", "FEDORA"):
        name = name.replace("os", "linux")
        name = f"{name}.tar.gz"
    elif os_type.upper() in ("DARWIN",):
        name = name.replace("os", "darwin")
        name = f"{name}.tar.gz"
    else:
        raise OSError("Unsupported OS type.")
    return name
    

def replace_machine_type(mch_type: str, name:str) -> str:
    if mch_type.upper() in ("AMD64", "X86_64", "INTEL64"):
        return name.replace("machine", "x64")
    elif  mch_type.upper() in ("ARM64",):
        return name.replace("machine", "arm64")
    elif mch_type.upper() in ("X86",):
        return name.replace("machine", "x32")
    else:
        raise OSError("Unsupported CPU type.")
    

def get_package_name(os_type: str, mch_type: str):
    name = "gitleaks_8.17.0_os_machine"
    name = replace_os_type(os_type=os_type, name=name)
    name = replace_machine_type(mch_type=mch_type, name=name)
    return name


def download_file(package_name: str, download_path: pathlib.Path = None) -> None:
    url = "https://github.com/gitleaks/gitleaks/releases/download/v8.17.0/" + package_name
    if download_path:
        urllib.request.urlretrieve(url, download_path)
    else:
        urllib.request.urlretrieve(url, package_name)
    

def exctrat_file(os_type: str, exctraction_path: str, file_path: str):
    if os_type in ("WINDOWS", "WIN"):
        from zipfile import ZipFile

        zip = ZipFile(file_path)
        zip.extractall(exctraction_path)
    else:
        import tarfile

        tar = tarfile.open(file_path)
        tar.extractall(exctraction_path)


def clean_up_path(path: pathlib.Path) -> None:
    for item in path.iterdir():
        if item.is_dir():
            clean_up_path(item)
        else:
            item.unlink()
    path.rmdir()

   
def get_gitleaks(clean_up: bool = False) -> str:
    platform_data = get_platform_data()
    os_type = platform_data["OS"]
    machine_type = platform_data["CPU"]
    package_name = get_package_name(os_type=os_type, mch_type=machine_type)
    file_path = pathlib.Path.home() / package_name
    exctraction_path = pathlib.Path.home() / "gitleaks"

    print(exctraction_path)

    if clean_up and exctraction_path.exists():
        clean_up_path(exctraction_path)

    download_file(package_name=package_name, download_path=file_path)
    exctrat_file(os_type, exctraction_path, file_path)
    file_path.unlink()
    return exctraction_path / "gitleaks"


if __name__ == "__main__":
    import subprocess
    import sys

    GITLEAKS_REPORT = "report.json"
    GITLEAKS_OPTS = "detect --redact -v"
    GITLEAKS_GIT_LOGS = "--since=2023-05-01"

    gitleaks_executable = get_gitleaks()
    command = f"{gitleaks_executable} {GITLEAKS_OPTS} --report-path {GITLEAKS_REPORT} --log-opts={GITLEAKS_GIT_LOGS}"
    gitleaks_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    sys.exit(gitleaks_process.returncode)
