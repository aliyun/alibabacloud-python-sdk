# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionRecordRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        priority: int = None,
        record_id: str = None,
        request_source: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
        weight: int = None,
    ):
        # A client token that ensures the idempotence of a request. Generate a unique value for this parameter on your client. The value can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # The priority of the MX record. A smaller value indicates a higher priority. The value can be an integer from 1 to 99.
        self.priority = priority
        # The ID of the DNS record.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The resolution line. The default value is **default**. For more information, see:
        # 
        # <props="china">
        # 
        # [Lines](https://help.aliyun.com/document_detail/29807.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [Lines](https://www.alibabacloud.com/help/en/doc-detail/29807.htm)
        self.request_source = request_source
        # The host record. This is the prefix of a domain name. Common prefixes are www, @, \\* for wildcard DNS, and mail for mailboxes.
        # 
        # For example, to resolve @.example.com, set the host record to "@". Do not leave it empty.
        self.rr = rr
        # The Time to Live (TTL) in seconds. Only the following values are supported: 5, 30, 60, 3600 (1 hour), 43200 (12 hours), and 86400 (24 hours). The default value is 60.
        self.ttl = ttl
        # The type of the DNS record. The following types are supported: A: An IPv4 record that maps a domain name to an IPv4 address. AAAA: An IPv6 record that maps a domain name to an IPv6 address. CNAME: An alias record that points a domain name to another domain name. MX: A mail exchanger record that points a domain name to a mail server address. TXT: A text record that contains arbitrary human-readable text. SRV: A service record that identifies a server for a specific service. This is common in directory management for Microsoft systems.
        self.type = type
        # The record value. Enter a value that corresponds to the DNS record type.
        self.value = value
        # The weight. An integer from 1 to 100, inclusive. The default value is 1. You can set different weights for each address. DNS queries return addresses in proportion to their weights.
        self.weight = weight

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

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

