# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataSourceParametersRequest(DaraModel):
    def __init__(
        self,
        cloud_code: str = None,
        data_source_type: str = None,
        region_id: str = None,
    ):
        # The code for the multicloud environment.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The type of the data source. Valid values:
        # 
        # - **ckafka**: Tencent Cloud CKafka.
        # 
        # - **obs**: Huawei Cloud OBS.
        # 
        # - **wafApi**: Tencent Cloud WAF attack log download API.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The region where the Data Management center for threat analysis is deployed. Select a region based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are outside China.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

