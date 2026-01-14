# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class GetAICoachScriptResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        append_question_flag: bool = None,
        assessment_scope: str = None,
        check_cheat_config: main_models.GetAICoachScriptResponseBodyCheckCheatConfig = None,
        closing_remarks: str = None,
        complete_strategy: main_models.GetAICoachScriptResponseBodyCompleteStrategy = None,
        cover_url: str = None,
        custom_reply_rules: List[main_models.GetAICoachScriptResponseBodyCustomReplyRules] = None,
        dialogue_input_text_limit: int = None,
        dialogue_text_flag: bool = None,
        dialogue_tip_flag: bool = None,
        dialogue_voice_limit: int = None,
        evaluate_report_flag: bool = None,
        expressiveness: Dict[str, int] = None,
        expressiveness_list: List[main_models.GetAICoachScriptResponseBodyExpressivenessList] = None,
        gif_dynamic_url: str = None,
        gif_static_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        initiator: str = None,
        interaction_input_types: List[str] = None,
        interaction_type: int = None,
        introduce: str = None,
        name: str = None,
        opening_remarks: str = None,
        order_ack_flag: bool = None,
        point_deduction_rule_list: List[main_models.GetAICoachScriptResponseBodyPointDeductionRuleList] = None,
        points: List[main_models.GetAICoachScriptResponseBodyPoints] = None,
        request_id: str = None,
        sample_dialogue_list: List[main_models.GetAICoachScriptResponseBodySampleDialogueList] = None,
        score_config: main_models.GetAICoachScriptResponseBodyScoreConfig = None,
        script_record_id: str = None,
        sparring_tip_content: str = None,
        sparring_tip_title: str = None,
        status: int = None,
        student_think_time_flag: bool = None,
        student_think_time_limit: int = None,
        type: int = None,
        voice_id: str = None,
        voice_language: str = None,
        weights: main_models.GetAICoachScriptResponseBodyWeights = None,
    ):
        self.agent_id = agent_id
        self.append_question_flag = append_question_flag
        self.assessment_scope = assessment_scope
        self.check_cheat_config = check_cheat_config
        self.closing_remarks = closing_remarks
        self.complete_strategy = complete_strategy
        self.cover_url = cover_url
        self.custom_reply_rules = custom_reply_rules
        self.dialogue_input_text_limit = dialogue_input_text_limit
        self.dialogue_text_flag = dialogue_text_flag
        self.dialogue_tip_flag = dialogue_tip_flag
        self.dialogue_voice_limit = dialogue_voice_limit
        self.evaluate_report_flag = evaluate_report_flag
        self.expressiveness = expressiveness
        self.expressiveness_list = expressiveness_list
        self.gif_dynamic_url = gif_dynamic_url
        self.gif_static_url = gif_static_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.initiator = initiator
        self.interaction_input_types = interaction_input_types
        self.interaction_type = interaction_type
        self.introduce = introduce
        self.name = name
        self.opening_remarks = opening_remarks
        self.order_ack_flag = order_ack_flag
        self.point_deduction_rule_list = point_deduction_rule_list
        self.points = points
        self.request_id = request_id
        self.sample_dialogue_list = sample_dialogue_list
        self.score_config = score_config
        self.script_record_id = script_record_id
        self.sparring_tip_content = sparring_tip_content
        self.sparring_tip_title = sparring_tip_title
        self.status = status
        self.student_think_time_flag = student_think_time_flag
        self.student_think_time_limit = student_think_time_limit
        self.type = type
        self.voice_id = voice_id
        self.voice_language = voice_language
        self.weights = weights

    def validate(self):
        if self.check_cheat_config:
            self.check_cheat_config.validate()
        if self.complete_strategy:
            self.complete_strategy.validate()
        if self.custom_reply_rules:
            for v1 in self.custom_reply_rules:
                 if v1:
                    v1.validate()
        if self.expressiveness_list:
            for v1 in self.expressiveness_list:
                 if v1:
                    v1.validate()
        if self.point_deduction_rule_list:
            for v1 in self.point_deduction_rule_list:
                 if v1:
                    v1.validate()
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()
        if self.sample_dialogue_list:
            for v1 in self.sample_dialogue_list:
                 if v1:
                    v1.validate()
        if self.score_config:
            self.score_config.validate()
        if self.weights:
            self.weights.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.append_question_flag is not None:
            result['appendQuestionFlag'] = self.append_question_flag

        if self.assessment_scope is not None:
            result['assessmentScope'] = self.assessment_scope

        if self.check_cheat_config is not None:
            result['checkCheatConfig'] = self.check_cheat_config.to_map()

        if self.closing_remarks is not None:
            result['closingRemarks'] = self.closing_remarks

        if self.complete_strategy is not None:
            result['completeStrategy'] = self.complete_strategy.to_map()

        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url

        result['customReplyRules'] = []
        if self.custom_reply_rules is not None:
            for k1 in self.custom_reply_rules:
                result['customReplyRules'].append(k1.to_map() if k1 else None)

        if self.dialogue_input_text_limit is not None:
            result['dialogueInputTextLimit'] = self.dialogue_input_text_limit

        if self.dialogue_text_flag is not None:
            result['dialogueTextFlag'] = self.dialogue_text_flag

        if self.dialogue_tip_flag is not None:
            result['dialogueTipFlag'] = self.dialogue_tip_flag

        if self.dialogue_voice_limit is not None:
            result['dialogueVoiceLimit'] = self.dialogue_voice_limit

        if self.evaluate_report_flag is not None:
            result['evaluateReportFlag'] = self.evaluate_report_flag

        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness

        result['expressivenessList'] = []
        if self.expressiveness_list is not None:
            for k1 in self.expressiveness_list:
                result['expressivenessList'].append(k1.to_map() if k1 else None)

        if self.gif_dynamic_url is not None:
            result['gifDynamicUrl'] = self.gif_dynamic_url

        if self.gif_static_url is not None:
            result['gifStaticUrl'] = self.gif_static_url

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.initiator is not None:
            result['initiator'] = self.initiator

        if self.interaction_input_types is not None:
            result['interactionInputTypes'] = self.interaction_input_types

        if self.interaction_type is not None:
            result['interactionType'] = self.interaction_type

        if self.introduce is not None:
            result['introduce'] = self.introduce

        if self.name is not None:
            result['name'] = self.name

        if self.opening_remarks is not None:
            result['openingRemarks'] = self.opening_remarks

        if self.order_ack_flag is not None:
            result['orderAckFlag'] = self.order_ack_flag

        result['pointDeductionRuleList'] = []
        if self.point_deduction_rule_list is not None:
            for k1 in self.point_deduction_rule_list:
                result['pointDeductionRuleList'].append(k1.to_map() if k1 else None)

        result['points'] = []
        if self.points is not None:
            for k1 in self.points:
                result['points'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['sampleDialogueList'] = []
        if self.sample_dialogue_list is not None:
            for k1 in self.sample_dialogue_list:
                result['sampleDialogueList'].append(k1.to_map() if k1 else None)

        if self.score_config is not None:
            result['scoreConfig'] = self.score_config.to_map()

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        if self.sparring_tip_content is not None:
            result['sparringTipContent'] = self.sparring_tip_content

        if self.sparring_tip_title is not None:
            result['sparringTipTitle'] = self.sparring_tip_title

        if self.status is not None:
            result['status'] = self.status

        if self.student_think_time_flag is not None:
            result['studentThinkTimeFlag'] = self.student_think_time_flag

        if self.student_think_time_limit is not None:
            result['studentThinkTimeLimit'] = self.student_think_time_limit

        if self.type is not None:
            result['type'] = self.type

        if self.voice_id is not None:
            result['voiceId'] = self.voice_id

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.weights is not None:
            result['weights'] = self.weights.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appendQuestionFlag') is not None:
            self.append_question_flag = m.get('appendQuestionFlag')

        if m.get('assessmentScope') is not None:
            self.assessment_scope = m.get('assessmentScope')

        if m.get('checkCheatConfig') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCheckCheatConfig()
            self.check_cheat_config = temp_model.from_map(m.get('checkCheatConfig'))

        if m.get('closingRemarks') is not None:
            self.closing_remarks = m.get('closingRemarks')

        if m.get('completeStrategy') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCompleteStrategy()
            self.complete_strategy = temp_model.from_map(m.get('completeStrategy'))

        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')

        self.custom_reply_rules = []
        if m.get('customReplyRules') is not None:
            for k1 in m.get('customReplyRules'):
                temp_model = main_models.GetAICoachScriptResponseBodyCustomReplyRules()
                self.custom_reply_rules.append(temp_model.from_map(k1))

        if m.get('dialogueInputTextLimit') is not None:
            self.dialogue_input_text_limit = m.get('dialogueInputTextLimit')

        if m.get('dialogueTextFlag') is not None:
            self.dialogue_text_flag = m.get('dialogueTextFlag')

        if m.get('dialogueTipFlag') is not None:
            self.dialogue_tip_flag = m.get('dialogueTipFlag')

        if m.get('dialogueVoiceLimit') is not None:
            self.dialogue_voice_limit = m.get('dialogueVoiceLimit')

        if m.get('evaluateReportFlag') is not None:
            self.evaluate_report_flag = m.get('evaluateReportFlag')

        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')

        self.expressiveness_list = []
        if m.get('expressivenessList') is not None:
            for k1 in m.get('expressivenessList'):
                temp_model = main_models.GetAICoachScriptResponseBodyExpressivenessList()
                self.expressiveness_list.append(temp_model.from_map(k1))

        if m.get('gifDynamicUrl') is not None:
            self.gif_dynamic_url = m.get('gifDynamicUrl')

        if m.get('gifStaticUrl') is not None:
            self.gif_static_url = m.get('gifStaticUrl')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

        if m.get('interactionInputTypes') is not None:
            self.interaction_input_types = m.get('interactionInputTypes')

        if m.get('interactionType') is not None:
            self.interaction_type = m.get('interactionType')

        if m.get('introduce') is not None:
            self.introduce = m.get('introduce')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('openingRemarks') is not None:
            self.opening_remarks = m.get('openingRemarks')

        if m.get('orderAckFlag') is not None:
            self.order_ack_flag = m.get('orderAckFlag')

        self.point_deduction_rule_list = []
        if m.get('pointDeductionRuleList') is not None:
            for k1 in m.get('pointDeductionRuleList'):
                temp_model = main_models.GetAICoachScriptResponseBodyPointDeductionRuleList()
                self.point_deduction_rule_list.append(temp_model.from_map(k1))

        self.points = []
        if m.get('points') is not None:
            for k1 in m.get('points'):
                temp_model = main_models.GetAICoachScriptResponseBodyPoints()
                self.points.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.sample_dialogue_list = []
        if m.get('sampleDialogueList') is not None:
            for k1 in m.get('sampleDialogueList'):
                temp_model = main_models.GetAICoachScriptResponseBodySampleDialogueList()
                self.sample_dialogue_list.append(temp_model.from_map(k1))

        if m.get('scoreConfig') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyScoreConfig()
            self.score_config = temp_model.from_map(m.get('scoreConfig'))

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        if m.get('sparringTipContent') is not None:
            self.sparring_tip_content = m.get('sparringTipContent')

        if m.get('sparringTipTitle') is not None:
            self.sparring_tip_title = m.get('sparringTipTitle')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('studentThinkTimeFlag') is not None:
            self.student_think_time_flag = m.get('studentThinkTimeFlag')

        if m.get('studentThinkTimeLimit') is not None:
            self.student_think_time_limit = m.get('studentThinkTimeLimit')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('voiceId') is not None:
            self.voice_id = m.get('voiceId')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('weights') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyWeights()
            self.weights = temp_model.from_map(m.get('weights'))

        return self

class GetAICoachScriptResponseBodyWeights(DaraModel):
    def __init__(
        self,
        ability_evaluation: int = None,
        ability_evaluation_enabled: bool = None,
        assessment_point: int = None,
        assessment_point_enabled: bool = None,
        custom_reply_rule_enabled: bool = None,
        expressiveness: int = None,
        expressiveness_enabled: bool = None,
        point_deduction_rule: int = None,
        point_deduction_rule_enabled: bool = None,
        similar_pronunciation_scoring_enabled: bool = None,
        standard: int = None,
        standard_enabled: bool = None,
    ):
        self.ability_evaluation = ability_evaluation
        self.ability_evaluation_enabled = ability_evaluation_enabled
        self.assessment_point = assessment_point
        self.assessment_point_enabled = assessment_point_enabled
        self.custom_reply_rule_enabled = custom_reply_rule_enabled
        self.expressiveness = expressiveness
        self.expressiveness_enabled = expressiveness_enabled
        self.point_deduction_rule = point_deduction_rule
        self.point_deduction_rule_enabled = point_deduction_rule_enabled
        self.similar_pronunciation_scoring_enabled = similar_pronunciation_scoring_enabled
        self.standard = standard
        self.standard_enabled = standard_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability_evaluation is not None:
            result['abilityEvaluation'] = self.ability_evaluation

        if self.ability_evaluation_enabled is not None:
            result['abilityEvaluationEnabled'] = self.ability_evaluation_enabled

        if self.assessment_point is not None:
            result['assessmentPoint'] = self.assessment_point

        if self.assessment_point_enabled is not None:
            result['assessmentPointEnabled'] = self.assessment_point_enabled

        if self.custom_reply_rule_enabled is not None:
            result['customReplyRuleEnabled'] = self.custom_reply_rule_enabled

        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness

        if self.expressiveness_enabled is not None:
            result['expressivenessEnabled'] = self.expressiveness_enabled

        if self.point_deduction_rule is not None:
            result['pointDeductionRule'] = self.point_deduction_rule

        if self.point_deduction_rule_enabled is not None:
            result['pointDeductionRuleEnabled'] = self.point_deduction_rule_enabled

        if self.similar_pronunciation_scoring_enabled is not None:
            result['similarPronunciationScoringEnabled'] = self.similar_pronunciation_scoring_enabled

        if self.standard is not None:
            result['standard'] = self.standard

        if self.standard_enabled is not None:
            result['standardEnabled'] = self.standard_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abilityEvaluation') is not None:
            self.ability_evaluation = m.get('abilityEvaluation')

        if m.get('abilityEvaluationEnabled') is not None:
            self.ability_evaluation_enabled = m.get('abilityEvaluationEnabled')

        if m.get('assessmentPoint') is not None:
            self.assessment_point = m.get('assessmentPoint')

        if m.get('assessmentPointEnabled') is not None:
            self.assessment_point_enabled = m.get('assessmentPointEnabled')

        if m.get('customReplyRuleEnabled') is not None:
            self.custom_reply_rule_enabled = m.get('customReplyRuleEnabled')

        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')

        if m.get('expressivenessEnabled') is not None:
            self.expressiveness_enabled = m.get('expressivenessEnabled')

        if m.get('pointDeductionRule') is not None:
            self.point_deduction_rule = m.get('pointDeductionRule')

        if m.get('pointDeductionRuleEnabled') is not None:
            self.point_deduction_rule_enabled = m.get('pointDeductionRuleEnabled')

        if m.get('similarPronunciationScoringEnabled') is not None:
            self.similar_pronunciation_scoring_enabled = m.get('similarPronunciationScoringEnabled')

        if m.get('standard') is not None:
            self.standard = m.get('standard')

        if m.get('standardEnabled') is not None:
            self.standard_enabled = m.get('standardEnabled')

        return self

class GetAICoachScriptResponseBodyScoreConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        level_enabled: bool = None,
        levels: List[main_models.GetAICoachScriptResponseBodyScoreConfigLevels] = None,
        pass_score: str = None,
    ):
        self.enabled = enabled
        self.level_enabled = level_enabled
        self.levels = levels
        self.pass_score = pass_score

    def validate(self):
        if self.levels:
            for v1 in self.levels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.level_enabled is not None:
            result['levelEnabled'] = self.level_enabled

        result['levels'] = []
        if self.levels is not None:
            for k1 in self.levels:
                result['levels'].append(k1.to_map() if k1 else None)

        if self.pass_score is not None:
            result['passScore'] = self.pass_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('levelEnabled') is not None:
            self.level_enabled = m.get('levelEnabled')

        self.levels = []
        if m.get('levels') is not None:
            for k1 in m.get('levels'):
                temp_model = main_models.GetAICoachScriptResponseBodyScoreConfigLevels()
                self.levels.append(temp_model.from_map(k1))

        if m.get('passScore') is not None:
            self.pass_score = m.get('passScore')

        return self

