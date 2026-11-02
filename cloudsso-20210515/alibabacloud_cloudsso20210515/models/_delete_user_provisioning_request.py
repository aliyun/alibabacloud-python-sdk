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
        # The deletion strategy. The processing strategy for synchronized RAM users when a RAM user synchronization is deleted. Valid values:
        # 
        # - Delete: Deletes the RAM users that have been synchronized from CloudSSO to Resource Access Management (RAM) user synchronization is deleted.
        # - Keep: Retains the RAM users that have been synchronized from CloudSSO to Resource Access Management (RAM) user synchronization is deleted.
        # 
        # > If this parameter is left empty, the deletion strategy specified when the RAM user synchronization was created is used.
        self.deletion_strategy = deletion_strategy
        # The directory ID.
        self.directory_id = directory_id
        # The ID of the Resource Access Management (RAM) user synchronization.
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

