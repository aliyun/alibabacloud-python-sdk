# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckHadoopDataSourceRequest(DaraModel):
    def __init__(
        self,
        check_dir: str = None,
        dbinstance_id: str = None,
        data_source_id: str = None,
        region_id: str = None,
    ):
        # The Hadoop path that you want to check.
        # 
        # This parameter is required.
        self.check_dir = check_dir
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_dir is not None:
            result['CheckDir'] = self.check_dir

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckDir') is not None:
            self.check_dir = m.get('CheckDir')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

