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
        # Filters for calls that ended on or before the specified time. Specify the time as a UNIX timestamp in milliseconds.
        self.end_actual_time_filter = end_actual_time_filter
        # Filters jobs by whether the call was answered.
        self.has_answered_filter = has_answered_filter
        # Filters jobs by whether the call was disconnected due to a rejection.
        self.has_hang_up_by_rejection_filter = has_hang_up_by_rejection_filter
        # Filters jobs by whether the call flow was completed.
        self.has_reached_end_of_flow_filter = has_reached_end_of_flow_filter
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The job failure reasons to filter by.
        self.job_failure_reasons_filter = job_failure_reasons_filter
        # The ID of the job group.
        # 
        # This parameter is required.
        self.job_group_id = job_group_id
        # The job status to filter by. Valid values:
        # 
        # - `Scheduling`: The job is scheduled and awaiting execution.
        # 
        # - `Executing`: The job is in progress.
        # 
        # - `Succeeded`: The job is completed and the contact was reached.
        # 
        # - `Paused`: The job is paused.
        # 
        # - `Failed`: The job completed but failed to reach the contact.
        # 
        # - `Cancelled`: The job was canceled by a user.
        self.job_status_filter = job_status_filter
        # The filter conditions for calls, based on their labels.
        # 
        # > This filter applies only to labels that are configured with a predefined set of values (enumerated values). These labels are typically used in large model scenarios.
        self.labels_json = labels_json
        # The page number.
        # 
        # >Notice: 
        # 
        # This parameter is required.
        self.page_number = page_number
        # Page size
        # >Notice: This parameter is required.
        self.page_size = page_size
        # The search query for a specific job, such as the contact\\"s phone number.
        self.query_text = query_text
        # Filters for calls that started on or after the specified time. Specify the time as a UNIX timestamp in milliseconds.
        self.start_actual_time_filter = start_actual_time_filter
        # The call statuses to filter by. You can specify multiple statuses as a JSON array of strings, such as `["Executing", "Succeeded"]`.
        # Valid values:
        # (Note: The **Succeeded** status is subdivided into more specific reasons. The general **Succeeded** (1: Connected) status is no longer returned. Instead, one of the more specific sub-statuses is returned.)
        # 
        # - **Executing** (0): The call is being placed.
        # 
        # - **Succeeded** (1): The call was connected.
        # 
        # - **NoAnswer** (2): Not connected - No answer.
        # 
        # - **NotExist** (3): Not connected - The dialed number does not exist.
        # 
        # - **Busy** (4): Not connected - The line was busy.
        # 
        # - **Cancelled** (5): Not placed - The job was stopped before the call could be dialed.
        # 
        # - **Failed** (6): The call failed.
        # 
        # - **NotConnected** (7): Not connected - The call could not be connected.
        # 
        # - **PoweredOff** (8): Not connected - The recipient\\"s phone was powered off.
        # 
        # - **OutOfService** (9): Not connected - The recipient\\"s number is out of service.
        # 
        # - **InArrears** (10): Not connected - The recipient\\"s account is in arrears.
        # 
        # - **EmptyNumber** (11): Not placed - The number was identified as an empty number and was not dialed.
        # 
        # - **PerDayCallCountLimit** (12): Not placed - The daily call limit was reached.
        # 
        # - **ContactBlockList** (13): Not placed - The number is on a blocklist.
        # 
        # - **CallerNotRegistered** (14): Not placed - The calling number is not registered.
        # 
        # - **Terminated** (15): Not placed - The call was terminated.
        # 
        # - **VerificationCancelled** (16): Not placed - Canceled after failing a pre-call verification.
        # 
        # - **OutOfServiceNoCall** (17): Not placed - The number is out of service and was not dialed.
        # 
        # - **InArrearsNoCall** (18): Not placed - The recipient is in arrears and was not dialed.
        # 
        # - **CallingNumberNotExist** (19): Not placed - The calling number does not exist.
        # 
        # - **SucceededFinish** (20): Connected - The call completed normally.
        # 
        # - **SucceededChatbotHangUpAfterNoAnswer** (21): Connected - The chatbot hung up after a rejection.
        # 
        # - **SucceededChatbotHangUpAfterSilence** (22): Connected - The chatbot hung up due to a silence timeout.
        # 
        # - **SucceededClientHangUpAfterNoAnswer** (23): Connected - The user hung up after a rejection.
        # 
        # - **SucceededClientHangUp** (24): Connected - The user hung up for no specific reason.
        # 
        # - **SucceededTransferByIntent** (25): Connected - The call was transferred to an agent based on user intent.
        # 
        # - **SucceededTransferAfterNoAnswer** (26): Connected - The call was transferred to an agent after a rejection.
        # 
        # - **SucceededInoInterAction** (27): Connected - No interaction from the user.
        # 
        # - **SucceededError** (28): Connected - The call was interrupted by a system error.
        # 
        # - **SucceededSpecialInterceptVoiceAssistant** (29): Connected - Intercepted by a voice assistant.
        # 
        # - **SucceededSpecialInterceptExtensionNumberTransfer** (30): Connected - Intercepted for an extension number transfer.
        # 
        # - **SucceededSpecialInterceptCustomSpecialIntercept** (31): Connected - Intercepted by a custom rule.
        # 
        # - **HighRiskSipCode** (32): Not placed - High-risk SIP code.
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

