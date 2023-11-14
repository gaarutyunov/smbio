def test_agnostic_path():
    from smbio import Path
    from pathlib import Path as pathlib_Path

    assert Path("C:\\Windows\\System32") == Path("C:/Windows/System32")
    assert Path("/usr/local/bin") == pathlib_Path("/usr/local/bin")
