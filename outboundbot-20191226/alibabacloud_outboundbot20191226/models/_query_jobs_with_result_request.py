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
        # The filter condition for the call end time.
        self.end_actual_time_filter = end_actual_time_filter
        # Specifies whether the call was answered.
        self.has_answered_filter = has_answered_filter
        # Specifies whether the call was hung up due to rejection.
        self.has_hang_up_by_rejection_filter = has_hang_up_by_rejection_filter
        # Specifies whether the call reached the end of the flow.
        self.has_reached_end_of_flow_filter = has_reached_end_of_flow_filter
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of job failure reasons.
        self.job_failure_reasons_filter = job_failure_reasons_filter
        # The ID of the job group.
        # 
        # This parameter is required.
        self.job_group_id = job_group_id
        # The job status filter. Valid values:
        # - Scheduling: scheduling.
        # - Executing: executing.
        # - Succeeded: ended - reached.
        # - Paused: paused.
        # - Failed: ended - not reached.
        # - Cancelled: cancelled - manual intervention.
        self.job_status_filter = job_status_filter
        # The filter condition for labels associated with calls.
        # 
        # > This condition only supports filtering by labels that have specific enumerated label values configured, that is, labels with specific label values configured in large language model scenarios.
        self.labels_json = labels_json
        # The page number.
        # 
        # >Notice: This parameter is required.</notice>
        self.page_number = page_number
        # The page size.
        # >Notice: This parameter is required.</notice>
        self.page_size = page_size
        # The search content. You can search by phone number.
        self.query_text = query_text
        # The filter condition for the call start time.
        self.start_actual_time_filter = start_actual_time_filter
        # The call status, such as ["Executing","Succeeded"]. Separate multiple values with commas (,).
        # 
        # Valid values:
        # 
        # (Note: The **Succeeded** status has been subdivided into specific reasons. The **Succeeded**: 1 (answered) status is no longer returned. Instead, specific sub-reason types are returned.)
        # 
        # - **Executing**: 0 (dialing).
        # - **Succeeded**: 1 (answered).
        # - **NoAnswer**: 2 (not answered - no one picked up).
        # - **NotExist**: 3 (not answered - nonexistent number).
        # - **Busy**: 4 (not answered - busy).
        # - **Cancelled**: 5 (not dialed - task stopped).
        # - **Failed**: 6 (failed).
        # - **NotConnected**: 7 (not answered - unreachable).
        # - **PoweredOff**: 8 (not answered - powered off).
        # - **OutOfService**: 9 (not answered - callee out of service).
        # - **InArrears**: 10 (not answered - callee has overdue payment).
        # - **EmptyNumber**: 11 (not dialed - nonexistent number, no outbound call).
        # - **PerDayCallCountLimit**: 12 (not dialed - daily limit exceeded).
        # - **ContactBlockList**: 13 (not dialed - blacklisted).
        # - **CallerNotRegistered**: 14 (not dialed - caller number not registered).
        # - **Terminated**: 15 (not dialed - terminated).
        # - **VerificationCancelled**: 16 (not dialed - cancelled due to pre-call verification failure).
        # - **OutOfServiceNoCall**: 17 (not dialed - callee out of service, no outbound call).
        # - **InArrearsNoCall**: 18 (not dialed - callee has overdue payment, no outbound call).
        # - **CallingNumberNotExist**: 19 (not dialed - caller number does not exist).
        # - **SucceededFinish**: 20 (answered - completed normally).
        # - **SucceededChatbotHangUpAfterNoAnswer**: 21 (answered - robot hung up after rejection).
        # - **SucceededChatbotHangUpAfterSilence**: 22 (answered - hung up due to silence timeout).
        # - **SucceededClientHangUpAfterNoAnswer**: 23 (answered - user hung up after rejection).
        # - **SucceededClientHangUp**: 24 (answered - user hung up without reason).
        # - **SucceededTransferByIntent**: 25 (answered - transferred to agent by intent).
        # - **SucceededTransferAfterNoAnswer**: 26 (answered - transferred to agent after rejection).
        # - **SucceededInoInterAction**: 27 (answered - no interaction from user side).
        # - **SucceededError**: 28 (answered - interrupted by system error).
        # - **SucceededSpecialInterceptVoiceAssistant**: 29 (answered - special interception - voice assistant).
        # - **SucceededSpecialInterceptExtensionNumberTransfer**: 30 (answered - special interception - extension number transfer).
        # - **SucceededSpecialInterceptCustomSpecialIntercept**: 31 (answered - special interception - custom interception).
        # - **HighRiskSipCode**: 32 (not dialed - high risk, no outbound call).
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

