# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataSourceLogRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_logs: str = None,
        log_code: str = None,
        region_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The code for the multicloud environment. Valid values:
        # 
        # - qcloud: Tencent Cloud.
        # 
        # - aliyun: Alibaba Cloud.
        # 
        # - hcloud: Huawei Cloud.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The ID of the data source. Threat Analysis calculates this ID as an MD5 hash value based on specific parameters. To obtain the data source ID, call the [ListDataSourceLogs](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854\\&activeTabKey=api%7CListDataSourceLogs) operation.
        # 
        # This parameter is required.
        self.data_source_instance_id = data_source_instance_id
        # The details of the data source parameters. The value must be a JSON array.
        # 
        # This parameter is required.
        self.data_source_instance_logs = data_source_instance_logs
        # The code of the log.
        self.log_code = log_code
        # The region where the Data Management Center of Threat Analysis is deployed. Select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Assets are in the Chinese mainland and Hong Kong (China).
        # 
        # - ap-southeast-1: Assets are outside China.
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

        if self.data_source_instance_logs is not None:
            result['DataSourceInstanceLogs'] = self.data_source_instance_logs

        if self.log_code is not None:
            result['LogCode'] = self.log_code

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

        if m.get('DataSourceInstanceLogs') is not None:
            self.data_source_instance_logs = m.get('DataSourceInstanceLogs')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

