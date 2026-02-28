# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListHistoricalSkillGroupReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListHistoricalSkillGroupReportResponseBodyData = None,
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
            temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHistoricalSkillGroupReportResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListHistoricalSkillGroupReportResponseBodyDataList] = None,
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
                temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHistoricalSkillGroupReportResponseBodyDataList(DaraModel):
    def __init__(
        self,
        back_2back: main_models.ListHistoricalSkillGroupReportResponseBodyDataListBack2Back = None,
        inbound: main_models.ListHistoricalSkillGroupReportResponseBodyDataListInbound = None,
        outbound: main_models.ListHistoricalSkillGroupReportResponseBodyDataListOutbound = None,
        overall: main_models.ListHistoricalSkillGroupReportResponseBodyDataListOverall = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
    ):
        self.back_2back = back_2back
        self.inbound = inbound
        self.outbound = outbound
        self.overall = overall
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name

    def validate(self):
        if self.back_2back:
            self.back_2back.validate()
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
        if self.back_2back is not None:
            result['Back2Back'] = self.back_2back.to_map()

        if self.inbound is not None:
            result['Inbound'] = self.inbound.to_map()

        if self.outbound is not None:
            result['Outbound'] = self.outbound.to_map()

        if self.overall is not None:
            result['Overall'] = self.overall.to_map()

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Back2Back') is not None:
            temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataListBack2Back()
            self.back_2back = temp_model.from_map(m.get('Back2Back'))

        if m.get('Inbound') is not None:
            temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataListInbound()
            self.inbound = temp_model.from_map(m.get('Inbound'))

        if m.get('Outbound') is not None:
            temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataListOutbound()
            self.outbound = temp_model.from_map(m.get('Outbound'))

        if m.get('Overall') is not None:
            temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataListOverall()
            self.overall = temp_model.from_map(m.get('Overall'))

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')

        return self

