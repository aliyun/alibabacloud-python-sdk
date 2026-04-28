# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KnowledgeFile(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        file_category: str = None,
        file_created_at: int = None,
        file_creator_id: str = None,
        file_id: str = None,
        file_image_time: int = None,
        file_last_modifier_id: str = None,
        file_last_modifier_type: str = None,
        file_name: str = None,
        file_name_path: str = None,
        file_size: int = None,
        file_updated_at: int = None,
        joined_at: int = None,
        knowledge_base_id: str = None,
        knowledge_category_id: str = None,
        revision_id: str = None,
    ):
        self.creator_id = creator_id
        self.drive_id = drive_id
        self.drive_name = drive_name
        self.file_category = file_category
        self.file_created_at = file_created_at
        self.file_creator_id = file_creator_id
        self.file_id = file_id
        self.file_image_time = file_image_time
        self.file_last_modifier_id = file_last_modifier_id
        self.file_last_modifier_type = file_last_modifier_type
        self.file_name = file_name
        self.file_name_path = file_name_path
        self.file_size = file_size
        self.file_updated_at = file_updated_at
        self.joined_at = joined_at
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_category_id = knowledge_category_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.drive_name is not None:
            result['drive_name'] = self.drive_name

        if self.file_category is not None:
            result['file_category'] = self.file_category

        if self.file_created_at is not None:
            result['file_created_at'] = self.file_created_at

        if self.file_creator_id is not None:
            result['file_creator_id'] = self.file_creator_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.file_image_time is not None:
            result['file_image_time'] = self.file_image_time

        if self.file_last_modifier_id is not None:
            result['file_last_modifier_id'] = self.file_last_modifier_id

        if self.file_last_modifier_type is not None:
            result['file_last_modifier_type'] = self.file_last_modifier_type

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.file_name_path is not None:
            result['file_name_path'] = self.file_name_path

        if self.file_size is not None:
            result['file_size'] = self.file_size

        if self.file_updated_at is not None:
            result['file_updated_at'] = self.file_updated_at

        if self.joined_at is not None:
            result['joined_at'] = self.joined_at

        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id

        if self.knowledge_category_id is not None:
            result['knowledge_category_id'] = self.knowledge_category_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')

        if m.get('file_category') is not None:
            self.file_category = m.get('file_category')

        if m.get('file_created_at') is not None:
            self.file_created_at = m.get('file_created_at')

        if m.get('file_creator_id') is not None:
            self.file_creator_id = m.get('file_creator_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('file_image_time') is not None:
            self.file_image_time = m.get('file_image_time')

        if m.get('file_last_modifier_id') is not None:
            self.file_last_modifier_id = m.get('file_last_modifier_id')

        if m.get('file_last_modifier_type') is not None:
            self.file_last_modifier_type = m.get('file_last_modifier_type')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('file_name_path') is not None:
            self.file_name_path = m.get('file_name_path')

        if m.get('file_size') is not None:
            self.file_size = m.get('file_size')

        if m.get('file_updated_at') is not None:
            self.file_updated_at = m.get('file_updated_at')

        if m.get('joined_at') is not None:
            self.joined_at = m.get('joined_at')

        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')

        if m.get('knowledge_category_id') is not None:
            self.knowledge_category_id = m.get('knowledge_category_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self

