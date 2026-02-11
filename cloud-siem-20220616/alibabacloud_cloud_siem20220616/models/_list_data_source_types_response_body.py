# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceTypesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataSourceTypesResponseBodyData] = None,
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
                temp_model = main_models.ListDataSourceTypesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourceTypesResponseBodyData(DaraModel):
    def __init__(
        self,
        cloud_code: str = None,
        data_source_type: str = None,
    ):
        # The code of the third-party cloud service.
        self.cloud_code = cloud_code
        # The type of the data source. Valid values:
        # 
        # *   obs: Huawei Cloud Object Storage Service (OBS)
        # *   wafApi: download API of Tencent Cloud Web Application Firewall (WAF)
        # *   ckafka: Tencent Cloud Kafka (CKafka)
        self.data_source_type = data_source_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        return self

