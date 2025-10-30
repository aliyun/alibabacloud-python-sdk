# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteExtensionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbnames: str = None,
        extension: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        # 
        # This parameter is required.
        self.dbnames = dbnames
        # The name of the extension.
        # 
        # This parameter is required.
        self.extension = extension
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

        if self.dbnames is not None:
            result['DBNames'] = self.dbnames

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBNames') is not None:
            self.dbnames = m.get('DBNames')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

