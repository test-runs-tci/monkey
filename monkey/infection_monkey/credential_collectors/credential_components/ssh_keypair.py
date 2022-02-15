from ..credential_type import CredentialType
from .i_credential_component import ICredentialComponent


class SSHKeypair(ICredentialComponent):
    def __init__(self, content: dict):
        super().__init__(type=CredentialType.SSH_KEYPAIR)
        self.content = content
