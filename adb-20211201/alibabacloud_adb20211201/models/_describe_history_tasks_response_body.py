# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeHistoryTasksResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeHistoryTasksResponseBodyAccessDeniedDetail = None,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.DescribeHistoryTasksResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # null
        self.access_denied_detail = access_denied_detail
        # The HTTP status code that is returned.
        self.code = code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The task list.
        self.items = items
        # The returned message. null
        # 
        # *   null****
        # *   null
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # Total record count.
        self.total_count = total_count

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

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
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeHistoryTasksResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeHistoryTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

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

class DescribeHistoryTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        action_info: str = None,
        caller_source: str = None,
        caller_uid: str = None,
        current_step_name: str = None,
        db_type: str = None,
        end_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        product: str = None,
        progress: float = None,
        reason_code: str = None,
        region_id: str = None,
        remain_time: int = None,
        start_time: str = None,
        status: str = None,
        task_detail: str = None,
        task_id: str = None,
        task_type: str = None,
        uid: str = None,
    ):
        # Allowed operation information. When used specifically, matches operation Action based on currentStepName+status in this information. If no Action is matched, represents task current status does not support operations.
        self.action_info = action_info
        # null
        self.caller_source = caller_source
        # null
        # 
        # *   **null**
        # *   **null**
        self.caller_uid = caller_uid
        # Current executing step name. If empty, represents task has not started.
        self.current_step_name = current_step_name
        # The database engine type.
        self.db_type = db_type
        # Task end time.
        self.end_time = end_time
        # Cluster ID.
        self.instance_id = instance_id
        # The instance ID.
        self.instance_name = instance_name
        # Instance type.
        self.instance_type = instance_type
        # The service name.
        self.product = product
        # Indicates the task progress.
        self.progress = progress
        # The reason why the current task was initiated.
        self.reason_code = reason_code
        # The region ID.
        self.region_id = region_id
        # Estimated remaining execution time, in seconds.
        self.remain_time = remain_time
        # Task start time.
        self.start_time = start_time
        # Task status. Valid values:
        # 
        # *   **Scheduled**
        # *   **Running**
        # *   **Succeed**
        # *   **Failed**: The task failed.
        # *   **Cancelling**
        # *   **Canceled**
        # *   **Waiting**
        self.status = status
        # The task details.
        self.task_detail = task_detail
        # Task ID.
        self.task_id = task_id
        # Task type.
        self.task_type = task_type
        # null
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info

        if self.caller_source is not None:
            result['CallerSource'] = self.caller_source

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.current_step_name is not None:
            result['CurrentStepName'] = self.current_step_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.product is not None:
            result['Product'] = self.product

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')

        if m.get('CallerSource') is not None:
            self.caller_source = m.get('CallerSource')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('CurrentStepName') is not None:
            self.current_step_name = m.get('CurrentStepName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskDetail') is not None:
            self.task_detail = m.get('TaskDetail')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class DescribeHistoryTasksResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # null
        self.auth_action = auth_action
        # null
        self.auth_principal_display_name = auth_principal_display_name
        # null
        self.auth_principal_owner_id = auth_principal_owner_id
        # null
        self.auth_principal_type = auth_principal_type
        # null
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # null
        # 
        # *   **null**
        # *   **null**
        self.no_permission_type = no_permission_type
        # null
        # 
        # *   **null**
        # *   **null**
        # *   **null**
        # *   **null**
        # *   **null**
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

