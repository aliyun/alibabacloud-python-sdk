# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveOutboundStatisticResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveOutboundStatisticResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The data types of personal information involved in cross-border data transfer.
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
                temp_model = main_models.DescribeSensitiveOutboundStatisticResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSensitiveOutboundStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        detection_result: str = None,
        info_count: int = None,
        outbound_count: int = None,
        sensitive_code: int = None,
        sensitive_level: str = None,
        sensitive_type: str = None,
    ):
        # The evaluation result. Valid values:
        # 
        # *   **report**: Risks exist in cross-border data transfer.
        # *   **none**: No risks exist in cross-border data transfer.
        self.detection_result = detection_result
        # The total number of entries returned.
        self.info_count = info_count
        # The number of data entries that are transferred across borders.
        self.outbound_count = outbound_count
        # The type of the sensitive data.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported types of sensitive data.
        self.sensitive_code = sensitive_code
        # The sensitivity level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.sensitive_level = sensitive_level
        # The type of the information. Valid values:
        # 
        # *   **info**: full personal information
        # *   **sensitive**: sensitive personal information
        self.sensitive_type = sensitive_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detection_result is not None:
            result['DetectionResult'] = self.detection_result

        if self.info_count is not None:
            result['InfoCount'] = self.info_count

        if self.outbound_count is not None:
            result['OutboundCount'] = self.outbound_count

        if self.sensitive_code is not None:
            result['SensitiveCode'] = self.sensitive_code

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectionResult') is not None:
            self.detection_result = m.get('DetectionResult')

        if m.get('InfoCount') is not None:
            self.info_count = m.get('InfoCount')

        if m.get('OutboundCount') is not None:
            self.outbound_count = m.get('OutboundCount')

        if m.get('SensitiveCode') is not None:
            self.sensitive_code = m.get('SensitiveCode')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveType') is not None:
            self.sensitive_type = m.get('SensitiveType')

        return self

