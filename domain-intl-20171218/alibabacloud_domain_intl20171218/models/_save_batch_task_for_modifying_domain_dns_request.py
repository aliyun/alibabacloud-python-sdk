# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveBatchTaskForModifyingDomainDnsRequest(DaraModel):
    def __init__(
        self,
        aliyun_dns: bool = None,
        domain_name: List[str] = None,
        domain_name_server: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.aliyun_dns = aliyun_dns
        # This parameter is required.
        self.domain_name = domain_name
        self.domain_name_server = domain_name_server
        self.lang = lang
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_server is not None:
            result['DomainNameServer'] = self.domain_name_server

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunDns') is not None:
            self.aliyun_dns = m.get('AliyunDns')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameServer') is not None:
            self.domain_name_server = m.get('DomainNameServer')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

