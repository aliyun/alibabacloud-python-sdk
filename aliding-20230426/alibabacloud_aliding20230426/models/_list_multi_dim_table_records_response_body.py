# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListMultiDimTableRecordsResponseBody(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: str = None,
        records: List[main_models.ListMultiDimTableRecordsResponseBodyRecords] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        self.records = records
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.ListMultiDimTableRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListMultiDimTableRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        created_by: main_models.ListMultiDimTableRecordsResponseBodyRecordsCreatedBy = None,
        created_time: int = None,
        fields: Dict[str, Any] = None,
        id: str = None,
        last_modified_by: main_models.ListMultiDimTableRecordsResponseBodyRecordsLastModifiedBy = None,
        last_modified_time: int = None,
    ):
        self.created_by = created_by
        self.created_time = created_time
        self.fields = fields
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_time = last_modified_time

    def validate(self):
        if self.created_by:
            self.created_by.validate()
        if self.last_modified_by:
            self.last_modified_by.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by.to_map()

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.fields is not None:
            result['Fields'] = self.fields

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by.to_map()

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            temp_model = main_models.ListMultiDimTableRecordsResponseBodyRecordsCreatedBy()
            self.created_by = temp_model.from_map(m.get('CreatedBy'))

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifiedBy') is not None:
            temp_model = main_models.ListMultiDimTableRecordsResponseBodyRecordsLastModifiedBy()
            self.last_modified_by = temp_model.from_map(m.get('LastModifiedBy'))

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        return self

class ListMultiDimTableRecordsResponseBodyRecordsLastModifiedBy(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListMultiDimTableRecordsResponseBodyRecordsCreatedBy(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

