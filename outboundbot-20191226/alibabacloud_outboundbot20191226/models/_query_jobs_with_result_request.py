# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryJobsWithResultRequest(DaraModel):
    def __init__(
        self,
        end_actual_time_filter: int = None,
        has_answered_filter: bool = None,
        has_hang_up_by_rejection_filter: bool = None,
        has_reached_end_of_flow_filter: bool = None,
        instance_id: str = None,
        job_failure_reasons_filter: str = None,
        job_group_id: str = None,
        job_status_filter: str = None,
        labels_json: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        query_text: str = None,
        start_actual_time_filter: int = None,
        task_status_filter: str = None,
    ):
        self.end_actual_time_filter = end_actual_time_filter
        self.has_answered_filter = has_answered_filter
        self.has_hang_up_by_rejection_filter = has_hang_up_by_rejection_filter
        self.has_reached_end_of_flow_filter = has_reached_end_of_flow_filter
        # This parameter is required.
        self.instance_id = instance_id
        self.job_failure_reasons_filter = job_failure_reasons_filter
        # This parameter is required.
        self.job_group_id = job_group_id
        self.job_status_filter = job_status_filter
        self.labels_json = labels_json
        self.page_number = page_number
        self.page_size = page_size
        self.query_text = query_text
        self.start_actual_time_filter = start_actual_time_filter
        self.task_status_filter = task_status_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_actual_time_filter is not None:
            result['EndActualTimeFilter'] = self.end_actual_time_filter

        if self.has_answered_filter is not None:
            result['HasAnsweredFilter'] = self.has_answered_filter

        if self.has_hang_up_by_rejection_filter is not None:
            result['HasHangUpByRejectionFilter'] = self.has_hang_up_by_rejection_filter

        if self.has_reached_end_of_flow_filter is not None:
            result['HasReachedEndOfFlowFilter'] = self.has_reached_end_of_flow_filter

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_failure_reasons_filter is not None:
            result['JobFailureReasonsFilter'] = self.job_failure_reasons_filter

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_status_filter is not None:
            result['JobStatusFilter'] = self.job_status_filter

        if self.labels_json is not None:
            result['LabelsJson'] = self.labels_json

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.start_actual_time_filter is not None:
            result['StartActualTimeFilter'] = self.start_actual_time_filter

        if self.task_status_filter is not None:
            result['TaskStatusFilter'] = self.task_status_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndActualTimeFilter') is not None:
            self.end_actual_time_filter = m.get('EndActualTimeFilter')

        if m.get('HasAnsweredFilter') is not None:
            self.has_answered_filter = m.get('HasAnsweredFilter')

        if m.get('HasHangUpByRejectionFilter') is not None:
            self.has_hang_up_by_rejection_filter = m.get('HasHangUpByRejectionFilter')

        if m.get('HasReachedEndOfFlowFilter') is not None:
            self.has_reached_end_of_flow_filter = m.get('HasReachedEndOfFlowFilter')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobFailureReasonsFilter') is not None:
            self.job_failure_reasons_filter = m.get('JobFailureReasonsFilter')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobStatusFilter') is not None:
            self.job_status_filter = m.get('JobStatusFilter')

        if m.get('LabelsJson') is not None:
            self.labels_json = m.get('LabelsJson')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('StartActualTimeFilter') is not None:
            self.start_actual_time_filter = m.get('StartActualTimeFilter')

        if m.get('TaskStatusFilter') is not None:
            self.task_status_filter = m.get('TaskStatusFilter')

        return self

