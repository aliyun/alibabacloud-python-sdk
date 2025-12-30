# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainRecordInfoResponseBody(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_name: str = None,
        group_id: str = None,
        group_name: str = None,
        line: str = None,
        locked: bool = None,
        priority: int = None,
        puny_code: str = None,
        rr: str = None,
        record_id: str = None,
        remark: str = None,
        request_id: str = None,
        status: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
    ):
        # The ID of the domain name.
        self.domain_id = domain_id
        # The domain name.
        self.domain_name = domain_name
        # The ID of the domain name group.
        self.group_id = group_id
        # The name of the domain name group.
        self.group_name = group_name
        # The DNS resolution line.
        self.line = line
        # The lock state of the DNS record. Valid values: **true and false**.
        self.locked = locked
        # The priority of the mail exchanger (MX) record.
        self.priority = priority
        # The Punycode for the domain name. This parameter is returned only for Chinese domain names.
        self.puny_code = puny_code
        # The hostname.
        self.rr = rr
        # The ID of the DNS record.
        self.record_id = record_id
        # The description of your DNS record.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The status of the DNS record. Valid values:
        # 
        # Enable: enabled
        # 
        # Disable: disabled
        self.status = status
        # The time for which the DNS record is cached in a local DNS system.
        self.ttl = ttl
        # The type of the DNS record.
        self.type = type
        # The record value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.line is not None:
            result['Line'] = self.line

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.puny_code is not None:
            result['PunyCode'] = self.puny_code

        if self.rr is not None:
            result['RR'] = self.rr

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PunyCode') is not None:
            self.puny_code = m.get('PunyCode')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

