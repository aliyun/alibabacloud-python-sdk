# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class RunSynchronizationJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        password_initialization: bool = None,
        synchronization_scope_config: main_models.RunSynchronizationJobRequestSynchronizationScopeConfig = None,
        target_id: str = None,
        target_type: str = None,
        user_identity_types: List[str] = None,
    ):
        # Synchronization task description
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Whether initialize password
        self.password_initialization = password_initialization
        # Synchronization scope
        self.synchronization_scope_config = synchronization_scope_config
        # The ID of the synchronization destination.
        # 
        # This parameter is required.
        self.target_id = target_id
        # The type of the synchronization destination. Valid values:
        # 
        # *   identity_provider
        # *   application
        # 
        # This parameter is required.
        self.target_type = target_type
        # User identity types
        self.user_identity_types = user_identity_types

    def validate(self):
        if self.synchronization_scope_config:
            self.synchronization_scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password_initialization is not None:
            result['PasswordInitialization'] = self.password_initialization

        if self.synchronization_scope_config is not None:
            result['SynchronizationScopeConfig'] = self.synchronization_scope_config.to_map()

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.user_identity_types is not None:
            result['UserIdentityTypes'] = self.user_identity_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PasswordInitialization') is not None:
            self.password_initialization = m.get('PasswordInitialization')

        if m.get('SynchronizationScopeConfig') is not None:
            temp_model = main_models.RunSynchronizationJobRequestSynchronizationScopeConfig()
            self.synchronization_scope_config = temp_model.from_map(m.get('SynchronizationScopeConfig'))

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('UserIdentityTypes') is not None:
            self.user_identity_types = m.get('UserIdentityTypes')

        return self

class RunSynchronizationJobRequestSynchronizationScopeConfig(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        organizational_unit_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The group IDs.
        self.group_ids = group_ids
        # The IDs of organizational units.
        self.organizational_unit_ids = organizational_unit_ids
        # UserIds
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.organizational_unit_ids is not None:
            result['OrganizationalUnitIds'] = self.organizational_unit_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('OrganizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('OrganizationalUnitIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

