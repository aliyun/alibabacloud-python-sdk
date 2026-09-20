# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreTablesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        restore_full: main_models.DescribeRestoreTablesResponseBodyRestoreFull = None,
        restore_incr_detail: main_models.DescribeRestoreTablesResponseBodyRestoreIncrDetail = None,
        restore_schema: main_models.DescribeRestoreTablesResponseBodyRestoreSchema = None,
        restore_summary: main_models.DescribeRestoreTablesResponseBodyRestoreSummary = None,
        tables: main_models.DescribeRestoreTablesResponseBodyTables = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The full restore details.
        self.restore_full = restore_full
        # The incremental restore details.
        self.restore_incr_detail = restore_incr_detail
        # The schema restore details.
        self.restore_schema = restore_schema
        # The restore summary.
        self.restore_summary = restore_summary
        self.tables = tables

    def validate(self):
        if self.restore_full:
            self.restore_full.validate()
        if self.restore_incr_detail:
            self.restore_incr_detail.validate()
        if self.restore_schema:
            self.restore_schema.validate()
        if self.restore_summary:
            self.restore_summary.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_full is not None:
            result['RestoreFull'] = self.restore_full.to_map()

        if self.restore_incr_detail is not None:
            result['RestoreIncrDetail'] = self.restore_incr_detail.to_map()

        if self.restore_schema is not None:
            result['RestoreSchema'] = self.restore_schema.to_map()

        if self.restore_summary is not None:
            result['RestoreSummary'] = self.restore_summary.to_map()

        if self.tables is not None:
            result['Tables'] = self.tables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreFull') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreFull()
            self.restore_full = temp_model.from_map(m.get('RestoreFull'))

        if m.get('RestoreIncrDetail') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreIncrDetail()
            self.restore_incr_detail = temp_model.from_map(m.get('RestoreIncrDetail'))

        if m.get('RestoreSchema') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreSchema()
            self.restore_schema = temp_model.from_map(m.get('RestoreSchema'))

        if m.get('RestoreSummary') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreSummary()
            self.restore_summary = temp_model.from_map(m.get('RestoreSummary'))

        if m.get('Tables') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyTables()
            self.tables = temp_model.from_map(m.get('Tables'))

        return self

