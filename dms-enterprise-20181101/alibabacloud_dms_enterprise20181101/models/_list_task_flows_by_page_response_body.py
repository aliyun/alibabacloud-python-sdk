# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowsByPageResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_flow_list: main_models.ListTaskFlowsByPageResponseBodyTaskFlowList = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The details of the returned task flows.
        self.task_flow_list = task_flow_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_flow_list:
            self.task_flow_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_flow_list is not None:
            result['TaskFlowList'] = self.task_flow_list.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskFlowList') is not None:
            temp_model = main_models.ListTaskFlowsByPageResponseBodyTaskFlowList()
            self.task_flow_list = temp_model.from_map(m.get('TaskFlowList'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTaskFlowsByPageResponseBodyTaskFlowList(DaraModel):
    def __init__(
        self,
        task_flow: List[main_models.ListTaskFlowsByPageResponseBodyTaskFlowListTaskFlow] = None,
    ):
        self.task_flow = task_flow

    def validate(self):
        if self.task_flow:
            for v1 in self.task_flow:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskFlow'] = []
        if self.task_flow is not None:
            for k1 in self.task_flow:
                result['TaskFlow'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_flow = []
        if m.get('TaskFlow') is not None:
            for k1 in m.get('TaskFlow'):
                temp_model = main_models.ListTaskFlowsByPageResponseBodyTaskFlowListTaskFlow()
                self.task_flow.append(temp_model.from_map(k1))

        return self

class ListTaskFlowsByPageResponseBodyTaskFlowListTaskFlow(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_nick_name: str = None,
        cron_begin_date: str = None,
        cron_end_date: str = None,
        cron_str: str = None,
        cron_switch: bool = None,
        cron_type: int = None,
        dag_name: str = None,
        dag_owner_id: str = None,
        dag_owner_nick_name: str = None,
        deploy_id: int = None,
        description: str = None,
        id: int = None,
        latest_instance_status: int = None,
        latest_instance_time: str = None,
        scenario_id: str = None,
        schedule_param: str = None,
        status: int = None,
        time_zone_id: str = None,
        trigger_type: int = None,
    ):
        # The ID of the user who created the task flow.
        self.creator_id = creator_id
        # The username of the user who created the task flow.
        self.creator_nick_name = creator_nick_name
        # The start time of scheduled scheduling. The task flow is not scheduled before this point in time.
        self.cron_begin_date = cron_begin_date
        # The end time of scheduled scheduling. The task flow is not scheduled after this point in time.
        self.cron_end_date = cron_end_date
        # Scheduled Cron.
        self.cron_str = cron_str
        # Whether to enable scheduled scheduling.
        self.cron_switch = cron_switch
        # Scheduling cycle type. Valid values:
        # - **2**: Hourly scheduling
        # - **3**: Daily scheduling
        # - **4**: Weekly scheduling
        # - **5**: Monthly scheduling
        self.cron_type = cron_type
        # The name of the task flow.
        self.dag_name = dag_name
        # The user ID of the task flow owner.
        self.dag_owner_id = dag_owner_id
        # The username of the owner of the task flow.
        self.dag_owner_nick_name = dag_owner_nick_name
        # The ID of the last deployment record of the task flow.
        self.deploy_id = deploy_id
        # The description of the task flow.
        self.description = description
        # The ID of the task flow.
        self.id = id
        # The status of the last execution of the task flow. Valid values:
        # 
        # *   **0**: invalid
        # *   **1**: scheduling disabled
        # *   **2**: waiting to be scheduled
        self.latest_instance_status = latest_instance_status
        # The time when the last execution record was created.
        self.latest_instance_time = latest_instance_time
        # The ID of the application scenario.
        self.scenario_id = scenario_id
        # Event scheduling configuration, JSON string format.
        self.schedule_param = schedule_param
        # The status of the task flow. Valid values:
        # 
        # *   **0**: invalid
        # *   **1**: scheduling disabled
        # *   **2**: waiting to be scheduled
        self.status = status
        # Time zone setting. Default value: East 8(Asia/Shanghai).
        self.time_zone_id = time_zone_id
        # The trigger type. Valid values:
        # - **0**: Periodic scheduling
        # - **1**: Run manually
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name

        if self.cron_begin_date is not None:
            result['CronBeginDate'] = self.cron_begin_date

        if self.cron_end_date is not None:
            result['CronEndDate'] = self.cron_end_date

        if self.cron_str is not None:
            result['CronStr'] = self.cron_str

        if self.cron_switch is not None:
            result['CronSwitch'] = self.cron_switch

        if self.cron_type is not None:
            result['CronType'] = self.cron_type

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id

        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name

        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status

        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.schedule_param is not None:
            result['ScheduleParam'] = self.schedule_param

        if self.status is not None:
            result['Status'] = self.status

        if self.time_zone_id is not None:
            result['TimeZoneId'] = self.time_zone_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')

        if m.get('CronBeginDate') is not None:
            self.cron_begin_date = m.get('CronBeginDate')

        if m.get('CronEndDate') is not None:
            self.cron_end_date = m.get('CronEndDate')

        if m.get('CronStr') is not None:
            self.cron_str = m.get('CronStr')

        if m.get('CronSwitch') is not None:
            self.cron_switch = m.get('CronSwitch')

        if m.get('CronType') is not None:
            self.cron_type = m.get('CronType')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')

        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')

        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')

        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScheduleParam') is not None:
            self.schedule_param = m.get('ScheduleParam')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeZoneId') is not None:
            self.time_zone_id = m.get('TimeZoneId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

