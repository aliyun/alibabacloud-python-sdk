# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVirusFileStatusRequest(DaraModel):
    def __init__(
        self,
        dev_tag: str = None,
        file_md_5: str = None,
        file_path: str = None,
        operation: str = None,
        virus_type: str = None,
    ):
        # The unique identifier of the user terminal device where the virus file is located. The value can be up to 64 characters in length. You can obtain the value from the following operation:
        # - [ListVirusFileStatuses](~~ListVirusFileStatuses~~): lists virus file statuses.
        # 
        # This parameter is required.
        self.dev_tag = dev_tag
        # The MD5 value of the virus file. The value must be a 32-character hexadecimal string. You can obtain the value from the following operation:
        # - [ListVirusFileStatuses](~~ListVirusFileStatuses~~): lists virus file statuses.
        # 
        # This parameter is required.
        self.file_md_5 = file_md_5
        # The absolute path of the virus file on the user terminal device. You can obtain the value from the following operation:
        # - [ListVirusFileStatuses](~~ListVirusFileStatuses~~): lists virus file statuses.
        # 
        # This parameter is required.
        self.file_path = file_path
        # The disposal action. Valid values:
        # - **AdminQuarantine**: quarantines the virus file. The server creates a disposal task and returns a TaskId. The user terminal device pulls and executes the quarantine.
        # - **AdminTrust**: trusts the virus file. Only the disposal status is updated. No disposal task is created, and TaskId returns an empty string.
        # 
        # This parameter is required.
        self.operation = operation
        # The virus type. This parameter is used for synchronization to update the virus type of the file. Valid values:
        # - **Backdoor**: backdoor program.
        # - **DDoS**: DDoS Trojan.
        # - **Downloader**: downloader Trojan.
        # - **Engtest**: DPI engine test program.
        # - **Hacktool**: hacker tool.
        # - **Trojan**: self-mutating Trojan.
        # - **Malbaseware**: contaminated base software.
        # - **MalScript**: malicious script.
        # - **Malware**: malicious program.
        # - **Miner**: mining programs.
        # - **Proxytool**: proxy tool.
        # - **RansomWare**: ransomware.
        # - **RiskWare**: riskware.
        # - **Rootkit**: kernel-hidden program.
        # - **Stealer**: credential stealer.
        # - **Scanner**: scanner.
        # - **Suspicious**: suspicious program.
        # - **Virus**: file-infecting virus.
        # - **WebShell**: webshell.
        # - **Worm**: worms.
        # - **BlackList**: file that hit a blacklist entry.
        # - **Exp**: vulnerability exploits program.
        # - **Patcher**: cracking program.
        # - **Gametool**: private server tool.
        # - **AdWare**: adware.
        # - **Maldoc**: malicious document.
        self.virus_type = virus_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.virus_type is not None:
            result['VirusType'] = self.virus_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('VirusType') is not None:
            self.virus_type = m.get('VirusType')

        return self

