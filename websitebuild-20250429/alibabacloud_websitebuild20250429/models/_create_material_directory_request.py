# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMaterialDirectoryRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        name: str = None,
        parent_directory_id: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.parent_directory_id = parent_directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')

        return self

