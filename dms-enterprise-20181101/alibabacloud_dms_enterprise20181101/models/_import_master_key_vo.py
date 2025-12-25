# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ImportMasterKeyVO(DaraModel):
    def __init__(
        self,
        encrypt_mek_data_base_64: str = None,
        mek_id: int = None,
        project_id: List[int] = None,
    ):
        self.encrypt_mek_data_base_64 = encrypt_mek_data_base_64
        self.mek_id = mek_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_mek_data_base_64 is not None:
            result['EncryptMekDataBase64'] = self.encrypt_mek_data_base_64

        if self.mek_id is not None:
            result['MekId'] = self.mek_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptMekDataBase64') is not None:
            self.encrypt_mek_data_base_64 = m.get('EncryptMekDataBase64')

        if m.get('MekId') is not None:
            self.mek_id = m.get('MekId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

