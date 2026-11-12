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
        # The destination database account.
        self.account = account
        # The delivery guarantee.
        self.consistency = consistency
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The data source ID.
        self.data_source_id = data_source_id
        # The data source name.
        self.data_source_name = data_source_name
        # The list of mapped columns in the destination table.
        self.dest_columns = dest_columns
        # The destination database name.
        self.dest_database = dest_database
        # The destination namespace.
        self.dest_schema = dest_schema
        # The destination table name.
        self.dest_table = dest_table
        # The maximum number of allowed error rows. If data in Kafka does not match the destination AnalyticDB for PostgreSQL table, a write failure occurs. If the number of error rows exceeds this value, the job fails.
        self.error_limit_count = error_limit_count
        # The service status message. For example, if an exception occurs, the cause of the exception is displayed. This parameter is empty when the service is in the Running state.
        self.error_message = error_message
        # The fallback offset.
        # 
        # - The FallbackOffset parameter defines the behavior when a consumer does not request a specific offset to consume, or when the requested offset exceeds the offset range recorded in the current Kafka cluster. You can choose to start consuming from the earliest or latest offset.
        self.fallback_offset = fallback_offset
        # The Kafka group name.
        self.group_name = group_name
        # The job configuration file.
        self.job_config = job_config
        # The job description.
        self.job_description = job_description
        # The job ID.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The match columns. Typically, these are all primary key columns of the destination table. If the values of all columns in this configuration are the same, the two rows of data are considered duplicate.
        self.match_columns = match_columns
        # The configuration mode.
        # 1. basic: requires specific configuration fields.
        # 2. professional: supports submitting YAML files.
        self.mode = mode
        # The last modification time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.modify_time = modify_time
        # The destination database password.
        self.password = password
        # The request ID.
        self.request_id = request_id
        # The list of source columns.
        self.src_columns = src_columns
        # The service status. Valid values:
        # 
        # - Init: initializing.
        # 
        # - Running: running.
        # 
        # - Exception: an exception occurred.
        # 
        # - Paused: paused.
        self.status = status
        # The update columns. Typically, these are all non-primary key columns of the destination table. When duplicate data is identified based on the match columns, the values of the update columns are updated so that the new data overwrites the old data.
        self.update_columns = update_columns
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

