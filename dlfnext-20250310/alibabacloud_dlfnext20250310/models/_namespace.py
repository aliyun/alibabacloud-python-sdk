# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import Dict


class Namespace(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        location: str = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.location = location
        self.name = name
        self.options = options
        self.owner = owner
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.id is not None:
            result['id'] = self.id

        if self.location is not None:
            result['location'] = self.location

        if self.name is not None:
            result['name'] = self.name

        if self.options is not None:
            result['options'] = self.options

        if self.owner is not None:
            result['owner'] = self.owner

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

