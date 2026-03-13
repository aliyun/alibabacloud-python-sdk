# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeSoarTaskAndActionsResponseBody(DaraModel):
    def __init__(
        self,
        details: main_models.DescribeSoarTaskAndActionsResponseBodyDetails = None,
        page: main_models.DescribeSoarTaskAndActionsResponseBodyPage = None,
        request_id: str = None,
    ):
        # The execution details of each task.
        self.details = details
        self.page = page
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.details:
            self.details.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.details is not None:
            result['Details'] = self.details.to_map()

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = main_models.DescribeSoarTaskAndActionsResponseBodyDetails()
            self.details = temp_model.from_map(m.get('Details'))

        if m.get('Page') is not None:
            temp_model = main_models.DescribeSoarTaskAndActionsResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSoarTaskAndActionsResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSoarTaskAndActionsResponseBodyDetails(DaraModel):
    def __init__(
        self,
        action_log_num: int = None,
        actions: List[main_models.DescribeSoarTaskAndActionsResponseBodyDetailsActions] = None,
        end_time: int = None,
        error_msg: str = None,
        raw_event_req: str = None,
        request_uuid: str = None,
        start_time: int = None,
        status: str = None,
        task_flow_md_5: str = None,
        task_name: str = None,
        trigger_type: str = None,
        trigger_user: str = None,
    ):
        self.action_log_num = action_log_num
        # The list of component actions during the running of the playbook.
        self.actions = actions
        # The end of the time range during which the playbook is run. The value is a 13-digit timestamp.
        self.end_time = end_time
        # The error message of the task. If the task is successful, this field is empty.
        self.error_msg = error_msg
        # The request parameters of the task.
        self.raw_event_req = raw_event_req
        # The request ID of the task. The value is unique.
        self.request_uuid = request_uuid
        # The beginning of the time range during which the playbook is run. The value is a 13-digit timestamp.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   **success**
        # *   **fail**
        # *   **running**
        self.status = status
        # The MD5 value of the playbook.
        self.task_flow_md_5 = task_flow_md_5
        # The name of the task. The value is the same as the playbook UUID.
        self.task_name = task_name
        # The task type. Valid values:
        # 
        # *   **debug**: a debugging task
        # *   **manual**: a manual task
        # *   **siem**: an event-triggered task
        self.trigger_type = trigger_type
        # The ID of the Alibaba Cloud account that triggers the task.
        self.trigger_user = trigger_user

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_log_num is not None:
            result['ActionLogNum'] = self.action_log_num

        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.raw_event_req is not None:
            result['RawEventReq'] = self.raw_event_req

        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_flow_md_5 is not None:
            result['TaskFlowMd5'] = self.task_flow_md_5

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.trigger_user is not None:
            result['TriggerUser'] = self.trigger_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionLogNum') is not None:
            self.action_log_num = m.get('ActionLogNum')

        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.DescribeSoarTaskAndActionsResponseBodyDetailsActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RawEventReq') is not None:
            self.raw_event_req = m.get('RawEventReq')

        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskFlowMd5') is not None:
            self.task_flow_md_5 = m.get('TaskFlowMd5')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TriggerUser') is not None:
            self.trigger_user = m.get('TriggerUser')

        return self

class DescribeSoarTaskAndActionsResponseBodyDetailsActions(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_uuid: str = None,
        asset_name: str = None,
        component: str = None,
        end_time: int = None,
        node_name: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The action name of the component.
        self.action = action
        # The UUID of the component execution record.
        self.action_uuid = action_uuid
        # The name of the asset that is used by the component.
        self.asset_name = asset_name
        # The component name.
        self.component = component
        # The end of the time range during which the component is run. The value is a 13-digit timestamp.
        self.end_time = end_time
        # The custom name of the node in the component.
        self.node_name = node_name
        # The beginning of the time range during which the component is run. The value is a 13-digit timestamp.
        self.start_time = start_time
        # The running result of the component. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_uuid is not None:
            result['ActionUuid'] = self.action_uuid

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.component is not None:
            result['Component'] = self.component

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionUuid') is not None:
            self.action_uuid = m.get('ActionUuid')

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

