# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoProvisioningGroupHistoryResponseBody(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_histories: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistories = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array consisting of AutoProvisioningGroupHistory data.
        self.auto_provisioning_group_histories = auto_provisioning_group_histories
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of queried scheduling tasks in the auto provisioning group.
        self.total_count = total_count

    def validate(self):
        if self.auto_provisioning_group_histories:
            self.auto_provisioning_group_histories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_group_histories is not None:
            result['AutoProvisioningGroupHistories'] = self.auto_provisioning_group_histories.to_map()

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
        if m.get('AutoProvisioningGroupHistories') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistories()
            self.auto_provisioning_group_histories = temp_model.from_map(m.get('AutoProvisioningGroupHistories'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistories(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_history: List[main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistory] = None,
    ):
        self.auto_provisioning_group_history = auto_provisioning_group_history

    def validate(self):
        if self.auto_provisioning_group_history:
            for v1 in self.auto_provisioning_group_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoProvisioningGroupHistory'] = []
        if self.auto_provisioning_group_history is not None:
            for k1 in self.auto_provisioning_group_history:
                result['AutoProvisioningGroupHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_provisioning_group_history = []
        if m.get('AutoProvisioningGroupHistory') is not None:
            for k1 in m.get('AutoProvisioningGroupHistory'):
                temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistory()
                self.auto_provisioning_group_history.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistory(DaraModel):
    def __init__(
        self,
        activity_details: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetails = None,
        last_event_time: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # An array consisting of ActivityDetail data.
        self.activity_details = activity_details
        # The execution time of the last instance creation performed by the single scheduling task.
        self.last_event_time = last_event_time
        # The start time of executing the single scheduling task.
        self.start_time = start_time
        # The execution status of the single scheduling task. Valid values:
        # 
        # *   prepare: The scheduling task is being executed.
        # *   success: The scheduling task is executed.
        # *   failed: The scheduling task failed to be executed.
        self.status = status
        # The ID of the scheduling task.
        self.task_id = task_id

    def validate(self):
        if self.activity_details:
            self.activity_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_details is not None:
            result['ActivityDetails'] = self.activity_details.to_map()

        if self.last_event_time is not None:
            result['LastEventTime'] = self.last_event_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityDetails') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetails()
            self.activity_details = temp_model.from_map(m.get('ActivityDetails'))

        if m.get('LastEventTime') is not None:
            self.last_event_time = m.get('LastEventTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetails(DaraModel):
    def __init__(
        self,
        activity_detail: List[main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetail] = None,
    ):
        self.activity_detail = activity_detail

    def validate(self):
        if self.activity_detail:
            for v1 in self.activity_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActivityDetail'] = []
        if self.activity_detail is not None:
            for k1 in self.activity_detail:
                result['ActivityDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity_detail = []
        if m.get('ActivityDetail') is not None:
            for k1 in m.get('ActivityDetail'):
                temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetail()
                self.activity_detail.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetail(DaraModel):
    def __init__(
        self,
        detail: str = None,
        status: str = None,
    ):
        # The execution details of instance creation performed by the single scheduling task.
        self.detail = detail
        # The execution status of instance creation performed by the single scheduling task. Valid values:
        # 
        # *   Successful: Instances are created.
        # *   Failed: Instances failed to be created.
        # *   InProgress: Instances are being created.
        # *   Warning: Some instances are created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

