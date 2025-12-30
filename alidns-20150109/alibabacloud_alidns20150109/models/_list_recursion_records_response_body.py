# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListRecursionRecordsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        records: main_models.ListRecursionRecordsResponseBodyRecords = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_items = total_items
        self.total_pages = total_pages

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.records is not None:
            result['Records'] = self.records.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Records') is not None:
            temp_model = main_models.ListRecursionRecordsResponseBodyRecords()
            self.records = temp_model.from_map(m.get('Records'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListRecursionRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        record: List[main_models.ListRecursionRecordsResponseBodyRecordsRecord] = None,
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
                temp_model = main_models.ListRecursionRecordsResponseBodyRecordsRecord()
                self.record.append(temp_model.from_map(k1))

        return self

class ListRecursionRecordsResponseBodyRecordsRecord(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: int = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        enable_status: str = None,
        priority: int = None,
        record_id: str = None,
        remark: str = None,
        request_source: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.creator = creator
        self.creator_sub_type = creator_sub_type
        self.creator_type = creator_type
        self.enable_status = enable_status
        self.priority = priority
        self.record_id = record_id
        self.remark = remark
        self.request_source = request_source
        self.rr = rr
        self.ttl = ttl
        self.type = type
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.value = value
        self.weight = weight
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

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.rr is not None:
            result['Rr'] = self.rr

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

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

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

