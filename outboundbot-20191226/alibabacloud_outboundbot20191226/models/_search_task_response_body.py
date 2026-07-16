# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class SearchTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        labels: List[main_models.SearchTaskResponseBodyLabels] = None,
        message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        search_task_info_list: List[main_models.SearchTaskResponseBodySearchTaskInfoList] = None,
        success: bool = None,
        total: int = None,
        variable_names: List[str] = None,
    ):
        # Request status code
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Labels available for filtering.
        # 
        # > Displays all labels with enumeration values in this job group.
        self.labels = labels
        # Response message
        self.message = message
        # Page number
        self.page_index = page_index
        # Number of items per page
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # List of tasks
        self.search_task_info_list = search_task_info_list
        # Indicates whether the request succeeded
        self.success = success
        # Total number of items
        self.total = total
        # Complete list of label keys
        self.variable_names = variable_names

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.search_task_info_list:
            for v1 in self.search_task_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SearchTaskInfoList'] = []
        if self.search_task_info_list is not None:
            for k1 in self.search_task_info_list:
                result['SearchTaskInfoList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        if self.variable_names is not None:
            result['VariableNames'] = self.variable_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.SearchTaskResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.search_task_info_list = []
        if m.get('SearchTaskInfoList') is not None:
            for k1 in m.get('SearchTaskInfoList'):
                temp_model = main_models.SearchTaskResponseBodySearchTaskInfoList()
                self.search_task_info_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('VariableNames') is not None:
            self.variable_names = m.get('VariableNames')

        return self

class SearchTaskResponseBodySearchTaskInfoList(DaraModel):
    def __init__(
        self,
        actual_time: int = None,
        call_duration: int = None,
        call_duration_display: str = None,
        called_number: str = None,
        calling_number: str = None,
        dial_exception: str = None,
        dial_exception_codes: List[str] = None,
        dial_exception_old: str = None,
        has_answered: bool = None,
        has_hang_up_by_rejection: bool = None,
        has_last_playback_completed: bool = None,
        has_reached_end_of_flow: bool = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_group_name: str = None,
        job_id: str = None,
        job_status: int = None,
        job_status_name: str = None,
        job_status_string: str = None,
        labels: List[main_models.SearchTaskResponseBodySearchTaskInfoListLabels] = None,
        recording_duration: int = None,
        script_name: str = None,
        task_create_time: int = None,
        task_end_reason: int = None,
        task_id: str = None,
        task_status: int = None,
        task_status_name: str = None,
        task_status_string: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # Actual execution time
        self.actual_time = actual_time
        # Call duration, in milliseconds
        self.call_duration = call_duration
        # Call duration
        self.call_duration_display = call_duration_display
        # Called number
        self.called_number = called_number
        # Calling number
        self.calling_number = calling_number
        # Exception details
        self.dial_exception = dial_exception
        # Exception codes shown on the remarks page
        self.dial_exception_codes = dial_exception_codes
        # Exception details
        self.dial_exception_old = dial_exception_old
        # Indicates whether the called party answered
        self.has_answered = has_answered
        # Indicates whether the call ended due to rejection
        self.has_hang_up_by_rejection = has_hang_up_by_rejection
        # Indicates whether the last audio playback completed before hangup
        self.has_last_playback_completed = has_last_playback_completed
        # Indicates whether the conversation ended
        self.has_reached_end_of_flow = has_reached_end_of_flow
        # Instance ID
        self.instance_id = instance_id
        # Job group ID
        self.job_group_id = job_group_id
        # Job group name
        self.job_group_name = job_group_name
        # Job ID
        self.job_id = job_id
        # Job status
        # 
        # - 0: Scheduling
        # 
        # - 1: Executing
        # 
        # - 2: Succeeded
        # 
        # - 3: Paused
        # 
        # - 4: Failed
        # 
        # - 5: Cancelled
        self.job_status = job_status
        # Display text for job status
        # 
        # - 0: Scheduling
        # 
        # - 1: Executing
        # 
        # - 2: Succeeded
        # 
        # - 3: Paused
        # 
        # - 4: Failed
        # 
        # - 5: Cancelled
        self.job_status_name = job_status_name
        # Job status
        # 
        # - Scheduling (0)
        # 
        # - Executing (1)
        # 
        # - Completed—Reached (2)
        # 
        # - Paused (3)
        # 
        # - Failed—Line busy (4)
        # 
        # - Cancelled (5)
        self.job_status_string = job_status_string
        # Labels matched for this outbound call
        self.labels = labels
        # Ringing duration, in seconds
        self.recording_duration = recording_duration
        # Scenario name
        self.script_name = script_name
        # Task creation time
        self.task_create_time = task_create_time
        # Reason why the task ended
        # 
        # - FINISHED(1,"Normal completion")
        # 
        # - CHATBOT_HANGUP_AFTER_NOANSWER(2, "Robot hangup after rejection")
        # 
        # - CHATBOT_HANGUP_AFTER_SILENCE(3, "Robot hangup after silence timeout")
        # 
        # - CLIENT_HANGUP_AFTER_NOANSWER(4, "Client hangup after rejection")
        # 
        # - CLIENT_HANGUP(5, "Client hangup without reason")
        # 
        # - TRANSFER_BY_INTENT(6, "Transfer to agent based on intent match")
        # 
        # - TRANSFER_AFTER_NOANSWER(7, "Transfer to agent after rejection")
        # 
        # - INO_INTERACTION(8, "No interaction from client side")
        # 
        # - ERROR(9, "System error interrupted")
        # 
        # - SPECIAL_INTERCEPT_VOICE_ASSISTANT(10, "Intercepted by voice assistant")
        # 
        # - SPECIAL_INTERCEPT_EXTENSION_NUMBER_TRANSFER(11, "Intercepted by extension transfer")
        self.task_end_reason = task_end_reason
        # Task ID
        self.task_id = task_id
        # Valid values:
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
        self.task_status = task_status
        # Display text for task status
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
        self.task_status_name = task_status_name
        # Task status
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
        self.task_status_string = task_status_string
        # User ID
        self.user_id = user_id
        # Username
        self.user_name = user_name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time

        if self.call_duration is not None:
            result['CallDuration'] = self.call_duration

        if self.call_duration_display is not None:
            result['CallDurationDisplay'] = self.call_duration_display

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.dial_exception is not None:
            result['DialException'] = self.dial_exception

        if self.dial_exception_codes is not None:
            result['DialExceptionCodes'] = self.dial_exception_codes

        if self.dial_exception_old is not None:
            result['DialExceptionOld'] = self.dial_exception_old

        if self.has_answered is not None:
            result['HasAnswered'] = self.has_answered

        if self.has_hang_up_by_rejection is not None:
            result['HasHangUpByRejection'] = self.has_hang_up_by_rejection

        if self.has_last_playback_completed is not None:
            result['HasLastPlaybackCompleted'] = self.has_last_playback_completed

        if self.has_reached_end_of_flow is not None:
            result['HasReachedEndOfFlow'] = self.has_reached_end_of_flow

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.job_status_name is not None:
            result['JobStatusName'] = self.job_status_name

        if self.job_status_string is not None:
            result['JobStatusString'] = self.job_status_string

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.recording_duration is not None:
            result['RecordingDuration'] = self.recording_duration

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.task_create_time is not None:
            result['TaskCreateTime'] = self.task_create_time

        if self.task_end_reason is not None:
            result['TaskEndReason'] = self.task_end_reason

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_name is not None:
            result['TaskStatusName'] = self.task_status_name

        if self.task_status_string is not None:
            result['TaskStatusString'] = self.task_status_string

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')

        if m.get('CallDuration') is not None:
            self.call_duration = m.get('CallDuration')

        if m.get('CallDurationDisplay') is not None:
            self.call_duration_display = m.get('CallDurationDisplay')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('DialException') is not None:
            self.dial_exception = m.get('DialException')

        if m.get('DialExceptionCodes') is not None:
            self.dial_exception_codes = m.get('DialExceptionCodes')

        if m.get('DialExceptionOld') is not None:
            self.dial_exception_old = m.get('DialExceptionOld')

        if m.get('HasAnswered') is not None:
            self.has_answered = m.get('HasAnswered')

        if m.get('HasHangUpByRejection') is not None:
            self.has_hang_up_by_rejection = m.get('HasHangUpByRejection')

        if m.get('HasLastPlaybackCompleted') is not None:
            self.has_last_playback_completed = m.get('HasLastPlaybackCompleted')

        if m.get('HasReachedEndOfFlow') is not None:
            self.has_reached_end_of_flow = m.get('HasReachedEndOfFlow')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('JobStatusName') is not None:
            self.job_status_name = m.get('JobStatusName')

        if m.get('JobStatusString') is not None:
            self.job_status_string = m.get('JobStatusString')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.SearchTaskResponseBodySearchTaskInfoListLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('RecordingDuration') is not None:
            self.recording_duration = m.get('RecordingDuration')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('TaskCreateTime') is not None:
            self.task_create_time = m.get('TaskCreateTime')

        if m.get('TaskEndReason') is not None:
            self.task_end_reason = m.get('TaskEndReason')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusName') is not None:
            self.task_status_name = m.get('TaskStatusName')

        if m.get('TaskStatusString') is not None:
            self.task_status_string = m.get('TaskStatusString')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class SearchTaskResponseBodySearchTaskInfoListLabels(DaraModel):
    def __init__(
        self,
        k: str = None,
        v: str = None,
    ):
        # Label name
        self.k = k
        # Matched label value
        self.v = v

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.k is not None:
            result['K'] = self.k

        if self.v is not None:
            result['V'] = self.v

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K') is not None:
            self.k = m.get('K')

        if m.get('V') is not None:
            self.v = m.get('V')

        return self

class SearchTaskResponseBodyLabels(DaraModel):
    def __init__(
        self,
        name: str = None,
        value_list: List[str] = None,
    ):
        # Label name
        self.name = name
        # List of label values
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

