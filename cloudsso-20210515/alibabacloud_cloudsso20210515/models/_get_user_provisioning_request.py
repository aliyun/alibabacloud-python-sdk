# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserProvisioningRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        user_provisioning_id: str = None,
    ):
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
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.user_provisioning_id is not None:
            result['UserProvisioningId'] = self.user_provisioning_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('UserProvisioningId') is not None:
            self.user_provisioning_id = m.get('UserProvisioningId')

        return self

