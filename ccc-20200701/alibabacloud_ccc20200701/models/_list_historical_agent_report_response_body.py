# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListHistoricalAgentReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListHistoricalAgentReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListHistoricalAgentReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHistoricalAgentReportResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListHistoricalAgentReportResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of agent historical data.
        self.list = list
        # The page number. Valid values: 1 to 100.
        self.page_number = page_number
        # The page size. Valid values: 1 to 100.
        self.page_size = page_size
        # The total count.
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
                temp_model = main_models.ListHistoricalAgentReportResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHistoricalAgentReportResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        back_2back: main_models.ListHistoricalAgentReportResponseBodyDataListBack2Back = None,
        display_id: str = None,
        inbound: main_models.ListHistoricalAgentReportResponseBodyDataListInbound = None,
        internal: main_models.ListHistoricalAgentReportResponseBodyDataListInternal = None,
        outbound: main_models.ListHistoricalAgentReportResponseBodyDataListOutbound = None,
        overall: main_models.ListHistoricalAgentReportResponseBodyDataListOverall = None,
        skill_group_ids: str = None,
        skill_group_names: str = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The agent name.
        self.agent_name = agent_name
        # The back-to-back call metrics.
        self.back_2back = back_2back
        # The agent display ID.
        self.display_id = display_id
        # The inbound data.
        self.inbound = inbound
        # The internal call metrics.
        self.internal = internal
        # The outbound data.
        self.outbound = outbound
        # The overall data.
        self.overall = overall
        # The list of skill group IDs to which the agent belongs. The format is a JSON array character string. Each array element is a skill group ID.
        self.skill_group_ids = skill_group_ids
        # The list of skill group names to which the agent belongs. The format is a JSON array character string. Each array element is a skill group name.
        self.skill_group_names = skill_group_names

    def validate(self):
        if self.back_2back:
            self.back_2back.validate()
        if self.inbound:
            self.inbound.validate()
        if self.internal:
            self.internal.validate()
        if self.outbound:
            self.outbound.validate()
        if self.overall:
            self.overall.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.back_2back is not None:
            result['Back2Back'] = self.back_2back.to_map()

        if self.display_id is not None:
            result['DisplayId'] = self.display_id

        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()

        if self.internal is not None:
            result['Internal'] = self.internal.to_map()

        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()

        if self.overall is not None:
            result['Overall'] = self.overall.to_map()

        if self.skill_group_ids is not None:
            result['SkillGroupIds'] = self.skill_group_ids

        if self.skill_group_names is not None:
            result['SkillGroupNames'] = self.skill_group_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Back2Back') is not None:
            temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListBack2Back()
            self.back_2back = temp_model.from_map(m.get('Back2Back'))

        if m.get('DisplayId') is not None:
            self.display_id = m.get('DisplayId')

        if m.get('Inbound') is not None:
            temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListInbound()
            self.inbound = temp_model.from_map(m.get('Inbound'))

        if m.get('Internal') is not None:
            temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListInternal()
            self.internal = temp_model.from_map(m.get('Internal'))

        if m.get('Outbound') is not None:
            temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListOutbound()
            self.outbound = temp_model.from_map(m.get('Outbound'))

        if m.get('Overall') is not None:
            temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListOverall()
            self.overall = temp_model.from_map(m.get('Overall'))

        if m.get('SkillGroupIds') is not None:
            self.skill_group_ids = m.get('SkillGroupIds')

        if m.get('SkillGroupNames') is not None:
            self.skill_group_names = m.get('SkillGroupNames')

        return self

