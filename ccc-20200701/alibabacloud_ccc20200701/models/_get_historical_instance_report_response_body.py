# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetHistoricalInstanceReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHistoricalInstanceReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message.
        self.message = message
        # Request ID.
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
            temp_model = main_models.GetHistoricalInstanceReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHistoricalInstanceReportResponseBodyData(DaraModel):
    def __init__(
        self,
        inbound: main_models.GetHistoricalInstanceReportResponseBodyDataInbound = None,
        internal: main_models.GetHistoricalInstanceReportResponseBodyDataInternal = None,
        outbound: main_models.GetHistoricalInstanceReportResponseBodyDataOutbound = None,
        overall: main_models.GetHistoricalInstanceReportResponseBodyDataOverall = None,
    ):
        # Inbound data.
        self.inbound = inbound
        # Internal call metrics.
        self.internal = internal
        # Outbound metrics.
        self.outbound = outbound
        # Overall metrics.
        self.overall = overall

    def validate(self):
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
        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()

        if self.internal is not None:
            result['Internal'] = self.internal.to_map()

        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()

        if self.overall is not None:
            result['Overall'] = self.overall.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Inbound') is not None:
            temp_model = main_models.GetHistoricalInstanceReportResponseBodyDataInbound()
            self.inbound = temp_model.from_map(m.get('Inbound'))

        if m.get('Internal') is not None:
            temp_model = main_models.GetHistoricalInstanceReportResponseBodyDataInternal()
            self.internal = temp_model.from_map(m.get('Internal'))

        if m.get('Outbound') is not None:
            temp_model = main_models.GetHistoricalInstanceReportResponseBodyDataOutbound()
            self.outbound = temp_model.from_map(m.get('Outbound'))

        if m.get('Overall') is not None:
            temp_model = main_models.GetHistoricalInstanceReportResponseBodyDataOverall()
            self.overall = temp_model.from_map(m.get('Overall'))

        return self

