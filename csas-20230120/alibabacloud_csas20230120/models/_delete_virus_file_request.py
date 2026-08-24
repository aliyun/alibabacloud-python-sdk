# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVirusFileRequest(DaraModel):
    def __init__(
        self,
        dev_tag: str = None,
        file_md_5: str = None,
        file_path: str = None,
    ):
        # The unique identifier of the user\\"s endpoint device where the virus file is located. The value can be up to 64 characters in length. You can obtain the value from the following operation:
        # - [ListVirusFileStatuses](~~ListVirusFileStatuses~~): lists virus file statuses.
        # 
        # This parameter is required.
        self.dev_tag = dev_tag
        # The MD5 value of the virus file. The value must be a 32-character hexadecimal string. You can obtain the value from the following operation:
        # - [ListVirusFileStatuses](~~ListVirusFileStatuses~~): lists virus file statuses.
        # 
        # This parameter is required.
        self.file_md_5 = file_md_5
        # The full path of the virus file on the user\\"s endpoint device. Only records with a handling action of Fail can be deleted. You can obtain the value from the following operation:
        # - [ListVirusFileStatuses](~~ListVirusFileStatuses~~): lists virus file statuses.
        # 
        # This parameter is required.
        self.file_path = file_path

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        return self

