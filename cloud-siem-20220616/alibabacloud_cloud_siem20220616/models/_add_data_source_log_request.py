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
        # The ID of the cloud account.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The code of the multi-cloud provider. Valid values:
        # - qcloud: Tencent Cloud.
        # - hcloud: Huawei Cloud.
        # - aliyun: Alibaba Cloud. This value is only used for Alibaba Cloud data source scenarios. When you query available multi-cloud data source types, the ListDataSourceTypes operation only supports qcloud and hcloud.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The ID of the data source instance. You can call the ListBindDataSources operation to query the ID.
        # 
        # This parameter is required.
        self.data_source_instance_id = data_source_instance_id
        # The details of the data source parameters. The value is a JSON array.
        # 
        # This parameter is required.
        self.data_source_instance_logs = data_source_instance_logs
        # The log code.
        self.log_code = log_code
        # The region where the data management center of Cloud Threat Detection and Response (CTDR) is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Your assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Your assets are located outside China.
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

