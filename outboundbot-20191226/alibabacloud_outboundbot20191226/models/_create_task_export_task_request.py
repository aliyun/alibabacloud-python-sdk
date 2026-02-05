# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskExportTaskRequest(DaraModel):
    def __init__(
        self,
        actual_time_gte: int = None,
        actual_time_lte: int = None,
        call_duration_gte: int = None,
        call_duration_lte: int = None,
        called_number: str = None,
        calling_number: str = None,
        has_answered: bool = None,
        has_hang_up_by_rejection: bool = None,
        has_reached_end_of_flow: bool = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_group_name_query: str = None,
        job_id: str = None,
        job_status_string_list: str = None,
        other_id: str = None,
        page_index: int = None,
        page_size: int = None,
        recording_duration_gte: int = None,
        recording_duration_lte: int = None,
        script_name_query: str = None,
        sort_by: str = None,
        sort_order: str = None,
        task_create_time_gte: int = None,
        task_create_time_lte: int = None,
        task_id: str = None,
        task_status_string_list: str = None,
        user_id_match: str = None,
    ):
        self.actual_time_gte = actual_time_gte
        self.actual_time_lte = actual_time_lte
        self.call_duration_gte = call_duration_gte
        self.call_duration_lte = call_duration_lte
        self.called_number = called_number
        self.calling_number = calling_number
        self.has_answered = has_answered
        self.has_hang_up_by_rejection = has_hang_up_by_rejection
        self.has_reached_end_of_flow = has_reached_end_of_flow
        # This parameter is required.
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.job_group_name_query = job_group_name_query
        self.job_id = job_id
        self.job_status_string_list = job_status_string_list
        self.other_id = other_id
        self.page_index = page_index
        self.page_size = page_size
        self.recording_duration_gte = recording_duration_gte
        self.recording_duration_lte = recording_duration_lte
        self.script_name_query = script_name_query
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.task_create_time_gte = task_create_time_gte
        self.task_create_time_lte = task_create_time_lte
        self.task_id = task_id
        self.task_status_string_list = task_status_string_list
        self.user_id_match = user_id_match

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time_gte is not None:
            result['ActualTimeGte'] = self.actual_time_gte

        if self.actual_time_lte is not None:
            result['ActualTimeLte'] = self.actual_time_lte

        if self.call_duration_gte is not None:
            result['CallDurationGte'] = self.call_duration_gte

        if self.call_duration_lte is not None:
            result['CallDurationLte'] = self.call_duration_lte

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.has_answered is not None:
            result['HasAnswered'] = self.has_answered

        if self.has_hang_up_by_rejection is not None:
            result['HasHangUpByRejection'] = self.has_hang_up_by_rejection

        if self.has_reached_end_of_flow is not None:
            result['HasReachedEndOfFlow'] = self.has_reached_end_of_flow

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_name_query is not None:
            result['JobGroupNameQuery'] = self.job_group_name_query

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_status_string_list is not None:
            result['JobStatusStringList'] = self.job_status_string_list

        if self.other_id is not None:
            result['OtherId'] = self.other_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.recording_duration_gte is not None:
            result['RecordingDurationGte'] = self.recording_duration_gte

        if self.recording_duration_lte is not None:
            result['RecordingDurationLte'] = self.recording_duration_lte

        if self.script_name_query is not None:
            result['ScriptNameQuery'] = self.script_name_query

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.task_create_time_gte is not None:
            result['TaskCreateTimeGte'] = self.task_create_time_gte

        if self.task_create_time_lte is not None:
            result['TaskCreateTimeLte'] = self.task_create_time_lte

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status_string_list is not None:
            result['TaskStatusStringList'] = self.task_status_string_list

        if self.user_id_match is not None:
            result['UserIdMatch'] = self.user_id_match

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTimeGte') is not None:
            self.actual_time_gte = m.get('ActualTimeGte')

        if m.get('ActualTimeLte') is not None:
            self.actual_time_lte = m.get('ActualTimeLte')

        if m.get('CallDurationGte') is not None:
            self.call_duration_gte = m.get('CallDurationGte')

        if m.get('CallDurationLte') is not None:
            self.call_duration_lte = m.get('CallDurationLte')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('HasAnswered') is not None:
            self.has_answered = m.get('HasAnswered')

        if m.get('HasHangUpByRejection') is not None:
            self.has_hang_up_by_rejection = m.get('HasHangUpByRejection')

        if m.get('HasReachedEndOfFlow') is not None:
            self.has_reached_end_of_flow = m.get('HasReachedEndOfFlow')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupNameQuery') is not None:
            self.job_group_name_query = m.get('JobGroupNameQuery')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStatusStringList') is not None:
            self.job_status_string_list = m.get('JobStatusStringList')

        if m.get('OtherId') is not None:
            self.other_id = m.get('OtherId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordingDurationGte') is not None:
            self.recording_duration_gte = m.get('RecordingDurationGte')

        if m.get('RecordingDurationLte') is not None:
            self.recording_duration_lte = m.get('RecordingDurationLte')

        if m.get('ScriptNameQuery') is not None:
            self.script_name_query = m.get('ScriptNameQuery')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('TaskCreateTimeGte') is not None:
            self.task_create_time_gte = m.get('TaskCreateTimeGte')

        if m.get('TaskCreateTimeLte') is not None:
            self.task_create_time_lte = m.get('TaskCreateTimeLte')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatusStringList') is not None:
            self.task_status_string_list = m.get('TaskStatusStringList')

        if m.get('UserIdMatch') is not None:
            self.user_id_match = m.get('UserIdMatch')

        return self

