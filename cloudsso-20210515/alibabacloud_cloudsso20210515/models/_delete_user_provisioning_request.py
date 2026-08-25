# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserProvisioningRequest(DaraModel):
    def __init__(
        self,
        deletion_strategy: str = None,
        directory_id: str = None,
        user_provisioning_id: str = None,
    ):
        # The deletion policy. The policy is used to manage synchronized users when you delete the RAM user provisioning. Valid values:
        # 
        # - Delete: When you delete the RAM user provisioning, the system deletes the synchronized users.
        # 
        # - Keep: When you delete the RAM user provisioning, the system retains the synchronized users.
        # 
        # > If you do not specify this parameter, the deletion policy that is configured when you create the RAM user provisioning is used.
        self.deletion_strategy = deletion_strategy
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The ID of the RAM user provisioning.
        self.user_provisioning_id = user_provisioning_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_strategy is not None:
            result['DeletionStrategy'] = self.deletion_strategy

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionStrategy') is not None:
            self.deletion_strategy = m.get('DeletionStrategy')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')

        return self

