# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSecretsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in the specified region.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the workspace that consists of multiple database instances. This parameter and the DBInstanceId parameter cannot both be left empty. If both parameters are specified, this parameter takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

