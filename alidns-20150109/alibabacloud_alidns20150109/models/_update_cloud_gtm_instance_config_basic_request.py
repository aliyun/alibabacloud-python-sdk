# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmInstanceConfigBasicRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        config_id: str = None,
        instance_id: str = None,
        schedule_hostname: str = None,
        schedule_zone_name: str = None,
        ttl: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh-CN**: Chinese.
        # 
        # - **en-US** (default): English.
        self.accept_language = accept_language
        # A client-generated token that you can use to ensure the idempotence of the request. Make sure that the token is unique among different requests. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The ID of the domain name instance configuration. For the same access domain name and GTM instance, you can configure both A and AAAA records. This results in two domain name instance configurations for the same GTM instance. The ConfigId uniquely identifies the configuration object that you want to modify.
        # 
        # Call the [ListCloudGtmInstanceConfigs](~~ListCloudGtmInstanceConfigs~~) operation to query the ConfigId of a domain name instance.
        self.config_id = config_id
        # The ID of the GTM 3.0 instance that you want to modify.
        self.instance_id = instance_id
        # The host record of the GTM access domain name.
        self.schedule_hostname = schedule_hostname
        # The root domain (such as example.com) or subdomain (such as a.example.com) of the GTM access domain name. This is usually a domain name that is hosted in the authoritative zone of the Alibaba Cloud DNS console under the account that owns the GTM instance.
        self.schedule_zone_name = schedule_zone_name
        # The global Time to Live (TTL) in seconds. This is the TTL for the DNS record that resolves the access domain name to an address in an address pool. The TTL affects how long the DNS record is cached on a carrier\\"s Local DNS server.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.schedule_hostname is not None:
            result['ScheduleHostname'] = self.schedule_hostname

        if self.schedule_zone_name is not None:
            result['ScheduleZoneName'] = self.schedule_zone_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScheduleHostname') is not None:
            self.schedule_hostname = m.get('ScheduleHostname')

        if m.get('ScheduleZoneName') is not None:
            self.schedule_zone_name = m.get('ScheduleZoneName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

