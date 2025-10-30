# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStreamingDataSourceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        data_source_config: str = None,
        data_source_description: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        region_id: str = None,
        service_id: int = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Data source configuration information.
        # 
        # This parameter is required.
        self.data_source_config = data_source_config
        # Data source description.
        self.data_source_description = data_source_description
        # Data source name.
        # 
        # This parameter is required.
        self.data_source_name = data_source_name
        # Data source type. Values:
        #  -  kafka
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # Region ID.
        # 
        # > You can view available region IDs through the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) interface.
        self.region_id = region_id
        # Real-time data service ID.
        # 
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_source_config is not None:
            result['DataSourceConfig'] = self.data_source_config

        if self.data_source_description is not None:
            result['DataSourceDescription'] = self.data_source_description

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceConfig') is not None:
            self.data_source_config = m.get('DataSourceConfig')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        return self

