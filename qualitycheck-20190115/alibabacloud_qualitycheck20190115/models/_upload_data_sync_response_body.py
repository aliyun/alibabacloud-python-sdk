# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class UploadDataSyncResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UploadDataSyncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.UploadDataSyncResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UploadDataSyncResponseBodyData(DaraModel):
    def __init__(
        self,
        result_info: List[main_models.UploadDataSyncResponseBodyDataResultInfo] = None,
    ):
        self.result_info = result_info

    def validate(self):
        if self.result_info:
            for v1 in self.result_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k1 in self.result_info:
                result['ResultInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k1 in m.get('ResultInfo'):
                temp_model = main_models.UploadDataSyncResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k1))

        return self

class UploadDataSyncResponseBodyDataResultInfo(DaraModel):
    def __init__(
        self,
        hand_score_id_list: main_models.UploadDataSyncResponseBodyDataResultInfoHandScoreIdList = None,
        rules: main_models.UploadDataSyncResponseBodyDataResultInfoRules = None,
        score: int = None,
    ):
        self.hand_score_id_list = hand_score_id_list
        self.rules = rules
        self.score = score

    def validate(self):
        if self.hand_score_id_list:
            self.hand_score_id_list.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list.to_map()

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandScoreIdList') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoHandScoreIdList()
            self.hand_score_id_list = temp_model.from_map(m.get('HandScoreIdList'))

        if m.get('Rules') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class UploadDataSyncResponseBodyDataResultInfoRules(DaraModel):
    def __init__(
        self,
        rule_hit_info: List[main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo] = None,
    ):
        self.rule_hit_info = rule_hit_info

    def validate(self):
        if self.rule_hit_info:
            for v1 in self.rule_hit_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleHitInfo'] = []
        if self.rule_hit_info is not None:
            for k1 in self.rule_hit_info:
                result['RuleHitInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_hit_info = []
        if m.get('RuleHitInfo') is not None:
            for k1 in m.get('RuleHitInfo'):
                temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo()
                self.rule_hit_info.append(temp_model.from_map(k1))

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo(DaraModel):
    def __init__(
        self,
        condition_info: main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo = None,
        hit: main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit = None,
        rid: str = None,
        tid: str = None,
    ):
        self.condition_info = condition_info
        self.hit = hit
        self.rid = rid
        self.tid = tid

    def validate(self):
        if self.condition_info:
            self.condition_info.validate()
        if self.hit:
            self.hit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_info is not None:
            result['ConditionInfo'] = self.condition_info.to_map()

        if self.hit is not None:
            result['Hit'] = self.hit.to_map()

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionInfo') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo()
            self.condition_info = temp_model.from_map(m.get('ConditionInfo'))

        if m.get('Hit') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit()
            self.hit = temp_model.from_map(m.get('Hit'))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit(DaraModel):
    def __init__(
        self,
        condition_hit_info: List[main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo] = None,
    ):
        self.condition_hit_info = condition_hit_info

    def validate(self):
        if self.condition_hit_info:
            for v1 in self.condition_hit_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionHitInfo'] = []
        if self.condition_hit_info is not None:
            for k1 in self.condition_hit_info:
                result['ConditionHitInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_hit_info = []
        if m.get('ConditionHitInfo') is not None:
            for k1 in m.get('ConditionHitInfo'):
                temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k1))

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo(DaraModel):
    def __init__(
        self,
        hit_cids: main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids = None,
        hit_key_words: main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords = None,
        phrase: main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase = None,
    ):
        self.hit_cids = hit_cids
        self.hit_key_words = hit_key_words
        self.phrase = phrase

    def validate(self):
        if self.hit_cids:
            self.hit_cids.validate()
        if self.hit_key_words:
            self.hit_key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hit_cids is not None:
            result['HitCids'] = self.hit_cids.to_map()

        if self.hit_key_words is not None:
            result['HitKeyWords'] = self.hit_key_words.to_map()

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitCids') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids()
            self.hit_cids = temp_model.from_map(m.get('HitCids'))

        if m.get('HitKeyWords') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords()
            self.hit_key_words = temp_model.from_map(m.get('HitKeyWords'))

        if m.get('Phrase') is not None:
            temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        end: int = None,
        identity: str = None,
        role: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.end = end
        self.identity = identity
        self.role = role
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

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end is not None:
            result['End'] = self.end

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.role is not None:
            result['Role'] = self.role

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords(DaraModel):
    def __init__(
        self,
        hit_key_word: List[main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord] = None,
    ):
        self.hit_key_word = hit_key_word

    def validate(self):
        if self.hit_key_word:
            for v1 in self.hit_key_word:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitKeyWord'] = []
        if self.hit_key_word is not None:
            for k1 in self.hit_key_word:
                result['HitKeyWord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_key_word = []
        if m.get('HitKeyWord') is not None:
            for k1 in m.get('HitKeyWord'):
                temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord()
                self.hit_key_word.append(temp_model.from_map(k1))

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord(DaraModel):
    def __init__(
        self,
        from_: int = None,
        pid: int = None,
        tid: str = None,
        to: int = None,
        val: str = None,
    ):
        self.from_ = from_
        self.pid = pid
        self.tid = tid
        self.to = to
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.to is not None:
            result['To'] = self.to

        if self.val is not None:
            result['Val'] = self.val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Val') is not None:
            self.val = m.get('Val')

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids(DaraModel):
    def __init__(
        self,
        cid_item: List[str] = None,
    ):
        self.cid_item = cid_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid_item is not None:
            result['CidItem'] = self.cid_item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidItem') is not None:
            self.cid_item = m.get('CidItem')

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo(DaraModel):
    def __init__(
        self,
        condition_basic_info: List[main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo] = None,
    ):
        self.condition_basic_info = condition_basic_info

    def validate(self):
        if self.condition_basic_info:
            for v1 in self.condition_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionBasicInfo'] = []
        if self.condition_basic_info is not None:
            for k1 in self.condition_basic_info:
                result['ConditionBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_basic_info = []
        if m.get('ConditionBasicInfo') is not None:
            for k1 in m.get('ConditionBasicInfo'):
                temp_model = main_models.UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k1))

        return self

class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo(DaraModel):
    def __init__(
        self,
        condition_info_cid: str = None,
    ):
        self.condition_info_cid = condition_info_cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_info_cid is not None:
            result['ConditionInfoCid'] = self.condition_info_cid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')

        return self

class UploadDataSyncResponseBodyDataResultInfoHandScoreIdList(DaraModel):
    def __init__(
        self,
        hand_score_id_list: List[str] = None,
    ):
        self.hand_score_id_list = hand_score_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandScoreIdList') is not None:
            self.hand_score_id_list = m.get('HandScoreIdList')

        return self

