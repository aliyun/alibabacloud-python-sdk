# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRdDefaultSyncListRequest(DaraModel):
    def __init__(
        self,
        folder_ids: str = None,
    ):
        # The list of folder IDs in the resource directory.
        # 
        # > You can call [GetRdTree](~~GetRdTree~~) to obtain folder IDs. Separate multiple folder IDs with commas (,). If you do not specify this parameter, the existing configuration list is cleared.
        self.folder_ids = folder_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_ids is not None:
            result['FolderIds'] = self.folder_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderIds') is not None:
            self.folder_ids = m.get('FolderIds')

        return self

