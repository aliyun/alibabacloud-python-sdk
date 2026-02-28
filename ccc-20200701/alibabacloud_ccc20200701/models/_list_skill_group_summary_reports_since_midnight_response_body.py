# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListSkillGroupSummaryReportsSinceMidnightResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        paged_skill_group_summary_report: main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReport = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.paged_skill_group_summary_report = paged_skill_group_summary_report
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.paged_skill_group_summary_report:
            self.paged_skill_group_summary_report.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.paged_skill_group_summary_report is not None:
            result['PagedSkillGroupSummaryReport'] = self.paged_skill_group_summary_report.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PagedSkillGroupSummaryReport') is not None:
            temp_model = main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReport()
            self.paged_skill_group_summary_report = temp_model.from_map(m.get('PagedSkillGroupSummaryReport'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReport(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportList(DaraModel):
    def __init__(
        self,
        inbound: main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListInbound = None,
        instance_id: str = None,
        outbound: main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListOutbound = None,
        overall: main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListOverall = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
        timestamp: str = None,
    ):
        self.inbound = inbound
        self.instance_id = instance_id
        self.outbound = outbound
        self.overall = overall
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.timestamp = timestamp

    def validate(self):
        if self.inbound:
            self.inbound.validate()
        if self.outbound:
            self.outbound.validate()
        if self.overall:
            self.overall.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()

        if self.overall is not None:
            result['Overall'] = self.overall.to_map()

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inbound') is not None:
            temp_model = main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListInbound()
            self.inbound = temp_model.from_map(m.get('Inbound'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Outbound') is not None:
            temp_model = main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListOutbound()
            self.outbound = temp_model.from_map(m.get('Outbound'))

        if m.get('Overall') is not None:
            temp_model = main_models.ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListOverall()
            self.overall = temp_model.from_map(m.get('Overall'))

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListOverall(DaraModel):
    def __init__(
        self,
        average_ready_time: int = None,
        average_talk_time: int = None,
        average_work_time: int = None,
        max_ready_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        occupancy_rate: float = None,
        satisfaction_index: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_break_time: int = None,
        total_calls: int = None,
        total_logged_in_time: int = None,
        total_ready_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_ready_time = average_ready_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.max_ready_time = max_ready_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.occupancy_rate = occupancy_rate
        self.satisfaction_index = satisfaction_index
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_break_time = total_break_time
        self.total_calls = total_calls
        self.total_logged_in_time = total_logged_in_time
        self.total_ready_time = total_ready_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_ready_time is not None:
            result['AverageReadyTime'] = self.average_ready_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        if self.max_ready_time is not None:
            result['MaxReadyTime'] = self.max_ready_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time

        if self.occupancy_rate is not None:
            result['OccupancyRate'] = self.occupancy_rate

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

        if self.total_break_time is not None:
            result['TotalBreakTime'] = self.total_break_time

        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls

        if self.total_logged_in_time is not None:
            result['TotalLoggedInTime'] = self.total_logged_in_time

        if self.total_ready_time is not None:
            result['TotalReadyTime'] = self.total_ready_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageReadyTime') is not None:
            self.average_ready_time = m.get('AverageReadyTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        if m.get('MaxReadyTime') is not None:
            self.max_ready_time = m.get('MaxReadyTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')

        if m.get('OccupancyRate') is not None:
            self.occupancy_rate = m.get('OccupancyRate')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

        if m.get('TotalBreakTime') is not None:
            self.total_break_time = m.get('TotalBreakTime')

        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')

        if m.get('TotalLoggedInTime') is not None:
            self.total_logged_in_time = m.get('TotalLoggedInTime')

        if m.get('TotalReadyTime') is not None:
            self.total_ready_time = m.get('TotalReadyTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListOutbound(DaraModel):
    def __init__(
        self,
        answer_rate: float = None,
        average_dialing_time: int = None,
        average_talk_time: int = None,
        average_work_time: int = None,
        calls_abandoned: int = None,
        calls_agent_handled: int = None,
        calls_answered: int = None,
        calls_dialed: int = None,
        calls_offered: int = None,
        calls_queuing_cancelled: int = None,
        calls_queuing_failed: int = None,
        calls_queuing_failure: int = None,
        calls_queuing_overflow: int = None,
        calls_queuing_rerouted: int = None,
        calls_queuing_timeout: int = None,
        calls_service_level_30: str = None,
        calls_service_level_30v2: int = None,
        max_dialing_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_dialing_time: int = None,
        total_talk_time: int = None,
        total_wait_time: int = None,
        total_work_time: int = None,
    ):
        self.answer_rate = answer_rate
        self.average_dialing_time = average_dialing_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_abandoned = calls_abandoned
        self.calls_agent_handled = calls_agent_handled
        self.calls_answered = calls_answered
        self.calls_dialed = calls_dialed
        self.calls_offered = calls_offered
        self.calls_queuing_cancelled = calls_queuing_cancelled
        self.calls_queuing_failed = calls_queuing_failed
        self.calls_queuing_failure = calls_queuing_failure
        self.calls_queuing_overflow = calls_queuing_overflow
        self.calls_queuing_rerouted = calls_queuing_rerouted
        self.calls_queuing_timeout = calls_queuing_timeout
        self.calls_service_level_30 = calls_service_level_30
        self.calls_service_level_30v2 = calls_service_level_30v2
        self.max_dialing_time = max_dialing_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_index = satisfaction_index
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_dialing_time = total_dialing_time
        self.total_talk_time = total_talk_time
        self.total_wait_time = total_wait_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate

        if self.average_dialing_time is not None:
            result['AverageDialingTime'] = self.average_dialing_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        if self.calls_abandoned is not None:
            result['CallsAbandoned'] = self.calls_abandoned

        if self.calls_agent_handled is not None:
            result['CallsAgentHandled'] = self.calls_agent_handled

        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        if self.calls_queuing_cancelled is not None:
            result['CallsQueuingCancelled'] = self.calls_queuing_cancelled

        if self.calls_queuing_failed is not None:
            result['CallsQueuingFailed'] = self.calls_queuing_failed

        if self.calls_queuing_failure is not None:
            result['CallsQueuingFailure'] = self.calls_queuing_failure

        if self.calls_queuing_overflow is not None:
            result['CallsQueuingOverflow'] = self.calls_queuing_overflow

        if self.calls_queuing_rerouted is not None:
            result['CallsQueuingRerouted'] = self.calls_queuing_rerouted

        if self.calls_queuing_timeout is not None:
            result['CallsQueuingTimeout'] = self.calls_queuing_timeout

        if self.calls_service_level_30 is not None:
            result['CallsServiceLevel30'] = self.calls_service_level_30

        if self.calls_service_level_30v2 is not None:
            result['CallsServiceLevel30V2'] = self.calls_service_level_30v2

        if self.max_dialing_time is not None:
            result['MaxDialingTime'] = self.max_dialing_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

        if self.total_dialing_time is not None:
            result['TotalDialingTime'] = self.total_dialing_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')

        if m.get('AverageDialingTime') is not None:
            self.average_dialing_time = m.get('AverageDialingTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        if m.get('CallsAbandoned') is not None:
            self.calls_abandoned = m.get('CallsAbandoned')

        if m.get('CallsAgentHandled') is not None:
            self.calls_agent_handled = m.get('CallsAgentHandled')

        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        if m.get('CallsQueuingCancelled') is not None:
            self.calls_queuing_cancelled = m.get('CallsQueuingCancelled')

        if m.get('CallsQueuingFailed') is not None:
            self.calls_queuing_failed = m.get('CallsQueuingFailed')

        if m.get('CallsQueuingFailure') is not None:
            self.calls_queuing_failure = m.get('CallsQueuingFailure')

        if m.get('CallsQueuingOverflow') is not None:
            self.calls_queuing_overflow = m.get('CallsQueuingOverflow')

        if m.get('CallsQueuingRerouted') is not None:
            self.calls_queuing_rerouted = m.get('CallsQueuingRerouted')

        if m.get('CallsQueuingTimeout') is not None:
            self.calls_queuing_timeout = m.get('CallsQueuingTimeout')

        if m.get('CallsServiceLevel30') is not None:
            self.calls_service_level_30 = m.get('CallsServiceLevel30')

        if m.get('CallsServiceLevel30V2') is not None:
            self.calls_service_level_30v2 = m.get('CallsServiceLevel30V2')

        if m.get('MaxDialingTime') is not None:
            self.max_dialing_time = m.get('MaxDialingTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

        if m.get('TotalDialingTime') is not None:
            self.total_dialing_time = m.get('TotalDialingTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class ListSkillGroupSummaryReportsSinceMidnightResponseBodyPagedSkillGroupSummaryReportListInbound(DaraModel):
    def __init__(
        self,
        abandoned_in_queue_of_queue_count: int = None,
        answered_by_agent_of_queue_count: int = None,
        answered_by_agent_of_queue_max_wait_time_duration: int = None,
        answered_by_agent_of_queue_wait_time_duration: int = None,
        average_ring_time: int = None,
        average_talk_time: int = None,
        average_work_time: int = None,
        calls_abandoned: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_out: int = None,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_overflow: str = None,
        calls_queuing_canceled: str = None,
        calls_queuing_failure: str = None,
        calls_queuing_rerouted: str = None,
        calls_queuing_timeout: int = None,
        calls_service_level_10: int = None,
        calls_service_level_20: int = None,
        calls_service_level_30: int = None,
        calls_timeout: int = None,
        give_up_by_agent_of_queue_count: int = None,
        handle_rate: float = None,
        in_coming_queue_of_queue_count: int = None,
        max_ring_time: int = None,
        max_talk_time: str = None,
        max_work_time: int = None,
        over_flow_in_queue_of_queue_count: int = None,
        queue_max_wait_time_duration: int = None,
        queue_wait_time_duration: int = None,
        satisfaction_index: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        service_level_20: float = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.abandoned_in_queue_of_queue_count = abandoned_in_queue_of_queue_count
        self.answered_by_agent_of_queue_count = answered_by_agent_of_queue_count
        self.answered_by_agent_of_queue_max_wait_time_duration = answered_by_agent_of_queue_max_wait_time_duration
        self.answered_by_agent_of_queue_wait_time_duration = answered_by_agent_of_queue_wait_time_duration
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_abandoned = calls_abandoned
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_handled = calls_handled
        self.calls_offered = calls_offered
        self.calls_overflow = calls_overflow
        self.calls_queuing_canceled = calls_queuing_canceled
        self.calls_queuing_failure = calls_queuing_failure
        self.calls_queuing_rerouted = calls_queuing_rerouted
        self.calls_queuing_timeout = calls_queuing_timeout
        self.calls_service_level_10 = calls_service_level_10
        self.calls_service_level_20 = calls_service_level_20
        self.calls_service_level_30 = calls_service_level_30
        self.calls_timeout = calls_timeout
        self.give_up_by_agent_of_queue_count = give_up_by_agent_of_queue_count
        self.handle_rate = handle_rate
        self.in_coming_queue_of_queue_count = in_coming_queue_of_queue_count
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.over_flow_in_queue_of_queue_count = over_flow_in_queue_of_queue_count
        self.queue_max_wait_time_duration = queue_max_wait_time_duration
        self.queue_wait_time_duration = queue_wait_time_duration
        self.satisfaction_index = satisfaction_index
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.service_level_20 = service_level_20
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandoned_in_queue_of_queue_count is not None:
            result['AbandonedInQueueOfQueueCount'] = self.abandoned_in_queue_of_queue_count

        if self.answered_by_agent_of_queue_count is not None:
            result['AnsweredByAgentOfQueueCount'] = self.answered_by_agent_of_queue_count

        if self.answered_by_agent_of_queue_max_wait_time_duration is not None:
            result['AnsweredByAgentOfQueueMaxWaitTimeDuration'] = self.answered_by_agent_of_queue_max_wait_time_duration

        if self.answered_by_agent_of_queue_wait_time_duration is not None:
            result['AnsweredByAgentOfQueueWaitTimeDuration'] = self.answered_by_agent_of_queue_wait_time_duration

        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        if self.calls_abandoned is not None:
            result['CallsAbandoned'] = self.calls_abandoned

        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out

        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out

        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        if self.calls_overflow is not None:
            result['CallsOverflow'] = self.calls_overflow

        if self.calls_queuing_canceled is not None:
            result['CallsQueuingCanceled'] = self.calls_queuing_canceled

        if self.calls_queuing_failure is not None:
            result['CallsQueuingFailure'] = self.calls_queuing_failure

        if self.calls_queuing_rerouted is not None:
            result['CallsQueuingRerouted'] = self.calls_queuing_rerouted

        if self.calls_queuing_timeout is not None:
            result['CallsQueuingTimeout'] = self.calls_queuing_timeout

        if self.calls_service_level_10 is not None:
            result['CallsServiceLevel10'] = self.calls_service_level_10

        if self.calls_service_level_20 is not None:
            result['CallsServiceLevel20'] = self.calls_service_level_20

        if self.calls_service_level_30 is not None:
            result['CallsServiceLevel30'] = self.calls_service_level_30

        if self.calls_timeout is not None:
            result['CallsTimeout'] = self.calls_timeout

        if self.give_up_by_agent_of_queue_count is not None:
            result['GiveUpByAgentOfQueueCount'] = self.give_up_by_agent_of_queue_count

        if self.handle_rate is not None:
            result['HandleRate'] = self.handle_rate

        if self.in_coming_queue_of_queue_count is not None:
            result['InComingQueueOfQueueCount'] = self.in_coming_queue_of_queue_count

        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time

        if self.over_flow_in_queue_of_queue_count is not None:
            result['OverFlowInQueueOfQueueCount'] = self.over_flow_in_queue_of_queue_count

        if self.queue_max_wait_time_duration is not None:
            result['QueueMaxWaitTimeDuration'] = self.queue_max_wait_time_duration

        if self.queue_wait_time_duration is not None:
            result['QueueWaitTimeDuration'] = self.queue_wait_time_duration

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

        if self.service_level_20 is not None:
            result['ServiceLevel20'] = self.service_level_20

        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonedInQueueOfQueueCount') is not None:
            self.abandoned_in_queue_of_queue_count = m.get('AbandonedInQueueOfQueueCount')

        if m.get('AnsweredByAgentOfQueueCount') is not None:
            self.answered_by_agent_of_queue_count = m.get('AnsweredByAgentOfQueueCount')

        if m.get('AnsweredByAgentOfQueueMaxWaitTimeDuration') is not None:
            self.answered_by_agent_of_queue_max_wait_time_duration = m.get('AnsweredByAgentOfQueueMaxWaitTimeDuration')

        if m.get('AnsweredByAgentOfQueueWaitTimeDuration') is not None:
            self.answered_by_agent_of_queue_wait_time_duration = m.get('AnsweredByAgentOfQueueWaitTimeDuration')

        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        if m.get('CallsAbandoned') is not None:
            self.calls_abandoned = m.get('CallsAbandoned')

        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')

        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')

        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        if m.get('CallsOverflow') is not None:
            self.calls_overflow = m.get('CallsOverflow')

        if m.get('CallsQueuingCanceled') is not None:
            self.calls_queuing_canceled = m.get('CallsQueuingCanceled')

        if m.get('CallsQueuingFailure') is not None:
            self.calls_queuing_failure = m.get('CallsQueuingFailure')

        if m.get('CallsQueuingRerouted') is not None:
            self.calls_queuing_rerouted = m.get('CallsQueuingRerouted')

        if m.get('CallsQueuingTimeout') is not None:
            self.calls_queuing_timeout = m.get('CallsQueuingTimeout')

        if m.get('CallsServiceLevel10') is not None:
            self.calls_service_level_10 = m.get('CallsServiceLevel10')

        if m.get('CallsServiceLevel20') is not None:
            self.calls_service_level_20 = m.get('CallsServiceLevel20')

        if m.get('CallsServiceLevel30') is not None:
            self.calls_service_level_30 = m.get('CallsServiceLevel30')

        if m.get('CallsTimeout') is not None:
            self.calls_timeout = m.get('CallsTimeout')

        if m.get('GiveUpByAgentOfQueueCount') is not None:
            self.give_up_by_agent_of_queue_count = m.get('GiveUpByAgentOfQueueCount')

        if m.get('HandleRate') is not None:
            self.handle_rate = m.get('HandleRate')

        if m.get('InComingQueueOfQueueCount') is not None:
            self.in_coming_queue_of_queue_count = m.get('InComingQueueOfQueueCount')

        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')

        if m.get('OverFlowInQueueOfQueueCount') is not None:
            self.over_flow_in_queue_of_queue_count = m.get('OverFlowInQueueOfQueueCount')

        if m.get('QueueMaxWaitTimeDuration') is not None:
            self.queue_max_wait_time_duration = m.get('QueueMaxWaitTimeDuration')

        if m.get('QueueWaitTimeDuration') is not None:
            self.queue_wait_time_duration = m.get('QueueWaitTimeDuration')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

        if m.get('ServiceLevel20') is not None:
            self.service_level_20 = m.get('ServiceLevel20')

        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

