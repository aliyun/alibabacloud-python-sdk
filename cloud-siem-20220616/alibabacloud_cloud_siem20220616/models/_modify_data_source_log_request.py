# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDataSourceLogRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_logs: str = None,
        data_source_type: str = None,
        log_code: str = None,
        log_instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
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
        # The ID of the data source. The threat analysis feature generates this ID by calculating an MD5 hash of the parameters.
        # Call the [DescribeDataSourceInstance](https://help.aliyun.com/document_detail/2639736.html) operation to obtain the data source ID.
        # 
        # This parameter is required.
        self.data_source_instance_id = data_source_instance_id
        # The details of the data source parameters, in a JSON array format.
        # 
        # This parameter is required.
        self.data_source_instance_logs = data_source_instance_logs
        # The type of the data source. Valid values:
        # 
        # - obs: Huawei Cloud Object Storage Service (OBS).
        # 
        # - wafApi: Tencent Cloud Web Application Firewall (WAF) download API.
        # 
        # - ckafka: Tencent Cloud CKafka.
        self.data_source_type = data_source_type
        # The code of the log.
        self.log_code = log_code
        # The ID of the log. The threat analysis feature generates this ID by calculating an MD5 hash of the parameters. Call the [ListDataSourceLogs](https://help.aliyun.com/document_detail/2639707.html) operation to obtain the log ID.
        # 
        # This parameter is required.
        self.log_instance_id = log_instance_id
        # The region where the Data Management hub is located. Select a region based on the location of your assets. Valid values:
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id

        if self.data_source_instance_logs is not None:
            result['DataSourceInstanceLogs'] = self.data_source_instance_logs

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_instance_id is not None:
            result['LogInstanceId'] = self.log_instance_id

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

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogInstanceId') is not None:
            self.log_instance_id = m.get('LogInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

