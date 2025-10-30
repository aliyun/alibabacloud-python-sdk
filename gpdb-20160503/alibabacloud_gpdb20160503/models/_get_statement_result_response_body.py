# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetStatementResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetStatementResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The result of the asynchronous call.
        self.data = data
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # API execution status, with values as follows:
        # 
        # - **false**: Execution failed.
        # - **true**: Execution succeeded.
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetStatementResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetStatementResultResponseBodyData(DaraModel):
    def __init__(
        self,
        column_metadata: main_models.GetStatementResultResponseBodyDataColumnMetadata = None,
        records: main_models.GetStatementResultResponseBodyDataRecords = None,
        total_num_rows: int = None,
    ):
        # List of column metadata.
        self.column_metadata = column_metadata
        # Multiple rows of data.
        self.records = records
        # Total number of entries.
        self.total_num_rows = total_num_rows

    def validate(self):
        if self.column_metadata:
            self.column_metadata.validate()
        if self.records:
            self.records.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_metadata is not None:
            result['ColumnMetadata'] = self.column_metadata.to_map()

        if self.records is not None:
            result['Records'] = self.records.to_map()

        if self.total_num_rows is not None:
            result['TotalNumRows'] = self.total_num_rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnMetadata') is not None:
            temp_model = main_models.GetStatementResultResponseBodyDataColumnMetadata()
            self.column_metadata = temp_model.from_map(m.get('ColumnMetadata'))

        if m.get('Records') is not None:
            temp_model = main_models.GetStatementResultResponseBodyDataRecords()
            self.records = temp_model.from_map(m.get('Records'))

        if m.get('TotalNumRows') is not None:
            self.total_num_rows = m.get('TotalNumRows')

        return self

class GetStatementResultResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        records: List[main_models.GetStatementResultResponseBodyDataRecordsRecords] = None,
    ):
        self.records = records

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
        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.GetStatementResultResponseBodyDataRecordsRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class GetStatementResultResponseBodyDataRecordsRecords(DaraModel):
    def __init__(
        self,
        record: List[main_models.Field] = None,
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
                temp_model = main_models.Field()
                self.record.append(temp_model.from_map(k1))

        return self

class GetStatementResultResponseBodyDataColumnMetadata(DaraModel):
    def __init__(
        self,
        column_metadata: List[main_models.ColumnMetadata] = None,
    ):
        self.column_metadata = column_metadata

    def validate(self):
        if self.column_metadata:
            for v1 in self.column_metadata:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnMetadata'] = []
        if self.column_metadata is not None:
            for k1 in self.column_metadata:
                result['ColumnMetadata'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_metadata = []
        if m.get('ColumnMetadata') is not None:
            for k1 in m.get('ColumnMetadata'):
                temp_model = main_models.ColumnMetadata()
                self.column_metadata.append(temp_model.from_map(k1))

        return self

