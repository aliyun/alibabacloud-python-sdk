# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDtsServiceLogRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        end_time: int = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
        status: str = None,
        sub_job_type: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration or synchronization task.
        self.dts_job_id = dts_job_id
        # The end of the time range to query. You can call the [DescribePreCheckStatus](https://help.aliyun.com/document_detail/209718.html) operation to query the execution time of the subtasks.
        # 
        # > *   To obtain the logs that are generated for DTS subtasks within a specific period of time, you can call the [DescribePreCheckStatus](https://help.aliyun.com/document_detail/209718.html) operation to query the execution time of the subtasks.
        # >*   Specify the time in the 13-digit UNIX timestamp format. Unit: milliseconds. You can use a search engine to obtain a UNIX timestamp converter.
        self.end_time = end_time
        # The keyword that is passed to specify the query content.
        # 
        # >  Fuzzy match is used and the keyword is case-sensitive.
        self.keyword = keyword
        # The number of the page to return. The value must be an integer that is greater than 0 and less than or equal to the maximum value supported by the integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of log entries to return on each page. Valid values: **20**, **50**, **100**, **500**, and **1000**. Default value: **20**.
        self.page_size = page_size
        # The ID of the region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query.
        # 
        # > *   To obtain the logs that are generated for Data Transmission Service (DTS) subtasks within a specific period of time, you can call the [DescribePreCheckStatus](https://help.aliyun.com/document_detail/209718.html) operation to query the execution time of the subtasks.
        # >*   Specify the time in the 13-digit UNIX timestamp format. Unit: milliseconds. You can use a search engine to obtain a UNIX timestamp converter.
        self.start_time = start_time
        # The log level. Separate multiple log levels with commas (,). Valid values:
        # 
        # *   **NORMAL**: displays the logs that are generated when the DTS task runs as expected.
        # *   **WARN**: displays the logs about severe issues that stop the DTS task from running.
        # *   **ERROR**: displays the logs about unexpected issues that stop specific processes form running.
        self.status = status
        # The type of a DTS subtask. Valid values:
        # 
        # *   **DATA_LOAD**: full migration or full synchronization
        # *   **ONLINE_WRITER**: incremental migration
        # *   **SYNC_WRITER**: incremental synchronization
        self.sub_job_type = sub_job_type
        # Whether it is a seamless integration (Zero-ETL) task, the value can be: - **true**: Yes. - **false**: No.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_job_type is not None:
            result['SubJobType'] = self.sub_job_type

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubJobType') is not None:
            self.sub_job_type = m.get('SubJobType')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

