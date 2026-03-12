# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveTaskForModifyingDomainDnsRequest(DaraModel):
    def __init__(
        self,
        aliyun_dns: bool = None,
        dns_list: List[str] = None,
        domain_name: str = None,
        lang: str = None,
        sale_id: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.aliyun_dns = aliyun_dns
        self.dns_list = dns_list
        self.domain_name = domain_name
        self.lang = lang
        self.sale_id = sale_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_dns is not None:
            result['AliyunDns'] = self.aliyun_dns

        if self.dns_list is not None:
            result['DnsList'] = self.dns_list

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')

        if m.get('DnsList') is not None:
            self.dns_list = m.get('DnsList')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

