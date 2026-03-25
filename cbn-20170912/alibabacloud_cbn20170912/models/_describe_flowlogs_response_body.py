# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowlogsResponseBody(DaraModel):
    def __init__(
        self,
        flow_logs: main_models.DescribeFlowlogsResponseBodyFlowLogs = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: str = None,
        total_count: str = None,
    ):
        self.flow_logs = flow_logs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.flow_logs:
            self.flow_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_logs is not None:
            result['FlowLogs'] = self.flow_logs.to_map()

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
        if m.get('FlowLogs') is not None:
            temp_model = main_models.DescribeFlowlogsResponseBodyFlowLogs()
            self.flow_logs = temp_model.from_map(m.get('FlowLogs'))

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

class DescribeFlowlogsResponseBodyFlowLogs(DaraModel):
    def __init__(
        self,
        flow_log: List[main_models.DescribeFlowlogsResponseBodyFlowLogsFlowLog] = None,
    ):
        self.flow_log = flow_log

    def validate(self):
        if self.flow_log:
            for v1 in self.flow_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowLog'] = []
        if self.flow_log is not None:
            for k1 in self.flow_log:
                result['FlowLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_log = []
        if m.get('FlowLog') is not None:
            for k1 in m.get('FlowLog'):
                temp_model = main_models.DescribeFlowlogsResponseBodyFlowLogsFlowLog()
                self.flow_log.append(temp_model.from_map(k1))

        return self

class DescribeFlowlogsResponseBodyFlowLogsFlowLog(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        creation_time: str = None,
        description: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        flow_log_version: str = None,
        interval: int = None,
        log_format_string: str = None,
        log_store_name: str = None,
        project_name: str = None,
        region_id: str = None,
        status: str = None,
        tags: main_models.DescribeFlowlogsResponseBodyFlowLogsFlowLogTags = None,
        transit_router_attachment_id: str = None,
        transit_router_id: str = None,
    ):
        self.cen_id = cen_id
        self.creation_time = creation_time
        self.description = description
        self.flow_log_id = flow_log_id
        self.flow_log_name = flow_log_name
        self.flow_log_version = flow_log_version
        self.interval = interval
        self.log_format_string = log_format_string
        self.log_store_name = log_store_name
        self.project_name = project_name
        self.region_id = region_id
        self.status = status
        self.tags = tags
        self.transit_router_attachment_id = transit_router_attachment_id
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.flow_log_version is not None:
            result['FlowLogVersion'] = self.flow_log_version

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_format_string is not None:
            result['LogFormatString'] = self.log_format_string

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('FlowLogVersion') is not None:
            self.flow_log_version = m.get('FlowLogVersion')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogFormatString') is not None:
            self.log_format_string = m.get('LogFormatString')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeFlowlogsResponseBodyFlowLogsFlowLogTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class DescribeFlowlogsResponseBodyFlowLogsFlowLogTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeFlowlogsResponseBodyFlowLogsFlowLogTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFlowlogsResponseBodyFlowLogsFlowLogTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeFlowlogsResponseBodyFlowLogsFlowLogTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

