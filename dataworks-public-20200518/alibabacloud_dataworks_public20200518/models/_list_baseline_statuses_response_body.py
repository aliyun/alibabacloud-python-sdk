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
        # The data returned.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
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
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The type of the baseline, including DAILY and HOURLY. Separate multiple types with commas (,).
        self.baseline_type = baseline_type
        # The data timestamp.
        self.bizdate = bizdate
        # The margin of the baseline instance. Unit: seconds.
        self.buffer = buffer
        # The timestamp of the predicted time when the baseline instance finished running.
        self.end_cast = end_cast
        # The timestamp of the alerting time of the baseline instance.
        self.exp_time = exp_time
        # The status of the baseline instance. Valid values: UNFINISH and FINISH.
        self.finish_status = finish_status
        # The timestamp of the actual time when the baseline instance finished running. This parameter is returned if the value of the FinishStatus parameter is FINISH.
        self.finish_time = finish_time
        # The ID of the cycle of the baseline instance. Valid values of the ID of an hour-level cycle: [1,24]. The ID of a day-level cycle is 1.
        self.in_group_id = in_group_id
        # The ID of the Alibaba Cloud account used by the baseline owner. Multiple IDs are separated by commas (,).
        self.owner = owner
        # The priority of the baseline. Valid values: {1,3,5,7,8}.
        self.priority = priority
        # The ID of the workspace to which the baseline belongs.
        self.project_id = project_id
        # The timestamp of the actual time when the baseline instance finished running.
        self.sla_time = sla_time
        # The status of the baseline. Valid values: ERROR, SAFE, DANGEROUS, and OVER. The value ERROR indicates that no nodes are associated with the baseline, or all nodes associated with the baseline are suspended. The value SAFE indicates that nodes are run before the alert duration begins. The value DANGEROUS indicates that nodes are still running after the alert duration ends but the committed completion time does not arrive. The value OVER indicates that nodes are still running after the committed completion time.
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

