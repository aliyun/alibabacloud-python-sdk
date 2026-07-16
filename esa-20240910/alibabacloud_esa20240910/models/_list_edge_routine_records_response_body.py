# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListEdgeRoutineRecordsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListEdgeRoutineRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number, which is the same as the PageNumber request parameter.
        self.page_number = page_number
        # The number of records displayed per page.
        self.page_size = page_size
        # The list of records.
        self.records = records
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListEdgeRoutineRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEdgeRoutineRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        record_cname: str = None,
        record_name: str = None,
        site_id: int = None,
        site_name: str = None,
        update_time: str = None,
    ):
        # The creation time of the record. The time is in ISO 8601 format and displayed in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The CNAME of the record. When the site uses CNAME access, this is the CNAME value that needs to be configured for the record.
        self.record_cname = record_cname
        # The record name.
        self.record_name = record_name
        # The site ID.
        self.site_id = site_id
        # The name of the site to which the record belongs.
        self.site_name = site_name
        # The update time of the record. The time is in ISO 8601 format and displayed in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.record_cname is not None:
            result['RecordCname'] = self.record_cname

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RecordCname') is not None:
            self.record_cname = m.get('RecordCname')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