class DescribeRestoreTablesResponseBodyTables(DaraModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

class DescribeRestoreTablesResponseBodyRestoreSummary(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        record_id: str = None,
        restore_to_date: str = None,
        start_time: str = None,
        state: str = None,
        target_cluster: str = None,
    ):
        # The completion time.
        self.end_time = end_time
        # The record ID.
        self.record_id = record_id
        # The point in time to which data is restored.
        self.restore_to_date = restore_to_date
        # The restore start time.
        self.start_time = start_time
        # The status.
        self.state = state
        # The target cluster for the restore.
        self.target_cluster = target_cluster

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.restore_to_date is not None:
            result['RestoreToDate'] = self.restore_to_date

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RestoreToDate') is not None:
            self.restore_to_date = m.get('RestoreToDate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TargetCluster') is not None:
            self.target_cluster = m.get('TargetCluster')

        return self

class DescribeRestoreTablesResponseBodyRestoreSchema(DaraModel):
    def __init__(
        self,
        fail: int = None,
        page_number: int = None,
        page_size: int = None,
        restore_schema_details: main_models.DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails = None,
        succeed: int = None,
        total: int = None,
    ):
        # The number of failed restores.
        self.fail = fail
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        self.restore_schema_details = restore_schema_details
        # The number of successful restores.
        self.succeed = succeed
        # The total number of records.
        self.total = total

    def validate(self):
        if self.restore_schema_details:
            self.restore_schema_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail is not None:
            result['Fail'] = self.fail

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.restore_schema_details is not None:
            result['RestoreSchemaDetails'] = self.restore_schema_details.to_map()

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RestoreSchemaDetails') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails()
            self.restore_schema_details = temp_model.from_map(m.get('RestoreSchemaDetails'))

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails(DaraModel):
    def __init__(
        self,
        restore_schema_detail: List[main_models.DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail] = None,
    ):
        self.restore_schema_detail = restore_schema_detail

    def validate(self):
        if self.restore_schema_detail:
            for v1 in self.restore_schema_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RestoreSchemaDetail'] = []
        if self.restore_schema_detail is not None:
            for k1 in self.restore_schema_detail:
                result['RestoreSchemaDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_schema_detail = []
        if m.get('RestoreSchemaDetail') is not None:
            for k1 in m.get('RestoreSchemaDetail'):
                temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail()
                self.restore_schema_detail.append(temp_model.from_map(k1))

        return self

class DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        message: str = None,
        start_time: str = None,
        state: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.message = message
        self.start_time = start_time
        self.state = state
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.message is not None:
            result['Message'] = self.message

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

class DescribeRestoreTablesResponseBodyRestoreIncrDetail(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        process: str = None,
        restore_delay: str = None,
        restore_start_ts: str = None,
        restored_ts: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The completion progress.
        self.process = process
        # The synchronization latency.
        self.restore_delay = restore_delay
        # The synchronization start position.
        self.restore_start_ts = restore_start_ts
        # The synchronization position.
        self.restored_ts = restored_ts
        # The start time.
        self.start_time = start_time
        # The status.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.process is not None:
            result['Process'] = self.process

        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay

        if self.restore_start_ts is not None:
            result['RestoreStartTs'] = self.restore_start_ts

        if self.restored_ts is not None:
            result['RestoredTs'] = self.restored_ts

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')

        if m.get('RestoreStartTs') is not None:
            self.restore_start_ts = m.get('RestoreStartTs')

        if m.get('RestoredTs') is not None:
            self.restored_ts = m.get('RestoredTs')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeRestoreTablesResponseBodyRestoreFull(DaraModel):
    def __init__(
        self,
        data_size: str = None,
        fail: int = None,
        page_number: int = None,
        page_size: int = None,
        restore_full_details: main_models.DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails = None,
        speed: str = None,
        succeed: int = None,
        total: int = None,
    ):
        # The total data size.
        self.data_size = data_size
        # The number of failed full restores.
        self.fail = fail
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        self.restore_full_details = restore_full_details
        # The total speed.
        self.speed = speed
        # The number of successful restores.
        self.succeed = succeed
        # The total number of records.
        self.total = total

    def validate(self):
        if self.restore_full_details:
            self.restore_full_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.restore_full_details is not None:
            result['RestoreFullDetails'] = self.restore_full_details.to_map()

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RestoreFullDetails') is not None:
            temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails()
            self.restore_full_details = temp_model.from_map(m.get('RestoreFullDetails'))

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails(DaraModel):
    def __init__(
        self,
        restore_full_detail: List[main_models.DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail] = None,
    ):
        self.restore_full_detail = restore_full_detail

    def validate(self):
        if self.restore_full_detail:
            for v1 in self.restore_full_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RestoreFullDetail'] = []
        if self.restore_full_detail is not None:
            for k1 in self.restore_full_detail:
                result['RestoreFullDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_full_detail = []
        if m.get('RestoreFullDetail') is not None:
            for k1 in m.get('RestoreFullDetail'):
                temp_model = main_models.DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail()
                self.restore_full_detail.append(temp_model.from_map(k1))

        return self

class DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail(DaraModel):
    def __init__(
        self,
        data_size: str = None,
        end_time: str = None,
        message: str = None,
        process: str = None,
        speed: str = None,
        start_time: str = None,
        state: str = None,
        table: str = None,
    ):
        self.data_size = data_size
        self.end_time = end_time
        self.message = message
        self.process = process
        self.speed = speed
        self.start_time = start_time
        self.state = state
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.message is not None:
            result['Message'] = self.message

        if self.process is not None:
            result['Process'] = self.process

        if self.speed is not None:
            result['Speed'] = self.speed

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

