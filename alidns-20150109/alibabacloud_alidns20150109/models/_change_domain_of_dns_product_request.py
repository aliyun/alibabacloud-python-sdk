# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDomainOfDnsProductRequest(DaraModel):
    def __init__(
        self,
        force: bool = None,
        instance_id: str = None,
        lang: str = None,
        new_domain: str = None,
        user_client_ip: str = None,
    ):
        # Specifies whether to forcibly bind a domain name to the instance. Valid values:
        # 
        # *   **false****: no**
        # *   **true**: **yes**
        # 
        # Default value: **false**.
        self.force = force
        # The ID of the Alibaba Cloud Domain Name System (DNS) instance.
        # 
        # You can call the [ListCloudGtmInstances ](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-listcloudgtminstances?spm=a2c63.p38356.help-menu-search-29697.d_0)operation to obtain the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **zh**.
        self.lang = lang
        # The domain name that you want to bind to the instance. If you leave this parameter empty, the domain name that is bound to the instance is unbound from the instance.
        self.new_domain = new_domain
        # The IP address of the client.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.new_domain is not None:
            result['NewDomain'] = self.new_domain

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NewDomain') is not None:
            self.new_domain = m.get('NewDomain')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

