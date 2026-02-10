# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainSecureRiskListResponseBody(DaraModel):
    def __init__(
        self,
        no_ssl_count: int = None,
        request_id: str = None,
        risk_count: int = None,
        risk_list: List[main_models.DescribeDomainSecureRiskListResponseBodyRiskList] = None,
    ):
        # The number of the websites for which no certificates are installed.
        self.no_ssl_count = no_ssl_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of risks.
        self.risk_count = risk_count
        # The risks.
        self.risk_list = risk_list

    def validate(self):
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.no_ssl_count is not None:
            result['NoSslCount'] = self.no_ssl_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NoSslCount') is not None:
            self.no_ssl_count = m.get('NoSslCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.DescribeDomainSecureRiskListResponseBodyRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        return self

class DescribeDomainSecureRiskListResponseBodyRiskList(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        domain: str = None,
        ssl_brand: str = None,
        ssl_status: int = None,
        uuid_list: List[str] = None,
        vul_count: int = None,
    ):
        # The number of alerts.
        self.alarm_count = alarm_count
        # The domain name.
        self.domain = domain
        # The issuer of the certificate.
        self.ssl_brand = ssl_brand
        # Indicates whether the certificate is configured. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.ssl_status = ssl_status
        # The UUIDs of the backend servers of the website.
        self.uuid_list = uuid_list
        # The number of vulnerabilities.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ssl_brand is not None:
            result['SslBrand'] = self.ssl_brand

        if self.ssl_status is not None:
            result['SslStatus'] = self.ssl_status

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('SslBrand') is not None:
            self.ssl_brand = m.get('SslBrand')

        if m.get('SslStatus') is not None:
            self.ssl_status = m.get('SslStatus')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

