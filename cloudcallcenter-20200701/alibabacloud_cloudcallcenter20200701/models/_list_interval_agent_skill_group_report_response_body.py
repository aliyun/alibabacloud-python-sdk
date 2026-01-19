# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class ListIntervalAgentSkillGroupReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListIntervalAgentSkillGroupReportResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListIntervalAgentSkillGroupReportResponseBodyData(DaraModel):
    def __init__(
        self,
        back_2back: main_models.ListIntervalAgentSkillGroupReportResponseBodyDataBack2Back = None,
        inbound: main_models.ListIntervalAgentSkillGroupReportResponseBodyDataInbound = None,
        internal: main_models.ListIntervalAgentSkillGroupReportResponseBodyDataInternal = None,
        outbound: main_models.ListIntervalAgentSkillGroupReportResponseBodyDataOutbound = None,
        overall: main_models.ListIntervalAgentSkillGroupReportResponseBodyDataOverall = None,
        stats_time: int = None,
    ):
        self.back_2back = back_2back
        self.inbound = inbound
        self.internal = internal
        self.outbound = outbound
        self.overall = overall
        self.stats_time = stats_time

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
        if self.back_2back is not None:
            result['Back2Back'] = self.back_2back.to_map()

        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()

        if self.internal is not None:
            result['Internal'] = self.internal.to_map()

        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()

        if self.overall is not None:
            result['Overall'] = self.overall.to_map()

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Back2Back') is not None:
            temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyDataBack2Back()
            self.back_2back = temp_model.from_map(m.get('Back2Back'))

        if m.get('Inbound') is not None:
            temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyDataInbound()
            self.inbound = temp_model.from_map(m.get('Inbound'))

        if m.get('Internal') is not None:
            temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyDataInternal()
            self.internal = temp_model.from_map(m.get('Internal'))

        if m.get('Outbound') is not None:
            temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyDataOutbound()
            self.outbound = temp_model.from_map(m.get('Outbound'))

        if m.get('Overall') is not None:
            temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyDataOverall()
            self.overall = temp_model.from_map(m.get('Overall'))

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

        return self

