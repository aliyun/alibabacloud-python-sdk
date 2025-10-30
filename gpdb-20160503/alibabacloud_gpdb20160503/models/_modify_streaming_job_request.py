# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyStreamingJobRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        consistency: str = None,
        dbinstance_id: str = None,
        dest_columns: List[str] = None,
        dest_database: str = None,
        dest_schema: str = None,
        dest_table: str = None,
        error_limit_count: int = None,
        fallback_offset: str = None,
        group_name: str = None,
        job_config: str = None,
        job_description: str = None,
        job_id: int = None,
        match_columns: List[str] = None,
        password: str = None,
        region_id: str = None,
        src_columns: List[str] = None,
        try_run: bool = None,
        update_columns: List[str] = None,
        write_mode: str = None,
    ):
        # Account name.
        self.account = account
        # The delivery guarantee setting.
        self.consistency = consistency
        # Instance ID
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Target data table mapping field list.
        self.dest_columns = dest_columns
        # Target database name.
        self.dest_database = dest_database
        # Target schema.
        self.dest_schema = dest_schema
        # Target table name.
        self.dest_table = dest_table
        # When the data in Kafka does not match the ADBPG target table, it will cause a write failure. This value is the number of error rows allowed; exceeding this will cause the task to fail.
        self.error_limit_count = error_limit_count
        # The fallback offset for data consumption.
        # 
        # *   This parameter specifies the starting offset from which data consumption resumes when a consumer does not request a consumption offset or requests a consumption offset that is beyond the range of the offset information recorded in the current Kafka cluster. You can choose to start data consumption from the earliest or latest offset.
        # 
        # Valid values:
        # *   EARLIEST
        # *   LATEST
        self.fallback_offset = fallback_offset
        # Kafka group name
        self.group_name = group_name
        # Job configuration file, required for professional mode.
        self.job_config = job_config
        # Job description.
        self.job_description = job_description
        # Job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Match columns, usually all primary key columns of the target table. If all column values in this configuration are the same, the two rows of data are considered duplicates.
        self.match_columns = match_columns
        # Password.
        self.password = password
        # Region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) API to view available region IDs.
        self.region_id = region_id
        # Source data field list.
        self.src_columns = src_columns
        # Specifies whether to test the real-time job. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.try_run = try_run
        # Update columns, usually all non-primary key columns of the target table. When data duplication is determined through MatchColumns, updating the UpdateColumns column values will result in new data overwriting old data.
        self.update_columns = update_columns
        # The write mode.
        # 
        # Valid values:
        # 
        # *   MERGE
        # *   INSERT
        # *   UPDATE
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

        if self.dest_columns is not None:
            result['DestColumns'] = self.dest_columns

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

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.match_columns is not None:
            result['MatchColumns'] = self.match_columns

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.src_columns is not None:
            result['SrcColumns'] = self.src_columns

        if self.try_run is not None:
            result['TryRun'] = self.try_run

        if self.update_columns is not None:
            result['UpdateColumns'] = self.update_columns

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

        if m.get('DestColumns') is not None:
            self.dest_columns = m.get('DestColumns')

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

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MatchColumns') is not None:
            self.match_columns = m.get('MatchColumns')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SrcColumns') is not None:
            self.src_columns = m.get('SrcColumns')

        if m.get('TryRun') is not None:
            self.try_run = m.get('TryRun')

        if m.get('UpdateColumns') is not None:
            self.update_columns = m.get('UpdateColumns')

        if m.get('WriteMode') is not None:
            self.write_mode = m.get('WriteMode')

        return self

