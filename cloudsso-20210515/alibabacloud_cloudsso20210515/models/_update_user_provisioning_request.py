# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserProvisioningRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        new_deletion_strategy: str = None,
        new_description: str = None,
        new_duplication_strategy: str = None,
        user_provisioning_id: str = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The new deletion policy. This policy specifies how to handle synchronized Resource Access Management (RAM) users when the Resource Access Management (RAM) user synchronization is deleted. Valid values:
        # 
        # - Delete: Delete the users. When the Resource Access Management (RAM) user synchronization is deleted, the system deletes the Resource Access Management (RAM) users that have been synchronized from CloudSSO to Resource Access Management (RAM).
        # - Keep: Keep the users. When the Resource Access Management (RAM) user synchronization is deleted, the system retains the Resource Access Management (RAM) users that have been synchronized from CloudSSO to Resource Access Management (RAM).
        self.new_deletion_strategy = new_deletion_strategy
        # The new description of the Resource Access Management (RAM) user synchronization.
        self.new_description = new_description
        # The new duplication strategy. This strategy specifies how to handle name conflicts when a CloudSSO user is synchronized to Resource Access Management (RAM) user with the same name already exists. Valid values:
        # 
        # - KeepBoth: Keep both users. When a CloudSSO user is synchronized to Resource Access Management (RAM) user with the same name already exists, the system appends the `_sso` suffix to the CloudSSO username and attempts to create a RAM user with the new username.
        # - TakeOver: Replace the existing user. When a CloudSSO user is synchronized to Resource Access Management (RAM) user with the same name already exists, the system directly replaces the existing RAM user with the synchronized CloudSSO user.
        self.new_duplication_strategy = new_duplication_strategy
        # The ID of the Resource Access Management (RAM) user synchronization.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_deletion_strategy is not None:
            result['NewDeletionStrategy'] = self.new_deletion_strategy

        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.new_duplication_strategy is not None:
            result['NewDuplicationStrategy'] = self.new_duplication_strategy

        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewDeletionStrategy') is not None:
            self.new_deletion_strategy = m.get('NewDeletionStrategy')

        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('NewDuplicationStrategy') is not None:
            self.new_duplication_strategy = m.get('NewDuplicationStrategy')

        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')

        return self

