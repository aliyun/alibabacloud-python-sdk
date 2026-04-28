# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FileLogDetail(DaraModel):
    def __init__(
        self,
        decompress_file_list: List[str] = None,
        new_name: str = None,
        parent_path: str = None,
        rev_version: int = None,
        revision_id: str = None,
        size: int = None,
        to_parent_path: str = None,
        to_parent_path_type: str = None,
        type: str = None,
    ):
        self.decompress_file_list = decompress_file_list
        self.new_name = new_name
        self.parent_path = parent_path
        self.rev_version = rev_version
        self.revision_id = revision_id
        self.size = size
        self.to_parent_path = to_parent_path
        self.to_parent_path_type = to_parent_path_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.decompress_file_list is not None:
            result['decompress_file_list'] = self.decompress_file_list

        if self.new_name is not None:
            result['new_name'] = self.new_name

        if self.parent_path is not None:
            result['parent_path'] = self.parent_path

        if self.rev_version is not None:
            result['rev_version'] = self.rev_version

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        if self.size is not None:
            result['size'] = self.size

        if self.to_parent_path is not None:
            result['to_parent_path'] = self.to_parent_path

        if self.to_parent_path_type is not None:
            result['to_parent_path_type'] = self.to_parent_path_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decompress_file_list') is not None:
            self.decompress_file_list = m.get('decompress_file_list')

        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')

        if m.get('parent_path') is not None:
            self.parent_path = m.get('parent_path')

        if m.get('rev_version') is not None:
            self.rev_version = m.get('rev_version')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('to_parent_path') is not None:
            self.to_parent_path = m.get('to_parent_path')

        if m.get('to_parent_path_type') is not None:
            self.to_parent_path_type = m.get('to_parent_path_type')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

