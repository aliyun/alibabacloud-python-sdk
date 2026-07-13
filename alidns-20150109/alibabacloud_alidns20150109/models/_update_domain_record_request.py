# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDomainRecordRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        line: str = None,
        priority: int = None,
        rr: str = None,
        record_id: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
    ):
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The resolution line. The default value is **default**.
        # For more information, see
        # <props="china">[Enumeration of resolution lines](https://help.aliyun.com/document_detail/29807.html).
        # <props="intl">[Enumeration of resolution lines](https://www.alibabacloud.com/help/en/doc-detail/29807.htm).
        self.line = line
        # The priority of the MX record. Valid values: `[1, 50]`.
        # 
        # This parameter is required if the record type is MX.
        self.priority = priority
        # The host record.
        # To resolve the root domain, such as example.com, set the host record to the at sign (@).
        # 
        # This parameter is required.
        self.rr = rr
        # The ID of the DNS record. To obtain the ID, call the [DescribeDomainRecords](https://help.aliyun.com/document_detail/2357159.html) operation.
        # 
        # This parameter is required.
        self.record_id = record_id
        # The time to live (TTL). The default value is 600 seconds (10 minutes).
        # For more information, see
        # <props="china">[TTL definition](https://help.aliyun.com/document_detail/29806.html).
        # <props="intl">[TTL definition](https://www.alibabacloud.com/help/en/doc-detail/29806.htm).
        self.ttl = ttl
        # The type of the DNS record. For more information, see
        # <props="china">[DNS record types](https://help.aliyun.com/document_detail/29805.html).
        # <props="intl">[DNS record types](https://www.alibabacloud.com/help/en/doc-detail/29805.htm).
        # 
        # This parameter is required.
        self.type = type
        # The client IP address.
        self.user_client_ip = user_client_ip
        # The record value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line is not None:
            result['Line'] = self.line

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rr is not None:
            result['RR'] = self.rr

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

