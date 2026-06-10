# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordFileResponseBody(DaraModel):
    def __init__(
        self,
        record_files: List[main_models.DescribeRecordFileResponseBodyRecordFiles] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the screen recording files.
        self.record_files = record_files
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.record_files:
            for v1 in self.record_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordFiles'] = []
        if self.record_files is not None:
            for k1 in self.record_files:
                result['RecordFiles'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_files = []
        if m.get('RecordFiles') is not None:
            for k1 in m.get('RecordFiles'):
                temp_model = main_models.DescribeRecordFileResponseBodyRecordFiles()
                self.record_files.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRecordFileResponseBodyRecordFiles(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        end_user_id: str = None,
        event_details: List[main_models.DescribeRecordFileResponseBodyRecordFilesEventDetails] = None,
        file_name: str = None,
        file_size: int = None,
        policy_id: str = None,
        record_end_time: str = None,
        record_expire: int = None,
        record_start_time: str = None,
        record_type: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        status: int = None,
    ):
        # The ID of the cloud desktop.
        self.desktop_id = desktop_id
        # The name of the cloud desktop.
        self.desktop_name = desktop_name
        # The name of the end user.
        self.end_user_id = end_user_id
        # The event details.
        self.event_details = event_details
        # The name of the screen recording file.
        self.file_name = file_name
        # The file size. Unit: bytes.
        self.file_size = file_size
        # The ID of the policy.
        self.policy_id = policy_id
        # The time when the screen recording ended. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format and is displayed in UTC.
        self.record_end_time = record_end_time
        # The expiration time of the screen recording file.
        self.record_expire = record_expire
        # The time when the screen recording started. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format and is displayed in UTC.
        self.record_start_time = record_start_time
        # The recording type. Valid values:
        # 
        # - `alltime`: continuous screen recording.
        # 
        # - `period`: interval screen recording.
        # 
        # - `event`: event-triggered screen recording.
        # 
        # - `session`: session-based screen recording.
        self.record_type = record_type
        # The ID of the region where the cloud desktop resides.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the resource group.
        self.resource_group_name = resource_group_name
        # The upload status of the screen recording file. Valid values:
        # 
        # - `0`: uploaded.
        # 
        # - `1`: uploading.
        self.status = status

    def validate(self):
        if self.event_details:
            for v1 in self.event_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        result['EventDetails'] = []
        if self.event_details is not None:
            for k1 in self.event_details:
                result['EventDetails'].append(k1.to_map() if k1 else None)

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.record_end_time is not None:
            result['RecordEndTime'] = self.record_end_time

        if self.record_expire is not None:
            result['RecordExpire'] = self.record_expire

        if self.record_start_time is not None:
            result['RecordStartTime'] = self.record_start_time

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        self.event_details = []
        if m.get('EventDetails') is not None:
            for k1 in m.get('EventDetails'):
                temp_model = main_models.DescribeRecordFileResponseBodyRecordFilesEventDetails()
                self.event_details.append(temp_model.from_map(k1))

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RecordEndTime') is not None:
            self.record_end_time = m.get('RecordEndTime')

        if m.get('RecordExpire') is not None:
            self.record_expire = m.get('RecordExpire')

        if m.get('RecordStartTime') is not None:
            self.record_start_time = m.get('RecordStartTime')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeRecordFileResponseBodyRecordFilesEventDetails(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_time: int = None,
        event_type: str = None,
    ):
        # The event details.
        self.event_name = event_name
        # The time when the event occurred.
        self.event_time = event_time
        # The event type.
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

