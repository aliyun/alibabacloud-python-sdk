# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListHistoricalScriptReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListHistoricalScriptReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        # Id of the request
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

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListHistoricalScriptReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHistoricalScriptReportResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListHistoricalScriptReportResponseBodyDataList] = None,
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
                temp_model = main_models.ListHistoricalScriptReportResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHistoricalScriptReportResponseBodyDataList(DaraModel):
    def __init__(
        self,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_rejected: int = None,
        calls_resolved: int = None,
        configured_concurrency: int = None,
        label_distribution: str = None,
        max_talk_time: int = None,
        rejection_breakdown: str = None,
        release_reason_breakdown: str = None,
        script_id: str = None,
        talk_turns_distribution: str = None,
        total_input_tokens: int = None,
        total_output_tokens: int = None,
        total_talk_time: int = None,
        total_tokens: int = None,
        used_concurrency: int = None,
    ):
        self.calls_handled = calls_handled
        self.calls_offered = calls_offered
        self.calls_rejected = calls_rejected
        self.calls_resolved = calls_resolved
        self.configured_concurrency = configured_concurrency
        self.label_distribution = label_distribution
        self.max_talk_time = max_talk_time
        self.rejection_breakdown = rejection_breakdown
        self.release_reason_breakdown = release_reason_breakdown
        self.script_id = script_id
        self.talk_turns_distribution = talk_turns_distribution
        self.total_input_tokens = total_input_tokens
        self.total_output_tokens = total_output_tokens
        self.total_talk_time = total_talk_time
        self.total_tokens = total_tokens
        self.used_concurrency = used_concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calls_handled is not None:
            result['CallsHandled'] = self.calls_handled

        if self.calls_offered is not None:
            result['CallsOffered'] = self.calls_offered

        if self.calls_rejected is not None:
            result['CallsRejected'] = self.calls_rejected

        if self.calls_resolved is not None:
            result['CallsResolved'] = self.calls_resolved

        if self.configured_concurrency is not None:
            result['ConfiguredConcurrency'] = self.configured_concurrency

        if self.label_distribution is not None:
            result['LabelDistribution'] = self.label_distribution

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.rejection_breakdown is not None:
            result['RejectionBreakdown'] = self.rejection_breakdown

        if self.release_reason_breakdown is not None:
            result['ReleaseReasonBreakdown'] = self.release_reason_breakdown

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.talk_turns_distribution is not None:
            result['TalkTurnsDistribution'] = self.talk_turns_distribution

        if self.total_input_tokens is not None:
            result['TotalInputTokens'] = self.total_input_tokens

        if self.total_output_tokens is not None:
            result['TotalOutputTokens'] = self.total_output_tokens

        if self.total_talk_time is not None:
            result['TotalTalkTime'] = self.total_talk_time

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.used_concurrency is not None:
            result['UsedConcurrency'] = self.used_concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallsHandled') is not None:
            self.calls_handled = m.get('CallsHandled')

        if m.get('CallsOffered') is not None:
            self.calls_offered = m.get('CallsOffered')

        if m.get('CallsRejected') is not None:
            self.calls_rejected = m.get('CallsRejected')

        if m.get('CallsResolved') is not None:
            self.calls_resolved = m.get('CallsResolved')

        if m.get('ConfiguredConcurrency') is not None:
            self.configured_concurrency = m.get('ConfiguredConcurrency')

        if m.get('LabelDistribution') is not None:
            self.label_distribution = m.get('LabelDistribution')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('RejectionBreakdown') is not None:
            self.rejection_breakdown = m.get('RejectionBreakdown')

        if m.get('ReleaseReasonBreakdown') is not None:
            self.release_reason_breakdown = m.get('ReleaseReasonBreakdown')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('TalkTurnsDistribution') is not None:
            self.talk_turns_distribution = m.get('TalkTurnsDistribution')

        if m.get('TotalInputTokens') is not None:
            self.total_input_tokens = m.get('TotalInputTokens')

        if m.get('TotalOutputTokens') is not None:
            self.total_output_tokens = m.get('TotalOutputTokens')

        if m.get('TotalTalkTime') is not None:
            self.total_talk_time = m.get('TotalTalkTime')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('UsedConcurrency') is not None:
            self.used_concurrency = m.get('UsedConcurrency')

        return self

