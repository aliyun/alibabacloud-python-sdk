# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class SyncQualityCheckResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SyncQualityCheckResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Result status code. 200 indicates success. Other values indicate failure. The caller can determine the reason for failure using this field.
        self.code = code
        # Returned result, including hit information.
        self.data = data
        # Error details if an error occurs. "successful" if successful.
        self.message = message
        # Unique request identifier.
        self.request_id = request_id
        # Indicates whether the request was successful. The caller can use this field to determine if the request succeeded: true for success; false/null for failure.
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.SyncQualityCheckResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SyncQualityCheckResponseBodyData(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        rules: List[main_models.SyncQualityCheckResponseBodyDataRules] = None,
        score: int = None,
        task_id: str = None,
        tid: str = None,
    ):
        # Time of recording and dialogue occurrence, in milliseconds since January 1, 1970, 00:00:00 UTC (UNIX timestamp in milliseconds, such as 1584535485856).
        self.begin_time = begin_time
        # List of hit rules. Each item is a rule. Only hit rule information and hit rule location information are returned.
        self.rules = rules
        # Final score, with a maximum of 100.
        self.score = score
        # Task ID.
        self.task_id = task_id
        # Unique identifier for the current conversation.
        self.tid = tid

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['Score'] = self.score

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.SyncQualityCheckResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class SyncQualityCheckResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        hit: List[main_models.SyncQualityCheckResponseBodyDataRulesHit] = None,
        rid: str = None,
        rule_info_base: main_models.SyncQualityCheckResponseBodyDataRulesRuleInfoBase = None,
        rule_name: str = None,
    ):
        # List of hit sentences. For this API, if a hit occurs, it is a single data entry.
        self.hit = hit
        # ID of the hit rule.
        self.rid = rid
        # Rule basic information
        self.rule_info_base = rule_info_base
        # Name of the hit rule.
        self.rule_name = rule_name

    def validate(self):
        if self.hit:
            for v1 in self.hit:
                 if v1:
                    v1.validate()
        if self.rule_info_base:
            self.rule_info_base.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hit'] = []
        if self.hit is not None:
            for k1 in self.hit:
                result['Hit'].append(k1.to_map() if k1 else None)

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_info_base is not None:
            result['RuleInfoBase'] = self.rule_info_base.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit = []
        if m.get('Hit') is not None:
            for k1 in m.get('Hit'):
                temp_model = main_models.SyncQualityCheckResponseBodyDataRulesHit()
                self.hit.append(temp_model.from_map(k1))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleInfoBase') is not None:
            temp_model = main_models.SyncQualityCheckResponseBodyDataRulesRuleInfoBase()
            self.rule_info_base = temp_model.from_map(m.get('RuleInfoBase'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class SyncQualityCheckResponseBodyDataRulesRuleInfoBase(DaraModel):
    def __init__(
        self,
        comments: str = None,
        level: int = None,
        rule_category_name: str = None,
        score_num: int = None,
        score_num_type: int = None,
        score_type: int = None,
        type: int = None,
    ):
        # Rule remarks
        self.comments = comments
        # Rule importance level
        self.level = level
        # Rule category name
        # >Notice: The requiredFields parameter must include "ruleInfoBase.ruleCategoryName".
        self.rule_category_name = rule_category_name
        # Score value
        self.score_num = score_num
        # Scoring type. 0: bonus/penalty points, 1: one-time score.
        self.score_num_type = score_num_type
        # 1 for bonus points, 3 for penalty points. Default is 1.
        self.score_type = score_type
        # Rule type ID
        # >Notice: The requiredFields parameter must include "ruleInfoBase".
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.level is not None:
            result['Level'] = self.level

        if self.rule_category_name is not None:
            result['RuleCategoryName'] = self.rule_category_name

        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('RuleCategoryName') is not None:
            self.rule_category_name = m.get('RuleCategoryName')

        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SyncQualityCheckResponseBodyDataRulesHit(DaraModel):
    def __init__(
        self,
        hit_key_words: List[main_models.SyncQualityCheckResponseBodyDataRulesHitHitKeyWords] = None,
        phrase: main_models.SyncQualityCheckResponseBodyDataRulesHitPhrase = None,
    ):
        # Keywords that met the condition.
        self.hit_key_words = hit_key_words
        # Dialogue content that met the condition.
        self.phrase = phrase

    def validate(self):
        if self.hit_key_words:
            for v1 in self.hit_key_words:
                 if v1:
                    v1.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitKeyWords'] = []
        if self.hit_key_words is not None:
            for k1 in self.hit_key_words:
                result['HitKeyWords'].append(k1.to_map() if k1 else None)

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_key_words = []
        if m.get('HitKeyWords') is not None:
            for k1 in m.get('HitKeyWords'):
                temp_model = main_models.SyncQualityCheckResponseBodyDataRulesHitHitKeyWords()
                self.hit_key_words.append(temp_model.from_map(k1))

        if m.get('Phrase') is not None:
            temp_model = main_models.SyncQualityCheckResponseBodyDataRulesHitPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class SyncQualityCheckResponseBodyDataRulesHitPhrase(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        identity: str = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        # Start time of this sentence relative to the entire conversation, in milliseconds.
        self.begin = begin
        # Emotional value of this sentence, 0-10. Higher values indicate stronger emotions.
        self.emotion_value = emotion_value
        # End time of this sentence relative to the entire conversation, in milliseconds.
        self.end = end
        # Deprecated field. Ignore it.
        self.identity = identity
        # Role of this sentence. Valid values: customer service representative, customer.
        self.role = role
        # Deprecated field. Ignore it.
        self.silence_duration = silence_duration
        # Speech rate of this sentence, in characters per minute.
        self.speech_rate = speech_rate
        # Dialogue content.
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.role is not None:
            result['Role'] = self.role

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class SyncQualityCheckResponseBodyDataRulesHitHitKeyWords(DaraModel):
    def __init__(
        self,
        cid: int = None,
        from_: int = None,
        pid: int = None,
        to: int = None,
        val: str = None,
    ):
        # Condition ID of the rule.
        self.cid = cid
        # Start position of the keyword.
        self.from_ = from_
        # Index value of the hit sentence in the entire conversation.
        self.pid = pid
        # End position of the keyword.
        self.to = to
        # Keyword.
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        if self.from_ is not None:
            result['From'] = self.from_

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.to is not None:
            result['To'] = self.to

        if self.val is not None:
            result['Val'] = self.val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Val') is not None:
            self.val = m.get('Val')

        return self

