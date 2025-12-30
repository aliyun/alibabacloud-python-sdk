# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeZoneRecordResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        line: str = None,
        priority: int = None,
        record_id: int = None,
        remark: str = None,
        request_id: str = None,
        rr: str = None,
        status: str = None,
        ttl: int = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The time when the DNS record was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the DNS record was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The resolution line.
        self.line = line
        # The priority of the mail exchanger (MX) record.
        self.priority = priority
        # The ID of the DNS record.
        self.record_id = record_id
        # The description of the DNS record.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The hostname.
        self.rr = rr
        # The state of the DNS record. Valid values:
        # 
        # *   **ENABLE**: The DNS record is enabled.
        # *   **DISABLE**: The DNS record is disabled.
        self.status = status
        # The time to live (TTL) of the DNS record.
        self.ttl = ttl
        # The type of the DNS record.
        self.type = type
        # The time when the DNS record was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the DNS record was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The record value.
        self.value = value
        # The weight value of the DNS record.
        self.weight = weight
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.line is not None:
            result['Line'] = self.line

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.status is not None:
            result['Status'] = self.status

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

