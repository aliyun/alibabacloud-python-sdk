# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableSmbAclRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        keytab: str = None,
        keytab_md_5: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The string that is generated after the system encodes the keytab file by using Base64.
        self.keytab = keytab
        # The string that is generated after the system encodes the keytab file by using MD5.
        self.keytab_md_5 = keytab_md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.keytab is not None:
            result['Keytab'] = self.keytab

        if self.keytab_md_5 is not None:
            result['KeytabMd5'] = self.keytab_md_5

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Keytab') is not None:
            self.keytab = m.get('Keytab')

        if m.get('KeytabMd5') is not None:
            self.keytab_md_5 = m.get('KeytabMd5')

        return self

