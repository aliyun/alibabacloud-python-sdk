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
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # - Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # 
        # - Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.deletion_strategy = deletion_strategy
        # The description.
        self.description = description
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # - KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # 
        # - TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.duplication_strategy = duplication_strategy
        # The identity ID of the RAM user provisioning. Valid values:
        # 
        # - If you set the `PrincipalType` parameter to `Group`, the value of this parameter is the ID of a CloudSSO user group (g-\\*\\*\\*\\*\\*\\*\\*\\*).
        # 
        # - If you set the `PrincipalType` parameter to `User`, the value of this parameter is the ID of a CloudSSO user (u-\\*\\*\\*\\*\\*\\*\\*\\*).
        self.principal_id = principal_id
        # The identity type of the RAM user provisioning. Valid values:
        # 
        # - User: The identity of the RAM user provisioning is a CloudSSO user.
        # 
        # - Group: The identity of the RAM user provisioning is a CloudSSO user group.
        self.principal_type = principal_type
        # The ID of the object for which you create the RAM user provisioning. The value is fixed as the ID of the member in the resource directory.
        self.target_id = target_id
        # The object for which you create the RAM user provisioning. The value is fixed as `RD-Account`.
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

