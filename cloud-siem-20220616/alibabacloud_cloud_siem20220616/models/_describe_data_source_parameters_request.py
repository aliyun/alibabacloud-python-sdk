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
        # The code of the cloud service provider.
        # 
        # Valid values:
        # 
        # *   qcloud
        # *   hcloud
        # *   aliyun
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The type of the data source. Valid values:
        # 
        # *   **ckafka**: Tencent Cloud TDMQ for CKafka
        # *   **obs**: Huawei Cloud Object Storage Service (OBS)
        # *   **wafApi**: download API of Tencent Cloud Web Application Firewall (WAF)
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
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

