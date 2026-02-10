# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateBatchUploadUrlRequest(DaraModel):
    def __init__(
        self,
        md_5list: List[str] = None,
        type: int = None,
    ):
        # The identifiers of files. Only MD5 hash values are supported.
        # 
        # This parameter is required.
        self.md_5list = md_5list
        # The type of the file. Valid values:
        # 
        # *   **0**: unknown file
        # *   **1**: binary file
        # *   **2**: webshell file
        # *   **4**: script file
        # 
        # > If you do not know the type of the file, set this parameter to **0**.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.md_5list is not None:
            result['Md5List'] = self.md_5list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5List') is not None:
            self.md_5list = m.get('Md5List')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

