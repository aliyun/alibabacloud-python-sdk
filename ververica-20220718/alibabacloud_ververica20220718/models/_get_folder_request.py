# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFolderRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        root_type: str = None,
    ):
        self.folder_id = folder_id
        self.root_type = root_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.root_type is not None:
            result['rootType'] = self.root_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('rootType') is not None:
            self.root_type = m.get('rootType')

        return self

