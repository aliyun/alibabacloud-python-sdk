# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionRecordWeightEnableStatusRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enable_status: str = None,
        request_source: str = None,
        rr: str = None,
        type: str = None,
        zone_id: str = None,
    ):
        # A client token that is used to ensure the idempotence of a request. The client generates the value of this parameter. The value must be unique for each request and can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # Specifies whether to enable the weight algorithm. Valid values: \\*\\*enable\\*\\* and \\*\\*disable\\*\\*.
        self.enable_status = enable_status
        # The DNS resolution line. The default value is **default**. For more information, see [DNS resolution lines](https://help.aliyun.com/document_detail/29807.html).
        # 
        # <props="china">
        # 
        # [Resolution Line Enumeration](https://help.aliyun.com/document_detail/29807.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [Enumeration of DNS record lines](https://www.alibabacloud.com/help/zh/doc-detail/29807.htm)
        self.request_source = request_source
        # The host record.
        self.rr = rr
        # The type of the DNS record. The following types are supported: \\*\\*A\\*\\*, which maps a domain name to an IPv4 address. \\*\\*AAAA\\*\\*, which maps a domain name to an IPv6 address. \\*\\*CNAME\\*\\*, an alias record that points a domain name to another domain name. \\*\\*MX\\*\\*, a mail exchanger record that points a domain name to a mail server address. \\*\\*TXT\\*\\*, an arbitrary, human-readable text DNS record. \\*\\*SRV\\*\\*, a service record that identifies a server that provides a specific service, commonly used for directory management in Microsoft systems.
        self.type = type
        # The zone ID for the domain name.
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

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.type is not None:
            result['Type'] = self.type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

