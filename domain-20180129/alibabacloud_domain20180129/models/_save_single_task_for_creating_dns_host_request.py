# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveSingleTaskForCreatingDnsHostRequest(DaraModel):
    def __init__(
        self,
        dns_name: str = None,
        instance_id: str = None,
        ip: List[str] = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # DNS name.
        # 
        # This parameter is required.
        self.dns_name = dns_name
        # Domain instance ID, which can be obtained by calling the [QueryDomainList](https://help.aliyun.com/document_detail/67712.html) API.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # List of IP addresses. You can specify up to 13 IP addresses. When specifying multiple IP addresses, pass them as a **list**.
        # 
        # This parameter is required.
        self.ip = ip
        # Language of the error message returned by the API. Valid values:  
        # - **zh**: Chinese  
        # - **en**: English  
        # 
        # Default value: **en**.
        self.lang = lang
        # User IP address, which can be set to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

