# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeStreamingJobResponseBody(DaraModel):
    def __init__(
        self,
        account: str = None,
        consistency: str = None,
        create_time: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        dest_columns: List[str] = None,
        dest_database: str = None,
        dest_schema: str = None,
        dest_table: str = None,
        error_limit_count: int = None,
        error_message: str = None,
        fallback_offset: str = None,
        group_name: str = None,
        job_config: str = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        match_columns: List[str] = None,
        mode: str = None,
        modify_time: str = None,
        password: str = None,
        request_id: str = None,
        src_columns: List[str] = None,
        status: str = None,
        update_columns: List[str] = None,
        write_mode: str = None,
    ):
        # Target database account.
        self.account = account
        # Delivery guarantee.
        self.consistency = consistency
        # Creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # Data source ID.
        self.data_source_id = data_source_id
        # Data source name.
        self.data_source_name = data_source_name
        # Target data table mapping field list.
        self.dest_columns = dest_columns
        # Target database name.
        self.dest_database = dest_database
        # Target namespace.
        self.dest_schema = dest_schema
        # Target table name.
        self.dest_table = dest_table
        # When data in Kafka does not match the ADBPG target table, it can cause write failures. This value represents the number of error rows allowed; if exceeded, the task will fail.
        self.error_limit_count = error_limit_count
        # Service status information, such as the reason for an exception. It is empty in the normal Running state.
        self.error_message = error_message
        # Fallback offset, which is the fallback position
        # 
        # - The FallbackOffset parameter defines the behavior when the consumer has not requested a specific offset to consume or the requested offset exceeds the current record\\"s offset information in the Kafka cluster. You can choose to start consuming from the earliest (newest) or latest (oldest) offset.
        self.fallback_offset = fallback_offset
        # Kafka group name
        self.group_name = group_name
        # Job configuration file.
        self.job_config = job_config
        # Job description.
        self.job_description = job_description
        # Job ID.
        self.job_id = job_id
        # Job name.
        self.job_name = job_name
        # Match columns, usually all primary key columns of the target table. If all column values in this configuration are the same, the two rows of data are considered duplicates.
        self.match_columns = match_columns
        # Configuration mode
        # 1. Basic mode requires specifying some configuration fields
        # 1. Professional mode supports submitting YAML files
        self.mode = mode
        # Last modified time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.modify_time = modify_time
        # Target database password.
        self.password = password
        # Request ID.
        self.request_id = request_id
        # Source field list.
        self.src_columns = src_columns
        # Service status, with possible values:
        # 
        # - Init: Initializing
        # 
        # - Running: Running
        # 
        # - Exception: Exception
        # 
        # - Paused: Paused
        self.status = status
        # Update columns, usually all non-primary key columns of the target table. When data duplication is determined through MatchColumns, updating the UpdateColumns column values will result in new data overwriting old data.
        self.update_columns = update_columns
        # Write mode.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.match_columns is not None:
            result['MatchColumns'] = self.match_columns

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.password is not None:
            result['Password'] = self.password

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.src_columns is not None:
            result['SrcColumns'] = self.src_columns

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

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

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

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

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('MatchColumns') is not None:
            self.match_columns = m.get('MatchColumns')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SrcColumns') is not None:
            self.src_columns = m.get('SrcColumns')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateColumns') is not None:
            self.update_columns = m.get('UpdateColumns')

        if m.get('WriteMode') is not None:
            self.write_mode = m.get('WriteMode')

        return self

