# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeExtensionsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database_name: str = None,
        extensions: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Database name.
        self.database_name = database_name
        # The extensions that you want to update. Separate multiple extensions with commas (,).
        # 
        # This parameter is required.
        self.extensions = extensions
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.extensions is not None:
            result['Extensions'] = self.extensions

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

