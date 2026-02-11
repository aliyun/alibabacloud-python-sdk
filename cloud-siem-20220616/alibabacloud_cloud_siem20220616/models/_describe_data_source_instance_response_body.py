# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeDataSourceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDataSourceInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDataSourceInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataSourceInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        data_source_instance_id: str = None,
        data_source_instance_params: List[main_models.DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams] = None,
    ):
        # The ID of the cloud account.
        self.account_id = account_id
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code
        # The ID of the data source. The ID is an MD5 hash value that is calculated by the threat analysis feature based on specific parameters.
        self.data_source_instance_id = data_source_instance_id
        # The parameters of the data source.
        self.data_source_instance_params = data_source_instance_params

    def validate(self):
        if self.data_source_instance_params:
            for v1 in self.data_source_instance_params:
                 if v1:
                    v1.validate()

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

        result['DataSourceInstanceParams'] = []
        if self.data_source_instance_params is not None:
            for k1 in self.data_source_instance_params:
                result['DataSourceInstanceParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceInstanceId') is not None:
            self.data_source_instance_id = m.get('DataSourceInstanceId')

        self.data_source_instance_params = []
        if m.get('DataSourceInstanceParams') is not None:
            for k1 in m.get('DataSourceInstanceParams'):
                temp_model = main_models.DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams()
                self.data_source_instance_params.append(temp_model.from_map(k1))

        return self

class DescribeDataSourceInstanceResponseBodyDataDataSourceInstanceParams(DaraModel):
    def __init__(
        self,
        para_code: str = None,
        para_value: str = None,
    ):
        # The code of the parameter.
        self.para_code = para_code
        # The value of the parameter.
        self.para_value = para_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.para_code is not None:
            result['ParaCode'] = self.para_code

        if self.para_value is not None:
            result['ParaValue'] = self.para_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParaCode') is not None:
            self.para_code = m.get('ParaCode')

        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')

        return self

