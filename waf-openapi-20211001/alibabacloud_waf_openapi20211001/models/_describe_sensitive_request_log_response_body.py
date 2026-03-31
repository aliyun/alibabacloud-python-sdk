# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveRequestLogResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveRequestLogResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The access logs.
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
                temp_model = main_models.DescribeSensitiveRequestLogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSensitiveRequestLogResponseBodyData(DaraModel):
    def __init__(
        self,
        account: str = None,
        api_format: str = None,
        api_id: str = None,
        client_ip: str = None,
        count: int = None,
        matched_host: str = None,
        remote_country_id: str = None,
        request_time: int = None,
        sensitive_list: str = None,
        trace_id: str = None,
    ):
        self.account = account
        # The API.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The IP address.
        self.client_ip = client_ip
        # The number of sensitive data records involved in cross-border data transfer.
        self.count = count
        # The domain name of the API.
        self.matched_host = matched_host
        # IP region, formatted as a region code.
        self.remote_country_id = remote_country_id
        # The time when the request was initiated. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.request_time = request_time
        # The details of sensitive data. The value is a string that consists of a JSON struct. The JSON struct contains key-value pairs. In a key-value pair, a key indicates the identifier of a sensitive data type, including built-in and custom types, and a value indicates specific sensitive data.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported sensitive data types.
        self.sensitive_list = sensitive_list
        # The trace ID.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.count is not None:
            result['Count'] = self.count

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.remote_country_id is not None:
            result['RemoteCountryId'] = self.remote_country_id

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        if self.sensitive_list is not None:
            result['SensitiveList'] = self.sensitive_list

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('RemoteCountryId') is not None:
            self.remote_country_id = m.get('RemoteCountryId')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        if m.get('SensitiveList') is not None:
            self.sensitive_list = m.get('SensitiveList')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

