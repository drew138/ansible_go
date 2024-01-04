def test_go_folder_exists(host):
    assert host.file("/usr/local/go").is_directory


def test_go_bin_exists(host):
    assert host.file("/usr/local/go/bin/go").exists