class ListHistoricalAgentReportResponseBodyDataListOverall(DaraModel):
    def __init__(
        self,
        average_break_time: float = None,
        average_hold_time: float = None,
        average_ready_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        break_code_detail_list: List[main_models.ListHistoricalAgentReportResponseBodyDataListOverallBreakCodeDetailList] = None,
        first_check_in_time: int = None,
        last_check_out_time: int = None,
        max_break_time: int = None,
        max_hold_time: int = None,
        max_ready_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        occupancy_rate: float = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_break_time: int = None,
        total_calls: int = None,
        total_hold_time: int = None,
        total_logged_in_time: int = None,
        total_off_site_logged_in_time: int = None,
        total_off_site_online_time: int = None,
        total_office_phone_logged_in_time: int = None,
        total_office_phone_online_time: int = None,
        total_on_site_logged_in_time: int = None,
        total_on_site_online_time: int = None,
        total_outbound_scenario_logged_in_time: int = None,
        total_outbound_scenario_ready_time: int = None,
        total_outbound_scenario_time: int = None,
        total_ready_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        # The average break duration. Formula: TotalBreakTime / number of breaks. The number of breaks is a non-API statistical field. Unit: seconds.
        self.average_break_time = average_break_time
        # The average hold duration. Unit: seconds. Formula: TotalHoldTime / (inbound CallsHold + outbound CallsHold).
        self.average_hold_time = average_hold_time
        # The average ready duration. Formula: TotalReadyTime / number of ready states. The number of ready states is a non-API statistical field. Unit: seconds.
        self.average_ready_time = average_ready_time
        # The average talk duration. Formula: TotalTalkTime / (CallsAnswered + CallsHandled). Unit: seconds.
        self.average_talk_time = average_talk_time
        # The average after-call work duration. Formula: TotalWorkTime / TotalCalls. Unit: seconds.
        self.average_work_time = average_work_time
        # The statistics for each break type.
        self.break_code_detail_list = break_code_detail_list
        # The earliest check-in time. The value is a UNIX timestamp. Unit: milliseconds.
        self.first_check_in_time = first_check_in_time
        # The last check-out time. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_check_out_time = last_check_out_time
        # The maximum break duration. Unit: seconds.
        self.max_break_time = max_break_time
        # The maximum hold time. Unit: seconds.
        self.max_hold_time = max_hold_time
        # The maximum ready duration. Unit: seconds.
        self.max_ready_time = max_ready_time
        # The maximum talk time. Unit: seconds.
        self.max_talk_time = max_talk_time
        # The maximum after-call work (ACW) time. Unit: seconds.
        self.max_work_time = max_work_time
        # The agent occupancy rate. Formula: (TotalWorkTime + TotalTalkTime) / TotalLoggedInTime.
        self.occupancy_rate = occupancy_rate
        # The satisfaction index, which is the average value of satisfaction survey key presses (single-digit numbers).
        self.satisfaction_index = satisfaction_index
        # The satisfaction rate. Formula: number of satisfied ratings/number of satisfaction survey responses.
        self.satisfaction_rate = satisfaction_rate
        # The number of satisfaction surveys sent.
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        # The number of satisfaction survey responses.
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        # The total break duration. Unit: seconds.
        self.total_break_time = total_break_time
        # The total number of calls. Formula: CallsOffered + CallsDialed.
        self.total_calls = total_calls
        # The total hold duration. Unit: seconds.
        self.total_hold_time = total_hold_time
        # The total logged-in duration, excluding break time. Unit: seconds.
        self.total_logged_in_time = total_logged_in_time
        # The total off-site online duration. Unit: seconds.
        self.total_off_site_logged_in_time = total_off_site_logged_in_time
        # The total off-site online duration. Unit: seconds.
        self.total_off_site_online_time = total_off_site_online_time
        # The total online duration in office phone mode. Unit: seconds.
        self.total_office_phone_logged_in_time = total_office_phone_logged_in_time
        # The total online duration in office phone mode. Unit: seconds.
        self.total_office_phone_online_time = total_office_phone_online_time
        # The total on-site online duration. Unit: seconds.
        self.total_on_site_logged_in_time = total_on_site_logged_in_time
        # The total on-site online duration. Unit: seconds.
        self.total_on_site_online_time = total_on_site_online_time
        # The total outbound-only online duration. Unit: seconds.
        self.total_outbound_scenario_logged_in_time = total_outbound_scenario_logged_in_time
        # The total outbound-only idle duration. Unit: seconds.
        self.total_outbound_scenario_ready_time = total_outbound_scenario_ready_time
        # The total outbound-only online duration. Unit: seconds.
        self.total_outbound_scenario_time = total_outbound_scenario_time
        # The total ready duration. Unit: seconds.
        self.total_ready_time = total_ready_time
        # The total talk time. Unit: seconds.
        self.total_talk_time = total_talk_time
        # The total after-call work (ACW) time. Unit: seconds.
        self.total_work_time = total_work_time

    def validate(self):
        if self.break_code_detail_list:
            for v1 in self.break_code_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_break_time is not None:
            result['AverageBreakTime'] = self.average_break_time

        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time

        if self.average_ready_time is not None:
            result['AverageReadyTime'] = self.average_ready_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        result['BreakCodeDetailList'] = []
        if self.break_code_detail_list is not None:
            for k1 in self.break_code_detail_list:
                result['BreakCodeDetailList'].append(k1.to_map() if k1 else None)

        if self.first_check_in_time is not None:
            result['FirstCheckInTime'] = self.first_check_in_time

        if self.last_check_out_time is not None:
            result['LastCheckOutTime'] = self.last_check_out_time

        if self.max_break_time is not None:
            result['MaxBreakTime'] = self.max_break_time

        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time

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

        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

        if self.total_break_time is not None:
            result['TotalBreakTime'] = self.total_break_time

        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls

        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time

        if self.total_logged_in_time is not None:
            result['TotalLoggedInTime'] = self.total_logged_in_time

        if self.total_off_site_logged_in_time is not None:
            result['TotalOffSiteLoggedInTime'] = self.total_off_site_logged_in_time

        if self.total_off_site_online_time is not None:
            result['TotalOffSiteOnlineTime'] = self.total_off_site_online_time

        if self.total_office_phone_logged_in_time is not None:
            result['TotalOfficePhoneLoggedInTime'] = self.total_office_phone_logged_in_time

        if self.total_office_phone_online_time is not None:
            result['TotalOfficePhoneOnlineTime'] = self.total_office_phone_online_time

        if self.total_on_site_logged_in_time is not None:
            result['TotalOnSiteLoggedInTime'] = self.total_on_site_logged_in_time

        if self.total_on_site_online_time is not None:
            result['TotalOnSiteOnlineTime'] = self.total_on_site_online_time

        if self.total_outbound_scenario_logged_in_time is not None:
            result['TotalOutboundScenarioLoggedInTime'] = self.total_outbound_scenario_logged_in_time

        if self.total_outbound_scenario_ready_time is not None:
            result['TotalOutboundScenarioReadyTime'] = self.total_outbound_scenario_ready_time

        if self.total_outbound_scenario_time is not None:
            result['TotalOutboundScenarioTime'] = self.total_outbound_scenario_time

        if self.total_ready_time is not None:
            result['TotalReadyTime'] = self.total_ready_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageBreakTime') is not None:
            self.average_break_time = m.get('AverageBreakTime')

        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')

        if m.get('AverageReadyTime') is not None:
            self.average_ready_time = m.get('AverageReadyTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        self.break_code_detail_list = []
        if m.get('BreakCodeDetailList') is not None:
            for k1 in m.get('BreakCodeDetailList'):
                temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListOverallBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k1))

        if m.get('FirstCheckInTime') is not None:
            self.first_check_in_time = m.get('FirstCheckInTime')

        if m.get('LastCheckOutTime') is not None:
            self.last_check_out_time = m.get('LastCheckOutTime')

        if m.get('MaxBreakTime') is not None:
            self.max_break_time = m.get('MaxBreakTime')

        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')

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

        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

        if m.get('TotalBreakTime') is not None:
            self.total_break_time = m.get('TotalBreakTime')

        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')

        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')

        if m.get('TotalLoggedInTime') is not None:
            self.total_logged_in_time = m.get('TotalLoggedInTime')

        if m.get('TotalOffSiteLoggedInTime') is not None:
            self.total_off_site_logged_in_time = m.get('TotalOffSiteLoggedInTime')

        if m.get('TotalOffSiteOnlineTime') is not None:
            self.total_off_site_online_time = m.get('TotalOffSiteOnlineTime')

        if m.get('TotalOfficePhoneLoggedInTime') is not None:
            self.total_office_phone_logged_in_time = m.get('TotalOfficePhoneLoggedInTime')

        if m.get('TotalOfficePhoneOnlineTime') is not None:
            self.total_office_phone_online_time = m.get('TotalOfficePhoneOnlineTime')

        if m.get('TotalOnSiteLoggedInTime') is not None:
            self.total_on_site_logged_in_time = m.get('TotalOnSiteLoggedInTime')

        if m.get('TotalOnSiteOnlineTime') is not None:
            self.total_on_site_online_time = m.get('TotalOnSiteOnlineTime')

        if m.get('TotalOutboundScenarioLoggedInTime') is not None:
            self.total_outbound_scenario_logged_in_time = m.get('TotalOutboundScenarioLoggedInTime')

        if m.get('TotalOutboundScenarioReadyTime') is not None:
            self.total_outbound_scenario_ready_time = m.get('TotalOutboundScenarioReadyTime')

        if m.get('TotalOutboundScenarioTime') is not None:
            self.total_outbound_scenario_time = m.get('TotalOutboundScenarioTime')

        if m.get('TotalReadyTime') is not None:
            self.total_ready_time = m.get('TotalReadyTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class ListHistoricalAgentReportResponseBodyDataListOverallBreakCodeDetailList(DaraModel):
    def __init__(
        self,
        break_code: str = None,
        count: int = None,
        duration: int = None,
    ):
        # The break type code.
        self.break_code = break_code
        # The number of occurrences of this break type.
        self.count = count
        # The total duration of this break type. Unit: seconds.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.break_code is not None:
            result['BreakCode'] = self.break_code

        if self.count is not None:
            result['Count'] = self.count

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

class ListHistoricalAgentReportResponseBodyDataListOutbound(DaraModel):
    def __init__(
        self,
        answer_rate: float = None,
        average_dialing_time: float = None,
        average_hold_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_answered: int = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_dialed: int = None,
        calls_hold: int = None,
        calls_ringed: int = None,
        max_dialing_time: int = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_dialing_time: int = None,
        total_hold_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        # The answer rate. Formula: CallsAnswered/CallsDialed. Because the answer event and the dial event may fall within different time ranges, the result may exceed 100% in some cases.
        self.answer_rate = answer_rate
        # The average dialing time. Formula: TotalDialingTime/CallsDialed. Unit: seconds.
        self.average_dialing_time = average_dialing_time
        # The average hold time. Formula: TotalHoldTime/CallsHold. Unit: seconds.
        self.average_hold_time = average_hold_time
        # The average ring time. Formula: TotalRingTime/CallsRinged. Unit: seconds.
        self.average_ring_time = average_ring_time
        # The average talk time. Formula: TotalTalkTime/CallsAnswered. Unit: seconds.
        self.average_talk_time = average_talk_time
        # The average after-call work (ACW) time. Formula: TotalWorkTime/CallsDialed. Unit: seconds.
        self.average_work_time = average_work_time
        # The number of calls answered.
        self.calls_answered = calls_answered
        # The number of attended transfers in. If a call is transferred in to this agent multiple times, each transfer is counted separately.
        self.calls_attended_transfer_in = calls_attended_transfer_in
        # The number of attended transfers out. If a call is transferred out to other agents multiple times, each transfer is counted separately.
        self.calls_attended_transfer_out = calls_attended_transfer_out
        # The number of blind transfers in. If a call is transferred in to this agent multiple times, each transfer is counted separately.
        self.calls_blind_transfer_in = calls_blind_transfer_in
        # The number of blind transfers out. If a call is transferred out to other agents multiple times, each transfer is counted separately.
        self.calls_blind_transfer_out = calls_blind_transfer_out
        # The number of calls dialed.
        self.calls_dialed = calls_dialed
        # The number of holds, which is the number of times calls were placed on hold.
        self.calls_hold = calls_hold
        # The number of calls that rang the agent.
        self.calls_ringed = calls_ringed
        # The maximum dialing time. Unit: seconds.
        self.max_dialing_time = max_dialing_time
        # The maximum hold time. Unit: seconds.
        self.max_hold_time = max_hold_time
        # The maximum ring time. Unit: seconds.
        self.max_ring_time = max_ring_time
        # The maximum talk time. Unit: seconds.
        self.max_talk_time = max_talk_time
        # The maximum after-call work (ACW) time. Unit: seconds.
        self.max_work_time = max_work_time
        # The satisfaction index, which is the average value of satisfaction survey key presses (single-digit numbers).
        self.satisfaction_index = satisfaction_index
        # The satisfaction rate. Formula: number of satisfied ratings/number of satisfaction survey responses.
        self.satisfaction_rate = satisfaction_rate
        # The number of satisfaction surveys sent.
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        # The number of satisfaction survey responses.
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        # The total dialing time. Unit: seconds.
        self.total_dialing_time = total_dialing_time
        # The total hold time. Unit: seconds.
        self.total_hold_time = total_hold_time
        # The total ring time. Unit: seconds.
        self.total_ring_time = total_ring_time
        # The total talk time. Unit: seconds.
        self.total_talk_time = total_talk_time
        # The total after-call work (ACW) time. Unit: seconds.
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

        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time

        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.calls_attended_transfer_in is not None:
            result['CallsAttendedTransferIn'] = self.calls_attended_transfer_in

        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out

        if self.calls_blind_transfer_in is not None:
            result['CallsBlindTransferIn'] = self.calls_blind_transfer_in

        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold

        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed

        if self.max_dialing_time is not None:
            result['MaxDialingTime'] = self.max_dialing_time

        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time

        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

        if self.total_dialing_time is not None:
            result['TotalDialingTime'] = self.total_dialing_time

        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time

        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')

        if m.get('AverageDialingTime') is not None:
            self.average_dialing_time = m.get('AverageDialingTime')

        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')

        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('CallsAttendedTransferIn') is not None:
            self.calls_attended_transfer_in = m.get('CallsAttendedTransferIn')

        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')

        if m.get('CallsBlindTransferIn') is not None:
            self.calls_blind_transfer_in = m.get('CallsBlindTransferIn')

        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')

        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')

        if m.get('MaxDialingTime') is not None:
            self.max_dialing_time = m.get('MaxDialingTime')

        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')

        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

        if m.get('TotalDialingTime') is not None:
            self.total_dialing_time = m.get('TotalDialingTime')

        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')

        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class ListHistoricalAgentReportResponseBodyDataListInternal(DaraModel):
    def __init__(
        self,
        average_talk_time: float = None,
        calls_answered: int = None,
        calls_dialed: int = None,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_talked: int = None,
        max_talk_time: int = None,
        total_talk_time: int = None,
    ):
        # The average talk duration. Unit: seconds.
        self.average_talk_time = average_talk_time
        # The number of calls answered.
        self.calls_answered = calls_answered
        # The number of calls dialed.
        self.calls_dialed = calls_dialed
        # The number of calls answered.
        self.calls_handled = calls_handled
        # The number of inbound calls.
        self.calls_offered = calls_offered
        # The number of calls participated in.
        self.calls_talked = calls_talked
        # The maximum talk time. Unit: seconds.
        self.max_talk_time = max_talk_time
        # The total talk time. Unit: seconds.
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        if self.calls_talked is not None:
            result['CallsTalked'] = self.calls_talked

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        if m.get('CallsTalked') is not None:
            self.calls_talked = m.get('CallsTalked')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        return self

class ListHistoricalAgentReportResponseBodyDataListInbound(DaraModel):
    def __init__(
        self,
        access_channel_type_details: List[main_models.ListHistoricalAgentReportResponseBodyDataListInboundAccessChannelTypeDetails] = None,
        average_first_response_time: float = None,
        average_hold_time: float = None,
        average_response_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_handled: int = None,
        calls_hold: int = None,
        calls_offered: int = None,
        calls_ringed: int = None,
        handle_rate: float = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        service_level_15: float = None,
        total_hold_time: int = None,
        total_messages_sent: int = None,
        total_messages_sent_by_agent: int = None,
        total_messages_sent_by_customer: str = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        # The statistics by channel.
        self.access_channel_type_details = access_channel_type_details
        # The average first response time for chat sessions. Unit: seconds.
        self.average_first_response_time = average_first_response_time
        # The average hold time. Formula: TotalHoldTime/CallsHold. Unit: seconds.
        self.average_hold_time = average_hold_time
        # The average response time for chat sessions.
        self.average_response_time = average_response_time
        # The average ring time. Formula: TotalRingTime/CallsRinged. Unit: seconds.
        self.average_ring_time = average_ring_time
        # The average talk time. Formula: TotalTalkTime/CallsHandled. Unit: seconds.
        self.average_talk_time = average_talk_time
        # The average after-call work (ACW) time. Formula: TotalWorkTime/CallsHandled. Unit: seconds.
        self.average_work_time = average_work_time
        # The number of attended transfers in. If a call is transferred in to this agent multiple times, each transfer is counted separately.
        self.calls_attended_transfer_in = calls_attended_transfer_in
        # The number of attended transfers out. If a call is transferred out to other agents multiple times, each transfer is counted separately.
        self.calls_attended_transfer_out = calls_attended_transfer_out
        # The number of blind transfers in. If a call is transferred in to this agent multiple times, each transfer is counted separately.
        self.calls_blind_transfer_in = calls_blind_transfer_in
        # The number of blind transfers out. If a call is transferred out to other agents multiple times, each transfer is counted separately.
        self.calls_blind_transfer_out = calls_blind_transfer_out
        # The number of calls answered by the agent.
        self.calls_handled = calls_handled
        # The number of holds, which is the number of times calls were placed on hold.
        self.calls_hold = calls_hold
        # The number of calls offered, which is the number of calls assigned to this agent, including calls blind-transferred and attended-transferred from other agents.
        self.calls_offered = calls_offered
        # The number of calls that rang the agent.
        self.calls_ringed = calls_ringed
        # The handle rate. Formula: CallsHandled/CallsOffered. Because the answer event and the offered event may fall within different time ranges, the result may exceed 100% in some cases.
        self.handle_rate = handle_rate
        # The maximum hold time. Unit: seconds.
        self.max_hold_time = max_hold_time
        # The maximum ring time. Unit: seconds.
        self.max_ring_time = max_ring_time
        # The maximum talk time. Unit: seconds.
        self.max_talk_time = max_talk_time
        # The maximum after-call work (ACW) time. Unit: seconds.
        self.max_work_time = max_work_time
        # The satisfaction index, which is the average value of satisfaction survey key presses (single-digit numbers).
        self.satisfaction_index = satisfaction_index
        # The satisfaction rate. Formula: number of satisfied ratings/number of satisfaction survey responses.
        self.satisfaction_rate = satisfaction_rate
        # The number of satisfaction surveys sent.
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        # The number of satisfaction survey responses.
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        # The 15-second service level.
        self.service_level_15 = service_level_15
        # The total hold time. Unit: seconds.
        self.total_hold_time = total_hold_time
        # The total number of messages sent in chat sessions.
        self.total_messages_sent = total_messages_sent
        # The total number of messages sent by the agent in chat sessions.
        self.total_messages_sent_by_agent = total_messages_sent_by_agent
        # The total number of messages sent by the customer in chat sessions.
        self.total_messages_sent_by_customer = total_messages_sent_by_customer
        # The total ring time. Unit: seconds.
        self.total_ring_time = total_ring_time
        # The total talk time. Unit: seconds.
        self.total_talk_time = total_talk_time
        # The total after-call work (ACW) time. Unit: seconds.
        self.total_work_time = total_work_time

    def validate(self):
        if self.access_channel_type_details:
            for v1 in self.access_channel_type_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessChannelTypeDetails'] = []
        if self.access_channel_type_details is not None:
            for k1 in self.access_channel_type_details:
                result['AccessChannelTypeDetails'].append(k1.to_map() if k1 else None)

        if self.average_first_response_time is not None:
            result['AverageFirstResponseTime'] = self.average_first_response_time

        if self.average_hold_time is not None:
            result['AverageHoldTime'] = self.average_hold_time

        if self.average_response_time is not None:
            result['AverageResponseTime'] = self.average_response_time

        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        if self.calls_attended_transfer_in is not None:
            result['CallsAttendedTransferIn'] = self.calls_attended_transfer_in

        if self.calls_attended_transfer_out is not None:
            result['CallsAttendedTransferOut'] = self.calls_attended_transfer_out

        if self.calls_blind_transfer_in is not None:
            result['CallsBlindTransferIn'] = self.calls_blind_transfer_in

        if self.calls_blind_transfer_out is not None:
            result['CallsBlindTransferOut'] = self.calls_blind_transfer_out

        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled

        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed

        if self.handle_rate is not None:
            result['HandleRate'] = self.handle_rate

        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time

        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_work_time is not None:
            result['MaxWorkTime'] = self.max_work_time

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

        if self.service_level_15 is not None:
            result['ServiceLevel15'] = self.service_level_15

        if self.total_hold_time is not None:
            result['TotalHoldTime'] = self.total_hold_time

        if self.total_messages_sent is not None:
            result['TotalMessagesSent'] = self.total_messages_sent

        if self.total_messages_sent_by_agent is not None:
            result['TotalMessagesSentByAgent'] = self.total_messages_sent_by_agent

        if self.total_messages_sent_by_customer is not None:
            result['TotalMessagesSentByCustomer'] = self.total_messages_sent_by_customer

        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_channel_type_details = []
        if m.get('AccessChannelTypeDetails') is not None:
            for k1 in m.get('AccessChannelTypeDetails'):
                temp_model = main_models.ListHistoricalAgentReportResponseBodyDataListInboundAccessChannelTypeDetails()
                self.access_channel_type_details.append(temp_model.from_map(k1))

        if m.get('AverageFirstResponseTime') is not None:
            self.average_first_response_time = m.get('AverageFirstResponseTime')

        if m.get('AverageHoldTime') is not None:
            self.average_hold_time = m.get('AverageHoldTime')

        if m.get('AverageResponseTime') is not None:
            self.average_response_time = m.get('AverageResponseTime')

        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        if m.get('CallsAttendedTransferIn') is not None:
            self.calls_attended_transfer_in = m.get('CallsAttendedTransferIn')

        if m.get('CallsAttendedTransferOut') is not None:
            self.calls_attended_transfer_out = m.get('CallsAttendedTransferOut')

        if m.get('CallsBlindTransferIn') is not None:
            self.calls_blind_transfer_in = m.get('CallsBlindTransferIn')

        if m.get('CallsBlindTransferOut') is not None:
            self.calls_blind_transfer_out = m.get('CallsBlindTransferOut')

        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')

        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')

        if m.get('HandleRate') is not None:
            self.handle_rate = m.get('HandleRate')

        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')

        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxWorkTime') is not None:
            self.max_work_time = m.get('MaxWorkTime')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

        if m.get('ServiceLevel15') is not None:
            self.service_level_15 = m.get('ServiceLevel15')

        if m.get('TotalHoldTime') is not None:
            self.total_hold_time = m.get('TotalHoldTime')

        if m.get('TotalMessagesSent') is not None:
            self.total_messages_sent = m.get('TotalMessagesSent')

        if m.get('TotalMessagesSentByAgent') is not None:
            self.total_messages_sent_by_agent = m.get('TotalMessagesSentByAgent')

        if m.get('TotalMessagesSentByCustomer') is not None:
            self.total_messages_sent_by_customer = m.get('TotalMessagesSentByCustomer')

        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class ListHistoricalAgentReportResponseBodyDataListInboundAccessChannelTypeDetails(DaraModel):
    def __init__(
        self,
        access_channel_type: str = None,
        calls_offered: int = None,
    ):
        # The channel type.
        self.access_channel_type = access_channel_type
        # The number of sessions offered.
        self.calls_offered = calls_offered

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        return self

class ListHistoricalAgentReportResponseBodyDataListBack2Back(DaraModel):
    def __init__(
        self,
        agent_handle_rate: str = None,
        answer_rate: str = None,
        average_customer_ring_time: str = None,
        average_ring_time: str = None,
        average_talk_time: str = None,
        calls_agent_handled: str = None,
        calls_answered: str = None,
        calls_customer_answered: str = None,
        calls_dialed: str = None,
        customer_answer_rate: str = None,
        max_customer_ring_time: str = None,
        max_ring_time: str = None,
        max_talk_time: str = None,
        total_customer_ring_time: str = None,
        total_ring_time: str = None,
        total_talk_time: str = None,
    ):
        # The agent answer rate.
        self.agent_handle_rate = agent_handle_rate
        # The answer rate. Formula: CallsAnswered/CallsDialed. Because the answer event and the dial event may fall within different time ranges, the result may exceed 100% in some cases.
        self.answer_rate = answer_rate
        # The average customer-side ring duration. Unit: seconds.
        self.average_customer_ring_time = average_customer_ring_time
        # The average ring duration. Unit: seconds.
        self.average_ring_time = average_ring_time
        # The average talk duration. Unit: seconds.
        self.average_talk_time = average_talk_time
        # The number of calls answered by the agent.
        self.calls_agent_handled = calls_agent_handled
        # The number of calls answered.
        self.calls_answered = calls_answered
        # The number of calls answered by the customer.
        self.calls_customer_answered = calls_customer_answered
        # The number of calls dialed.
        self.calls_dialed = calls_dialed
        # The customer answer rate.
        self.customer_answer_rate = customer_answer_rate
        # The maximum customer-side ring duration. Unit: seconds.
        self.max_customer_ring_time = max_customer_ring_time
        # The maximum ring time. Unit: seconds.
        self.max_ring_time = max_ring_time
        # The maximum talk time. Unit: seconds.
        self.max_talk_time = max_talk_time
        # The total customer-side ring duration. Unit: seconds.
        self.total_customer_ring_time = total_customer_ring_time
        # The total ring time. Unit: seconds.
        self.total_ring_time = total_ring_time
        # The total talk time. Unit: seconds.
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_handle_rate is not None:
            result['AgentHandleRate'] = self.agent_handle_rate

        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate

        if self.average_customer_ring_time is not None:
            result['AverageCustomerRingTime'] = self.average_customer_ring_time

        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.calls_agent_handled is not None:
            result['CallsAgentHandled'] = self.calls_agent_handled

        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.calls_customer_answered is not None:
            result['CallsCustomerAnswered'] = self.calls_customer_answered

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        if self.customer_answer_rate is not None:
            result['CustomerAnswerRate'] = self.customer_answer_rate

        if self.max_customer_ring_time is not None:
            result['MaxCustomerRingTime'] = self.max_customer_ring_time

        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.total_customer_ring_time is not None:
            result['TotalCustomerRingTime'] = self.total_customer_ring_time

        if self.total_ring_time is not None:
            result['TotalRingTime'] = self.total_ring_time

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentHandleRate') is not None:
            self.agent_handle_rate = m.get('AgentHandleRate')

        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')

        if m.get('AverageCustomerRingTime') is not None:
            self.average_customer_ring_time = m.get('AverageCustomerRingTime')

        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('CallsAgentHandled') is not None:
            self.calls_agent_handled = m.get('CallsAgentHandled')

        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('CallsCustomerAnswered') is not None:
            self.calls_customer_answered = m.get('CallsCustomerAnswered')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        if m.get('CustomerAnswerRate') is not None:
            self.customer_answer_rate = m.get('CustomerAnswerRate')

        if m.get('MaxCustomerRingTime') is not None:
            self.max_customer_ring_time = m.get('MaxCustomerRingTime')

        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('TotalCustomerRingTime') is not None:
            self.total_customer_ring_time = m.get('TotalCustomerRingTime')

        if m.get('TotalRingTime') is not None:
            self.total_ring_time = m.get('TotalRingTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        return self

