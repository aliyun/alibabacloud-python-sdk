# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveRequestsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveRequestsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The tracing results of the data.
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
                temp_model = main_models.DescribeSensitiveRequestsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSensitiveRequestsResponseBodyData(DaraModel):
    def __init__(
        self,
        abnormal_count: int = None,
        api_format: str = None,
        api_id: str = None,
        client_ip: str = None,
        detection_result: str = None,
        event_count: int = None,
        info_count: List[main_models.DescribeSensitiveRequestsResponseBodyDataInfoCount] = None,
        matched_host: str = None,
        sensitive_list: List[str] = None,
    ):
        # The number of risks in the previous 30 days.
        self.abnormal_count = abnormal_count
        # The API.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The IP address.
        self.client_ip = client_ip
        # The evaluation result. Valid values:
        # 
        # *   **leak**: Data leaks may occur.
        # *   **none**: No data leak can occur.
        self.detection_result = detection_result
        # The number of events in the previous 30 days.
        self.event_count = event_count
        # The statistics of the sensitive data.
        self.info_count = info_count
        # The domain name of the API.
        self.matched_host = matched_host
        # The sensitive data.
        self.sensitive_list = sensitive_list

    def validate(self):
        if self.info_count:
            for v1 in self.info_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_count is not None:
            result['AbnormalCount'] = self.abnormal_count

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        result['InfoCount'] = []
        if self.info_count is not None:
            for k1 in self.info_count:
                result['InfoCount'].append(k1.to_map() if k1 else None)

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.sensitive_list is not None:
            result['SensitiveList'] = self.sensitive_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalCount') is not None:
            self.abnormal_count = m.get('AbnormalCount')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('DetectionResult') is not None:
            self.detection_result = m.get('DetectionResult')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        self.info_count = []
        if m.get('InfoCount') is not None:
            for k1 in m.get('InfoCount'):
                temp_model = main_models.DescribeSensitiveRequestsResponseBodyDataInfoCount()
                self.info_count.append(temp_model.from_map(k1))

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('SensitiveList') is not None:
            self.sensitive_list = m.get('SensitiveList')

        return self

class DescribeSensitiveRequestsResponseBodyDataInfoCount(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
    ):
        # The type of the sensitive data.
        self.code = code
        # The number of sensitive data entries.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

