# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteBackupFileRequest(DaraModel):
    def __init__(
        self,
        backup_file_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.backup_file_id_list = backup_file_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_file_id_list is not None:
            result['BackupFileIdList'] = self.backup_file_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupFileIdList') is not None:
            self.backup_file_id_list = m.get('BackupFileIdList')

        return self

