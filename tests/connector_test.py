def test_connector():
    from smbio import Connector

    connector = Connector(r"\\localhost\IPC$")
    assert connector.server == "localhost"
    assert connector.share == "IPC$"
