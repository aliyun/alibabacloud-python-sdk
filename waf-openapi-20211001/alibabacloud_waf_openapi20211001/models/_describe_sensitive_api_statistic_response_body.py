# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveApiStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveApiStatisticResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The statistics.
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
                temp_model = main_models.DescribeSensitiveApiStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSensitiveApiStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        info_outbound_count: int = None,
        list: List[main_models.DescribeSensitiveApiStatisticResponseBodyDataList] = None,
        matched_host: str = None,
        sensitive_outbound_count: int = None,
    ):
        # The number of personal information records involved in cross-border data transfer by domain name.
        self.info_outbound_count = info_outbound_count
        # The domain name-related APIs.
        self.list = list
        # The domain name or IP address.
        self.matched_host = matched_host
        # The number of sensitive personal information records involved in cross-border data transfer by domain name.
        self.sensitive_outbound_count = sensitive_outbound_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_outbound_count is not None:
            result['InfoOutboundCount'] = self.info_outbound_count

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.sensitive_outbound_count is not None:
            result['SensitiveOutboundCount'] = self.sensitive_outbound_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoOutboundCount') is not None:
            self.info_outbound_count = m.get('InfoOutboundCount')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeSensitiveApiStatisticResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('SensitiveOutboundCount') is not None:
            self.sensitive_outbound_count = m.get('SensitiveOutboundCount')

        return self

class DescribeSensitiveApiStatisticResponseBodyDataList(DaraModel):
    def __init__(
        self,
        api_format: str = None,
        api_id: str = None,
        info_count: int = None,
        sensitive_code: List[str] = None,
        sensitive_count: int = None,
    ):
        # The API.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The number of personal information records involved in cross-border data transfer by API.
        self.info_count = info_count
        # The types of sensitive data.
        self.sensitive_code = sensitive_code
        # The number of sensitive personal information records involved in cross-border data transfer by API.
        self.sensitive_count = sensitive_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.info_count is not None:
            result['InfoCount'] = self.info_count

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('InfoCount') is not None:
            self.info_count = m.get('InfoCount')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        return self

