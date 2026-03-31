# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveStatisticResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The statistics of the sensitive data.
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
                temp_model = main_models.DescribeSensitiveStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSensitiveStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        api_format: str = None,
        client_ip: str = None,
        count: int = None,
        matched_host: str = None,
        sensitive_code: str = None,
    ):
        # The API.
        self.api_format = api_format
        # The IP address.
        self.client_ip = client_ip
        # The number of entries returned.
        self.count = count
        # The domain name.
        self.matched_host = matched_host
        # The type of the sensitive data.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported types of sensitive data.
        self.sensitive_code = sensitive_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.count is not None:
            result['Count'] = self.count

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        return self

