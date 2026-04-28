# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class UncompressedFileInfo(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        is_folder: bool = None,
        items: List[main_models.UncompressedFileInfo] = None,
        name: str = None,
        size: int = None,
        updated_at: int = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id
        # Whether it is a folder.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.is_folder = is_folder
        # Subfiles
        self.items = items
        # The name of the file.
        self.name = name
        # The size of the file.
        self.size = size
        # Update time.
        self.updated_at = updated_at

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.is_folder is not None:
            result['is_folder'] = self.is_folder

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.size is not None:
            result['size'] = self.size

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('is_folder') is not None:
            self.is_folder = m.get('is_folder')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UncompressedFileInfo()
                self.items.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

