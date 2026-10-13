# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchTaskRequest(DaraModel):
    def __init__(
        self,
        actual_time_gte: int = None,
        actual_time_lte: int = None,
        call_duration_gte: int = None,
        call_duration_lte: int = None,
        called_number: str = None,
        calling_number: str = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_group_name_query: str = None,
        job_id: str = None,
        job_status_string_list: str = None,
        labels_json: List[str] = None,
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
        # The start time of the call.
        self.actual_time_gte = actual_time_gte
        # The end time of the call.
        self.actual_time_lte = actual_time_lte
        # The minimum call duration for the search, in milliseconds.
        self.call_duration_gte = call_duration_gte
        # The maximum call duration for the search, in milliseconds.
        self.call_duration_lte = call_duration_lte
        # The called number.
        self.called_number = called_number
        # The calling number.
        self.calling_number = calling_number
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The job group ID.
        self.job_group_id = job_group_id
        # The name of the job group.
        self.job_group_name_query = job_group_name_query
        # The job ID.
        self.job_id = job_id
        # The job statuses. Separate multiple statuses with commas (,). If this field is not empty, it overwrites jobStatusList. Valid values:
        # 
        # - Scheduling: The job is being scheduled.
        # - Executing: The job is being executed.
        # - Succeeded: The job is finished and the called party is reached.
        # - Paused: The job is stopped.
        # - Failed: The job is finished but the called party is not reached.
        # - Cancelled: The job is canceled.
        self.job_status_string_list = job_status_string_list
        # The filter conditions for call labels.
        # 
        # > You can only filter by labels that are configured with specific enumerated label values, which means labels configured with specific values in large language model scenarios.
        self.labels_json = labels_json
        # The other IDs.
        # 
        # **This includes the following IDs:**
        # 
        # - sessionID
        # 
        # - taskid
        # 
        # - jobid
        self.other_id = other_id
        # The page number.
        # 
        # > Page numbers for this API operation start from 0 by default.
        self.page_index = page_index
        # The number of entries per page.
        # 
        # > If this parameter is left empty, the default value is 10.
        self.page_size = page_size
        # The minimum ringing duration for the search.
        self.recording_duration_gte = recording_duration_gte
        # The minimum ringing duration for the search.
        self.recording_duration_lte = recording_duration_lte
        # The scenario name.
        self.script_name_query = script_name_query
        # The sort field. Default value: actualTime.
        self.sort_by = sort_by
        # The sort order. Valid values:
        # 
        # - asc: Ascending order.
        # 
        # - desc: Descending order. This is the default value.
        self.sort_order = sort_order
        # The start time of the task.
        # 
        # > This parameter must be specified together with the TaskCreateTimeLte parameter. Otherwise, it does not take effect.
        self.task_create_time_gte = task_create_time_gte
        # The end time of the task.
        # > This parameter must be specified together with the TaskCreateTimeGte parameter. Otherwise, it does not take effect.
        self.task_create_time_lte = task_create_time_lte
        # The task ID.
        self.task_id = task_id
        # The call statuses. Separate multiple statuses with commas (,). Valid values:
        # (Note: The **Succeeded** status is subdivided into specific causes. The **Succeeded**: 1 (Connected) status is not displayed. All subsequent returned values are specific subdivided cause types.)
        # 
        # - **Executing**: 0 (Dialing).
        # - **Succeeded**: 1 (Connected).
        # - **NoAnswer**: 2 (Not connected - No answer).
        # - **NotExist**: 3 (Not connected - Nonexistent number).
        # - **Busy**: 4 (Not connected - Busy).
        # - **Cancelled**: 5 (Not called - Task stopped).
        # - **Failed**: 6 (Failed).
        # - **NotConnected**: 7 (Not connected - Unreachable).
        # - **PoweredOff**: 8 (Not connected - Powered off).
        # - **OutOfService**: 9 (Not connected - Suspended).
        # - **InArrears**: 10 (Not connected - Overdue payment).
        # - **EmptyNumber**: 11 (Not called - Nonexistent number, no call).
        # - **PerDayCallCountLimit**: 12 (Not called - Daily limit exceeded).
        # - **ContactBlockList**: 13 (Not called - Blacklisted).
        # - **CallerNotRegistered**: 14 (Not called - Calling number not registered).
        # - **Terminated**: 15 (Not called - Terminated).
        # - **VerificationCancelled**: 16 (Not called - Canceled due to pre-call verification failure).
        # - **OutOfServiceNoCall**: 17 (Not called - Suspended, no call).
        # - **InArrearsNoCall**: 18 (Not called - Overdue payment, no call).
        # - **CallingNumberNotExist**: 19 (Not called - Calling number does not exist).
        # - **SucceededFinish**: 20 (Connected - Finished normally).
        # - **SucceededChatbotHangUpAfterNoAnswer**: 21 (Connected - Bot hung up after unrecognized intent).
        # - **SucceededChatbotHangUpAfterSilence**: 22 (Connected - Hung up due to silence timeout).
        # - **SucceededClientHangUpAfterNoAnswer**: 23 (Connected - User hung up after unrecognized intent).
        # - **SucceededClientHangUp**: 24 (Connected - User hung up without reason).
        # - **SucceededTransferByIntent**: 25 (Connected - Transferred to agent due to matched intent).
        # - **SucceededTransferAfterNoAnswer**: 26 (Connected - Transferred to agent after unrecognized intent).
        # - **SucceededInoInterAction**: 27 (Connected - No interaction on the user side).
        # - **SucceededError**: 28 (Connected - Interrupted due to system exception).
        # - **SucceededSpecialInterceptVoiceAssistant**: 29 (Connected - Special interception - Voice assistant).
        # - **SucceededSpecialInterceptExtensionNumberTransfer**: 30 (Connected - Special interception - Extension number transfer).
        # - **SucceededSpecialInterceptCustomSpecialIntercept**: 31 (Connected - Special interception - Custom interception).
        # - **HighRiskSipCode**: 32 (Not called - High risk, no call).
        self.task_status_string_list = task_status_string_list
        # The user ID, which is the unique identifier of the user.
        # 
        # > This field is passed when you upload an outbound call list.
        # > - If the list is uploaded in JSON format, the user ID is the value of referenceId.
        # > - If the list is uploaded in an Excel file, the user ID is the value of contactId.
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

        if self.labels_json is not None:
            result['LabelsJson'] = self.labels_json

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

        if m.get('LabelsJson') is not None:
            self.labels_json = m.get('LabelsJson')

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

