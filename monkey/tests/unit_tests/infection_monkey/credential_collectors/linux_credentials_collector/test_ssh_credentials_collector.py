import pytest

from infection_monkey.credential_collectors import SSHKeypair, Username
from infection_monkey.credential_collectors.ssh_collector import SSHCredentialCollector
from infection_monkey.i_puppet.credential_collection import Credentials


def patch_ssh_handler(ssh_creds, monkeypatch):
    monkeypatch.setattr(
        "infection_monkey.credential_collectors.ssh_collector.ssh_handler.get_ssh_info",
        lambda: ssh_creds,
    )


@pytest.mark.parametrize(
    "ssh_creds", [([{"name": "", "home_dir": "", "public_key": None, "private_key": None}]), ([])]
)
def test_ssh_credentials_empty_results(monkeypatch, ssh_creds):
    patch_ssh_handler(ssh_creds, monkeypatch)
    collected = SSHCredentialCollector().collect_credentials()
    assert not collected


def test_ssh_info_result_parsing(monkeypatch):

    ssh_creds = [
        {
            "name": "ubuntu",
            "home_dir": "/home/ubuntu",
            "public_key": "SomePublicKeyUbuntu",
            "private_key": "ExtremelyGoodPrivateKey",
        },
        {
            "name": "mcus",
            "home_dir": "/home/mcus",
            "public_key": "AnotherPublicKey",
            "private_key": None,
        },
        {"name": "guest", "home_dir": "/", "public_key": None, "private_key": None},
    ]
    patch_ssh_handler(ssh_creds, monkeypatch)

    # Expected credentials
    username = Username("ubuntu")
    username2 = Username("mcus")
    username3 = Username("guest")

    ssh_keypair1 = SSHKeypair(
        {"public_key": "SomePublicKeyUbuntu", "private_key": "ExtremelyGoodPrivateKey"}
    )
    ssh_keypair2 = SSHKeypair({"public_key": "AnotherPublicKey"})

    expected = [
        Credentials(identities=[username], secrets=[ssh_keypair1]),
        Credentials(identities=[username2], secrets=[ssh_keypair2]),
        Credentials(identities=[username3], secrets=[]),
    ]
    collected = SSHCredentialCollector().collect_credentials()
    assert expected == collected
