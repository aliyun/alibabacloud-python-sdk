# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateNatIpResponseBody(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
        nat_ip: str = None,
        nat_ip_id: str = None,
        nat_ips: List[main_models.CreateNatIpResponseBodyNatIps] = None,
        request_id: str = None,
    ):
        # The IPv4 prefix returned by the legacy operation. This parameter is deprecated.
        self.ipv_4prefix = ipv_4prefix
        # The created NAT IP address.
        self.nat_ip = nat_ip
        # The instance ID of the created NAT IP address.
        self.nat_ip_id = nat_ip_id
        # The NAT IP address information returned after the NAT IP address is created. When you create a NAT IP address by using an IPv4 prefix, all NAT IP address information is returned. When you create a single NAT IP address, we recommend that you use this parameter to obtain the NAT IP address information.
        self.nat_ips = nat_ips
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.nat_ips:
            for v1 in self.nat_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.nat_ip_id is not None:
            result['NatIpId'] = self.nat_ip_id

        result['NatIps'] = []
        if self.nat_ips is not None:
            for k1 in self.nat_ips:
                result['NatIps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NatIpId') is not None:
            self.nat_ip_id = m.get('NatIpId')

        self.nat_ips = []
        if m.get('NatIps') is not None:
            for k1 in m.get('NatIps'):
                temp_model = main_models.CreateNatIpResponseBodyNatIps()
                self.nat_ips.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateNatIpResponseBodyNatIps(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
        nat_ip: str = None,
        nat_ip_id: str = None,
    ):
        # The IPv4 prefix in the list of NAT IP addresses created by using an IPv4 prefix.
        self.ipv_4prefix = ipv_4prefix
        # The NAT IP address in the list of NAT IP addresses created by using an IPv4 prefix.
        self.nat_ip = nat_ip
        # The NAT IP address ID in the list of NAT IP addresses created by using an IPv4 prefix.
        self.nat_ip_id = nat_ip_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.nat_ip_id is not None:
            result['NatIpId'] = self.nat_ip_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NatIpId') is not None:
            self.nat_ip_id = m.get('NatIpId')

        return self