class ListIntervalAgentSkillGroupReportResponseBodyDataOverall(DaraModel):
    def __init__(
        self,
        average_break_time: float = None,
        average_hold_time: float = None,
        average_ready_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        break_code_detail_list: List[main_models.ListIntervalAgentSkillGroupReportResponseBodyDataOverallBreakCodeDetailList] = None,
        first_check_in_time: int = None,
        last_checkout_time: int = None,
        max_break_time: int = None,
        max_hold_time: int = None,
        max_ready_time: int = None,
        max_talk_time: int = None,
        max_work_time: int = None,
        occupancy_rate: float = None,
        satisfaction_count: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_break_time: int = None,
        total_calls: int = None,
        total_hold_time: int = None,
        total_logged_in_time: int = None,
        total_off_site_online_time: int = None,
        total_office_phone_online_time: int = None,
        total_on_site_online_time: int = None,
        total_outbound_scenario_ready_time: int = None,
        total_outbound_scenario_time: int = None,
        total_ready_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_break_time = average_break_time
        self.average_hold_time = average_hold_time
        self.average_ready_time = average_ready_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.break_code_detail_list = break_code_detail_list
        self.first_check_in_time = first_check_in_time
        self.last_checkout_time = last_checkout_time
        self.max_break_time = max_break_time
        self.max_hold_time = max_hold_time
        self.max_ready_time = max_ready_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.occupancy_rate = occupancy_rate
        self.satisfaction_count = satisfaction_count
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_break_time = total_break_time
        self.total_calls = total_calls
        self.total_hold_time = total_hold_time
        self.total_logged_in_time = total_logged_in_time
        self.total_off_site_online_time = total_off_site_online_time
        self.total_office_phone_online_time = total_office_phone_online_time
        self.total_on_site_online_time = total_on_site_online_time
        self.total_outbound_scenario_ready_time = total_outbound_scenario_ready_time
        self.total_outbound_scenario_time = total_outbound_scenario_time
        self.total_ready_time = total_ready_time
        self.total_talk_time = total_talk_time
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

        if self.last_checkout_time is not None:
            result['LastCheckoutTime'] = self.last_checkout_time

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

        if self.satisfaction_count is not None:
            result['SatisfactionCount'] = self.satisfaction_count

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

        if self.total_off_site_online_time is not None:
            result['TotalOffSiteOnlineTime'] = self.total_off_site_online_time

        if self.total_office_phone_online_time is not None:
            result['TotalOfficePhoneOnlineTime'] = self.total_office_phone_online_time

        if self.total_on_site_online_time is not None:
            result['TotalOnSiteOnlineTime'] = self.total_on_site_online_time

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
                temp_model = main_models.ListIntervalAgentSkillGroupReportResponseBodyDataOverallBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k1))

        if m.get('FirstCheckInTime') is not None:
            self.first_check_in_time = m.get('FirstCheckInTime')

        if m.get('LastCheckoutTime') is not None:
            self.last_checkout_time = m.get('LastCheckoutTime')

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

        if m.get('SatisfactionCount') is not None:
            self.satisfaction_count = m.get('SatisfactionCount')

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

        if m.get('TotalOffSiteOnlineTime') is not None:
            self.total_off_site_online_time = m.get('TotalOffSiteOnlineTime')

        if m.get('TotalOfficePhoneOnlineTime') is not None:
            self.total_office_phone_online_time = m.get('TotalOfficePhoneOnlineTime')

        if m.get('TotalOnSiteOnlineTime') is not None:
            self.total_on_site_online_time = m.get('TotalOnSiteOnlineTime')

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

class ListIntervalAgentSkillGroupReportResponseBodyDataOverallBreakCodeDetailList(DaraModel):
    def __init__(
        self,
        break_code: str = None,
        count: int = None,
        duration: int = None,
    ):
        self.break_code = break_code
        self.count = count
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

class ListIntervalAgentSkillGroupReportResponseBodyDataOutbound(DaraModel):
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
        satisfaction_count: int = None,
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
        self.answer_rate = answer_rate
        self.average_dialing_time = average_dialing_time
        self.average_hold_time = average_hold_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_answered = calls_answered
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_dialed = calls_dialed
        self.calls_hold = calls_hold
        self.calls_ringed = calls_ringed
        self.max_dialing_time = max_dialing_time
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_count = satisfaction_count
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_dialing_time = total_dialing_time
        self.total_hold_time = total_hold_time
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

        if self.satisfaction_count is not None:
            result['SatisfactionCount'] = self.satisfaction_count

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

        if m.get('SatisfactionCount') is not None:
            self.satisfaction_count = m.get('SatisfactionCount')

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

class ListIntervalAgentSkillGroupReportResponseBodyDataInternal(DaraModel):
    def __init__(
        self,
        average_talk_time: float = None,
        calls_answered: int = None,
        calls_dialed: int = None,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_talk: int = None,
        max_talk_time: int = None,
        total_talk_time: int = None,
    ):
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_dialed = calls_dialed
        self.calls_handled = calls_handled
        self.calls_offered = calls_offered
        self.calls_talk = calls_talk
        self.max_talk_time = max_talk_time
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

        if self.calls_talk is not None:
            result['CallsTalk'] = self.calls_talk

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

        if m.get('CallsTalk') is not None:
            self.calls_talk = m.get('CallsTalk')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        return self

