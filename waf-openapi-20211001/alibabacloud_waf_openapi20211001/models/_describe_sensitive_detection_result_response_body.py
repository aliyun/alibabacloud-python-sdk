# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveDetectionResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSensitiveDetectionResultResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned for the compliance detection results.
        self.data = data
        # The ID of the request.
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
            temp_model = main_models.DescribeSensitiveDetectionResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSensitiveDetectionResultResponseBodyData(DaraModel):
    def __init__(
        self,
        result: List[main_models.DescribeSensitiveDetectionResultResponseBodyDataResult] = None,
    ):
        # The compliance detection results for sensitive data.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeSensitiveDetectionResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeSensitiveDetectionResultResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        detection_result: str = None,
        list: List[main_models.DescribeSensitiveDetectionResultResponseBodyDataResultList] = None,
        max: main_models.DescribeSensitiveDetectionResultResponseBodyDataResultMax = None,
    ):
        # The result of the compliance detection. Valid values:
        # 
        # - **report**: A risk of outbound data transfer is detected.
        # 
        # - **none**: No risk of outbound data transfer is detected.
        self.detection_result = detection_result
        # The detection results for each sensitive data type.
        self.list = list
        # The statistics for the most frequently detected sensitive data type.
        self.max = max

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.max:
            self.max.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.max is not None:
            result['Max'] = self.max.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionResult') is not None:
            self.detection_result = m.get('DetectionResult')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeSensitiveDetectionResultResponseBodyDataResultList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Max') is not None:
            temp_model = main_models.DescribeSensitiveDetectionResultResponseBodyDataResultMax()
            self.max = temp_model.from_map(m.get('Max'))

        return self

class DescribeSensitiveDetectionResultResponseBodyDataResultMax(DaraModel):
    def __init__(
        self,
        info_count: int = None,
        outbound_count: int = None,
        sensitive_code: int = None,
    ):
        # The number of personal information items for the most frequently detected sensitive data type.
        self.info_count = info_count
        # The number of outbound transfers of personal information for the most frequently detected sensitive data type.
        self.outbound_count = outbound_count
        # The code of the sensitive data type that is most frequently detected.
        self.sensitive_code = sensitive_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_count is not None:
            result['InfoCount'] = self.info_count

        if self.outbound_count is not None:
            result['OutboundCount'] = self.outbound_count

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoCount') is not None:
            self.info_count = m.get('InfoCount')

        if m.get('OutboundCount') is not None:
            self.outbound_count = m.get('OutboundCount')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        return self

class DescribeSensitiveDetectionResultResponseBodyDataResultList(DaraModel):
    def __init__(
        self,
        info_count: int = None,
        outbound_count: int = None,
        sensitive_code: int = None,
    ):
        # The number of personal information items.
        self.info_count = info_count
        # The number of outbound transfers of personal information.
        self.outbound_count = outbound_count
        # The code of the sensitive data type.
        self.sensitive_code = sensitive_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_count is not None:
            result['InfoCount'] = self.info_count

        if self.outbound_count is not None:
            result['OutboundCount'] = self.outbound_count

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoCount') is not None:
            self.info_count = m.get('InfoCount')

        if m.get('OutboundCount') is not None:
            self.outbound_count = m.get('OutboundCount')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        return self

