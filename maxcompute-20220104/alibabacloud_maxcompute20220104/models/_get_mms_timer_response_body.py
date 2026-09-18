# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetMmsTimerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMmsTimerResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMmsTimerResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMmsTimerResponseBodyData(DaraModel):
    def __init__(
        self,
        config: main_models.GetMmsTimerResponseBodyDataConfig = None,
        create_time: str = None,
        db_id: int = None,
        id: int = None,
        name: str = None,
        schedule_type: str = None,
        source_id: int = None,
        src_db_name: str = None,
        stopped: bool = None,
        type: str = None,
        update_time: str = None,
        value: str = None,
    ):
        # The configuration of the migration job.
        self.config = config
        # The creation time of the scheduled task. This is a Unix timestamp in milliseconds.
        self.create_time = create_time
        # The ID of the source database.
        self.db_id = db_id
        # The ID of the scheduled task.
        self.id = id
        # The name of the scheduled task.
        self.name = name
        # The scheduling type of the scheduled task. Valid values: `Daily` and `Hourly`.
        self.schedule_type = schedule_type
        # The ID of the data source.
        self.source_id = source_id
        # The name of the source database.
        self.src_db_name = src_db_name
        # Indicates whether the scheduled task is stopped.
        self.stopped = stopped
        # The type of the scheduled task.
        self.type = type
        # The last update time of the scheduled task, in ISO 8601 format.
        self.update_time = update_time
        # The scheduling time. If `scheduleType` is `Daily`, the value is in the `HH:MM` format. If `scheduleType` is `Hourly`, the value is in the `MM` format.
        self.value = value

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.db_id is not None:
            result['dbId'] = self.db_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.stopped is not None:
            result['stopped'] = self.stopped

        if self.type is not None:
            result['type'] = self.type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetMmsTimerResponseBodyDataConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetMmsTimerResponseBodyDataConfig(DaraModel):
    def __init__(
        self,
        column_mapping: Dict[str, str] = None,
        enable_data_migration: bool = None,
        enable_schema_migration: bool = None,
        enable_verification: bool = None,
        others: Dict[str, Any] = None,
        partition_filters: Dict[str, str] = None,
        partitions: List[int] = None,
        table_black_list: List[str] = None,
        table_mapping: Dict[str, str] = None,
        table_white_list: List[str] = None,
        tables: List[str] = None,
    ):
        # A map of source column names to destination column names.
        self.column_mapping = column_mapping
        # Whether to migrate table data.
        self.enable_data_migration = enable_data_migration
        # Whether to migrate the table schema.
        self.enable_schema_migration = enable_schema_migration
        # Whether to enable verification. The system performs verification by running a `SELECT COUNT(*)` query on both the source and destination to compare the row count.
        self.enable_verification = enable_verification
        # Other configurations.
        self.others = others
        # A map of table names to their corresponding partition filter expressions.
        self.partition_filters = partition_filters
        # If `type` is set to `Partitions`, this parameter specifies a list of partition IDs to migrate.
        self.partitions = partitions
        # If `type` is set to `Database`, this parameter specifies a table deny list. Tables on this list are excluded from the migration.
        self.table_black_list = table_black_list
        # A map of source table names to destination table names.
        self.table_mapping = table_mapping
        # If `type` is set to `Database`, this parameter specifies a table allowlist. If this parameter is not specified, all tables in the database are migrated.
        self.table_white_list = table_white_list
        # If `type` is set to `Tables`, this parameter specifies a list of table names to migrate.
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_mapping is not None:
            result['columnMapping'] = self.column_mapping

        if self.enable_data_migration is not None:
            result['enableDataMigration'] = self.enable_data_migration

        if self.enable_schema_migration is not None:
            result['enableSchemaMigration'] = self.enable_schema_migration

        if self.enable_verification is not None:
            result['enableVerification'] = self.enable_verification

        if self.others is not None:
            result['others'] = self.others

        if self.partition_filters is not None:
            result['partitionFilters'] = self.partition_filters

        if self.partitions is not None:
            result['partitions'] = self.partitions

        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list

        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping

        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list

        if self.tables is not None:
            result['tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnMapping') is not None:
            self.column_mapping = m.get('columnMapping')

        if m.get('enableDataMigration') is not None:
            self.enable_data_migration = m.get('enableDataMigration')

        if m.get('enableSchemaMigration') is not None:
            self.enable_schema_migration = m.get('enableSchemaMigration')

        if m.get('enableVerification') is not None:
            self.enable_verification = m.get('enableVerification')

        if m.get('others') is not None:
            self.others = m.get('others')

        if m.get('partitionFilters') is not None:
            self.partition_filters = m.get('partitionFilters')

        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')

        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')

        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')

        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        return self

