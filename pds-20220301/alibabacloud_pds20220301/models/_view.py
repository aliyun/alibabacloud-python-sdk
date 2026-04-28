# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class View(DaraModel):
    def __init__(
        self,
        category: str = None,
        created_at: str = None,
        description: str = None,
        ex_fields_info: Dict[str, Any] = None,
        file_count: int = None,
        name: str = None,
        owner: str = None,
        updated_at: str = None,
        view_id: str = None,
    ):
        self.category = category
        self.created_at = created_at
        self.description = description
        self.ex_fields_info = ex_fields_info
        self.file_count = file_count
        self.name = name
        self.owner = owner
        self.updated_at = updated_at
        self.view_id = view_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.ex_fields_info is not None:
            result['ex_fields_info'] = self.ex_fields_info

        if self.file_count is not None:
            result['file_count'] = self.file_count

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.view_id is not None:
            result['view_id'] = self.view_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('ex_fields_info') is not None:
            self.ex_fields_info = m.get('ex_fields_info')

        if m.get('file_count') is not None:
            self.file_count = m.get('file_count')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('view_id') is not None:
            self.view_id = m.get('view_id')

        return self

