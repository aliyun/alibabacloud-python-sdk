# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDnsHostResponseBody(DaraModel):
    def __init__(
        self,
        dns_host_list: List[main_models.QueryDnsHostResponseBodyDnsHostList] = None,
        request_id: str = None,
    ):
        self.dns_host_list = dns_host_list
        self.request_id = request_id

    def validate(self):
        if self.dns_host_list:
            for v1 in self.dns_host_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DnsHostList'] = []
        if self.dns_host_list is not None:
            for k1 in self.dns_host_list:
                result['DnsHostList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dns_host_list = []
        if m.get('DnsHostList') is not None:
            for k1 in m.get('DnsHostList'):
                temp_model = main_models.QueryDnsHostResponseBodyDnsHostList()
                self.dns_host_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDnsHostResponseBodyDnsHostList(DaraModel):
    def __init__(
        self,
        dns_name: str = None,
        ip_list: List[str] = None,
    ):
        self.dns_name = dns_name
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        return self

