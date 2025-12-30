# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeSubDomainRecordsResponseBody(DaraModel):
    def __init__(
        self,
        domain_records: main_models.DescribeSubDomainRecordsResponseBodyDomainRecords = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned Domain Name System (DNS) records.
        self.domain_records = domain_records
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domain_records:
            self.domain_records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_records is not None:
            result['DomainRecords'] = self.domain_records.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainRecords') is not None:
            temp_model = main_models.DescribeSubDomainRecordsResponseBodyDomainRecords()
            self.domain_records = temp_model.from_map(m.get('DomainRecords'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSubDomainRecordsResponseBodyDomainRecords(DaraModel):
    def __init__(
        self,
        record: List[main_models.DescribeSubDomainRecordsResponseBodyDomainRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        if self.record:
            for v1 in self.record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Record'] = []
        if self.record is not None:
            for k1 in self.record:
                result['Record'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k1 in m.get('Record'):
                temp_model = main_models.DescribeSubDomainRecordsResponseBodyDomainRecordsRecord()
                self.record.append(temp_model.from_map(k1))

        return self

class DescribeSubDomainRecordsResponseBodyDomainRecordsRecord(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        line: str = None,
        locked: bool = None,
        priority: int = None,
        rr: str = None,
        record_id: str = None,
        remark: str = None,
        status: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
        weight: int = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The DNS resolution line.
        self.line = line
        # The lock status of the DNS record.
        self.locked = locked
        # The priority of the mail exchanger (MX) record.
        self.priority = priority
        # The hostname.
        self.rr = rr
        # The ID of the DNS record.
        self.record_id = record_id
        # The description of the DNS record.
        self.remark = remark
        # The status of the DNS record.
        self.status = status
        # The time-to-live (TTL) of the DNS record.
        self.ttl = ttl
        # The type of the DNS record.
        self.type = type
        # The record value.
        self.value = value
        # The weight of the DNS record.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.line is not None:
            result['Line'] = self.line

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rr is not None:
            result['RR'] = self.rr

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

