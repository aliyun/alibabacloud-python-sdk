# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FileDeleteUserTagsRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        key_list: List[str] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The tags that you want to remove from a file. You cannot leave this parameter empty. You can specify up to 1,000 tags.
        # 
        # This parameter is required.
        self.key_list = key_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.key_list is not None:
            result['key_list'] = self.key_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('key_list') is not None:
            self.key_list = m.get('key_list')

        return self

