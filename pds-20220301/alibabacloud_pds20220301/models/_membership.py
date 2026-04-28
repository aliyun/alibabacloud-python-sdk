# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Membership(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        updated_at: int = None,
        user_id: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.domain_id = domain_id
        self.group_id = group_id
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        self.updated_at = updated_at
        self.user_id = user_id

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

        if self.member_role is not None:
            result['member_role'] = self.member_role

        if self.member_type is not None:
            result['member_type'] = self.member_type

        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.user_id is not None:
            result['user_id'] = self.user_id

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

        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')

        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')

        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

