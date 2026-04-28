# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class Album(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        base_face_file: main_models.File = None,
        base_face_group_id: str = None,
        cover_file: main_models.File = None,
        created_at: str = None,
        description: str = None,
        file_count: int = None,
        name: str = None,
        owner: str = None,
        updated_at: str = None,
        user_tags: Dict[str, str] = None,
    ):
        self.album_id = album_id
        self.base_face_file = base_face_file
        self.base_face_group_id = base_face_group_id
        self.cover_file = cover_file
        self.created_at = created_at
        self.description = description
        self.file_count = file_count
        self.name = name
        self.owner = owner
        self.updated_at = updated_at
        self.user_tags = user_tags

    def validate(self):
        if self.base_face_file:
            self.base_face_file.validate()
        if self.cover_file:
            self.cover_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_id is not None:
            result['album_id'] = self.album_id

        if self.base_face_file is not None:
            result['base_face_file'] = self.base_face_file.to_map()

        if self.base_face_group_id is not None:
            result['base_face_group_id'] = self.base_face_group_id

        if self.cover_file is not None:
            result['cover_file'] = self.cover_file.to_map()

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.file_count is not None:
            result['file_count'] = self.file_count

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.user_tags is not None:
            result['user_tags'] = self.user_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('album_id') is not None:
            self.album_id = m.get('album_id')

        if m.get('base_face_file') is not None:
            temp_model = main_models.File()
            self.base_face_file = temp_model.from_map(m.get('base_face_file'))

        if m.get('base_face_group_id') is not None:
            self.base_face_group_id = m.get('base_face_group_id')

        if m.get('cover_file') is not None:
            temp_model = main_models.File()
            self.cover_file = temp_model.from_map(m.get('cover_file'))

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('file_count') is not None:
            self.file_count = m.get('file_count')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')

        return self

