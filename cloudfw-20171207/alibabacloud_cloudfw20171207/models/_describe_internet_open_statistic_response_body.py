# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetOpenStatisticResponseBody(DaraModel):
    def __init__(
        self,
        internet_ip_num: int = None,
        internet_port_num: int = None,
        internet_risk_ip_num: int = None,
        internet_risk_port_num: int = None,
        internet_risk_service_num: int = None,
        internet_service_num: int = None,
        internet_slb_ip_num: int = None,
        internet_slb_ip_port_num: int = None,
        internet_unprotected_port_num: int = None,
        request_id: str = None,
    ):
        self.internet_ip_num = internet_ip_num
        self.internet_port_num = internet_port_num
        self.internet_risk_ip_num = internet_risk_ip_num
        self.internet_risk_port_num = internet_risk_port_num
        self.internet_risk_service_num = internet_risk_service_num
        self.internet_service_num = internet_service_num
        self.internet_slb_ip_num = internet_slb_ip_num
        self.internet_slb_ip_port_num = internet_slb_ip_port_num
        self.internet_unprotected_port_num = internet_unprotected_port_num
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_ip_num is not None:
            result['InternetIpNum'] = self.internet_ip_num

        if self.internet_port_num is not None:
            result['InternetPortNum'] = self.internet_port_num

        if self.internet_risk_ip_num is not None:
            result['InternetRiskIpNum'] = self.internet_risk_ip_num

        if self.internet_risk_port_num is not None:
            result['InternetRiskPortNum'] = self.internet_risk_port_num

        if self.internet_risk_service_num is not None:
            result['InternetRiskServiceNum'] = self.internet_risk_service_num

        if self.internet_service_num is not None:
            result['InternetServiceNum'] = self.internet_service_num

        if self.internet_slb_ip_num is not None:
            result['InternetSlbIpNum'] = self.internet_slb_ip_num

        if self.internet_slb_ip_port_num is not None:
            result['InternetSlbIpPortNum'] = self.internet_slb_ip_port_num

        if self.internet_unprotected_port_num is not None:
            result['InternetUnprotectedPortNum'] = self.internet_unprotected_port_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIpNum') is not None:
            self.internet_ip_num = m.get('InternetIpNum')

        if m.get('InternetPortNum') is not None:
            self.internet_port_num = m.get('InternetPortNum')

        if m.get('InternetRiskIpNum') is not None:
            self.internet_risk_ip_num = m.get('InternetRiskIpNum')

        if m.get('InternetRiskPortNum') is not None:
            self.internet_risk_port_num = m.get('InternetRiskPortNum')

        if m.get('InternetRiskServiceNum') is not None:
            self.internet_risk_service_num = m.get('InternetRiskServiceNum')

        if m.get('InternetServiceNum') is not None:
            self.internet_service_num = m.get('InternetServiceNum')

        if m.get('InternetSlbIpNum') is not None:
            self.internet_slb_ip_num = m.get('InternetSlbIpNum')

        if m.get('InternetSlbIpPortNum') is not None:
            self.internet_slb_ip_port_num = m.get('InternetSlbIpPortNum')

        if m.get('InternetUnprotectedPortNum') is not None:
            self.internet_unprotected_port_num = m.get('InternetUnprotectedPortNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

