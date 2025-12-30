# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        charge_type: str = None,
        client_token: str = None,
        enable_status: str = None,
        instance_id: str = None,
        remark: str = None,
        schedule_hostname: str = None,
        schedule_rr_type: str = None,
        schedule_zone_mode: str = None,
        schedule_zone_name: str = None,
        ttl: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The enabling state of the access domain name. Valid values:
        # 
        # *   enable: The access domain name is enabled and the intelligent scheduling policy of the corresponding GTM instance takes effect.
        # *   disable: The access domain name is disabled and the intelligent scheduling policy of the corresponding GTM instance is unavailable.
        self.enable_status = enable_status
        # The ID of the Global Traffic Manager (GTM) 3.0 instance. This ID uniquely identifies a GTM 3.0 instance.
        self.instance_id = instance_id
        # The description of the access domain name.
        self.remark = remark
        # The hostname of the access domain name.
        self.schedule_hostname = schedule_hostname
        # The type of the Domain Name System (DNS) record configured for the access domain name. Valid values:
        # 
        # *   A: IPv4 address
        # *   AAAA: IPv6 address
        # *   CNAME: domain name
        self.schedule_rr_type = schedule_rr_type
        # The configuration mode of the access domain name. Valid values:
        # 
        # *   sys_assign: system allocation. This mode is not supported.
        # *   custom: custom allocation. You must select a zone within the account to which the instance belongs and enter a hostname to generate an access domain name.
        self.schedule_zone_mode = schedule_zone_mode
        # The name of the parent zone for the access domain name configured in GTM. In most cases, the value of this parameter is the name of a zone hosted by Alibaba Cloud DNS. This zone belongs to the account to which the GTM instance belongs. You can specify the name of a zone or subzone.
        self.schedule_zone_name = schedule_zone_name
        # The global time to live (TTL) period. Unit: seconds. The global TTL period affects how long the DNS records that map the access domain name to the addresses in the address pools are cached in the local DNS servers of Internet service providers (ISPs). You can specify a custom value.
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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.schedule_hostname is not None:
            result['ScheduleHostname'] = self.schedule_hostname

        if self.schedule_rr_type is not None:
            result['ScheduleRrType'] = self.schedule_rr_type

        if self.schedule_zone_mode is not None:
            result['ScheduleZoneMode'] = self.schedule_zone_mode

        if self.schedule_zone_name is not None:
            result['ScheduleZoneName'] = self.schedule_zone_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ScheduleHostname') is not None:
            self.schedule_hostname = m.get('ScheduleHostname')

        if m.get('ScheduleRrType') is not None:
            self.schedule_rr_type = m.get('ScheduleRrType')

        if m.get('ScheduleZoneMode') is not None:
            self.schedule_zone_mode = m.get('ScheduleZoneMode')

        if m.get('ScheduleZoneName') is not None:
            self.schedule_zone_name = m.get('ScheduleZoneName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

