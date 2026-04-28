# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class Permission(DaraModel):
    def __init__(
        self,
        action_list: List[main_models.PermissionActionList] = None,
        collection: str = None,
        condition: main_models.PermissionCondition = None,
        created_at: int = None,
        effect: str = None,
        identity_id: str = None,
        identity_type: str = None,
        resource: str = None,
        resource_type: str = None,
        updated_at: int = None,
        user_tags: List[str] = None,
    ):
        # Action list.
        self.action_list = action_list
        # The permission set. Set this parameter to global for global permissions. In other scenarios, this parameter is empty by default.
        self.collection = collection
        # Condition
        self.condition = condition
        # The creation time in the millisecond timestamp format.
        self.created_at = created_at
        # Effect. Valid values: allow, deny.
        self.effect = effect
        # Identity ID.
        self.identity_id = identity_id
        # Identity type. Valid values: IT_User, IT_Group, IT_Role.
        self.identity_type = identity_type
        # The ID of the resource.
        self.resource = resource
        # The type of the resource. The file type resource is RT_File.
        self.resource_type = resource_type
        # The time when the modification was made. The value is a millisecond timestamp.
        self.updated_at = updated_at
        # Custom tag.
        self.user_tags = user_tags

    def validate(self):
        if self.action_list:
            for v1 in self.action_list:
                 if v1:
                    v1.validate()
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['action_list'] = []
        if self.action_list is not None:
            for k1 in self.action_list:
                result['action_list'].append(k1.to_map() if k1 else None)

        if self.collection is not None:
            result['collection'] = self.collection

        if self.condition is not None:
            result['condition'] = self.condition.to_map()

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.effect is not None:
            result['effect'] = self.effect

        if self.identity_id is not None:
            result['identity_id'] = self.identity_id

        if self.identity_type is not None:
            result['identity_type'] = self.identity_type

        if self.resource is not None:
            result['resource'] = self.resource

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.user_tags is not None:
            result['user_tags'] = self.user_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_list = []
        if m.get('action_list') is not None:
            for k1 in m.get('action_list'):
                temp_model = main_models.PermissionActionList()
                self.action_list.append(temp_model.from_map(k1))

        if m.get('collection') is not None:
            self.collection = m.get('collection')

        if m.get('condition') is not None:
            temp_model = main_models.PermissionCondition()
            self.condition = temp_model.from_map(m.get('condition'))

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('effect') is not None:
            self.effect = m.get('effect')

        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')

        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')

        return self

class PermissionActionList(DaraModel):
    def __init__(
        self,
        action: str = None,
    ):
        # Specific action, such as FILE.ALL
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        return self

