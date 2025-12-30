# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGtmInstanceGlobalConfigRequest(DaraModel):
    def __init__(
        self,
        alert_group: str = None,
        cname_custom_domain_name: str = None,
        cname_mode: str = None,
        instance_id: str = None,
        instance_name: str = None,
        lang: str = None,
        lba_strategy: str = None,
        ttl: int = None,
        user_domain_name: str = None,
    ):
        # The alert group. Only one alert group is supported.
        # 
        # >  This parameter is required only for the first modification.
        self.alert_group = alert_group
        # If you set **CnameMode** to **CUSTOM**, you must specify the CnameCustomDomainName parameter, which must be set to a primary domain name.
        self.cname_custom_domain_name = cname_custom_domain_name
        # Specifies whether to use a system-assigned canonical name (CNAME) or a custom CNAME to access GTM. Valid values:
        # 
        # *   **SYSTEM_ASSIGN**: system-assigned CNAME
        # *   **CUSTOM**: custom CNAME
        self.cname_mode = cname_mode
        # The ID of the GTM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the GTM instance.
        # 
        # >  This parameter is required only for the first modification.
        self.instance_name = instance_name
        # The language.
        self.lang = lang
        # The balancing policy. Valid values:
        # 
        # *   **ALL_RR**: load balancing
        # *   **RATIO**: weighted round-robin
        # 
        # >  This parameter is required only for the first modification.
        self.lba_strategy = lba_strategy
        # The global time-to-live (TTL).
        self.ttl = ttl
        # The primary domain name.
        # 
        # >  This parameter is required only for the first modification.
        self.user_domain_name = user_domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group

        if self.cname_custom_domain_name is not None:
            result['CnameCustomDomainName'] = self.cname_custom_domain_name

        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.user_domain_name is not None:
            result['UserDomainName'] = self.user_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')

        if m.get('CnameCustomDomainName') is not None:
            self.cname_custom_domain_name = m.get('CnameCustomDomainName')

        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('UserDomainName') is not None:
            self.user_domain_name = m.get('UserDomainName')

        return self

