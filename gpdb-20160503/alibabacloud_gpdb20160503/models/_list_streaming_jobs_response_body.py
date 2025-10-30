# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListStreamingJobsResponseBody(DaraModel):
    def __init__(
        self,
        job_items: List[main_models.ListStreamingJobsResponseBodyJobItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The queried jobs.
        self.job_items = job_items
        # Current page number.
        self.page_number = page_number
        # Number of records per page.
        self.page_record_count = page_record_count
        # Request ID.
        self.request_id = request_id
        # Total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.job_items:
            for v1 in self.job_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobItems'] = []
        if self.job_items is not None:
            for k1 in self.job_items:
                result['JobItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_items = []
        if m.get('JobItems') is not None:
            for k1 in m.get('JobItems'):
                temp_model = main_models.ListStreamingJobsResponseBodyJobItems()
                self.job_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListStreamingJobsResponseBodyJobItems(DaraModel):
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
        error_message: str = None,
        fallback_offset: str = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        match_columns: List[str] = None,
        mode: str = None,
        modify_time: str = None,
        password: str = None,
        src_columns: List[str] = None,
        status: str = None,
        update_columns: List[str] = None,
        write_mode: str = None,
    ):
        # The name of the database account.
        self.account = account
        # The delivery guarantee setting.
        self.consistency = consistency
        # The time when the job was created.
        self.create_time = create_time
        # The data source ID.
        self.data_source_id = data_source_id
        # The name of the data source.
        self.data_source_name = data_source_name
        # The mapped fields in the destination table.
        self.dest_columns = dest_columns
        # The name of the destination database.
        self.dest_database = dest_database
        # The name of the destination namespace.
        self.dest_schema = dest_schema
        # The name of the destination table.
        self.dest_table = dest_table
        # The error message returned.
        # 
        # This parameter is returned only when the return value of **Status** is **false**.
        self.error_message = error_message
        # The fallback offset for data consumption.
        # 
        # *   This parameter indicates the starting offset from which data consumption resumes when a consumer does not request a consumption offset or requests a consumption offset that is beyond the range of the offset information recorded in the current Kafka cluster. Valid values: EARLIEST and LATEST.
        self.fallback_offset = fallback_offset
        # The description of the job.
        self.job_description = job_description
        # The job ID.
        self.job_id = job_id
        # The name of the job.
        self.job_name = job_name
        # The update condition columns that are used to join the source data and the destination table. Typically, the columns are all the primary key columns of the destination table. If the values of all columns specified by this parameter in different rows are the same, the rows are considered duplicates.
        self.match_columns = match_columns
        # The configuration mode. Valid values:
        # 
        # 1.  basic: In basic mode, you must configure the configuration parameters.
        # 2.  professional: In professional mode, you can submit a YAML configuration file.
        self.mode = mode
        # The time when the job was last modified.
        self.modify_time = modify_time
        # The password of the database account.
        self.password = password
        # The source fields.
        self.src_columns = src_columns
        # The status of the job. Valid values:
        # 
        # *   Init
        # *   Running
        # *   Exception
        # *   Paused
        self.status = status
        # The columns to be updated if a row of data meets the update condition. Typically, the columns are all non-primary key columns of the destination table. When the columns specified by the MatchColumns parameter are used as conditions to join the source data and the destination table, data in columns of the UpdateColumns type is updated if data is matched.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.fallback_offset is not None:
            result['FallbackOffset'] = self.fallback_offset

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

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FallbackOffset') is not None:
            self.fallback_offset = m.get('FallbackOffset')

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

        if m.get('SrcColumns') is not None:
            self.src_columns = m.get('SrcColumns')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateColumns') is not None:
            self.update_columns = m.get('UpdateColumns')

        if m.get('WriteMode') is not None:
            self.write_mode = m.get('WriteMode')

        return self

