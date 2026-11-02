# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserProvisioningRequest(DaraModel):
    def __init__(
        self,
        deletion_strategy: str = None,
        description: str = None,
        directory_id: str = None,
        duplication_strategy: str = None,
        principal_id: str = None,
        principal_type: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The deletion policy. Specifies the action to take for synchronized Resource Access Management (RAM) users when a Resource Access Management (RAM) user synchronization is deleted. Valid values:
        # 
        # - Delete: Delete. When a Resource Access Management (RAM) user synchronization is deleted, the system deletes the Resource Access Management (RAM) users that have been synchronized from CloudSSO to RAM.
        # - Keep: Keep. When a Resource Access Management (RAM) user synchronization is deleted, the system retains the Resource Access Management (RAM) users that have been synchronized from CloudSSO to RAM.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the directory.
        self.directory_id = directory_id
        # The conflict resolution policy. Specifies the action to take when a CloudSSO user is synchronized to Resource Access Management (RAM) user with the same name already exists. Valid values:
        # 
        # - KeepBoth: Keep both. When a CloudSSO user is synchronized to Resource Access Management (RAM) user with the same name already exists, the system adds the `_sso` suffix to the username of the CloudSSO user and attempts to create a RAM user with the suffixed username.
        # - TakeOver: Take over. When a CloudSSO user is synchronized to Resource Access Management (RAM) user with the same name already exists, the system replaces the existing RAM user with the synchronized CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The ID of the identity for the Resource Access Management (RAM) user synchronization. Valid values:
        # 
        # - When `PrincipalType` is set to `Group`, the value is the ID of the CloudSSO group (g-********).
        # - When `PrincipalType` is set to `User`, the value is the ID of the CloudSSO user (u-********).
        self.principal_id = principal_id
        # The type of the Resource Access Management (RAM) user synchronization. Valid values:
        # - User: The Resource Access Management (RAM) user synchronization is a CloudSSO user.
        # - Group: The Resource Access Management (RAM) user synchronization is a CloudSSO group.
        self.principal_type = principal_type
        # The ID of the destination for the Resource Access Management (RAM) user synchronization. Currently, the value is the ID of the account in a resource directory.
        self.target_id = target_id
        # The type of the destination for the Resource Access Management (RAM) user synchronization. Currently, the only valid value is `RD-Account`.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.duplication_strategy is not None:
            result['DuplicationStrategy'] = self.duplication_strategy

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DuplicationStrategy') is not None:
            self.duplication_strategy = m.get('DuplicationStrategy')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

