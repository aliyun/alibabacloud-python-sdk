# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStreamingJobShrinkRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        consistency: str = None,
        dbinstance_id: str = None,
        data_source_id: str = None,
        dest_columns_shrink: str = None,
        dest_database: str = None,
        dest_schema: str = None,
        dest_table: str = None,
        error_limit_count: int = None,
        fallback_offset: str = None,
        group_name: str = None,
        job_config: str = None,
        job_description: str = None,
        job_name: str = None,
        match_columns_shrink: str = None,
        mode: str = None,
        password: str = None,
        region_id: str = None,
        src_columns_shrink: str = None,
        try_run: bool = None,
        update_columns_shrink: str = None,
        write_mode: str = None,
    ):
        # The account for the destination database.
        self.account = account
        # The delivery guarantee.
        self.consistency = consistency
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The list of mapped fields in the destination table.
        self.dest_columns_shrink = dest_columns_shrink
        # The name of the destination database.
        self.dest_database = dest_database
        # The destination namespace.
        self.dest_schema = dest_schema
        # The name of the destination table.
        self.dest_table = dest_table
        # The maximum number of allowed error rows. When data in Kafka does not match the destination AnalyticDB for PostgreSQL table, a write failure occurs. If the number of error rows exceeds this value, the task fails.
        self.error_limit_count = error_limit_count
        # The fallback offset.
        # 
        # - The FallbackOffset parameter defines the behavior when a consumer does not request a specific offset to consume, or when the requested offset exceeds the offset range recorded in the current Kafka cluster. You can choose to start consuming from the earliest or latest offset.
        self.fallback_offset = fallback_offset
        # The name of the Kafka group.
        self.group_name = group_name
        # The task configuration file. This parameter is required in professional mode.
        self.job_config = job_config
        # The task description.
        self.job_description = job_description
        # The task name.
        # 
        # This parameter is required.
        self.job_name = job_name
        # The match columns. Typically, these are all the primary key columns of the destination table. If the values of all columns in this configuration are the same, the two rows of data are considered duplicate.
        self.match_columns_shrink = match_columns_shrink
        # The configuration mode.
        # 1. The basic mode requires you to specify certain configuration fields.
        # 2. The professional mode supports submitting a YAML file.
        self.mode = mode
        # The password for the destination database.
        self.password = password
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        self.region_id = region_id
        # The list of source data fields.
        self.src_columns_shrink = src_columns_shrink
        # Specifies whether to test the real-time task. Valid values:
        # 
        # - true
        # 
        # - false
        # 
        # Default value: false.
        self.try_run = try_run
        # The update columns. Typically, these are all the non-primary key columns of the destination table. When duplicate data is identified based on MatchColumns, updating the values of the UpdateColumns overwrites the old data with the new data.
        self.update_columns_shrink = update_columns_shrink
        # The write mode.
        self.write_mode = write_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.consistency is not None:
            result['Consistency'] = self.consistency

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.dest_columns_shrink is not None:
            result['DestColumns'] = self.dest_columns_shrink

        if self.dest_database is not None:
            result['DestDatabase'] = self.dest_database

        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema

        if self.dest_table is not None:
            result['DestTable'] = self.dest_table

        if self.error_limit_count is not None:
            result['ErrorLimitCount'] = self.error_limit_count

        if self.fallback_offset is not None:
            result['FallbackOffset'] = self.fallback_offset

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.job_config is not None:
            result['JobConfig'] = self.job_config

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.match_columns_shrink is not None:
            result['MatchColumns'] = self.match_columns_shrink

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.src_columns_shrink is not None:
            result['SrcColumns'] = self.src_columns_shrink

        if self.try_run is not None:
            result['TryRun'] = self.try_run

        if self.update_columns_shrink is not None:
            result['UpdateColumns'] = self.update_columns_shrink

        if self.write_mode is not None:
            result['WriteMode'] = self.write_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Consistency') is not None:
            self.consistency = m.get('Consistency')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DestColumns') is not None:
            self.dest_columns_shrink = m.get('DestColumns')

        if m.get('DestDatabase') is not None:
            self.dest_database = m.get('DestDatabase')

        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')

        if m.get('DestTable') is not None:
            self.dest_table = m.get('DestTable')

        if m.get('ErrorLimitCount') is not None:
            self.error_limit_count = m.get('ErrorLimitCount')

        if m.get('FallbackOffset') is not None:
            self.fallback_offset = m.get('FallbackOffset')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('MatchColumns') is not None:
            self.match_columns_shrink = m.get('MatchColumns')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SrcColumns') is not None:
            self.src_columns_shrink = m.get('SrcColumns')

        if m.get('TryRun') is not None:
            self.try_run = m.get('TryRun')

        if m.get('UpdateColumns') is not None:
            self.update_columns_shrink = m.get('UpdateColumns')

        if m.get('WriteMode') is not None:
            self.write_mode = m.get('WriteMode')

        return self

