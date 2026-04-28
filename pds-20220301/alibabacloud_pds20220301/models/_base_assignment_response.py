# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseAssignmentResponse(DaraModel):
    def __init__(
        self,
        associated_role_tag_id: str = None,
        created_at: str = None,
        creator: str = None,
        disinherit_sub_group: bool = None,
        domain_id: str = None,
        identity: main_models.Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
        updated_at: str = None,
    ):
        self.associated_role_tag_id = associated_role_tag_id
        self.created_at = created_at
        self.creator = creator
        self.disinherit_sub_group = disinherit_sub_group
        self.domain_id = domain_id
        self.identity = identity
        self.manage_resource_id = manage_resource_id
        self.manage_resource_type = manage_resource_type
        self.role_id = role_id
        self.updated_at = updated_at

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_role_tag_id is not None:
            result['associated_role_tag_id'] = self.associated_role_tag_id

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id

        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type

        if self.role_id is not None:
            result['role_id'] = self.role_id

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('associated_role_tag_id') is not None:
            self.associated_role_tag_id = m.get('associated_role_tag_id')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')

        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

