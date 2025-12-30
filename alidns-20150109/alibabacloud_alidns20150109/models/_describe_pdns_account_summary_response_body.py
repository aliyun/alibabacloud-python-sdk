# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsAccountSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribePdnsAccountSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.DescribePdnsAccountSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePdnsAccountSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        domain_count: int = None,
        http_count: int = None,
        https_count: int = None,
        sub_domain_count: int = None,
        threat_count: int = None,
        total_count: int = None,
        user_id: int = None,
    ):
        self.domain_count = domain_count
        self.http_count = http_count
        self.https_count = https_count
        self.sub_domain_count = sub_domain_count
        self.threat_count = threat_count
        self.total_count = total_count
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.http_count is not None:
            result['HttpCount'] = self.http_count

        if self.https_count is not None:
            result['HttpsCount'] = self.https_count

        if self.sub_domain_count is not None:
            result['SubDomainCount'] = self.sub_domain_count

        if self.threat_count is not None:
            result['ThreatCount'] = self.threat_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('HttpCount') is not None:
            self.http_count = m.get('HttpCount')

        if m.get('HttpsCount') is not None:
            self.https_count = m.get('HttpsCount')

        if m.get('SubDomainCount') is not None:
            self.sub_domain_count = m.get('SubDomainCount')

        if m.get('ThreatCount') is not None:
            self.threat_count = m.get('ThreatCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

