# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteReplicationLinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        promote_to_master: bool = None,
        resource_owner_id: int = None,
    ):
        # The ID of the DR instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to delete the data synchronization link between the DR instance and the primary instance and promote the DR instance to the primary instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.promote_to_master = promote_to_master
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.promote_to_master is not None:
            result['PromoteToMaster'] = self.promote_to_master

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('PromoteToMaster') is not None:
            self.promote_to_master = m.get('PromoteToMaster')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

