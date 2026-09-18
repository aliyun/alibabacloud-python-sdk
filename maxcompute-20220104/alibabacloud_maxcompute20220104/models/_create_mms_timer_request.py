# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class CreateMmsTimerRequest(DaraModel):
    def __init__(
        self,
        column_mapping: Dict[str, str] = None,
        enable_data_migration: bool = None,
        enable_schema_migration: bool = None,
        enable_verification: bool = None,
        name: str = None,
        others: Dict[str, Any] = None,
        partition_filters: Dict[str, str] = None,
        partitions: List[int] = None,
        schedule_type: str = None,
        source_id: int = None,
        src_db_name: str = None,
        table_black_list: List[str] = None,
        table_mapping: Dict[str, str] = None,
        table_white_list: List[str] = None,
        tables: List[str] = None,
        value: str = None,
    ):
        # A map of source column names to target column names.
        self.column_mapping = column_mapping
        # Specifies whether to migrate table data.
        self.enable_data_migration = enable_data_migration
        # Specifies whether to migrate the table schema.
        self.enable_schema_migration = enable_schema_migration
        # Specifies whether to enable data verification. If set to `true`, the system runs a `SELECT COUNT(*)` query on both the source and target tables and compares the row counts.
        self.enable_verification = enable_verification
        # The name of the scheduled task.
        self.name = name
        # Other configuration settings.
        self.others = others
        # A map of table names to their corresponding partition filter expressions.
        self.partition_filters = partition_filters
        # A list of IDs for the table partitions to migrate. This parameter takes effect only when the `type` parameter is set to `Partitions`.
        self.partitions = partitions
        # The schedule type for the task.
        self.schedule_type = schedule_type
        # The ID of the data source.
        self.source_id = source_id
        # The name of the source database.
        self.src_db_name = src_db_name
        # A blacklist of tables to exclude from the migration. This parameter takes effect only when the `type` parameter is set to `Database`.
        self.table_black_list = table_black_list
        # A map of source table names to target table names.
        self.table_mapping = table_mapping
        # A whitelist of tables to migrate. This parameter takes effect only when the `type` parameter is set to `Database`. If omitted, all tables in the source database are migrated.
        self.table_white_list = table_white_list
        # A list of table names to migrate. This parameter takes effect only when the `type` parameter is set to `Tables`.
        self.tables = tables
        # The time to run the scheduled task. If `scheduleType` is set to `Daily`, the value is the time in `HH:MM` format. If `scheduleType` is set to `Hourly`, the value is the minute of the hour (`MM`).
        self.value = value

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

        if self.name is not None:
            result['name'] = self.name

        if self.others is not None:
            result['others'] = self.others

        if self.partition_filters is not None:
            result['partitionFilters'] = self.partition_filters

        if self.partitions is not None:
            result['partitions'] = self.partitions

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name

        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list

        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping

        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list

        if self.tables is not None:
            result['tables'] = self.tables

        if self.value is not None:
            result['value'] = self.value

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

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('others') is not None:
            self.others = m.get('others')

        if m.get('partitionFilters') is not None:
            self.partition_filters = m.get('partitionFilters')

        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')

        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')

        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')

        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

