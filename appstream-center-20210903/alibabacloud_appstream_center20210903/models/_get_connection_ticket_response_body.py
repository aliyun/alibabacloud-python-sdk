# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210903 import models as main_models
from darabonba.model import DaraModel

class GetConnectionTicketResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        avatar_id: str = None,
        bind_queue_info: main_models.GetConnectionTicketResponseBodyBindQueueInfo = None,
        code: str = None,
        login_token: str = None,
        message: str = None,
        next_poll_interval_ms: int = None,
        os_type: str = None,
        policy: main_models.GetConnectionTicketResponseBodyPolicy = None,
        region_id: str = None,
        request_id: str = None,
        retry_times: int = None,
        task_id: str = None,
        task_status: str = None,
        tenant_id: int = None,
        ticket: str = None,
    ):
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_instance_persistent_id = app_instance_persistent_id
        self.avatar_id = avatar_id
        self.bind_queue_info = bind_queue_info
        self.code = code
        self.login_token = login_token
        self.message = message
        self.next_poll_interval_ms = next_poll_interval_ms
        self.os_type = os_type
        self.policy = policy
        self.region_id = region_id
        # Id of the request
        self.request_id = request_id
        self.retry_times = retry_times
        self.task_id = task_id
        self.task_status = task_status
        self.tenant_id = tenant_id
        self.ticket = ticket

    def validate(self):
        if self.bind_queue_info:
            self.bind_queue_info.validate()
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.bind_queue_info is not None:
            result['BindQueueInfo'] = self.bind_queue_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.message is not None:
            result['Message'] = self.message

        if self.next_poll_interval_ms is not None:
            result['NextPollIntervalMs'] = self.next_poll_interval_ms

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('BindQueueInfo') is not None:
            temp_model = main_models.GetConnectionTicketResponseBodyBindQueueInfo()
            self.bind_queue_info = temp_model.from_map(m.get('BindQueueInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextPollIntervalMs') is not None:
            self.next_poll_interval_ms = m.get('NextPollIntervalMs')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Policy') is not None:
            temp_model = main_models.GetConnectionTicketResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        return self

class GetConnectionTicketResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        resolution_adaptive: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.resolution_adaptive = resolution_adaptive
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resolution_adaptive is not None:
            result['ResolutionAdaptive'] = self.resolution_adaptive

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResolutionAdaptive') is not None:
            self.resolution_adaptive = m.get('ResolutionAdaptive')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        return self



class GetConnectionTicketResponseBodyBindQueueInfo(DaraModel):
    def __init__(
        self,
        queue_status: str = None,
        rank: int = None,
        ready_timeout: int = None,
        remaining_time: int = None,
        request_key: str = None,
        target_id: str = None,
        wait_time: int = None,
    ):
        self.queue_status = queue_status
        self.rank = rank
        self.ready_timeout = ready_timeout
        self.remaining_time = remaining_time
        self.request_key = request_key
        self.target_id = target_id
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.queue_status is not None:
            result['QueueStatus'] = self.queue_status

        if self.rank is not None:
            result['Rank'] = self.rank

        if self.ready_timeout is not None:
            result['ReadyTimeout'] = self.ready_timeout

        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time

        if self.request_key is not None:
            result['RequestKey'] = self.request_key

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueStatus') is not None:
            self.queue_status = m.get('QueueStatus')

        if m.get('Rank') is not None:
            self.rank = m.get('Rank')

        if m.get('ReadyTimeout') is not None:
            self.ready_timeout = m.get('ReadyTimeout')

        if m.get('RemainingTime') is not None:
            self.remaining_time = m.get('RemainingTime')

        if m.get('RequestKey') is not None:
            self.request_key = m.get('RequestKey')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

