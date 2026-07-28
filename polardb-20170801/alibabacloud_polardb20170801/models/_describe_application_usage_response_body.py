# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationUsageResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        daily_usage: List[main_models.DescribeApplicationUsageResponseBodyDailyUsage] = None,
        days: int = None,
        message: str = None,
        model_usage: List[main_models.DescribeApplicationUsageResponseBodyModelUsage] = None,
        request_id: str = None,
        session_summary: main_models.DescribeApplicationUsageResponseBodySessionSummary = None,
        skill_usage: main_models.DescribeApplicationUsageResponseBodySkillUsage = None,
        summary: main_models.DescribeApplicationUsageResponseBodySummary = None,
    ):
        # The Hermes application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The usage statistics grouped by UTC date.
        self.daily_usage = daily_usage
        # The number of days covered by this statistical period.
        self.days = days
        # The response message.
        self.message = message
        # The usage statistics grouped by model.
        self.model_usage = model_usage
        # The request ID.
        self.request_id = request_id
        # The current session runtime and storage statistics.
        self.session_summary = session_summary
        # The aggregated statistics of skill activities.
        self.skill_usage = skill_usage
        # The aggregated usage within the query period.
        self.summary = summary

    def validate(self):
        if self.daily_usage:
            for v1 in self.daily_usage:
                 if v1:
                    v1.validate()
        if self.model_usage:
            for v1 in self.model_usage:
                 if v1:
                    v1.validate()
        if self.session_summary:
            self.session_summary.validate()
        if self.skill_usage:
            self.skill_usage.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        result['DailyUsage'] = []
        if self.daily_usage is not None:
            for k1 in self.daily_usage:
                result['DailyUsage'].append(k1.to_map() if k1 else None)

        if self.days is not None:
            result['Days'] = self.days

        if self.message is not None:
            result['Message'] = self.message

        result['ModelUsage'] = []
        if self.model_usage is not None:
            for k1 in self.model_usage:
                result['ModelUsage'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_summary is not None:
            result['SessionSummary'] = self.session_summary.to_map()

        if self.skill_usage is not None:
            result['SkillUsage'] = self.skill_usage.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.daily_usage = []
        if m.get('DailyUsage') is not None:
            for k1 in m.get('DailyUsage'):
                temp_model = main_models.DescribeApplicationUsageResponseBodyDailyUsage()
                self.daily_usage.append(temp_model.from_map(k1))

        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.model_usage = []
        if m.get('ModelUsage') is not None:
            for k1 in m.get('ModelUsage'):
                temp_model = main_models.DescribeApplicationUsageResponseBodyModelUsage()
                self.model_usage.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionSummary') is not None:
            temp_model = main_models.DescribeApplicationUsageResponseBodySessionSummary()
            self.session_summary = temp_model.from_map(m.get('SessionSummary'))

        if m.get('SkillUsage') is not None:
            temp_model = main_models.DescribeApplicationUsageResponseBodySkillUsage()
            self.skill_usage = temp_model.from_map(m.get('SkillUsage'))

        if m.get('Summary') is not None:
            temp_model = main_models.DescribeApplicationUsageResponseBodySummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

class DescribeApplicationUsageResponseBodySummary(DaraModel):
    def __init__(
        self,
        apicalls: int = None,
        cache_read_tokens: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        reasoning_tokens: int = None,
        sessions: int = None,
    ):
        # The number of model API calls.
        self.apicalls = apicalls
        # The number of tokens served from cache hits.
        self.cache_read_tokens = cache_read_tokens
        # The number of input tokens.
        self.input_tokens = input_tokens
        # The number of output tokens.
        self.output_tokens = output_tokens
        # The number of reasoning tokens.
        self.reasoning_tokens = reasoning_tokens
        # The number of sessions.
        self.sessions = sessions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apicalls is not None:
            result['APICalls'] = self.apicalls

        if self.cache_read_tokens is not None:
            result['CacheReadTokens'] = self.cache_read_tokens

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.reasoning_tokens is not None:
            result['ReasoningTokens'] = self.reasoning_tokens

        if self.sessions is not None:
            result['Sessions'] = self.sessions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APICalls') is not None:
            self.apicalls = m.get('APICalls')

        if m.get('CacheReadTokens') is not None:
            self.cache_read_tokens = m.get('CacheReadTokens')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('ReasoningTokens') is not None:
            self.reasoning_tokens = m.get('ReasoningTokens')

        if m.get('Sessions') is not None:
            self.sessions = m.get('Sessions')

        return self

class DescribeApplicationUsageResponseBodySkillUsage(DaraModel):
    def __init__(
        self,
        distinct_skills: int = None,
        total_actions: int = None,
        total_edits: int = None,
        total_loads: int = None,
    ):
        # The number of distinct skills that have activity records.
        self.distinct_skills = distinct_skills
        # The total number of skill-related operations.
        self.total_actions = total_actions
        # The number of times skills were edited or managed.
        self.total_edits = total_edits
        # The number of times skills were loaded or viewed.
        self.total_loads = total_loads

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distinct_skills is not None:
            result['DistinctSkills'] = self.distinct_skills

        if self.total_actions is not None:
            result['TotalActions'] = self.total_actions

        if self.total_edits is not None:
            result['TotalEdits'] = self.total_edits

        if self.total_loads is not None:
            result['TotalLoads'] = self.total_loads

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctSkills') is not None:
            self.distinct_skills = m.get('DistinctSkills')

        if m.get('TotalActions') is not None:
            self.total_actions = m.get('TotalActions')

        if m.get('TotalEdits') is not None:
            self.total_edits = m.get('TotalEdits')

        if m.get('TotalLoads') is not None:
            self.total_loads = m.get('TotalLoads')

        return self

class DescribeApplicationUsageResponseBodySessionSummary(DaraModel):
    def __init__(
        self,
        active_sessions: int = None,
        stored_sessions: int = None,
    ):
        # The number of currently active sessions.
        self.active_sessions = active_sessions
        # The total number of sessions in session storage.
        self.stored_sessions = stored_sessions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_sessions is not None:
            result['ActiveSessions'] = self.active_sessions

        if self.stored_sessions is not None:
            result['StoredSessions'] = self.stored_sessions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveSessions') is not None:
            self.active_sessions = m.get('ActiveSessions')

        if m.get('StoredSessions') is not None:
            self.stored_sessions = m.get('StoredSessions')

        return self

class DescribeApplicationUsageResponseBodyModelUsage(DaraModel):
    def __init__(
        self,
        apicalls: int = None,
        cache_read_tokens: int = None,
        input_tokens: int = None,
        model: str = None,
        output_tokens: int = None,
        provider: str = None,
        reasoning_tokens: int = None,
        sessions: int = None,
    ):
        # The number of API calls for this model.
        self.apicalls = apicalls
        # The number of tokens served from cache hits for this model.
        self.cache_read_tokens = cache_read_tokens
        # The number of input tokens consumed by this model.
        self.input_tokens = input_tokens
        # The model identifier.
        self.model = model
        # The number of output tokens generated by this model.
        self.output_tokens = output_tokens
        # The model provider.
        self.provider = provider
        # The number of reasoning tokens generated by this model.
        self.reasoning_tokens = reasoning_tokens
        # The number of sessions that used this model.
        self.sessions = sessions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apicalls is not None:
            result['APICalls'] = self.apicalls

        if self.cache_read_tokens is not None:
            result['CacheReadTokens'] = self.cache_read_tokens

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.model is not None:
            result['Model'] = self.model

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.reasoning_tokens is not None:
            result['ReasoningTokens'] = self.reasoning_tokens

        if self.sessions is not None:
            result['Sessions'] = self.sessions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APICalls') is not None:
            self.apicalls = m.get('APICalls')

        if m.get('CacheReadTokens') is not None:
            self.cache_read_tokens = m.get('CacheReadTokens')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ReasoningTokens') is not None:
            self.reasoning_tokens = m.get('ReasoningTokens')

        if m.get('Sessions') is not None:
            self.sessions = m.get('Sessions')

        return self

class DescribeApplicationUsageResponseBodyDailyUsage(DaraModel):
    def __init__(
        self,
        apicalls: int = None,
        cache_read_tokens: int = None,
        date: str = None,
        input_tokens: int = None,
        output_tokens: int = None,
        reasoning_tokens: int = None,
        sessions: int = None,
    ):
        # The number of model API calls for the day.
        self.apicalls = apicalls
        # The number of tokens served from cache hits for the day.
        self.cache_read_tokens = cache_read_tokens
        # The UTC date.
        self.date = date
        # The number of input tokens for the day.
        self.input_tokens = input_tokens
        # The number of output tokens for the day.
        self.output_tokens = output_tokens
        # The number of reasoning tokens for the day.
        self.reasoning_tokens = reasoning_tokens
        # The number of sessions for the day.
        self.sessions = sessions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apicalls is not None:
            result['APICalls'] = self.apicalls

        if self.cache_read_tokens is not None:
            result['CacheReadTokens'] = self.cache_read_tokens

        if self.date is not None:
            result['Date'] = self.date

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.reasoning_tokens is not None:
            result['ReasoningTokens'] = self.reasoning_tokens

        if self.sessions is not None:
            result['Sessions'] = self.sessions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APICalls') is not None:
            self.apicalls = m.get('APICalls')

        if m.get('CacheReadTokens') is not None:
            self.cache_read_tokens = m.get('CacheReadTokens')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('ReasoningTokens') is not None:
            self.reasoning_tokens = m.get('ReasoningTokens')

        if m.get('Sessions') is not None:
            self.sessions = m.get('Sessions')

        return self

