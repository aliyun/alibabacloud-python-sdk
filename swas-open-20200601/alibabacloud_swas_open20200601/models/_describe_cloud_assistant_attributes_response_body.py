# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudAssistantAttributesResponseBody(DaraModel):
    def __init__(
        self,
        cloud_assistant: List[main_models.DescribeCloudAssistantAttributesResponseBodyCloudAssistant] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The installation status of Cloud Assistant on the instances.
        self.cloud_assistant = cloud_assistant
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.cloud_assistant:
            for v1 in self.cloud_assistant:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAssistant'] = []
        if self.cloud_assistant is not None:
            for k1 in self.cloud_assistant:
                result['CloudAssistant'].append(k1.to_map() if k1 else None)

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
        self.cloud_assistant = []
        if m.get('CloudAssistant') is not None:
            for k1 in m.get('CloudAssistant'):
                temp_model = main_models.DescribeCloudAssistantAttributesResponseBodyCloudAssistant()
                self.cloud_assistant.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudAssistantAttributesResponseBodyCloudAssistant(DaraModel):
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
        # The number of running tasks of Cloud Assistant on the instance.
        self.active_task_count = active_task_count
        # Indicates whether Cloud Assistant is running on the instance. Valid values:
        # 
        # true: A heartbeat was detected within the last 2 minutes.
        # 
        # false: No heartbeat was detected within the last 2 minutes.
        self.cloud_assistant_status = cloud_assistant_status
        # The version number of the Cloud Assistant Agent. This value is empty if the Cloud Assistant Agent is not installed or is not running.
        self.cloud_assistant_version = cloud_assistant_version
        # The instance ID of the simple application server instance.
        self.instance_id = instance_id
        # The number of completed tasks of Cloud Assistant on the instance.
        self.invocation_count = invocation_count
        # The time of the last heartbeat of Cloud Assistant. This value is updated approximately every minute, with a random fluctuation of up to 5 seconds (minimum 55 seconds, maximum 65 seconds).
        self.last_heartbeat_time = last_heartbeat_time
        # The time when the last command was executed. The time is displayed in UTC (Z) in the YYYY-MM-DDThh:mm:ssZ format.
        self.last_invoked_time = last_invoked_time
        # The operating system type of the instance. Valid values:
        # 
        # - Windows.
        # - Linux.
        # - FreeBSD.
        self.ostype = ostype
        # Indicates whether Cloud Assistant on the instance supports the session management feature. If session management is not supported, the Cloud Assistant version is outdated. Update the client to the latest version.
        # 
        # The minimum Cloud Assistant versions that support session management are as follows:
        # 
        # Linux: 2.2.3.189
        # Windows: 2.1.3.189
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

