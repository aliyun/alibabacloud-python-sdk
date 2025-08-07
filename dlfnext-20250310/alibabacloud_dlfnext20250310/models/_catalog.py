# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import Dict


class Catalog(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        is_shared: bool = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        share_id: str = None,
        status: str = None,
        type: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.is_shared = is_shared
        self.name = name
        self.options = options
        self.owner = owner
        self.share_id = share_id
        self.status = status
        self.type = type
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

        if self.is_shared is not None:
            result['isShared'] = self.is_shared

        if self.name is not None:
            result['name'] = self.name

        if self.options is not None:
            result['options'] = self.options

        if self.owner is not None:
            result['owner'] = self.owner

        if self.share_id is not None:
            result['shareId'] = self.share_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

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

        if m.get('isShared') is not None:
            self.is_shared = m.get('isShared')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('shareId') is not None:
            self.share_id = m.get('shareId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

