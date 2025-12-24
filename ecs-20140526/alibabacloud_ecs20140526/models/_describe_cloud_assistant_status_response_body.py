# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudAssistantStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_cloud_assistant_status_set: main_models.DescribeCloudAssistantStatusResponseBodyInstanceCloudAssistantStatusSet = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the installation status of Cloud Assistant on the instances.
        self.instance_cloud_assistant_status_set = instance_cloud_assistant_status_set
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances.
        self.total_count = total_count

    def validate(self):
        if self.instance_cloud_assistant_status_set:
            self.instance_cloud_assistant_status_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_cloud_assistant_status_set is not None:
            result['InstanceCloudAssistantStatusSet'] = self.instance_cloud_assistant_status_set.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCloudAssistantStatusSet') is not None:
            temp_model = main_models.DescribeCloudAssistantStatusResponseBodyInstanceCloudAssistantStatusSet()
            self.instance_cloud_assistant_status_set = temp_model.from_map(m.get('InstanceCloudAssistantStatusSet'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudAssistantStatusResponseBodyInstanceCloudAssistantStatusSet(DaraModel):
    def __init__(
        self,
        instance_cloud_assistant_status: List[main_models.DescribeCloudAssistantStatusResponseBodyInstanceCloudAssistantStatusSetInstanceCloudAssistantStatus] = None,
    ):
        self.instance_cloud_assistant_status = instance_cloud_assistant_status

    def validate(self):
        if self.instance_cloud_assistant_status:
            for v1 in self.instance_cloud_assistant_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceCloudAssistantStatus'] = []
        if self.instance_cloud_assistant_status is not None:
            for k1 in self.instance_cloud_assistant_status:
                result['InstanceCloudAssistantStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_cloud_assistant_status = []
        if m.get('InstanceCloudAssistantStatus') is not None:
            for k1 in m.get('InstanceCloudAssistantStatus'):
                temp_model = main_models.DescribeCloudAssistantStatusResponseBodyInstanceCloudAssistantStatusSetInstanceCloudAssistantStatus()
                self.instance_cloud_assistant_status.append(temp_model.from_map(k1))

        return self

class DescribeCloudAssistantStatusResponseBodyInstanceCloudAssistantStatusSetInstanceCloudAssistantStatus(DaraModel):
    def __init__(
        self,
        active_task_count: int = None,
        cloud_assistant_status: str = None,
        cloud_assistant_version: str = None,
        instance_id: str = None,
        invocation_count: int = None,
        last_heartbeat_time: str = None,
        last_invoked_time: str = None,
        ostype: str = None,
        support_session_manager: bool = None,
    ):
        # The number of tasks that Cloud Assistant was running on the instance.
        self.active_task_count = active_task_count
        # Indicates whether Cloud Assistant is running on the instance. Valid values:
        # 
        # *   true: Heartbeats are detected in the last 2 minutes.
        # *   false: No heartbeats are detected in the last 2 minutes.
        self.cloud_assistant_status = cloud_assistant_status
        # The version number of Cloud Assistant Agent. This parameter is empty if Cloud Assistant Agent is not installed or is not running on the instance.
        self.cloud_assistant_version = cloud_assistant_version
        # The ID of the instance.
        self.instance_id = instance_id
        # The number of tasks that Cloud Assistant completed on the instance.
        self.invocation_count = invocation_count
        # The last heartbeat time of Cloud Assistant. The value is updated every minute on average. The interval can be 55, 60, or 65 seconds.
        self.last_heartbeat_time = last_heartbeat_time
        # The time when commands were last run.
        self.last_invoked_time = last_invoked_time
        # The operating system type of the instance. Valid values:
        # 
        # *   Windows
        # *   Linux
        # *   FreeBSD
        self.ostype = ostype
        # Indicates whether Cloud Assistant supports Session Manager on the instance. If Session Manager is not supported, the version of Cloud Assistant Agent is outdated. Update Cloud Assistant Agent to the latest version.
        # 
        # To support Session Manager, the version of Cloud Assistant Agent cannot be earlier than the following versions:
        # 
        # *   Linux: 2.2.3.189
        # *   Windows: 2.1.3.189
        self.support_session_manager = support_session_manager

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_task_count is not None:
            result['ActiveTaskCount'] = self.active_task_count

        if self.cloud_assistant_status is not None:
            result['CloudAssistantStatus'] = self.cloud_assistant_status

        if self.cloud_assistant_version is not None:
            result['CloudAssistantVersion'] = self.cloud_assistant_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_count is not None:
            result['InvocationCount'] = self.invocation_count

        if self.last_heartbeat_time is not None:
            result['LastHeartbeatTime'] = self.last_heartbeat_time

        if self.last_invoked_time is not None:
            result['LastInvokedTime'] = self.last_invoked_time

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.support_session_manager is not None:
            result['SupportSessionManager'] = self.support_session_manager

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTaskCount') is not None:
            self.active_task_count = m.get('ActiveTaskCount')

        if m.get('CloudAssistantStatus') is not None:
            self.cloud_assistant_status = m.get('CloudAssistantStatus')

        if m.get('CloudAssistantVersion') is not None:
            self.cloud_assistant_version = m.get('CloudAssistantVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationCount') is not None:
            self.invocation_count = m.get('InvocationCount')

        if m.get('LastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('LastHeartbeatTime')

        if m.get('LastInvokedTime') is not None:
            self.last_invoked_time = m.get('LastInvokedTime')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('SupportSessionManager') is not None:
            self.support_session_manager = m.get('SupportSessionManager')

        return self

