# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class GetInstanceTrendingReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetInstanceTrendingReportResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The internal error code.
        self.code = code
        # The scenario ID.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The dynamic error parameters.
        self.params = params
        # Id of the request
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

        if self.params is not None:
            result['Params'] = self.params

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
                temp_model = main_models.GetInstanceTrendingReportResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceTrendingReportResponseBodyData(DaraModel):
    def __init__(
        self,
        calls_handled: int = None,
        calls_offered: int = None,
        calls_rejected: int = None,
        calls_resolved: int = None,
        configured_concurrency: int = None,
        label_breakdown: str = None,
        max_talk_time: int = None,
        rejection_breakdown: str = None,
        release_reason_breakdown: str = None,
        stats_time: int = None,
        talk_turns_distribution: str = None,
        total_input_tokens: int = None,
        total_output_tokens: int = None,
        total_talk_time: int = None,
        total_tokens: int = None,
        used_concurrency: int = None,
    ):
        # The number of answered sessions.
        self.calls_handled = calls_handled
        # The number of incoming sessions.
        self.calls_offered = calls_offered
        # The number of rejected sessions.
        self.calls_rejected = calls_rejected
        # The number of resolved sessions, based on the model evaluation results.
        self.calls_resolved = calls_resolved
        # The latest configured concurrency.
        self.configured_concurrency = configured_concurrency
        # The distribution of labels.
        self.label_breakdown = label_breakdown
        # The maximum talk time, in milliseconds.
        self.max_talk_time = max_talk_time
        # The distribution of rejection reasons.
        self.rejection_breakdown = rejection_breakdown
        # The distribution of hang-up reasons after a session is connected.
        self.release_reason_breakdown = release_reason_breakdown
        # The statistical time. The value is a UNIX timestamp in milliseconds.
        self.stats_time = stats_time
        # The distribution of dialog turns.
        self.talk_turns_distribution = talk_turns_distribution
        # Reserved for future use.
        self.total_input_tokens = total_input_tokens
        # Reserved for future use.
        self.total_output_tokens = total_output_tokens
        # The total talk time, in milliseconds.
        self.total_talk_time = total_talk_time
        # Reserved for future use.
        self.total_tokens = total_tokens
        # The maximum concurrency used.
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

        if self.label_breakdown is not None:
            result['LabelBreakdown'] = self.label_breakdown

        if self.max_talk_time is not None:
            result['MaxTalkTime'] = self.max_talk_time

        if self.rejection_breakdown is not None:
            result['RejectionBreakdown'] = self.rejection_breakdown

        if self.release_reason_breakdown is not None:
            result['ReleaseReasonBreakdown'] = self.release_reason_breakdown

        if self.stats_time is not None:
            result['StatsTime'] = self.stats_time

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

        if m.get('LabelBreakdown') is not None:
            self.label_breakdown = m.get('LabelBreakdown')

        if m.get('MaxTalkTime') is not None:
            self.max_talk_time = m.get('MaxTalkTime')

        if m.get('RejectionBreakdown') is not None:
            self.rejection_breakdown = m.get('RejectionBreakdown')

        if m.get('ReleaseReasonBreakdown') is not None:
            self.release_reason_breakdown = m.get('ReleaseReasonBreakdown')

        if m.get('StatsTime') is not None:
            self.stats_time = m.get('StatsTime')

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

