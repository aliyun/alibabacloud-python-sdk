# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HotKnowledgeBaseFile(DaraModel):
    def __init__(
        self,
        action_count: int = None,
        action_list: List[str] = None,
        category: str = None,
        count_at: int = None,
        drive_id: str = None,
        file_id: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        revision_id: str = None,
    ):
        self.action_count = action_count
        self.action_list = action_list
        self.category = category
        self.count_at = count_at
        self.drive_id = drive_id
        self.file_id = file_id
        self.knowledge_base_id = knowledge_base_id
        self.name = name
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_count is not None:
            result['action_count'] = self.action_count

        if self.action_list is not None:
            result['action_list'] = self.action_list

        if self.category is not None:
            result['category'] = self.category

        if self.count_at is not None:
            result['count_at'] = self.count_at

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id

        if self.name is not None:
            result['name'] = self.name

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_count') is not None:
            self.action_count = m.get('action_count')

        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('count_at') is not None:
            self.count_at = m.get('count_at')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self