class ListHistoricalSkillGroupReportResponseBodyDataListOverall(DaraModel):
    def __init__(
        self,
        average_break_time: float = None,
        average_hold_time: float = None,
        average_ready_time: float = None,
        average_talk_time: float = None,
        average_work_time: float = None,
        break_code_detail_list: List[main_models.ListHistoricalSkillGroupReportResponseBodyDataListOverallBreakCodeDetailList] = None,
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
        self.max_break_time = max_break_time
        self.max_hold_time = max_hold_time
        self.max_ready_time = max_ready_time
        self.max_talk_time = max_talk_time
        self.max_work_time = max_work_time
        self.occupancy_rate = occupancy_rate
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.total_break_time = total_break_time
        self.total_calls = total_calls
        self.total_hold_time = total_hold_time
        self.total_logged_in_time = total_logged_in_time
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
                temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataListOverallBreakCodeDetailList()
                self.break_code_detail_list.append(temp_model.from_map(k1))

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

        if m.get('TotalReadyTime') is not None:
            self.total_ready_time = m.get('TotalReadyTime')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')

        return self

class ListHistoricalSkillGroupReportResponseBodyDataListOverallBreakCodeDetailList(DaraModel):
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

class ListHistoricalSkillGroupReportResponseBodyDataListOutbound(DaraModel):
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

class ListHistoricalSkillGroupReportResponseBodyDataListInbound(DaraModel):
    def __init__(
        self,
        abandon_rate: float = None,
        access_channel_type_details: List[main_models.ListHistoricalSkillGroupReportResponseBodyDataListInboundAccessChannelTypeDetails] = None,
        average_abandon_time: float = None,
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
        calls_abandoned_in_queue: int = None,
        calls_abandoned_in_ring: int = None,
        calls_attended_transfer_in: int = None,
        calls_attended_transfer_out: int = None,
        calls_blind_transfer_in: int = None,
        calls_blind_transfer_out: int = None,
        calls_handled: int = None,
        calls_hold: int = None,
        calls_offered: int = None,
        calls_overflow: int = None,
        calls_queued: int = None,
        calls_queuing_failed: int = None,
        calls_queuing_overflow: int = None,
        calls_queuing_timeout: int = None,
        calls_ringed: int = None,
        calls_timeout: int = None,
        handle_rate: float = None,
        max_abandon_time: int = None,
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
        self.abandon_rate = abandon_rate
        self.access_channel_type_details = access_channel_type_details
        self.average_abandon_time = average_abandon_time
        self.average_abandoned_in_queue_time = average_abandoned_in_queue_time
        self.average_abandoned_in_ring_time = average_abandoned_in_ring_time
        self.average_first_response_time = average_first_response_time
        self.average_hold_time = average_hold_time
        self.average_response_time = average_response_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.average_wait_time = average_wait_time
        self.average_work_time = average_work_time
        self.calls_abandoned = calls_abandoned
        self.calls_abandoned_in_queue = calls_abandoned_in_queue
        self.calls_abandoned_in_ring = calls_abandoned_in_ring
        self.calls_attended_transfer_in = calls_attended_transfer_in
        self.calls_attended_transfer_out = calls_attended_transfer_out
        self.calls_blind_transfer_in = calls_blind_transfer_in
        self.calls_blind_transfer_out = calls_blind_transfer_out
        self.calls_handled = calls_handled
        self.calls_hold = calls_hold
        self.calls_offered = calls_offered
        self.calls_overflow = calls_overflow
        self.calls_queued = calls_queued
        self.calls_queuing_failed = calls_queuing_failed
        self.calls_queuing_overflow = calls_queuing_overflow
        self.calls_queuing_timeout = calls_queuing_timeout
        self.calls_ringed = calls_ringed
        self.calls_timeout = calls_timeout
        self.handle_rate = handle_rate
        self.max_abandon_time = max_abandon_time
        self.max_abandoned_in_queue_time = max_abandoned_in_queue_time
        self.max_abandoned_in_ring_time = max_abandoned_in_ring_time
        self.max_hold_time = max_hold_time
        self.max_ring_time = max_ring_time
        self.max_talk_time = max_talk_time
        self.max_wait_time = max_wait_time
        self.max_work_time = max_work_time
        self.satisfaction_index = satisfaction_index
        self.satisfaction_rate = satisfaction_rate
        self.satisfaction_surveys_offered = satisfaction_surveys_offered
        self.satisfaction_surveys_responded = satisfaction_surveys_responded
        self.service_level_15 = service_level_15
        self.service_level_20 = service_level_20
        self.service_level_30 = service_level_30
        self.total_abandon_time = total_abandon_time
        self.total_abandoned_in_queue_time = total_abandoned_in_queue_time
        self.total_abandoned_in_ring_time = total_abandoned_in_ring_time
        self.total_hold_time = total_hold_time
        self.total_messages_sent = total_messages_sent
        self.total_messages_sent_by_agent = total_messages_sent_by_agent
        self.total_messages_sent_by_customer = total_messages_sent_by_customer
        self.total_ring_time = total_ring_time
        self.total_talk_time = total_talk_time
        self.total_wait_time = total_wait_time
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
        if self.abandon_rate is not None:
            result['AbandonRate'] = self.abandon_rate

        result['AccessChannelTypeDetails'] = []
        if self.access_channel_type_details is not None:
            for k1 in self.access_channel_type_details:
                result['AccessChannelTypeDetails'].append(k1.to_map() if k1 else None)

        if self.average_abandon_time is not None:
            result['AverageAbandonTime'] = self.average_abandon_time

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

        if self.calls_abandoned_in_queue is not None:
            result['CallsAbandonedInQueue'] = self.calls_abandoned_in_queue

        if self.calls_abandoned_in_ring is not None:
            result['CallsAbandonedInRing'] = self.calls_abandoned_in_ring

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

        if self.calls_overflow is not None:
            result['CallsOverflow'] = self.calls_overflow

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

        if self.calls_timeout is not None:
            result['CallsTimeout'] = self.calls_timeout

        if self.handle_rate is not None:
            result['HandleRate'] = self.handle_rate

        if self.max_abandon_time is not None:
            result['MaxAbandonTime'] = self.max_abandon_time

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

        self.access_channel_type_details = []
        if m.get('AccessChannelTypeDetails') is not None:
            for k1 in m.get('AccessChannelTypeDetails'):
                temp_model = main_models.ListHistoricalSkillGroupReportResponseBodyDataListInboundAccessChannelTypeDetails()
                self.access_channel_type_details.append(temp_model.from_map(k1))

        if m.get('AverageAbandonTime') is not None:
            self.average_abandon_time = m.get('AverageAbandonTime')

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

        if m.get('CallsAbandonedInQueue') is not None:
            self.calls_abandoned_in_queue = m.get('CallsAbandonedInQueue')

        if m.get('CallsAbandonedInRing') is not None:
            self.calls_abandoned_in_ring = m.get('CallsAbandonedInRing')

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

        if m.get('CallsOverflow') is not None:
            self.calls_overflow = m.get('CallsOverflow')

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

        if m.get('CallsTimeout') is not None:
            self.calls_timeout = m.get('CallsTimeout')

        if m.get('HandleRate') is not None:
            self.handle_rate = m.get('HandleRate')

        if m.get('MaxAbandonTime') is not None:
            self.max_abandon_time = m.get('MaxAbandonTime')

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

class ListHistoricalSkillGroupReportResponseBodyDataListInboundAccessChannelTypeDetails(DaraModel):
    def __init__(
        self,
        access_channel_type: str = None,
        calls_offered: int = None,
    ):
        self.access_channel_type = access_channel_type
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

class ListHistoricalSkillGroupReportResponseBodyDataListBack2Back(DaraModel):
    def __init__(
        self,
        agent_handle_rate: float = None,
        answer_rate: float = None,
        average_customer_ring_time: float = None,
        average_ring_time: float = None,
        average_talk_time: float = None,
        calls_answered: int = None,
        calls_customer_answered: int = None,
        calls_dialed: int = None,
        customer_answer_rate: float = None,
        max_customer_ring_time: int = None,
        max_ring_time: int = None,
        max_talk_time: int = None,
        total_customer_ring_time: int = None,
        total_ring_time: int = None,
        total_talk_time: int = None,
    ):
        self.agent_handle_rate = agent_handle_rate
        self.answer_rate = answer_rate
        self.average_customer_ring_time = average_customer_ring_time
        self.average_ring_time = average_ring_time
        self.average_talk_time = average_talk_time
        self.calls_answered = calls_answered
        self.calls_customer_answered = calls_customer_answered
        self.calls_dialed = calls_dialed
        self.customer_answer_rate = customer_answer_rate
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

