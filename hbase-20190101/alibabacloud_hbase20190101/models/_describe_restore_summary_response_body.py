# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreSummaryResponseBody(DaraModel):
    def __init__(
        self,
        has_more_restore_record: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rescords: main_models.DescribeRestoreSummaryResponseBodyRescords = None,
        total: int = None,
    ):
        # Indicates whether there is a next page. This parameter is currently not used.
        self.has_more_restore_record = has_more_restore_record
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.rescords = rescords
        # The total number of records.
        self.total = total

    def validate(self):
        if self.rescords:
            self.rescords.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more_restore_record is not None:
            result['HasMoreRestoreRecord'] = self.has_more_restore_record

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rescords is not None:
            result['Rescords'] = self.rescords.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMoreRestoreRecord') is not None:
            self.has_more_restore_record = m.get('HasMoreRestoreRecord')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rescords') is not None:
            temp_model = main_models.DescribeRestoreSummaryResponseBodyRescords()
            self.rescords = temp_model.from_map(m.get('Rescords'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRestoreSummaryResponseBodyRescords(DaraModel):
    def __init__(
        self,
        rescord: List[main_models.DescribeRestoreSummaryResponseBodyRescordsRescord] = None,
    ):
        self.rescord = rescord

    def validate(self):
        if self.rescord:
            for v1 in self.rescord:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rescord'] = []
        if self.rescord is not None:
            for k1 in self.rescord:
                result['Rescord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rescord = []
        if m.get('Rescord') is not None:
            for k1 in m.get('Rescord'):
                temp_model = main_models.DescribeRestoreSummaryResponseBodyRescordsRescord()
                self.rescord.append(temp_model.from_map(k1))

        return self

class DescribeRestoreSummaryResponseBodyRescordsRescord(DaraModel):
    def __init__(
        self,
        bulk_load_process: str = None,
        create_time: str = None,
        finish_time: str = None,
        hfile_restore_process: str = None,
        log_process: str = None,
        record_id: str = None,
        schema_process: str = None,
        status: str = None,
    ):
        self.bulk_load_process = bulk_load_process
        self.create_time = create_time
        self.finish_time = finish_time
        self.hfile_restore_process = hfile_restore_process
        self.log_process = log_process
        self.record_id = record_id
        self.schema_process = schema_process
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bulk_load_process is not None:
            result['BulkLoadProcess'] = self.bulk_load_process

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.hfile_restore_process is not None:
            result['HfileRestoreProcess'] = self.hfile_restore_process

        if self.log_process is not None:
            result['LogProcess'] = self.log_process

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.schema_process is not None:
            result['SchemaProcess'] = self.schema_process

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BulkLoadProcess') is not None:
            self.bulk_load_process = m.get('BulkLoadProcess')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('HfileRestoreProcess') is not None:
            self.hfile_restore_process = m.get('HfileRestoreProcess')

        if m.get('LogProcess') is not None:
            self.log_process = m.get('LogProcess')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SchemaProcess') is not None:
            self.schema_process = m.get('SchemaProcess')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

