# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMaterialDirectoryRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        directory_id: str = None,
    ):
        self.biz_id = biz_id
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        return self