class ListIntervalAgentSkillGroupReportResponseBodyDataInbound(DaraModel):
    def __init__(
        self,
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
        satisfaction_count: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        total_hold_time: int = None,
        total_messages_sent: int = None,
        total_messages_sent_by_agent: int = None,
        total_messages_sent_by_customer: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        self.average_first_response_time = average_first_response_time
        self.average_hold_time = average_hold_time
        self.average_response_time = average_response_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_work_time = average_work_time
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_handled = calls_handled
        self.calls_hold = calls_hold
        self.calls_offered = calls_offered
        self.calls_ringed = calls_ringed
        self.handle_rate = handle_rate
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.satisfaction_count = satisfaction_count
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_hold_time = total_hold_time
        self.total_messages_sent = total_messages_sent
        self.total_messages_sent_by_agent = total_messages_sent_by_agent
        self.total_messages_sent_by_customer = total_messages_sent_by_customer
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

        if self.satisfaction_count is not None:
            result['SatisfactionCount'] = self.satisfaction_count

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

        if self.satisfaction_rate is not None:
            result['SatisfactionRate'] = self.satisfaction_rate

        if self.satisfaction_surveys_offered is not None:
            result['SatisfactionSurveysOffered'] = self.satisfaction_surveys_offered

        if self.satisfaction_surveys_responded is not None:
            result['SatisfactionSurveysResponded'] = self.satisfaction_surveys_responded

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

        if m.get('SatisfactionCount') is not None:
            self.satisfaction_count = m.get('SatisfactionCount')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

        if m.get('SatisfactionRate') is not None:
            self.satisfaction_rate = m.get('SatisfactionRate')

        if m.get('SatisfactionSurveysOffered') is not None:
            self.satisfaction_surveys_offered = m.get('SatisfactionSurveysOffered')

        if m.get('SatisfactionSurveysResponded') is not None:
            self.satisfaction_surveys_responded = m.get('SatisfactionSurveysResponded')

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

class ListIntervalAgentSkillGroupReportResponseBodyDataBack2Back(DaraModel):
    def __init__(
        self,
        agent_answer_rate: float = None,
        answer_rate: float = None,
        average_customer_ring_time: float = None,
        average_ring_time: float = None,
        average_talk_time: int = None,
        calls_answered: int = None,
        calls_customer_handled: int = None,
        calls_dialed: int = None,
        customer_handle_rate: float = None,
        max_customer_ring_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        total_customer_ring_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
    ):
        self.agent_answer_rate = agent_answer_rate
        self.answer_rate = answer_rate
        self.average_customer_ring_time = average_customer_ring_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_customer_handled = calls_customer_handled
        self.calls_dialed = calls_dialed
        self.customer_handle_rate = customer_handle_rate
        self.max_customer_ring_time = max_customer_ring_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.total_customer_ring_time = total_customer_ring_time
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_answer_rate is not None:
            result['AgentAnswerRate'] = self.agent_answer_rate

        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate

        if self.average_customer_ring_time is not None:
            result['AverageCustomerRingTime'] = self.average_customer_ring_time

        if self.average_ring_time is not None:
            result['AverageRingTime'] = self.average_ring_time

        if self.average_talk_time is not None:
            result['AverageTalkTime'] = self.average_talk_time

        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.calls_customer_handled is not None:
            result['CallsCustomerHandled'] = self.calls_customer_handled

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        if self.customer_handle_rate is not None:
            result['CustomerHandleRate'] = self.customer_handle_rate

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
        if m.get('AgentAnswerRate') is not None:
            self.agent_answer_rate = m.get('AgentAnswerRate')

        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')

        if m.get('AverageCustomerRingTime') is not None:
            self.average_customer_ring_time = m.get('AverageCustomerRingTime')

        if m.get('AverageRingTime') is not None:
            self.average_ring_time = m.get('AverageRingTime')

        if m.get('AverageTalkTime') is not None:
            self.average_talk_time = m.get('AverageTalkTime')

        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('CallsCustomerHandled') is not None:
            self.calls_customer_handled = m.get('CallsCustomerHandled')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        if m.get('CustomerHandleRate') is not None:
            self.customer_handle_rate = m.get('CustomerHandleRate')

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

