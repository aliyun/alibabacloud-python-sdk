# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSourceLogsRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The code for the cloud service provider. Valid values:
        # 
        # - qcloud: Tencent Cloud.
        # 
        # - aliyun: Alibaba Cloud.
        # 
        # - hcloud: Huawei Cloud.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The ID of the data source. This ID is an MD5 hash value that is calculated by threat analysis based on specific parameters.
        # 
        # This parameter is required.
        self.data_source_instance_id = data_source_instance_id
        # The region where the Data Management hub of threat analysis is deployed. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or Hong Kong (China).
        # 
        # - ap-southeast-1: Your assets are in a region outside China.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

