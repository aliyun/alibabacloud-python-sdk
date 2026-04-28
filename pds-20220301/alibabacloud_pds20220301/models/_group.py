# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Group(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        updated_at: int = None,
    ):
        # The time when the group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The ID of the user who created the group.
        self.creator = creator
        # The description of the group.
        self.description = description
        # The ID of the domain.
        self.domain_id = domain_id
        # The ID of the group.
        self.group_id = group_id
        # The name of the group.
        self.group_name = group_name
        # The time when the group was modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.group_name is not None:
            result['group_name'] = self.group_name

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

