# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsProductInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # The ID of the DNS instance. . You can call the [DescribeDomainInfo](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomaininfo?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en
        self.lang = lang
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

