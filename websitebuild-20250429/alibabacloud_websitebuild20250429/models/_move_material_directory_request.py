# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveMaterialDirectoryRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        directory_id: str = None,
        parent_directory_id: str = None,
        sort_num: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.directory_id = directory_id
        # This parameter is required.
        self.parent_directory_id = parent_directory_id
        # This parameter is required.
        self.sort_num = sort_num

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

        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id

        if self.sort_num is not None:
            result['SortNum'] = self.sort_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')

        if m.get('SortNum') is not None:
            self.sort_num = m.get('SortNum')

        return self

