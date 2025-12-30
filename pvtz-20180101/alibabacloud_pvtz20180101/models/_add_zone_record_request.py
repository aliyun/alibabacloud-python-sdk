# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddZoneRecordRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
        line: str = None,
        priority: int = None,
        remark: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The DNS request source. Valid values:
        # 
        # *   default: the default resolution line. The default line is equivalent to a global line. We recommend that you configure a default line to ensure that a DNS record can be returned if no intelligent line is matched.
        # *   Alibaba Cloud lines: indicate that DNS requests are originated from Alibaba Cloud, including Alibaba Cloud public cloud, Alibaba Finance Cloud, and Alibaba Gov Cloud.
        # *   Custom lines: You can configure custom lines so that Private DNS can return specific IP addresses for DNS requests that are originated from a specific CIDR block.
        # 
        # > 
        # 
        # *   Only built-in authoritative acceleration zones support custom lines.
        # 
        # *   Set Line to default if you want to choose the default line. Set Line to a specific line code if you want to choose an Alibaba Cloud line or a custom line. Example: aliyun_r_cn-beijing-a.
        self.line = line
        # The priority of the mail exchanger (MX) record. Valid values: **1 to 99**. A smaller value indicates a higher priority.
        self.priority = priority
        # The description of the DNS record.
        self.remark = remark
        # The hostname. The hostname is the prefix of the subdomain name for the zone. Example: www, @, \\* (used for wildcard DNS resolution), and mail (used for specifying the mail server that receives emails).
        # 
        # For example, if you want to resolve the domain name @.exmaple.com, you must set Rr to @ instead of leaving Rr empty.
        # 
        # This parameter is required.
        self.rr = rr
        # The time to live (TTL) period. Valid values: 5, 30, 60, 3600, 43200, and 86400. Unit: seconds. Default value: 60.
        self.ttl = ttl
        # The type of the DNS record. Valid values:
        # 
        # *   **A**: An A record maps a domain name to an IPv4 address in the dotted decimal notation format.
        # *   **AAAA**: An AAAA record maps a domain name to an IPv6 address.
        # *   **CNAME**: A canonical name (CNAME) record maps a domain name to another domain name.
        # *   **TXT**: A text (TXT) record usually serves as a Sender Policy Framework (SPF) record to prevent email spam. The record value of the TXT record can be up to 255 characters in length.
        # *   **MX**: A mail exchanger (MX) record maps a domain name to the domain name of a mail server.
        # *   **PTR**: A pointer (PTR) record maps an IP address to a domain name.
        # *   **SRV**: A service (SRV) record specifies a server that hosts a specific service. Enter a record value in the format of Priority Weight Port Destination domain name. Separate these items with spaces.
        # 
        # >  Before you add a PTR record, you must configure a reverse lookup zone. For more information, see [Add PTR records](https://help.aliyun.com/document_detail/2592976.html).
        # 
        # This parameter is required.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The record value. You need to enter the record value based on the DNS record type.
        # 
        # This parameter is required.
        self.value = value
        # The weight value of the address. You can set a different weight value for each address. This way, addresses are returned based on the weight values for DNS requests. A weight value must be an integer that ranges from 1 to 100. Default value: 1.
        self.weight = weight
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line is not None:
            result['Line'] = self.line

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

