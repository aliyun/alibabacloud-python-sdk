# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecSensitiveDomainStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecSensitiveDomainStatisticResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecSensitiveDomainStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecSensitiveDomainStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        api_count: int = None,
        domain_count: int = None,
        sensitive_code: str = None,
        sensitive_level: str = None,
        sensitive_name: str = None,
    ):
        # The number of APIs that are involved.
        self.api_count = api_count
        # The number of sites that are involved.
        self.domain_count = domain_count
        # The code of the sensitive data.
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported sensitive data types.
        self.sensitive_code = sensitive_code
        # The sensitivity level of the sensitive data.Valid values:
        # 
        # * **S1**: low sensitivity.
        # * **S2**: moderate sensitivity.
        # * **S3**: high sensitivity.
        self.sensitive_level = sensitive_level
        # The name of the sensitive data.
        self.sensitive_name = sensitive_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_count is not None:
            result['ApiCount'] = self.api_count

        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiCount') is not None:
            self.api_count = m.get('ApiCount')

        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')

        return self

