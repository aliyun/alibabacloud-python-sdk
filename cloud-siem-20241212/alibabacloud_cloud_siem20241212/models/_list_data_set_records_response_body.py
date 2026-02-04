# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListDataSetRecordsResponseBody(DaraModel):
    def __init__(
        self,
        data_set_records: List[main_models.ListDataSetRecordsResponseBodyDataSetRecords] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_set_records = data_set_records
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_set_records:
            for v1 in self.data_set_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSetRecords'] = []
        if self.data_set_records is not None:
            for k1 in self.data_set_records:
                result['DataSetRecords'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.data_set_records = []
        if m.get('DataSetRecords') is not None:
            for k1 in m.get('DataSetRecords'):
                temp_model = main_models.ListDataSetRecordsResponseBodyDataSetRecords()
                self.data_set_records.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataSetRecordsResponseBodyDataSetRecords(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        data_set_id: str = None,
        data_set_name: str = None,
        data_set_record_id: str = None,
        data_set_record_values: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.data_set_record_id = data_set_record_id
        self.data_set_record_values = data_set_record_values
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

        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name

        if self.data_set_record_id is not None:
            result['DataSetRecordId'] = self.data_set_record_id

        if self.data_set_record_values is not None:
            result['DataSetRecordValues'] = self.data_set_record_values

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')

        if m.get('DataSetRecordId') is not None:
            self.data_set_record_id = m.get('DataSetRecordId')

        if m.get('DataSetRecordValues') is not None:
            self.data_set_record_values = m.get('DataSetRecordValues')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

