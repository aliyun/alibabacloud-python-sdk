# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ExecuteStatementResponseBody(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        dbinstance_id: str = None,
        data: main_models.ExecuteStatementResponseBodyData = None,
        database: str = None,
        id: str = None,
        message: str = None,
        request_id: str = None,
        secret_arn: str = None,
        status: str = None,
    ):
        # The time when the SQL statements were created.
        self.created_at = created_at
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The returned results of the synchronous call.
        self.data = data
        # The name of the database.
        self.database = database
        # The ID of the job for asynchronously executing the SQL statements.
        self.id = id
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ARN of the access credential for the created Data API account.
        self.secret_arn = secret_arn
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.database is not None:
            result['Database'] = self.database

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Data') is not None:
            temp_model = main_models.ExecuteStatementResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ExecuteStatementResponseBodyData(DaraModel):
    def __init__(
        self,
        column_metadata: main_models.ExecuteStatementResponseBodyDataColumnMetadata = None,
        records: main_models.ExecuteStatementResponseBodyDataRecords = None,
        total_num_rows: int = None,
    ):
        # The metadata of the columns.
        self.column_metadata = column_metadata
        # The rows of data.
        self.records = records
        # The total number of entries returned.
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
            temp_model = main_models.ExecuteStatementResponseBodyDataColumnMetadata()
            self.column_metadata = temp_model.from_map(m.get('ColumnMetadata'))

        if m.get('Records') is not None:
            temp_model = main_models.ExecuteStatementResponseBodyDataRecords()
            self.records = temp_model.from_map(m.get('Records'))

        if m.get('TotalNumRows') is not None:
            self.total_num_rows = m.get('TotalNumRows')

        return self

class ExecuteStatementResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        records: List[main_models.ExecuteStatementResponseBodyDataRecordsRecords] = None,
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
                temp_model = main_models.ExecuteStatementResponseBodyDataRecordsRecords()
                self.records.append(temp_model.from_map(k1))

        return self

class ExecuteStatementResponseBodyDataRecordsRecords(DaraModel):
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

class ExecuteStatementResponseBodyDataColumnMetadata(DaraModel):
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

