# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSensitiveOutboundDistributionResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeSensitiveOutboundDistributionResponseBodyData] = None,
        request_id: str = None,
    ):
        # A list of outbound traffic distributions that contain personal information.
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
                temp_model = main_models.DescribeSensitiveOutboundDistributionResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSensitiveOutboundDistributionResponseBodyData(DaraModel):
    def __init__(
        self,
        country: str = None,
        info_outbound_count: int = None,
        sensitive_outbound_count: int = None,
    ):
        # The destination country.
        self.country = country
        # The number of outbound personal information entries.
        self.info_outbound_count = info_outbound_count
        # The number of outbound sensitive information entries.
        self.sensitive_outbound_count = sensitive_outbound_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.country is not None:
            result['Country'] = self.country

        if self.info_outbound_count is not None:
            result['InfoOutboundCount'] = self.info_outbound_count

        if self.sensitive_outbound_count is not None:
            result['SensitiveOutboundCount'] = self.sensitive_outbound_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('InfoOutboundCount') is not None:
            self.info_outbound_count = m.get('InfoOutboundCount')

        if m.get('SensitiveOutboundCount') is not None:
            self.sensitive_outbound_count = m.get('SensitiveOutboundCount')

        return self

