# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnSLSRealTimeLogTypeResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.DescribeDcdnSLSRealTimeLogTypeResponseBodyContent = None,
        request_id: str = None,
    ):
        # The returned results.
        self.content = content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.DescribeDcdnSLSRealTimeLogTypeResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnSLSRealTimeLogTypeResponseBodyContent(DaraModel):
    def __init__(
        self,
        business: List[main_models.DescribeDcdnSLSRealTimeLogTypeResponseBodyContentBusiness] = None,
    ):
        self.business = business

    def validate(self):
        if self.business:
            for v1 in self.business:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Business'] = []
        if self.business is not None:
            for k1 in self.business:
                result['Business'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business = []
        if m.get('Business') is not None:
            for k1 in m.get('Business'):
                temp_model = main_models.DescribeDcdnSLSRealTimeLogTypeResponseBodyContentBusiness()
                self.business.append(temp_model.from_map(k1))

        return self

class DescribeDcdnSLSRealTimeLogTypeResponseBodyContentBusiness(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        desc: str = None,
    ):
        # The type of real-time logs. Valid values:
        # 
        # *   **dcdn_log_access_l1**: access logs.
        # *   **dcdn_log_er**: EdgeRoutine logs
        # *   **dcdn_log_waf**: WAF interception logs
        self.business_type = business_type
        # The description of the real-time log type.
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.desc is not None:
            result['Desc'] = self.desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        return self

