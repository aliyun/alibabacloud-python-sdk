# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListBaselineStatusesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListBaselineStatusesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of baseline instances returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The unique ID of the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListBaselineStatusesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBaselineStatusesResponseBodyData(DaraModel):
    def __init__(
        self,
        baseline_statuses: List[main_models.ListBaselineStatusesResponseBodyDataBaselineStatuses] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of baseline instances.
        self.baseline_statuses = baseline_statuses
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of baseline instances.
        self.total_count = total_count

    def validate(self):
        if self.baseline_statuses:
            for v1 in self.baseline_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaselineStatuses'] = []
        if self.baseline_statuses is not None:
            for k1 in self.baseline_statuses:
                result['BaselineStatuses'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_statuses = []
        if m.get('BaselineStatuses') is not None:
            for k1 in m.get('BaselineStatuses'):
                temp_model = main_models.ListBaselineStatusesResponseBodyDataBaselineStatuses()
                self.baseline_statuses.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBaselineStatusesResponseBodyDataBaselineStatuses(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        baseline_name: str = None,
        baseline_type: str = None,
        bizdate: int = None,
        buffer: int = None,
        end_cast: int = None,
        exp_time: int = None,
        finish_status: str = None,
        finish_time: int = None,
        in_group_id: int = None,
        owner: str = None,
        priority: int = None,
        project_id: int = None,
        sla_time: int = None,
        status: str = None,
    ):
        # The ID of the baseline.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline. Valid values: DAILY and HOURLY.
        self.baseline_type = baseline_type
        # The business date timestamp.
        self.bizdate = bizdate
        # The buffer time of the baseline instance, in seconds.
        self.buffer = buffer
        # The estimated completion time of the baseline instance.
        self.end_cast = end_cast
        # The warning time of the baseline instance.
        # 
        # The format is a 13-digit number, such as `1553531400000`.
        self.exp_time = exp_time
        # The completion status of the baseline instance. Valid values: UNFINISH and FINISH.
        self.finish_status = finish_status
        # The completion timestamp of the baseline instance. This parameter is returned only when FinishStatus is FINISH.
        self.finish_time = finish_time
        # The cycle number of the baseline instance. The value is 1 for daily baselines. The value ranges from 1 to 24 for hourly baselines.
        self.in_group_id = in_group_id
        # The Alibaba Cloud UID of the baseline owner. Separate multiple owners with commas (,).
        self.owner = owner
        # The priority of the baseline. Valid values: 1, 3, 5, 7, and 8.
        self.priority = priority
        # The ID of the workspace where the baseline resides.
        self.project_id = project_id
        # The actual completion time of the baseline instance.
        # 
        # The format is a 13-digit number, such as `1553531400000`.
        self.sla_time = sla_time
        # The status of the baseline. Valid values: ERROR, SAFE, DANGEROUS, and OVER.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.baseline_type is not None:
            result['BaselineType'] = self.baseline_type

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.buffer is not None:
            result['Buffer'] = self.buffer

        if self.end_cast is not None:
            result['EndCast'] = self.end_cast

        if self.exp_time is not None:
            result['ExpTime'] = self.exp_time

        if self.finish_status is not None:
            result['FinishStatus'] = self.finish_status

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.in_group_id is not None:
            result['InGroupId'] = self.in_group_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sla_time is not None:
            result['SlaTime'] = self.sla_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('BaselineType') is not None:
            self.baseline_type = m.get('BaselineType')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('Buffer') is not None:
            self.buffer = m.get('Buffer')

        if m.get('EndCast') is not None:
            self.end_cast = m.get('EndCast')

        if m.get('ExpTime') is not None:
            self.exp_time = m.get('ExpTime')

        if m.get('FinishStatus') is not None:
            self.finish_status = m.get('FinishStatus')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InGroupId') is not None:
            self.in_group_id = m.get('InGroupId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SlaTime') is not None:
            self.sla_time = m.get('SlaTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

