import urllib.request
import urllib.error

def check_pypi_name(name: str) -> bool:
    """Return True if the name is available on PyPI."""
    url = f"https://pypi.org/pypi/{name}/json"
    try:
        urllib.request.urlopen(url, timeout=10)
        return False  # 200 OK means the name is taken
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return True  # 404 means available
        return False
    except Exception:
        return False  # Network error, assume taken to be safe
