# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRecursionRecordRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        priority: int = None,
        request_source: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # A client token to ensure the idempotence of the request. Generate a unique value on your client. The token must be unique for each request. It can contain only ASCII characters and must not exceed 64 characters in length.
        self.client_token = client_token
        # The priority of the MX record. A smaller value indicates a higher priority. Valid values: 1 to 99.
        self.priority = priority
        # The DNS resolution line. The default value is **default**. For more information, see:
        # 
        # <props="china">
        # 
        # [DNS resolution lines](https://help.aliyun.com/document_detail/29807.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [DNS resolution lines](https://www.alibabacloud.com/help/en/doc-detail/29807.htm)
        self.request_source = request_source
        # The host record. The host record is the prefix of a domain name. Common examples include www, @, \\* (for wildcard DNS), and mail (for mailboxes).
        # 
        # For example, to resolve @.example.com, set the host record to "@", not an empty string.
        self.rr = rr
        # The time to live (TTL) in seconds. This is the duration for which the record is cached. Supported values: 5, 30, 60, 3600 (1 hour), 43200 (12 hours), and 86400 (24 hours). Default value: 60.
        self.ttl = ttl
        # The type of the DNS record. The following record types are supported: A: An IPv4 record that maps a domain name to an IPv4 address. AAAA: An IPv6 record that maps a domain name to an IPv6 address. CNAME: A canonical name record that points a domain name to another domain name. MX: A mail exchanger record that points a domain name to a mail server address. TXT: A text record that contains any human-readable text. SRV: A service record that identifies a server that provides a specific service. This is common in directory management for Microsoft systems. NS: A name server record that delegates a subdomain to another DNS provider for resolution. CAA: A Certification Authority Authorization record that restricts which certification authorities (CAs) can issue certificates for a domain. URL: A URL record that points a domain name to an existing site. SVCB: A service binding record that is used for service discovery. It provides information about supported protocols and service parameters through a DNS record. HTTPS: A record type specific to HTTPS services. An HTTPS record can define secure HTTPS connection protocols and optimal service endpoint addresses.
        self.type = type
        # The client IP address.
        self.user_client_ip = user_client_ip
        # The record value. Enter a value that corresponds to the specified record type.
        self.value = value
        # The weight of the record. Valid values are integers from 1 to 100. The default value is 1. Set different weights for each address. DNS queries then return addresses based on the specified weight ratio.
        self.weight = weight
        # The ID of the zone.
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

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

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

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

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