class GetHistoricalInstanceReportResponseBodyDataOverall(DaraModel):
    def __init__(
        self,
        average_break_time: float = None,
        average_hold_time: float = None,
        average_ready_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        max_break_time: int = None,
        max_hold_time: int = None,
        max_logged_in_agents: int = None,
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
        total_ready_time: int = None,
        total_talk_time: int = None,
        total_work_time: int = None,
    ):
        # Average break duration, in seconds. Calculation Formula: TotalBreakTime / Count of breaks. The count of breaks is not an exposed API field.
        self.average_break_time = average_break_time
        # Average call hold duration, in seconds. Calculation Formula: TotalHoldTime / (InboundCallsHold + OutboundCallsHold).
        self.average_hold_time = average_hold_time
        # Average ready duration, in seconds. Calculation Formula: TotalReadyTime / Count of ready events. The count of ready events is not currently exposed externally.
        self.average_ready_time = average_ready_time
        # Average talk time, in seconds. Calculation Formula: TotalTalkTime / (CallsAnswered + CallsHandled).
        self.average_talk_time = average_talk_time
        # Average post-processing time per call, in seconds. Calculation Formula: TotalWorkTime / TotalCalls.
        self.average_work_time = average_work_time
        # Maximum short break duration, in seconds.
        self.max_break_time = max_break_time
        # Maximum call hold duration, in seconds.
        self.max_hold_time = max_hold_time
        # Maximum number of agents simultaneously logged on during the Time Range.
        self.max_logged_in_agents = max_logged_in_agents
        # Maximum ready time, in seconds.
        self.max_ready_time = max_ready_time
        # Maximum talk time, in seconds.
        self.max_talk_time = max_talk_time
        # Maximum post-processing time per call, in seconds.
        self.max_work_time = max_work_time
        # Agent occupancy rate. Calculation Formula: (TotalWorkTime + TotalTalkTime) / TotalLoggedInTime.
        self.occupancy_rate = occupancy_rate
        # Satisfaction index, which is the average value of the satisfaction keypress digits (single-digit numbers).
        self.satisfaction_index = satisfaction_index
        # Satisfaction rate. Calculation Formula: Count of evaluations marked as satisfied / Count of satisfaction survey responses.
        self.satisfaction_rate = satisfaction_rate
        # Sending Count of satisfaction surveys.
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        # Count of satisfaction survey responses.
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        # Total break time, in seconds.
        self.total_break_time = total_break_time
        # Total call volume. Calculation Formula: CallsOffered + CallsDialed.
        self.total_calls = total_calls
        # Total hold time, in seconds.
        self.total_hold_time = total_hold_time
        # Total logon duration, in seconds. Exclude break time.
        self.total_logged_in_time = total_logged_in_time
        # Total ready time, in seconds.
        self.total_ready_time = total_ready_time
        # Total talk time, in seconds.
        self.total_talk_time = total_talk_time
        # Total post-processing time, in seconds.
        self.total_work_time = total_work_time

    def validate(self):
        pass

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

        if self.max_break_time is not None:
            result['MaxBreakTime'] = self.max_break_time

        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time

        if self.max_logged_in_agents is not None:
            result['MaxLoggedInAgents'] = self.max_logged_in_agents

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

        if m.get('MaxBreakTime') is not None:
            self.max_break_time = m.get('MaxBreakTime')

        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')

        if m.get('MaxLoggedInAgents') is not None:
            self.max_logged_in_agents = m.get('MaxLoggedInAgents')

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

        if m.get('TotalReadyTime') is not None:
            self.total_ready_time = m.get('TotalReadyTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class GetHistoricalInstanceReportResponseBodyDataOutbound(DaraModel):
    def __init__(
        self,
        answer_rate: float = None,
        average_dialing_time: float = None,
        average_hold_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        calls_answered: int = None,
        calls_attended_transferred: int = None,
        calls_blind_transferred: int = None,
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
        # Answer rate. Calculation Formula: CallsAnswered / CallsDialed. (Because the answering event and the acknowledgement event may fall into different time ranges, the result may exceed 100% in certain cases.)
        self.answer_rate = answer_rate
        # Average Dial-up Time, in seconds. Calculation Formula: TotalDialingTime / CallsDialed.
        self.average_dialing_time = average_dialing_time
        # Average hold duration, in seconds. Calculation formula: TotalHoldTime / CallsHold.
        self.average_hold_time = average_hold_time
        # Average ring time, in seconds. Calculation Formula: TotalRingTime / CallsRinged.
        self.average_ring_time = average_ring_time
        # Average talk time, in seconds. Calculation Formula: TotalTalkTime / CallsAnswered.
        self.average_talk_time = average_talk_time
        # Average post-processing time per call, in seconds. Calculation Formula: TotalWorkTime / CallsDialed.
        self.average_work_time = average_work_time
        # Answered Call Count.
        self.calls_answered = calls_answered
        # Number of attended transfers, which refers to the quantity of calls that underwent attended transfer. If a single call is transferred multiple times, it is counted as one.
        self.calls_attended_transferred = calls_attended_transferred
        # Number of blind transfers, which refers to the quantity of calls that underwent blind transfer. If a single call is transferred multiple times, it is counted as one.
        self.calls_blind_transferred = calls_blind_transferred
        # Dial-up Call Count.
        self.calls_dialed = calls_dialed
        # Hold Count, which is the number of calls that were placed on hold. If a single call was put on hold multiple times, it is counted as one.
        self.calls_hold = calls_hold
        # Number of calls that rang for agents. If a single call is assigned to multiple agents and rings for each, it is counted as one.
        self.calls_ringed = calls_ringed
        # Maximum Dial-up Time, in seconds.
        self.max_dialing_time = max_dialing_time
        # Maximum call hold duration, in seconds.
        self.max_hold_time = max_hold_time
        # Maximum ring duration, in seconds.
        self.max_ring_time = max_ring_time
        # Maximum Talk Time, in seconds.
        self.max_talk_time = max_talk_time
        # Maximum post-processing time per call, in seconds.
        self.max_work_time = max_work_time
        # Satisfaction Index, which is the average of the satisfaction keypress digits (single-digit numbers).
        self.satisfaction_index = satisfaction_index
        # Satisfaction Rate. Calculation Formula: Number of responses marked as satisfied / Count of satisfaction survey responses.
        self.satisfaction_rate = satisfaction_rate
        # Sending Count of satisfaction surveys.
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        # Response Count of satisfaction surveys.
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        # Total dial-up duration, in seconds.
        self.total_dialing_time = total_dialing_time
        # Total hold duration, in seconds.
        self.total_hold_time = total_hold_time
        # Total Ring Time, in seconds.
        self.total_ring_time = total_ring_time
        # Total Talk Time, in seconds.
        self.total_talk_time = total_talk_time
        # Total post-processing duration, in seconds.
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

        if self.calls_attended_transferred is not None:
            result['CallsAttendedTransferred'] = self.calls_attended_transferred

        if self.calls_blind_transferred is not None:
            result['CallsBlindTransferred'] = self.calls_blind_transferred

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

        if m.get('CallsAttendedTransferred') is not None:
            self.calls_attended_transferred = m.get('CallsAttendedTransferred')

        if m.get('CallsBlindTransferred') is not None:
            self.calls_blind_transferred = m.get('CallsBlindTransferred')

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

class GetHistoricalInstanceReportResponseBodyDataInternal(DaraModel):
    def __init__(
        self,
        calls_answered: int = None,
        calls_dialed: int = None,
    ):
        # Number of answered calls.
        self.calls_answered = calls_answered
        # Dial-up volume.
        self.calls_dialed = calls_dialed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calls_answered is not None:
            result['CallsAnswered'] = self.calls_answered

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallsAnswered') is not None:
            self.calls_answered = m.get('CallsAnswered')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        return self

class GetHistoricalInstanceReportResponseBodyDataInbound(DaraModel):
    def __init__(
        self,
        abandon_rate: float = None,
        access_channel_type_detail_list: List[main_models.GetHistoricalInstanceReportResponseBodyDataInboundAccessChannelTypeDetailList] = None,
        average_abandon_time: float = None,
        average_abandoned_in_ivrtime: float = None,
        average_abandoned_in_queue_time: float = None,
        average_abandoned_in_ring_time: float = None,
        average_first_response_time: float = None,
        average_hold_time: float = None,
        average_response_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        average_wait_time: float = None,
        average_work_time: float = None,
        calls_abandoned: int = None,
        calls_abandoned_in_ivr: int = None,
        calls_abandoned_in_queue: int = None,
        calls_abandoned_in_ring: int = None,
        calls_abandoned_in_voice_navigator: int = None,
        calls_attended_transferred: int = None,
        calls_blind_transferred: int = None,
        calls_caused_ivrexception: int = None,
        calls_forward_to_outside_number: int = None,
        calls_handled: int = None,
        calls_hold: int = None,
        calls_ivrexception: int = None,
        calls_offered: int = None,
        calls_queued: int = None,
        calls_queuing_failed: int = None,
        calls_queuing_overflow: int = None,
        calls_queuing_timeout: int = None,
        calls_ringed: int = None,
        calls_to_voicemail: int = None,
        calls_voicemail: int = None,
        handle_rate: float = None,
        max_abandon_time: int = None,
        max_abandoned_in_ivrtime: int = None,
        max_abandoned_in_queue_time: int = None,
        max_abandoned_in_ring_time: int = None,
        max_hold_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        max_wait_time: int = None,
        max_work_time: int = None,
        satisfaction_index: float = None,
        satisfaction_rate: float = None,
        satisfaction_surveys_offered: int = None,
        satisfaction_surveys_responded: int = None,
        service_level_15: float = None,
        service_level_20: float = None,
        service_level_30: float = None,
        total_abandon_time: int = None,
        total_abandoned_in_ivrtime: int = None,
        total_abandoned_in_queue_time: int = None,
        total_abandoned_in_ring_time: int = None,
        total_hold_time: int = None,
        total_messages_sent: int = None,
        total_messages_sent_by_agent: int = None,
        total_messages_sent_by_customer: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
        total_wait_time: int = None,
        total_work_time: int = None,
    ):
        # Abandon rate. Calculation Formula: CallsAbandoned / CallsOffered (because abandonment events and assignment events may fall into different time ranges, the result may exceed 100% in certain cases).
        self.abandon_rate = abandon_rate
        # Statistics for each channel.
        self.access_channel_type_detail_list = access_channel_type_detail_list
        # Average abandon time, in seconds. Calculation formula: TotalAbandonTime / CallsAbandoned.
        self.average_abandon_time = average_abandon_time
        # Average IVR abandonment duration, in seconds. Calculation Formula: TotalAbandonedInIVRTime / CallsAbandonedInIVR.
        self.average_abandoned_in_ivrtime = average_abandoned_in_ivrtime
        # [responses_200_schema_properties_Data_properties_Inbound_properties_MaxAbandonedInQueueTime_type]integer
        self.average_abandoned_in_queue_time = average_abandoned_in_queue_time
        # Average ring-time abandon duration, in seconds. Calculation formula: TotalAbandonedInRingTime / CallsAbandonedInRing.
        self.average_abandoned_in_ring_time = average_abandoned_in_ring_time
        # Average first response time for chat sessions, in seconds.
        self.average_first_response_time = average_first_response_time
        # Average call hold duration, in seconds. Calculation Formula: TotalHoldTime / CallsHold.
        self.average_hold_time = average_hold_time
        # Average response time (RT) for chat sessions.
        self.average_response_time = average_response_time
        # Average ring time in seconds. Calculation Formula: TotalRingTime / CallsRinged.
        self.average_ring_time = average_ring_time
        # Average talk time, in seconds. Calculation Formula: TotalTalkTime / CallsHandled.
        self.average_talk_time = average_talk_time
        # [responses_200_schema_properties_Data_properties_Inbound_properties_AverageFirstResponseTime_type]number
        self.average_wait_time = average_wait_time
        # Average post-processing time, in seconds. Calculation formula: TotalWorkTime / CallsHandled.
        self.average_work_time = average_work_time
        # Total number of abandoned calls. Calculation Formula: CallsAbandonedInIVR + CallsAbandonedInQueue + CallsAbandonedInRing.
        self.calls_abandoned = calls_abandoned
        # Number of calls abandoned in IVR, which refers to the count of calls where the customer hung up during the IVR flow after entering it. This is determined by the hang-up reason in call details being marked as "IVR abandoned."
        self.calls_abandoned_in_ivr = calls_abandoned_in_ivr
        # Number of calls abandoned in queue, which refers to the number of calls where the customer hung up while waiting in the queue after the call entered the queue.
        self.calls_abandoned_in_queue = calls_abandoned_in_queue
        # Number of calls abandoned during ringing, which refers to the quantity of calls where the customer hung up while the agent\\"s phone was ringing.
        self.calls_abandoned_in_ring = calls_abandoned_in_ring
        # Number of calls abandoned in the Intelligent Voice Navigator module.
        self.calls_abandoned_in_voice_navigator = calls_abandoned_in_voice_navigator
        # Number of consultative transfers, which refers to the number of calls that were transferred via consultative transfer. If a single call is transferred multiple times, it is counted as one.
        self.calls_attended_transferred = calls_attended_transferred
        # The number of blind transfers, which refers to the count of calls directly transferred without consultation. If a single call is transferred multiple times, it is counted as one.
        self.calls_blind_transferred = calls_blind_transferred
        # Number of calls that caused IVR exceptions.
        self.calls_caused_ivrexception = calls_caused_ivrexception
        # Number of calls forwarded to an external number.
        self.calls_forward_to_outside_number = calls_forward_to_outside_number
        # Acknowledgement count, which refers to the number of calls answered by agents. If a single call is answered by multiple agents, it is counted only once.
        self.calls_handled = calls_handled
        # [responses_200_schema_properties_Data_properties_Inbound_properties_TotalAbandonTime_type]integer
        self.calls_hold = calls_hold
        # Number of calls with IVR exceptions. A call is counted when the IVR enters a hang-up reason node and the hang-up reason configured in that node is "transfer to agent failed."
        self.calls_ivrexception = calls_ivrexception
        # [responses_200_schema_properties_Data_properties_Inbound_properties_TotalAbandonedInRingTime_type]integer
        self.calls_offered = calls_offered
        # Number of calls entering the queue. If a single call enters the queue multiple times, it is counted once.
        self.calls_queued = calls_queued
        # The number of queue failures, which refers to the count of calls where the customer hung up while waiting in the queue after entering it.
        self.calls_queuing_failed = calls_queuing_failed
        # The number of calls that overflowed from the queue, where queue overflow refers to calls exceeding the queue capacity while waiting in the IVR queue.
        self.calls_queuing_overflow = calls_queuing_overflow
        # Number of calls that timed out during the queuing phase.
        self.calls_queuing_timeout = calls_queuing_timeout
        # Number of calls that rang agents. If a single call is assigned to multiple agents and rings, it is counted once.
        self.calls_ringed = calls_ringed
        # The number of calls routed to voicemail.
        self.calls_to_voicemail = calls_to_voicemail
        # Number of calls transferred to voicemail. The count increases by 1 when a call enters the voicemail module configured in IVR.
        self.calls_voicemail = calls_voicemail
        # [responses_200_schema_properties_Data_properties_Inbound_properties_CallsBlindTransferred_type]integer
        self.handle_rate = handle_rate
        # Maximum abandon time, in seconds. A call is considered abandoned if the customer hangs up after entering the IVR but before an agent answers.
        self.max_abandon_time = max_abandon_time
        # Maximum IVR abandonment duration, in seconds. IVR abandonment is defined as a customer hanging up during IVR interaction. This does not include hang-ups while waiting in queue or during agent ringing after call assignment.
        self.max_abandoned_in_ivrtime = max_abandoned_in_ivrtime
        # Maximum queue abandonment duration, in seconds.
        self.max_abandoned_in_queue_time = max_abandoned_in_queue_time
        # Maximum ringing abandonment duration, in seconds. Ringing abandonment is defined as the customer hanging up while the call is ringing on the agent\\"s side after being assigned to the agent.
        self.max_abandoned_in_ring_time = max_abandoned_in_ring_time
        # Maximum hold time, in seconds.
        self.max_hold_time = max_hold_time
        # Maximum ring duration, in seconds.
        self.max_ring_time = max_ring_time
        # Maximum talk time, in seconds.
        self.max_talk_time = max_talk_time
        # Maximum wait time, in seconds.
        self.max_wait_time = max_wait_time
        # Maximum post-processing time, in seconds.
        self.max_work_time = max_work_time
        # [responses_200_schema_properties_Data_properties_Inbound_properties_CallsQueuingOverflow_type]integer
        self.satisfaction_index = satisfaction_index
        # Satisfaction rate. Calculation Formula: Number of evaluations marked as satisfied / Count of satisfaction survey responses.
        self.satisfaction_rate = satisfaction_rate
        # Sending Count of satisfaction surveys.
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        # Count of satisfaction survey responses.
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        # Service level within 15 seconds.
        self.service_level_15 = service_level_15
        # Service level within 20 seconds: number of calls with wait time less than or equal to 20 seconds divided by CallsQueued.
        self.service_level_20 = service_level_20
        # Service level within 30 seconds.
        self.service_level_30 = service_level_30
        # Total abandonment duration, in seconds.
        self.total_abandon_time = total_abandon_time
        # Total IVR abandonment duration, in seconds.
        self.total_abandoned_in_ivrtime = total_abandoned_in_ivrtime
        # Total queue abandon time, in seconds.
        self.total_abandoned_in_queue_time = total_abandoned_in_queue_time
        # [responses_200_schema_properties_Data_properties_Inbound_properties_SatisfactionSurveysOffered_type]integer
        self.total_abandoned_in_ring_time = total_abandoned_in_ring_time
        # Total call hold duration, in seconds.
        self.total_hold_time = total_hold_time
        # Total number of messages sent in chat sessions.
        self.total_messages_sent = total_messages_sent
        # Total number of messages sent by agents in chat sessions.
        self.total_messages_sent_by_agent = total_messages_sent_by_agent
        # Total number of messages sent by the customer in chat sessions.
        self.total_messages_sent_by_customer = total_messages_sent_by_customer
        # [responses_200_schema_properties_Data_properties_Inbound_properties_CallsQueuingFailed_type]integer
        self.total_ring_time = total_ring_time
        # [responses_200_schema_properties_Data_properties_Inbound_properties_CallsToVoicemail_type]integer
        self.total_talk_time = total_talk_time
        # Total wait time, in seconds.
        self.total_wait_time = total_wait_time
        # Total post-processing duration, in seconds.
        self.total_work_time = total_work_time

    def validate(self):
        if self.access_channel_type_detail_list:
            for v1 in self.access_channel_type_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandon_rate is not None:
            result['AbandonRate'] = self.abandon_rate

        result['AccessChannelTypeDetailList'] = []
        if self.access_channel_type_detail_list is not None:
            for k1 in self.access_channel_type_detail_list:
                result['AccessChannelTypeDetailList'].append(k1.to_map() if k1 else None)

        if self.average_abandon_time is not None:
            result['AverageAbandonTime'] = self.average_abandon_time

        if self.average_abandoned_in_ivrtime is not None:
            result['AverageAbandonedInIVRTime'] = self.average_abandoned_in_ivrtime

        if self.average_abandoned_in_queue_time is not None:
            result['AverageAbandonedInQueueTime'] = self.average_abandoned_in_queue_time

        if self.average_abandoned_in_ring_time is not None:
            result['AverageAbandonedInRingTime'] = self.average_abandoned_in_ring_time

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

        if self.average_wait_time is not None:
            result['AverageWaitTime'] = self.average_wait_time

        if self.average_work_time is not None:
            result['AverageWorkTime'] = self.average_work_time

        if self.calls_abandoned is not None:
            result['CallsAbandoned'] = self.calls_abandoned

        if self.calls_abandoned_in_ivr is not None:
            result['CallsAbandonedInIVR'] = self.calls_abandoned_in_ivr

        if self.calls_abandoned_in_queue is not None:
            result['CallsAbandonedInQueue'] = self.calls_abandoned_in_queue

        if self.calls_abandoned_in_ring is not None:
            result['CallsAbandonedInRing'] = self.calls_abandoned_in_ring

        if self.calls_abandoned_in_voice_navigator is not None:
            result['CallsAbandonedInVoiceNavigator'] = self.calls_abandoned_in_voice_navigator

        if self.calls_attended_transferred is not None:
            result['CallsAttendedTransferred'] = self.calls_attended_transferred

        if self.calls_blind_transferred is not None:
            result['CallsBlindTransferred'] = self.calls_blind_transferred

        if self.calls_caused_ivrexception is not None:
            result['CallsCausedIVRException'] = self.calls_caused_ivrexception

        if self.calls_forward_to_outside_number is not None:
            result['CallsForwardToOutsideNumber'] = self.calls_forward_to_outside_number

        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled

        if self.calls_hold is not None:
            result['CallsHold'] = self.calls_hold

        if self.calls_ivrexception is not None:
            result['CallsIVRException'] = self.calls_ivrexception

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        if self.calls_queued is not None:
            result['CallsQueued'] = self.calls_queued

        if self.calls_queuing_failed is not None:
            result['CallsQueuingFailed'] = self.calls_queuing_failed

        if self.calls_queuing_overflow is not None:
            result['CallsQueuingOverflow'] = self.calls_queuing_overflow

        if self.calls_queuing_timeout is not None:
            result['CallsQueuingTimeout'] = self.calls_queuing_timeout

        if self.calls_ringed is not None:
            result['CallsRinged'] = self.calls_ringed

        if self.calls_to_voicemail is not None:
            result['CallsToVoicemail'] = self.calls_to_voicemail

        if self.calls_voicemail is not None:
            result['CallsVoicemail'] = self.calls_voicemail

        if self.handle_rate is not None:
            result['HandleRate'] = self.handle_rate

        if self.max_abandon_time is not None:
            result['MaxAbandonTime'] = self.max_abandon_time

        if self.max_abandoned_in_ivrtime is not None:
            result['MaxAbandonedInIVRTime'] = self.max_abandoned_in_ivrtime

        if self.max_abandoned_in_queue_time is not None:
            result['MaxAbandonedInQueueTime'] = self.max_abandoned_in_queue_time

        if self.max_abandoned_in_ring_time is not None:
            result['MaxAbandonedInRingTime'] = self.max_abandoned_in_ring_time

        if self.max_hold_time is not None:
            result['MaxHoldTime'] = self.max_hold_time

        if self.max_ring_time is not None:
            result['MaxRingTime'] = self.max_ring_time

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.max_wait_time is not None:
            result['MaxWaitTime'] = self.max_wait_time

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

        if self.service_level_20 is not None:
            result['ServiceLevel20'] = self.service_level_20

        if self.service_level_30 is not None:
            result['ServiceLevel30'] = self.service_level_30

        if self.total_abandon_time is not None:
            result['TotalAbandonTime'] = self.total_abandon_time

        if self.total_abandoned_in_ivrtime is not None:
            result['TotalAbandonedInIVRTime'] = self.total_abandoned_in_ivrtime

        if self.total_abandoned_in_queue_time is not None:
            result['TotalAbandonedInQueueTime'] = self.total_abandoned_in_queue_time

        if self.total_abandoned_in_ring_time is not None:
            result['TotalAbandonedInRingTime'] = self.total_abandoned_in_ring_time

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

        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time

        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonRate') is not None:
            self.abandon_rate = m.get('AbandonRate')

        self.access_channel_type_detail_list = []
        if m.get('AccessChannelTypeDetailList') is not None:
            for k1 in m.get('AccessChannelTypeDetailList'):
                temp_model = main_models.GetHistoricalInstanceReportResponseBodyDataInboundAccessChannelTypeDetailList()
                self.access_channel_type_detail_list.append(temp_model.from_map(k1))

        if m.get('AverageAbandonTime') is not None:
            self.average_abandon_time = m.get('AverageAbandonTime')

        if m.get('AverageAbandonedInIVRTime') is not None:
            self.average_abandoned_in_ivrtime = m.get('AverageAbandonedInIVRTime')

        if m.get('AverageAbandonedInQueueTime') is not None:
            self.average_abandoned_in_queue_time = m.get('AverageAbandonedInQueueTime')

        if m.get('AverageAbandonedInRingTime') is not None:
            self.average_abandoned_in_ring_time = m.get('AverageAbandonedInRingTime')

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

        if m.get('AverageWaitTime') is not None:
            self.average_wait_time = m.get('AverageWaitTime')

        if m.get('AverageWorkTime') is not None:
            self.average_work_time = m.get('AverageWorkTime')

        if m.get('CallsAbandoned') is not None:
            self.calls_abandoned = m.get('CallsAbandoned')

        if m.get('CallsAbandonedInIVR') is not None:
            self.calls_abandoned_in_ivr = m.get('CallsAbandonedInIVR')

        if m.get('CallsAbandonedInQueue') is not None:
            self.calls_abandoned_in_queue = m.get('CallsAbandonedInQueue')

        if m.get('CallsAbandonedInRing') is not None:
            self.calls_abandoned_in_ring = m.get('CallsAbandonedInRing')

        if m.get('CallsAbandonedInVoiceNavigator') is not None:
            self.calls_abandoned_in_voice_navigator = m.get('CallsAbandonedInVoiceNavigator')

        if m.get('CallsAttendedTransferred') is not None:
            self.calls_attended_transferred = m.get('CallsAttendedTransferred')

        if m.get('CallsBlindTransferred') is not None:
            self.calls_blind_transferred = m.get('CallsBlindTransferred')

        if m.get('CallsCausedIVRException') is not None:
            self.calls_caused_ivrexception = m.get('CallsCausedIVRException')

        if m.get('CallsForwardToOutsideNumber') is not None:
            self.calls_forward_to_outside_number = m.get('CallsForwardToOutsideNumber')

        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')

        if m.get('CallsHold') is not None:
            self.calls_hold = m.get('CallsHold')

        if m.get('CallsIVRException') is not None:
            self.calls_ivrexception = m.get('CallsIVRException')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        if m.get('CallsQueued') is not None:
            self.calls_queued = m.get('CallsQueued')

        if m.get('CallsQueuingFailed') is not None:
            self.calls_queuing_failed = m.get('CallsQueuingFailed')

        if m.get('CallsQueuingOverflow') is not None:
            self.calls_queuing_overflow = m.get('CallsQueuingOverflow')

        if m.get('CallsQueuingTimeout') is not None:
            self.calls_queuing_timeout = m.get('CallsQueuingTimeout')

        if m.get('CallsRinged') is not None:
            self.calls_ringed = m.get('CallsRinged')

        if m.get('CallsToVoicemail') is not None:
            self.calls_to_voicemail = m.get('CallsToVoicemail')

        if m.get('CallsVoicemail') is not None:
            self.calls_voicemail = m.get('CallsVoicemail')

        if m.get('HandleRate') is not None:
            self.handle_rate = m.get('HandleRate')

        if m.get('MaxAbandonTime') is not None:
            self.max_abandon_time = m.get('MaxAbandonTime')

        if m.get('MaxAbandonedInIVRTime') is not None:
            self.max_abandoned_in_ivrtime = m.get('MaxAbandonedInIVRTime')

        if m.get('MaxAbandonedInQueueTime') is not None:
            self.max_abandoned_in_queue_time = m.get('MaxAbandonedInQueueTime')

        if m.get('MaxAbandonedInRingTime') is not None:
            self.max_abandoned_in_ring_time = m.get('MaxAbandonedInRingTime')

        if m.get('MaxHoldTime') is not None:
            self.max_hold_time = m.get('MaxHoldTime')

        if m.get('MaxRingTime') is not None:
            self.max_ring_time = m.get('MaxRingTime')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('MaxWaitTime') is not None:
            self.max_wait_time = m.get('MaxWaitTime')

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

        if m.get('ServiceLevel20') is not None:
            self.service_level_20 = m.get('ServiceLevel20')

        if m.get('ServiceLevel30') is not None:
            self.service_level_30 = m.get('ServiceLevel30')

        if m.get('TotalAbandonTime') is not None:
            self.total_abandon_time = m.get('TotalAbandonTime')

        if m.get('TotalAbandonedInIVRTime') is not None:
            self.total_abandoned_in_ivrtime = m.get('TotalAbandonedInIVRTime')

        if m.get('TotalAbandonedInQueueTime') is not None:
            self.total_abandoned_in_queue_time = m.get('TotalAbandonedInQueueTime')

        if m.get('TotalAbandonedInRingTime') is not None:
            self.total_abandoned_in_ring_time = m.get('TotalAbandonedInRingTime')

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

        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class GetHistoricalInstanceReportResponseBodyDataInboundAccessChannelTypeDetailList(DaraModel):
    def __init__(
        self,
        access_channel_type: str = None,
        calls_offered: int = None,
    ):
        # Channel Type.
        self.access_channel_type = access_channel_type
        # Number of assigned sessions.
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

