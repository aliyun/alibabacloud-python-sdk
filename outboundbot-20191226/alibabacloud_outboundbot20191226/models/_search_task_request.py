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
        # Call start time
        self.actual_time_gte = actual_time_gte
        # Call end time
        self.actual_time_lte = actual_time_lte
        # Minimum call duration, in milliseconds
        self.call_duration_gte = call_duration_gte
        # Maximum call duration, in milliseconds
        self.call_duration_lte = call_duration_lte
        # Called number
        self.called_number = called_number
        # Calling number
        self.calling_number = calling_number
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Job group ID
        self.job_group_id = job_group_id
        # Job group name
        self.job_group_name_query = job_group_name_query
        # Job ID
        self.job_id = job_id
        # Job status. Separate multiple statuses with commas. If you specify this parameter, it overrides jobStatusList.
        # 
        # - Scheduling: The job is being scheduled.
        # 
        # - Executing: The job is running.
        # 
        # - Succeeded: The job completed successfully.
        # 
        # - Paused: The job was paused.
        # 
        # - Failed: The job failed.
        # 
        # - Cancelled: The job was cancelled.
        self.job_status_string_list = job_status_string_list
        # Label-based filter condition for calls
        # 
        # > You can only use labels that have specific enumeration values. For example, labels configured with specific values in Large Language Model (LLM) scenarios.
        self.labels_json = labels_json
        # Other ID
        # 
        # **Valid values include the following:**
        # 
        # - sessionID
        # 
        # - taskid
        # 
        # - jobid
        self.other_id = other_id
        # Page number
        # 
        # > The first page is 0.
        self.page_index = page_index
        # Number of items per page
        # 
        # > If you omit this parameter, the default value is 10.
        self.page_size = page_size
        # Minimum ring duration, in seconds
        self.recording_duration_gte = recording_duration_gte
        # The minimum ringing duration for the search.
        self.recording_duration_lte = recording_duration_lte
        # Scenario name
        self.script_name_query = script_name_query
        # Sort field. Default value: actualTime
        self.sort_by = sort_by
        # Sort order. Valid values:
        # 
        # - asc (ascending)
        # 
        # - desc (descending). Default value.
        self.sort_order = sort_order
        # Start time of the task
        # 
        # > You must specify both TaskCreateTimeGte and TaskCreateTimeLte. If you omit either, the filter does not work.
        self.task_create_time_gte = task_create_time_gte
        # End time of the task
        # 
        # > You must specify both TaskCreateTimeGte and TaskCreateTimeLte. If you omit either, the filter does not work.
        self.task_create_time_lte = task_create_time_lte
        # Task ID
        self.task_id = task_id
        # Call status. Separate multiple statuses with commas.
        # 
        # - **Executing**: 0 (Calling).
        # 
        # - **Succeeded**: 1 (Connected).
        # 
        # - **NoAnswer**: 2 (No answer).
        # 
        # - **NotExist**: 3 (Nonexistent number).
        # 
        # - **Busy**: 4 (Line busy).
        # 
        # - **Cancelled**: 5 (Call canceled due to job stop).
        # 
        # - **Failed**: 6 (Call failed).
        # 
        # - **NotConnected**: 7 (Cannot connect).
        # 
        # - **PoweredOff**: 8 (Phone powered off).
        # 
        # - **OutOfService**: 9 (Called number out of service).
        # 
        # - **InArrears**: 10 (Called number overdue payment).
        # 
        # - **EmptyNumber**: 11 (Empty number, no outbound call).
        # 
        # - **PerDayCallCountLimit**: 12 (Daily call limit exceeded).
        # 
        # - **ContactBlockList**: 13 (Blacklisted).
        # 
        # - **CallerNotRegistered**: 14 (Caller number not registered).
        # 
        # - **Terminated**: 15 (Call terminated).
        # 
        # - **VerificationCancelled**: 16 (Call canceled due to pre-call validation failure).
        # 
        # - **OutOfServiceNoCall**: 17 (Called number out of service, no outbound call).
        # 
        # - **InArrearsNoCall**: 18 (Called number overdue payment, no outbound call).
        # 
        # - **CallingNumberNotExist**: 19 (Caller number does not exist).
        # 
        # - **SucceededFinish**: 20 (Connected and ended normally).
        # 
        # - **SucceededChatbotHangUpAfterNoAnswer**: 21 (Connected and robot hung up after rejection).
        # 
        # - **SucceededChatbotHangUpAfterSilence**: 22 (Connected and robot hung up after silence timeout).
        # 
        # - **SucceededClientHangUpAfterNoAnswer**: 23 (Connected and client hung up after rejection).
        # 
        # - **SucceededClientHangUp**: 24 (Connected and client hung up without reason).
        # 
        # - **SucceededTransferByIntent**: 25 (Connected and transferred to agent based on intent match).
        # 
        # - **SucceededTransferAfterNoAnswer**: 26 (Connected and transferred to agent after rejection).
        # 
        # - **SucceededInoInterAction**: 27 (Connected and no interaction from client side).
        # 
        # - **SucceededError**: 28 (Connected but system error interrupted).
        # 
        # - **SucceededSpecialInterceptVoiceAssistant**: 29 (Connected but intercepted by voice assistant).
        # 
        # - **SucceededSpecialInterceptExtensionNumberTransfer**: 30 (Connected but intercepted by extension transfer).
        # 
        # - **SucceededSpecialInterceptCustomSpecialIntercept**: 31 (Connected but intercepted by custom rule).
        # 
        # - **HighRiskSipCode**: 32 (High-risk SIP code, no outbound call).
        self.task_status_string_list = task_status_string_list
        # User ID. A unique identifier for a user.
        # 
        # > This field is passed when you upload an outbound call list.
        # >
        # > - If you upload the list in JSON format, the user ID is the value of referenceId.
        # >
        # > - If you upload the list as an Excel file, the user ID is the value of contactId.
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

