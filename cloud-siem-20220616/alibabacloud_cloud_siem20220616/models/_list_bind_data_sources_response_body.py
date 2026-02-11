# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListBindDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListBindDataSourcesResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListBindDataSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBindDataSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_name: str = None,
        data_source_remark: str = None,
        data_source_type: str = None,
        log_count: int = None,
        task_count: int = None,
    ):
        # The ID of the cloud account.
        self.account_id = account_id
        # The username of the cloud account.
        self.account_name = account_name
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.data_source_instance_id = data_source_instance_id
        # The name of the data source.
        self.data_source_name = data_source_name
        # The remarks on the data source.
        self.data_source_remark = data_source_remark
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        self.data_source_type = data_source_type
        # The number of logs that are added within the data source.
        self.log_count = log_count
        # The number of existing tasks that are created to add logs within the data source.
        self.task_count = task_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.data_source_instance_id is not None:
            result['DataSourceInstanceId'] = self.data_source_instance_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_remark is not None:
            result['DataSourceRemark'] = self.data_source_remark

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.log_count is not None:
            result['LogCount'] = self.log_count

        if self.task_count is not None:
            result['TaskCount'] = self.task_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceRemark') is not None:
            self.data_source_remark = m.get('DataSourceRemark')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')

        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')

        return self

