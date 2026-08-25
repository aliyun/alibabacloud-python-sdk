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
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The new deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # - Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # 
        # - Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        self.new_deletion_strategy = new_deletion_strategy
        # The new description of the RAM user provisioning.
        self.new_description = new_description
        # The new conflict handling policy. The policy is used when a RAM user has the same username as the CloudSSO user who is synchronized to RAM. Valid values:
        # 
        # - KeepBoth: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system creates a RAM user whose username is the username of the CloudSSO user plus the suffix `_sso`.
        # 
        # - TakeOver: When a CloudSSO user is synchronized to RAM, if a RAM user who has the same username as the CloudSSO user exists, the system replaces the RAM user with the CloudSSO user.
        self.new_duplication_strategy = new_duplication_strategy
        # The ID of the RAM user provisioning.
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

