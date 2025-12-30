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
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The configuration ID of the access domain name. Two configuration IDs exist when the access domain name is bound to the same GTM instance but an A record and an AAAA record are configured for the access domain name. The configuration ID uniquely identifies a configuration.
        # 
        # You can call the [ListCloudGtmInstanceConfigs](https://help.aliyun.com/document_detail/2797349.html) operation to query the value of ConfigId for the access domain name.
        self.config_id = config_id
        # The ID of the GTM 3.0 instance for which you want to modify the TTL configuration.
        self.instance_id = instance_id
        # Host record of the domain accessed by GTM.
        self.schedule_hostname = schedule_hostname
        # The zone (such as example.com) or subzone (such as a.example.com) of the GTM access domain name. In most cases, the zone or subzone is hosted in Authoritative DNS Resolution of the Alibaba Cloud DNS console within the account to which the GTM instance belongs.
        self.schedule_zone_name = schedule_zone_name
        # The global TTL value, in seconds. The global TTL value affects how long the DNS records that map the access domain name to the addresses in the address pools are cached in the local DNS servers of Internet service providers (ISPs).
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

