# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeScheduleTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeScheduleTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result data.
        self.data = data
        # The message that is returned for the request.
        # 
        # >  If the request is successful, **Successful** is returned. If the request fails, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeScheduleTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeScheduleTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        timer_infos: List[main_models.DescribeScheduleTasksResponseBodyDataTimerInfos] = None,
        total_record_count: int = None,
    ):
        # The page number of the page returned.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The details of the scheduled tasks.
        self.timer_infos = timer_infos
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.timer_infos:
            for v1 in self.timer_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['TimerInfos'] = []
        if self.timer_infos is not None:
            for k1 in self.timer_infos:
                result['TimerInfos'].append(k1.to_map() if k1 else None)

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.timer_infos = []
        if m.get('TimerInfos') is not None:
            for k1 in m.get('TimerInfos'):
                temp_model = main_models.DescribeScheduleTasksResponseBodyDataTimerInfos()
                self.timer_infos.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeScheduleTasksResponseBodyDataTimerInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        crontab_job_id: str = None,
        dbcluster_id: str = None,
        db_cluster_description: str = None,
        db_cluster_status: str = None,
        order_id: str = None,
        planned_end_time: str = None,
        planned_flashing_off_time: str = None,
        planned_start_time: str = None,
        planned_time: str = None,
        region: str = None,
        status: str = None,
        task_cancel: bool = None,
        task_id: str = None,
    ):
        # The type of the scheduled tasks.
        self.action = action
        # The ID of the scheduled task.
        self.crontab_job_id = crontab_job_id
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The description of the cluster.
        self.db_cluster_description = db_cluster_description
        # The state of the cluster.
        self.db_cluster_status = db_cluster_status
        # The ID of the order.
        # 
        # >  This parameter is returned only when you set the `Action` parameter to **CreateDBNodes** or **ModifyDBNodeClass**.
        self.order_id = order_id
        # The latest start time of the task that you specified when you created the scheduled task. The time is displayed in UTC.
        self.planned_end_time = planned_end_time
        self.planned_flashing_off_time = planned_flashing_off_time
        # The earliest start time of the task that you specified when you created the scheduled task. The time is displayed in UTC.
        self.planned_start_time = planned_start_time
        # The expected start time of the task. The time is displayed in UTC.
        self.planned_time = planned_time
        # The ID of the region in which the scheduled task runs.
        self.region = region
        # The state of the scheduled task.
        self.status = status
        # Indicates whether the scheduled task can be canceled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.task_cancel = task_cancel
        # The ID of the task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.crontab_job_id is not None:
            result['CrontabJobId'] = self.crontab_job_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.db_cluster_description is not None:
            result['DbClusterDescription'] = self.db_cluster_description

        if self.db_cluster_status is not None:
            result['DbClusterStatus'] = self.db_cluster_status

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_flashing_off_time is not None:
            result['PlannedFlashingOffTime'] = self.planned_flashing_off_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.planned_time is not None:
            result['PlannedTime'] = self.planned_time

        if self.region is not None:
            result['Region'] = self.region

        if self.status is not None:
            result['Status'] = self.status

        if self.task_cancel is not None:
            result['TaskCancel'] = self.task_cancel

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CrontabJobId') is not None:
            self.crontab_job_id = m.get('CrontabJobId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DbClusterDescription') is not None:
            self.db_cluster_description = m.get('DbClusterDescription')

        if m.get('DbClusterStatus') is not None:
            self.db_cluster_status = m.get('DbClusterStatus')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedFlashingOffTime') is not None:
            self.planned_flashing_off_time = m.get('PlannedFlashingOffTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('PlannedTime') is not None:
            self.planned_time = m.get('PlannedTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskCancel') is not None:
            self.task_cancel = m.get('TaskCancel')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

