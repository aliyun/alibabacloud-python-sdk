# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeProcessTasksResponseBody(DaraModel):
    def __init__(
        self,
        page: main_models.DescribeProcessTasksResponseBodyPage = None,
        process_tasks: List[main_models.DescribeProcessTasksResponseBodyProcessTasks] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page = page
        # The handling tasks.
        self.process_tasks = process_tasks
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()
        if self.process_tasks:
            for v1 in self.process_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page.to_map()

        result['ProcessTasks'] = []
        if self.process_tasks is not None:
            for k1 in self.process_tasks:
                result['ProcessTasks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = main_models.DescribeProcessTasksResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        self.process_tasks = []
        if m.get('ProcessTasks') is not None:
            for k1 in m.get('ProcessTasks'):
                temp_model = main_models.DescribeProcessTasksResponseBodyProcessTasks()
                self.process_tasks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeProcessTasksResponseBodyProcessTasks(DaraModel):
    def __init__(
        self,
        creator: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        err_code: str = None,
        err_msg: str = None,
        err_tip: str = None,
        event_uuid: str = None,
        gmt_create_millis: int = None,
        gmt_modified_millis: int = None,
        input_params: str = None,
        process_strategy_uuid: str = None,
        process_time: int = None,
        remove_time: int = None,
        req_uuid: str = None,
        scene_code: str = None,
        scene_name: str = None,
        scope: str = None,
        source: str = None,
        task_id: str = None,
        task_status: int = None,
        trigger_source: str = None,
        yun_code: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to submit the handling task.
        self.creator = creator
        # The name of the handling entity.
        self.entity_name = entity_name
        # The type of the handling entity.
        self.entity_type = entity_type
        # The UUID of the handling entity.
        self.entity_uuid = entity_uuid
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_msg = err_msg
        # The error tip returned if the call failed.
        self.err_tip = err_tip
        # The UUID of the event.
        self.event_uuid = event_uuid
        # The creation time of the handling task. The value is a 13-digit timestamp.
        self.gmt_create_millis = gmt_create_millis
        # The modification time of the handling task. The value is a 13-digit timestamp.
        self.gmt_modified_millis = gmt_modified_millis
        # The input parameter of the handling task.
        self.input_params = input_params
        # The ID of the associated policy.
        self.process_strategy_uuid = process_strategy_uuid
        # The delivery time of the handling task. The value is a 13-digit timestamp.
        self.process_time = process_time
        # The unblocking time of the handling task. The value is a 13-digit timestamp.
        self.remove_time = remove_time
        # The UUID of the playbook execution record.
        self.req_uuid = req_uuid
        # The scenario code of the handling task.
        self.scene_code = scene_code
        # The scenario name of the handling task.
        self.scene_name = scene_name
        # The ID of the Alibaba Cloud account that is specified in the handling task.
        self.scope = scope
        # The submission source of the handling task.
        self.source = source
        # The unique identifier of the handling task.
        self.task_id = task_id
        # The status of the handling task.
        self.task_status = task_status
        # The triggering source of the handling task. Valid values:
        # 
        # *   **system**: triggered when you manually handle an event.
        # *   **custom**: triggered by an event based on an automatic response rule.
        # *   **custom_alert**: triggered by an alert based on an automatic response rule.
        # *   **soar-manual**: triggered when you use SOAR to manually run a playbook.
        # *   **soar-mdr**: triggered by Managed Security Service.
        self.trigger_source = trigger_source
        # The code of the cloud service that is associated with the handling task.
        self.yun_code = yun_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.err_tip is not None:
            result['ErrTip'] = self.err_tip

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.gmt_create_millis is not None:
            result['GmtCreateMillis'] = self.gmt_create_millis

        if self.gmt_modified_millis is not None:
            result['GmtModifiedMillis'] = self.gmt_modified_millis

        if self.input_params is not None:
            result['InputParams'] = self.input_params

        if self.process_strategy_uuid is not None:
            result['ProcessStrategyUuid'] = self.process_strategy_uuid

        if self.process_time is not None:
            result['ProcessTime'] = self.process_time

        if self.remove_time is not None:
            result['RemoveTime'] = self.remove_time

        if self.req_uuid is not None:
            result['ReqUuid'] = self.req_uuid

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.source is not None:
            result['Source'] = self.source

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.yun_code is not None:
            result['YunCode'] = self.yun_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('ErrTip') is not None:
            self.err_tip = m.get('ErrTip')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('GmtCreateMillis') is not None:
            self.gmt_create_millis = m.get('GmtCreateMillis')

        if m.get('GmtModifiedMillis') is not None:
            self.gmt_modified_millis = m.get('GmtModifiedMillis')

        if m.get('InputParams') is not None:
            self.input_params = m.get('InputParams')

        if m.get('ProcessStrategyUuid') is not None:
            self.process_strategy_uuid = m.get('ProcessStrategyUuid')

        if m.get('ProcessTime') is not None:
            self.process_time = m.get('ProcessTime')

        if m.get('RemoveTime') is not None:
            self.remove_time = m.get('RemoveTime')

        if m.get('ReqUuid') is not None:
            self.req_uuid = m.get('ReqUuid')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('YunCode') is not None:
            self.yun_code = m.get('YunCode')

        return self

class DescribeProcessTasksResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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

