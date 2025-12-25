# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class SearchDataTrackResultResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        track_result: main_models.SearchDataTrackResultResponseBodyTrackResult = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The parsing result of the data tracking task.
        self.track_result = track_result

    def validate(self):
        if self.track_result:
            self.track_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.track_result is not None:
            result['TrackResult'] = self.track_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TrackResult') is not None:
            temp_model = main_models.SearchDataTrackResultResponseBodyTrackResult()
            self.track_result = temp_model.from_map(m.get('TrackResult'))

        return self

class SearchDataTrackResultResponseBodyTrackResult(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.SearchDataTrackResultResponseBodyTrackResultEventList] = None,
        table_info_list: List[main_models.SearchDataTrackResultResponseBodyTrackResultTableInfoList] = None,
        total_count: int = None,
    ):
        # The details of the event logs.
        self.event_list = event_list
        # The metadata of tables for which you track data operations.
        self.table_info_list = table_info_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()
        if self.table_info_list:
            for v1 in self.table_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k1 in self.table_info_list:
                result['TableInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.SearchDataTrackResultResponseBodyTrackResultEventList()
                self.event_list.append(temp_model.from_map(k1))

        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k1 in m.get('TableInfoList'):
                temp_model = main_models.SearchDataTrackResultResponseBodyTrackResultTableInfoList()
                self.table_info_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchDataTrackResultResponseBodyTrackResultTableInfoList(DaraModel):
    def __init__(
        self,
        columns: List[main_models.SearchDataTrackResultResponseBodyTrackResultTableInfoListColumns] = None,
        description: str = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        # The information about columns.
        self.columns = columns
        # The description of the column.
        self.description = description
        # The name of the database.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.SearchDataTrackResultResponseBodyTrackResultTableInfoListColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class SearchDataTrackResultResponseBodyTrackResultTableInfoListColumns(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_position: int = None,
        column_type: str = None,
        fictive: bool = None,
    ):
        # The name of the column.
        self.column_name = column_name
        # The position of the column.
        self.column_position = column_position
        # The data type of the column. Examples: BIGINT, INT, and VARCHAR.
        self.column_type = column_type
        # Indicates whether the column is a virtual column. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fictive = fictive

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_position is not None:
            result['ColumnPosition'] = self.column_position

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.fictive is not None:
            result['Fictive'] = self.fictive

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnPosition') is not None:
            self.column_position = m.get('ColumnPosition')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Fictive') is not None:
            self.fictive = m.get('Fictive')

        return self

class SearchDataTrackResultResponseBodyTrackResultEventList(DaraModel):
    def __init__(
        self,
        data_after: List[str] = None,
        data_before: List[str] = None,
        event_id: int = None,
        event_length: int = None,
        event_timestamp: str = None,
        event_type: str = None,
        roll_sql: str = None,
    ):
        # The data records after you perform data operations in the database.
        self.data_after = data_after
        # The data records before you perform data operations in the database.
        self.data_before = data_before
        # The ID of the event.
        self.event_id = event_id
        # The length of the event content. Unit: bytes.
        self.event_length = event_length
        # The event time.
        self.event_timestamp = event_timestamp
        # The type of the event. Valid values:
        # 
        # *   **WRITE_ROWS**: indicates an INSERT operation.
        # *   **UPDATE_ROWS**: indicates an UPDATE operation.
        # *   **DELETE_ROWS**: indicates a DELETE operation.
        # *   **EXT_WRITE_ROWS**: indicates an INSERT operation, which is equivalent to WRITE_ROWS.
        # *   **EXT_UPDATE_ROWS**: indicates an UPDATE operation, which is equivalent to UPDATE_ROWS.
        # *   **EXT_DELETE_ROWS**: indicates a DELETE operation, which is equivalent to DELETE_ROWS.
        self.event_type = event_type
        # The SQL statements used to roll back the data change.
        self.roll_sql = roll_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_after is not None:
            result['DataAfter'] = self.data_after

        if self.data_before is not None:
            result['DataBefore'] = self.data_before

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_length is not None:
            result['EventLength'] = self.event_length

        if self.event_timestamp is not None:
            result['EventTimestamp'] = self.event_timestamp

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.roll_sql is not None:
            result['RollSQL'] = self.roll_sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataAfter') is not None:
            self.data_after = m.get('DataAfter')

        if m.get('DataBefore') is not None:
            self.data_before = m.get('DataBefore')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventLength') is not None:
            self.event_length = m.get('EventLength')

        if m.get('EventTimestamp') is not None:
            self.event_timestamp = m.get('EventTimestamp')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('RollSQL') is not None:
            self.roll_sql = m.get('RollSQL')

        return self

