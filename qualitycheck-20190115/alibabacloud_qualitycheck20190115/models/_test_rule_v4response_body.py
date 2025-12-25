# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class TestRuleV4ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TestRuleV4ResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.TestRuleV4ResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TestRuleV4ResponseBodyData(DaraModel):
    def __init__(
        self,
        hit_rule_review_info_list: List[main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoList] = None,
        hit_task_flow_list: List[main_models.TestRuleV4ResponseBodyDataHitTaskFlowList] = None,
        unhit_rule_review_info_list: List[main_models.TestRuleV4ResponseBodyDataUnhitRuleReviewInfoList] = None,
    ):
        self.hit_rule_review_info_list = hit_rule_review_info_list
        self.hit_task_flow_list = hit_task_flow_list
        self.unhit_rule_review_info_list = unhit_rule_review_info_list

    def validate(self):
        if self.hit_rule_review_info_list:
            for v1 in self.hit_rule_review_info_list:
                 if v1:
                    v1.validate()
        if self.hit_task_flow_list:
            for v1 in self.hit_task_flow_list:
                 if v1:
                    v1.validate()
        if self.unhit_rule_review_info_list:
            for v1 in self.unhit_rule_review_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitRuleReviewInfoList'] = []
        if self.hit_rule_review_info_list is not None:
            for k1 in self.hit_rule_review_info_list:
                result['HitRuleReviewInfoList'].append(k1.to_map() if k1 else None)

        result['HitTaskFlowList'] = []
        if self.hit_task_flow_list is not None:
            for k1 in self.hit_task_flow_list:
                result['HitTaskFlowList'].append(k1.to_map() if k1 else None)

        result['UnhitRuleReviewInfoList'] = []
        if self.unhit_rule_review_info_list is not None:
            for k1 in self.unhit_rule_review_info_list:
                result['UnhitRuleReviewInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_rule_review_info_list = []
        if m.get('HitRuleReviewInfoList') is not None:
            for k1 in m.get('HitRuleReviewInfoList'):
                temp_model = main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoList()
                self.hit_rule_review_info_list.append(temp_model.from_map(k1))

        self.hit_task_flow_list = []
        if m.get('HitTaskFlowList') is not None:
            for k1 in m.get('HitTaskFlowList'):
                temp_model = main_models.TestRuleV4ResponseBodyDataHitTaskFlowList()
                self.hit_task_flow_list.append(temp_model.from_map(k1))

        self.unhit_rule_review_info_list = []
        if m.get('UnhitRuleReviewInfoList') is not None:
            for k1 in m.get('UnhitRuleReviewInfoList'):
                temp_model = main_models.TestRuleV4ResponseBodyDataUnhitRuleReviewInfoList()
                self.unhit_rule_review_info_list.append(temp_model.from_map(k1))

        return self

class TestRuleV4ResponseBodyDataUnhitRuleReviewInfoList(DaraModel):
    def __init__(
        self,
        condition_info_list: List[main_models.ConditionBasicInfo] = None,
        matched: bool = None,
        rid: int = None,
        task_flow_type: int = None,
    ):
        self.condition_info_list = condition_info_list
        self.matched = matched
        self.rid = rid
        self.task_flow_type = task_flow_type

    def validate(self):
        if self.condition_info_list:
            for v1 in self.condition_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionInfoList'] = []
        if self.condition_info_list is not None:
            for k1 in self.condition_info_list:
                result['ConditionInfoList'].append(k1.to_map() if k1 else None)

        if self.matched is not None:
            result['Matched'] = self.matched

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.task_flow_type is not None:
            result['TaskFlowType'] = self.task_flow_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_info_list = []
        if m.get('ConditionInfoList') is not None:
            for k1 in m.get('ConditionInfoList'):
                temp_model = main_models.ConditionBasicInfo()
                self.condition_info_list.append(temp_model.from_map(k1))

        if m.get('Matched') is not None:
            self.matched = m.get('Matched')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')

        return self

class TestRuleV4ResponseBodyDataHitTaskFlowList(DaraModel):
    def __init__(
        self,
        graph_flow: main_models.TaskGraphFlow = None,
        rid: int = None,
        task_flow_type: int = None,
    ):
        self.graph_flow = graph_flow
        self.rid = rid
        self.task_flow_type = task_flow_type

    def validate(self):
        if self.graph_flow:
            self.graph_flow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_flow is not None:
            result['GraphFlow'] = self.graph_flow.to_map()

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.task_flow_type is not None:
            result['TaskFlowType'] = self.task_flow_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GraphFlow') is not None:
            temp_model = main_models.TaskGraphFlow()
            self.graph_flow = temp_model.from_map(m.get('GraphFlow'))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')

        return self

class TestRuleV4ResponseBodyDataHitRuleReviewInfoList(DaraModel):
    def __init__(
        self,
        branch_hit_id: int = None,
        branch_info_list: List[main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListBranchInfoList] = None,
        condition_hit_info_list: List[main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoList] = None,
        condition_info_list: List[main_models.ConditionBasicInfo] = None,
        judge_node_name: str = None,
        lambda_: str = None,
        matched: bool = None,
        node_type: str = None,
        rid: int = None,
        rule_name: str = None,
        rule_score_type: int = None,
        score_num_type: int = None,
        task_flow_id: int = None,
    ):
        self.branch_hit_id = branch_hit_id
        self.branch_info_list = branch_info_list
        self.condition_hit_info_list = condition_hit_info_list
        self.condition_info_list = condition_info_list
        self.judge_node_name = judge_node_name
        self.lambda_ = lambda_
        self.matched = matched
        self.node_type = node_type
        self.rid = rid
        self.rule_name = rule_name
        self.rule_score_type = rule_score_type
        self.score_num_type = score_num_type
        self.task_flow_id = task_flow_id

    def validate(self):
        if self.branch_info_list:
            for v1 in self.branch_info_list:
                 if v1:
                    v1.validate()
        if self.condition_hit_info_list:
            for v1 in self.condition_hit_info_list:
                 if v1:
                    v1.validate()
        if self.condition_info_list:
            for v1 in self.condition_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_hit_id is not None:
            result['BranchHitId'] = self.branch_hit_id

        result['BranchInfoList'] = []
        if self.branch_info_list is not None:
            for k1 in self.branch_info_list:
                result['BranchInfoList'].append(k1.to_map() if k1 else None)

        result['ConditionHitInfoList'] = []
        if self.condition_hit_info_list is not None:
            for k1 in self.condition_hit_info_list:
                result['ConditionHitInfoList'].append(k1.to_map() if k1 else None)

        result['ConditionInfoList'] = []
        if self.condition_info_list is not None:
            for k1 in self.condition_info_list:
                result['ConditionInfoList'].append(k1.to_map() if k1 else None)

        if self.judge_node_name is not None:
            result['JudgeNodeName'] = self.judge_node_name

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.matched is not None:
            result['Matched'] = self.matched

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type

        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type

        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchHitId') is not None:
            self.branch_hit_id = m.get('BranchHitId')

        self.branch_info_list = []
        if m.get('BranchInfoList') is not None:
            for k1 in m.get('BranchInfoList'):
                temp_model = main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListBranchInfoList()
                self.branch_info_list.append(temp_model.from_map(k1))

        self.condition_hit_info_list = []
        if m.get('ConditionHitInfoList') is not None:
            for k1 in m.get('ConditionHitInfoList'):
                temp_model = main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoList()
                self.condition_hit_info_list.append(temp_model.from_map(k1))

        self.condition_info_list = []
        if m.get('ConditionInfoList') is not None:
            for k1 in m.get('ConditionInfoList'):
                temp_model = main_models.ConditionBasicInfo()
                self.condition_info_list.append(temp_model.from_map(k1))

        if m.get('JudgeNodeName') is not None:
            self.judge_node_name = m.get('JudgeNodeName')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Matched') is not None:
            self.matched = m.get('Matched')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')

        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')

        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')

        return self

class TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoList(DaraModel):
    def __init__(
        self,
        cid: List[str] = None,
        key_words: List[main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListKeyWords] = None,
        phrase: main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListPhrase = None,
    ):
        self.cid = cid
        self.key_words = key_words
        self.phrase = phrase

    def validate(self):
        if self.key_words:
            for v1 in self.key_words:
                 if v1:
                    v1.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cid is not None:
            result['Cid'] = self.cid

        result['KeyWords'] = []
        if self.key_words is not None:
            for k1 in self.key_words:
                result['KeyWords'].append(k1.to_map() if k1 else None)

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        self.key_words = []
        if m.get('KeyWords') is not None:
            for k1 in m.get('KeyWords'):
                temp_model = main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListKeyWords()
                self.key_words.append(temp_model.from_map(k1))

        if m.get('Phrase') is not None:
            temp_model = main_models.TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListPhrase(DaraModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        channel_id: int = None,
        emotion_fine_grained_value: int = None,
        emotion_value: int = None,
        end: int = None,
        hit_status: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        pid: int = None,
        renter_id: int = None,
        role: str = None,
        sid: int = None,
        silence_duration: int = None,
        speech_rate: int = None,
        uuid: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.channel_id = channel_id
        self.emotion_fine_grained_value = emotion_fine_grained_value
        self.emotion_value = emotion_value
        self.end = end
        self.hit_status = hit_status
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.pid = pid
        self.renter_id = renter_id
        self.role = role
        self.sid = sid
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.uuid = uuid
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

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.emotion_fine_grained_value is not None:
            result['EmotionFineGrainedValue'] = self.emotion_fine_grained_value

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status

        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.renter_id is not None:
            result['RenterId'] = self.renter_id

        if self.role is not None:
            result['Role'] = self.role

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EmotionFineGrainedValue') is not None:
            self.emotion_fine_grained_value = m.get('EmotionFineGrainedValue')

        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')

        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RenterId') is not None:
            self.renter_id = m.get('RenterId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListKeyWords(DaraModel):
    def __init__(
        self,
        cid: str = None,
        customize_code: str = None,
        from_: int = None,
        oid: str = None,
        operator_key: str = None,
        pid: int = None,
        similar_phrase: str = None,
        tid: str = None,
        to: int = None,
        uuid: str = None,
        val: str = None,
    ):
        self.cid = cid
        self.customize_code = customize_code
        self.from_ = from_
        self.oid = oid
        self.operator_key = operator_key
        self.pid = pid
        self.similar_phrase = similar_phrase
        self.tid = tid
        self.to = to
        self.uuid = uuid
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

        if self.customize_code is not None:
            result['CustomizeCode'] = self.customize_code

        if self.from_ is not None:
            result['From'] = self.from_

        if self.oid is not None:
            result['Oid'] = self.oid

        if self.operator_key is not None:
            result['OperatorKey'] = self.operator_key

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.similar_phrase is not None:
            result['SimilarPhrase'] = self.similar_phrase

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.to is not None:
            result['To'] = self.to

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.val is not None:
            result['Val'] = self.val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('CustomizeCode') is not None:
            self.customize_code = m.get('CustomizeCode')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Oid') is not None:
            self.oid = m.get('Oid')

        if m.get('OperatorKey') is not None:
            self.operator_key = m.get('OperatorKey')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('SimilarPhrase') is not None:
            self.similar_phrase = m.get('SimilarPhrase')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Val') is not None:
            self.val = m.get('Val')

        return self

class TestRuleV4ResponseBodyDataHitRuleReviewInfoListBranchInfoList(DaraModel):
    def __init__(
        self,
        check_type: int = None,
        index: int = None,
        lambda_: str = None,
        name: str = None,
        next_node_id: int = None,
        situation: main_models.NextNodeSituations = None,
        triggers: List[str] = None,
    ):
        self.check_type = check_type
        self.index = index
        self.lambda_ = lambda_
        self.name = name
        self.next_node_id = next_node_id
        self.situation = situation
        self.triggers = triggers

    def validate(self):
        if self.situation:
            self.situation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.index is not None:
            result['Index'] = self.index

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.name is not None:
            result['Name'] = self.name

        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id

        if self.situation is not None:
            result['Situation'] = self.situation.to_map()

        if self.triggers is not None:
            result['Triggers'] = self.triggers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')

        if m.get('Situation') is not None:
            temp_model = main_models.NextNodeSituations()
            self.situation = temp_model.from_map(m.get('Situation'))

        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')

        return self

