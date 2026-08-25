# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_sources: List[main_models.DescribeDataSourcesResponseBodyDataSources] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code. A value of 200 indicates success.
        self.code = code
        # The data sources.
        self.data_sources = data_sources
        # The response message. The value is "successful" if the request was successful, or an error message if the request failed.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The page size. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # 
        # - false: The request failed.
        self.success = success
        # The total number of returned data sources.
        self.total_count = total_count

    def validate(self):
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.DescribeDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataSourcesResponseBodyDataSources(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_info: str = None,
        created_time: int = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        exclude: str = None,
        include: str = None,
        index_available: bool = None,
        index_level: str = None,
        index_update_time: bool = None,
        indexing: bool = None,
        options: str = None,
        paths: List[str] = None,
        plan_id: str = None,
        schedule: str = None,
        speed_limit: str = None,
        updated_time: int = None,
    ):
        # The client group ID used to access the data source.
        self.cluster_id = cluster_id
        # The connection information of the data source, which describes how to access the data source.
        self.connection_info = connection_info
        # The time when the data source was created. UNIX timestamp in seconds.
        self.created_time = created_time
        # The data source ID.
        self.data_source_id = data_source_id
        # The data source name.
        self.data_source_name = data_source_name
        # The data source type.
        self.data_source_type = data_source_type
        # The paths excluded from analysis. Archiving feature only.
        self.exclude = exclude
        # The paths included in the analysis. Archiving feature only.
        self.include = include
        # Whether the index is available. Archiving feature only.
        self.index_available = index_available
        # The index level. Valid values:
        # 
        # - OFF: No index is created.
        # 
        # - META: A metadata index is created.
        # 
        # - ALL: A full-text index is created. This value is deprecated.
        self.index_level = index_level
        # The time when the index was last updated. UNIX timestamp in seconds. Archiving feature only.
        self.index_update_time = index_update_time
        # Whether an index is being built. Archiving feature only.
        self.indexing = indexing
        # The analysis options. Archiving feature only.
        self.options = options
        # The analysis paths. Archiving feature only.
        self.paths = paths
        # The analysis plan ID. Archiving feature only.
        self.plan_id = plan_id
        # The analysis schedule. Archiving feature only. Format: `I|{startTime}|{interval}`. `{startTime}` is the start time as a UNIX timestamp in seconds. `{interval}` is the execution interval in ISO 8601 format. Example: PT1H for one hour, P1D for one day.
        self.schedule = schedule
        # The rate limit configuration. Archiving feature only.
        self.speed_limit = speed_limit
        # The time when the data source was last updated. UNIX timestamp in seconds.
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.include is not None:
            result['Include'] = self.include

        if self.index_available is not None:
            result['IndexAvailable'] = self.index_available

        if self.index_level is not None:
            result['IndexLevel'] = self.index_level

        if self.index_update_time is not None:
            result['IndexUpdateTime'] = self.index_update_time

        if self.indexing is not None:
            result['Indexing'] = self.indexing

        if self.options is not None:
            result['Options'] = self.options

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectionInfo') is not None:
            self.connection_info = m.get('ConnectionInfo')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('IndexAvailable') is not None:
            self.index_available = m.get('IndexAvailable')

        if m.get('IndexLevel') is not None:
            self.index_level = m.get('IndexLevel')

        if m.get('IndexUpdateTime') is not None:
            self.index_update_time = m.get('IndexUpdateTime')

        if m.get('Indexing') is not None:
            self.indexing = m.get('Indexing')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