class GetAICoachScriptResponseBodyScoreConfigLevels(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        name: str = None,
    ):
        self.max = max
        self.min = min
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetAICoachScriptResponseBodySampleDialogueList(DaraModel):
    def __init__(
        self,
        message: str = None,
        role: str = None,
    ):
        self.message = message
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class GetAICoachScriptResponseBodyPoints(DaraModel):
    def __init__(
        self,
        answer_list: List[main_models.GetAICoachScriptResponseBodyPointsAnswerList] = None,
        knowledge_list: List[str] = None,
        name: str = None,
        point_id: str = None,
        question_description: str = None,
        sort_no: int = None,
        weight: int = None,
    ):
        self.answer_list = answer_list
        self.knowledge_list = knowledge_list
        self.name = name
        self.point_id = point_id
        self.question_description = question_description
        self.sort_no = sort_no
        self.weight = weight

    def validate(self):
        if self.answer_list:
            for v1 in self.answer_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerList'] = []
        if self.answer_list is not None:
            for k1 in self.answer_list:
                result['answerList'].append(k1.to_map() if k1 else None)

        if self.knowledge_list is not None:
            result['knowledgeList'] = self.knowledge_list

        if self.name is not None:
            result['name'] = self.name

        if self.point_id is not None:
            result['pointId'] = self.point_id

        if self.question_description is not None:
            result['questionDescription'] = self.question_description

        if self.sort_no is not None:
            result['sortNo'] = self.sort_no

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_list = []
        if m.get('answerList') is not None:
            for k1 in m.get('answerList'):
                temp_model = main_models.GetAICoachScriptResponseBodyPointsAnswerList()
                self.answer_list.append(temp_model.from_map(k1))

        if m.get('knowledgeList') is not None:
            self.knowledge_list = m.get('knowledgeList')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pointId') is not None:
            self.point_id = m.get('pointId')

        if m.get('questionDescription') is not None:
            self.question_description = m.get('questionDescription')

        if m.get('sortNo') is not None:
            self.sort_no = m.get('sortNo')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetAICoachScriptResponseBodyPointsAnswerList(DaraModel):
    def __init__(
        self,
        answer_values: List[main_models.GetAICoachScriptResponseBodyPointsAnswerListAnswerValues] = None,
        enabled_keyword: bool = None,
        name: str = None,
        name_list: List[str] = None,
        operators: str = None,
        parameters: List[main_models.GetAICoachScriptResponseBodyPointsAnswerListParameters] = None,
        type: str = None,
        weight: int = None,
    ):
        self.answer_values = answer_values
        self.enabled_keyword = enabled_keyword
        self.name = name
        self.name_list = name_list
        self.operators = operators
        self.parameters = parameters
        self.type = type
        self.weight = weight

    def validate(self):
        if self.answer_values:
            for v1 in self.answer_values:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['answerValues'] = []
        if self.answer_values is not None:
            for k1 in self.answer_values:
                result['answerValues'].append(k1.to_map() if k1 else None)

        if self.enabled_keyword is not None:
            result['enabledKeyword'] = self.enabled_keyword

        if self.name is not None:
            result['name'] = self.name

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.operators is not None:
            result['operators'] = self.operators

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_values = []
        if m.get('answerValues') is not None:
            for k1 in m.get('answerValues'):
                temp_model = main_models.GetAICoachScriptResponseBodyPointsAnswerListAnswerValues()
                self.answer_values.append(temp_model.from_map(k1))

        if m.get('enabledKeyword') is not None:
            self.enabled_keyword = m.get('enabledKeyword')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('operators') is not None:
            self.operators = m.get('operators')

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.GetAICoachScriptResponseBodyPointsAnswerListParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetAICoachScriptResponseBodyPointsAnswerListParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetAICoachScriptResponseBodyPointsAnswerListAnswerValues(DaraModel):
    def __init__(
        self,
        answer_name: str = None,
        answer_weight: int = None,
        keyword_values: List[main_models.GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesKeywordValues] = None,
        keyword_weight: int = None,
        scoring_rules: List[main_models.GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesScoringRules] = None,
    ):
        self.answer_name = answer_name
        self.answer_weight = answer_weight
        self.keyword_values = keyword_values
        self.keyword_weight = keyword_weight
        self.scoring_rules = scoring_rules

    def validate(self):
        if self.keyword_values:
            for v1 in self.keyword_values:
                 if v1:
                    v1.validate()
        if self.scoring_rules:
            for v1 in self.scoring_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_name is not None:
            result['answerName'] = self.answer_name

        if self.answer_weight is not None:
            result['answerWeight'] = self.answer_weight

        result['keywordValues'] = []
        if self.keyword_values is not None:
            for k1 in self.keyword_values:
                result['keywordValues'].append(k1.to_map() if k1 else None)

        if self.keyword_weight is not None:
            result['keywordWeight'] = self.keyword_weight

        result['scoringRules'] = []
        if self.scoring_rules is not None:
            for k1 in self.scoring_rules:
                result['scoringRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerName') is not None:
            self.answer_name = m.get('answerName')

        if m.get('answerWeight') is not None:
            self.answer_weight = m.get('answerWeight')

        self.keyword_values = []
        if m.get('keywordValues') is not None:
            for k1 in m.get('keywordValues'):
                temp_model = main_models.GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesKeywordValues()
                self.keyword_values.append(temp_model.from_map(k1))

        if m.get('keywordWeight') is not None:
            self.keyword_weight = m.get('keywordWeight')

        self.scoring_rules = []
        if m.get('scoringRules') is not None:
            for k1 in m.get('scoringRules'):
                temp_model = main_models.GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesScoringRules()
                self.scoring_rules.append(temp_model.from_map(k1))

        return self

class GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesScoringRules(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetAICoachScriptResponseBodyPointsAnswerListAnswerValuesKeywordValues(DaraModel):
    def __init__(
        self,
        name: str = None,
        weight: int = None,
    ):
        self.name = name
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetAICoachScriptResponseBodyPointDeductionRuleList(DaraModel):
    def __init__(
        self,
        description: str = None,
        punishment_types: List[str] = None,
        rule_value: str = None,
        weight: int = None,
    ):
        self.description = description
        self.punishment_types = punishment_types
        self.rule_value = rule_value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.punishment_types is not None:
            result['punishmentTypes'] = self.punishment_types

        if self.rule_value is not None:
            result['ruleValue'] = self.rule_value

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('punishmentTypes') is not None:
            self.punishment_types = m.get('punishmentTypes')

        if m.get('ruleValue') is not None:
            self.rule_value = m.get('ruleValue')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetAICoachScriptResponseBodyExpressivenessList(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enabled: bool = None,
        expressiveness_id: str = None,
        name: str = None,
        rule: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.desc = desc
        self.enabled = enabled
        self.expressiveness_id = expressiveness_id
        self.name = name
        self.rule = rule
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.expressiveness_id is not None:
            result['expressivenessId'] = self.expressiveness_id

        if self.name is not None:
            result['name'] = self.name

        if self.rule is not None:
            result['rule'] = self.rule

        if self.type is not None:
            result['type'] = self.type

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('expressivenessId') is not None:
            self.expressiveness_id = m.get('expressivenessId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('rule') is not None:
            self.rule = m.get('rule')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class GetAICoachScriptResponseBodyCustomReplyRules(DaraModel):
    def __init__(
        self,
        action: main_models.GetAICoachScriptResponseBodyCustomReplyRulesAction = None,
        logic: str = None,
        main_condition: main_models.GetAICoachScriptResponseBodyCustomReplyRulesMainCondition = None,
        priority: int = None,
        sub_condition: main_models.GetAICoachScriptResponseBodyCustomReplyRulesSubCondition = None,
    ):
        self.action = action
        self.logic = logic
        self.main_condition = main_condition
        self.priority = priority
        self.sub_condition = sub_condition

    def validate(self):
        if self.action:
            self.action.validate()
        if self.main_condition:
            self.main_condition.validate()
        if self.sub_condition:
            self.sub_condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action.to_map()

        if self.logic is not None:
            result['logic'] = self.logic

        if self.main_condition is not None:
            result['mainCondition'] = self.main_condition.to_map()

        if self.priority is not None:
            result['priority'] = self.priority

        if self.sub_condition is not None:
            result['subCondition'] = self.sub_condition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCustomReplyRulesAction()
            self.action = temp_model.from_map(m.get('action'))

        if m.get('logic') is not None:
            self.logic = m.get('logic')

        if m.get('mainCondition') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCustomReplyRulesMainCondition()
            self.main_condition = temp_model.from_map(m.get('mainCondition'))

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('subCondition') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCustomReplyRulesSubCondition()
            self.sub_condition = temp_model.from_map(m.get('subCondition'))

        return self

class GetAICoachScriptResponseBodyCustomReplyRulesSubCondition(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetAICoachScriptResponseBodyCustomReplyRulesMainCondition(DaraModel):
    def __init__(
        self,
        parameters: main_models.GetAICoachScriptResponseBodyCustomReplyRulesMainConditionParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
        self.type = type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCustomReplyRulesMainConditionParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetAICoachScriptResponseBodyCustomReplyRulesMainConditionParameters(DaraModel):
    def __init__(
        self,
        assess_point_id: str = None,
    ):
        self.assess_point_id = assess_point_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assess_point_id is not None:
            result['assessPointId'] = self.assess_point_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assessPointId') is not None:
            self.assess_point_id = m.get('assessPointId')

        return self

class GetAICoachScriptResponseBodyCustomReplyRulesAction(DaraModel):
    def __init__(
        self,
        parameters: main_models.GetAICoachScriptResponseBodyCustomReplyRulesActionParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
        self.type = type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            temp_model = main_models.GetAICoachScriptResponseBodyCustomReplyRulesActionParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetAICoachScriptResponseBodyCustomReplyRulesActionParameters(DaraModel):
    def __init__(
        self,
        assess_point_id: str = None,
        custom_content: str = None,
    ):
        self.assess_point_id = assess_point_id
        self.custom_content = custom_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assess_point_id is not None:
            result['assessPointId'] = self.assess_point_id

        if self.custom_content is not None:
            result['customContent'] = self.custom_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assessPointId') is not None:
            self.assess_point_id = m.get('assessPointId')

        if m.get('customContent') is not None:
            self.custom_content = m.get('customContent')

        return self

class GetAICoachScriptResponseBodyCompleteStrategy(DaraModel):
    def __init__(
        self,
        abnormal_quit_session_expired: int = None,
        abnormal_quit_session_expired_flag: bool = None,
        click_complete_auto_end: bool = None,
        duration: int = None,
        duration_flag: bool = None,
        full_coverage_auto_end: bool = None,
    ):
        self.abnormal_quit_session_expired = abnormal_quit_session_expired
        self.abnormal_quit_session_expired_flag = abnormal_quit_session_expired_flag
        self.click_complete_auto_end = click_complete_auto_end
        self.duration = duration
        self.duration_flag = duration_flag
        self.full_coverage_auto_end = full_coverage_auto_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_quit_session_expired is not None:
            result['abnormalQuitSessionExpired'] = self.abnormal_quit_session_expired

        if self.abnormal_quit_session_expired_flag is not None:
            result['abnormalQuitSessionExpiredFlag'] = self.abnormal_quit_session_expired_flag

        if self.click_complete_auto_end is not None:
            result['clickCompleteAutoEnd'] = self.click_complete_auto_end

        if self.duration is not None:
            result['duration'] = self.duration

        if self.duration_flag is not None:
            result['durationFlag'] = self.duration_flag

        if self.full_coverage_auto_end is not None:
            result['fullCoverageAutoEnd'] = self.full_coverage_auto_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('abnormalQuitSessionExpired') is not None:
            self.abnormal_quit_session_expired = m.get('abnormalQuitSessionExpired')

        if m.get('abnormalQuitSessionExpiredFlag') is not None:
            self.abnormal_quit_session_expired_flag = m.get('abnormalQuitSessionExpiredFlag')

        if m.get('clickCompleteAutoEnd') is not None:
            self.click_complete_auto_end = m.get('clickCompleteAutoEnd')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('durationFlag') is not None:
            self.duration_flag = m.get('durationFlag')

        if m.get('fullCoverageAutoEnd') is not None:
            self.full_coverage_auto_end = m.get('fullCoverageAutoEnd')

        return self

class GetAICoachScriptResponseBodyCheckCheatConfig(DaraModel):
    def __init__(
        self,
        check_image: bool = None,
        check_voice: bool = None,
    ):
        self.check_image = check_image
        self.check_voice = check_voice

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_image is not None:
            result['checkImage'] = self.check_image

        if self.check_voice is not None:
            result['checkVoice'] = self.check_voice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkImage') is not None:
            self.check_image = m.get('checkImage')

        if m.get('checkVoice') is not None:
            self.check_voice = m.get('checkVoice')

        return self

