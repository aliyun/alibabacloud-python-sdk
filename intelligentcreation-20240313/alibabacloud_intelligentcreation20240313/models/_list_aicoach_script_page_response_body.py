# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class ListAICoachScriptPageResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        list: List[main_models.ListAICoachScriptPageResponseBodyList] = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.list = list
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListAICoachScriptPageResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAICoachScriptPageResponseBodyList(DaraModel):
    def __init__(
        self,
        append_question_flag: str = None,
        assessment_scope: str = None,
        closing_remarks: str = None,
        complete_strategy: main_models.ListAICoachScriptPageResponseBodyListCompleteStrategy = None,
        cover_url: str = None,
        custom_reply_rules: List[main_models.ListAICoachScriptPageResponseBodyListCustomReplyRules] = None,
        dialogue_text_flag: bool = None,
        dialogue_tip_flag: bool = None,
        evaluate_report_flag: bool = None,
        expressiveness: Dict[str, str] = None,
        gif_dynamic_url: str = None,
        gif_static_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        initiator: str = None,
        interaction_type: str = None,
        introduce: str = None,
        name: str = None,
        opening_remarks: str = None,
        order_ack_flag: bool = None,
        sample_dialogue_list: List[main_models.ListAICoachScriptPageResponseBodyListSampleDialogueList] = None,
        score_config: main_models.ListAICoachScriptPageResponseBodyListScoreConfig = None,
        script_record_id: str = None,
        sparring_tip_content: str = None,
        sparring_tip_title: str = None,
        status: int = None,
        student_think_time_flag: bool = None,
        type: int = None,
        weights: main_models.ListAICoachScriptPageResponseBodyListWeights = None,
    ):
        self.append_question_flag = append_question_flag
        self.assessment_scope = assessment_scope
        self.closing_remarks = closing_remarks
        self.complete_strategy = complete_strategy
        self.cover_url = cover_url
        self.custom_reply_rules = custom_reply_rules
        self.dialogue_text_flag = dialogue_text_flag
        self.dialogue_tip_flag = dialogue_tip_flag
        self.evaluate_report_flag = evaluate_report_flag
        self.expressiveness = expressiveness
        self.gif_dynamic_url = gif_dynamic_url
        self.gif_static_url = gif_static_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.initiator = initiator
        self.interaction_type = interaction_type
        self.introduce = introduce
        self.name = name
        self.opening_remarks = opening_remarks
        self.order_ack_flag = order_ack_flag
        self.sample_dialogue_list = sample_dialogue_list
        self.score_config = score_config
        self.script_record_id = script_record_id
        self.sparring_tip_content = sparring_tip_content
        self.sparring_tip_title = sparring_tip_title
        self.status = status
        self.student_think_time_flag = student_think_time_flag
        self.type = type
        self.weights = weights

    def validate(self):
        if self.complete_strategy:
            self.complete_strategy.validate()
        if self.custom_reply_rules:
            for v1 in self.custom_reply_rules:
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
        if self.append_question_flag is not None:
            result['appendQuestionFlag'] = self.append_question_flag

        if self.assessment_scope is not None:
            result['assessmentScope'] = self.assessment_scope

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

        if self.dialogue_text_flag is not None:
            result['dialogueTextFlag'] = self.dialogue_text_flag

        if self.dialogue_tip_flag is not None:
            result['dialogueTipFlag'] = self.dialogue_tip_flag

        if self.evaluate_report_flag is not None:
            result['evaluateReportFlag'] = self.evaluate_report_flag

        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness

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

        if self.type is not None:
            result['type'] = self.type

        if self.weights is not None:
            result['weights'] = self.weights.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendQuestionFlag') is not None:
            self.append_question_flag = m.get('appendQuestionFlag')

        if m.get('assessmentScope') is not None:
            self.assessment_scope = m.get('assessmentScope')

        if m.get('closingRemarks') is not None:
            self.closing_remarks = m.get('closingRemarks')

        if m.get('completeStrategy') is not None:
            temp_model = main_models.ListAICoachScriptPageResponseBodyListCompleteStrategy()
            self.complete_strategy = temp_model.from_map(m.get('completeStrategy'))

        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')

        self.custom_reply_rules = []
        if m.get('customReplyRules') is not None:
            for k1 in m.get('customReplyRules'):
                temp_model = main_models.ListAICoachScriptPageResponseBodyListCustomReplyRules()
                self.custom_reply_rules.append(temp_model.from_map(k1))

        if m.get('dialogueTextFlag') is not None:
            self.dialogue_text_flag = m.get('dialogueTextFlag')

        if m.get('dialogueTipFlag') is not None:
            self.dialogue_tip_flag = m.get('dialogueTipFlag')

        if m.get('evaluateReportFlag') is not None:
            self.evaluate_report_flag = m.get('evaluateReportFlag')

        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')

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

        self.sample_dialogue_list = []
        if m.get('sampleDialogueList') is not None:
            for k1 in m.get('sampleDialogueList'):
                temp_model = main_models.ListAICoachScriptPageResponseBodyListSampleDialogueList()
                self.sample_dialogue_list.append(temp_model.from_map(k1))

        if m.get('scoreConfig') is not None:
            temp_model = main_models.ListAICoachScriptPageResponseBodyListScoreConfig()
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

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('weights') is not None:
            temp_model = main_models.ListAICoachScriptPageResponseBodyListWeights()
            self.weights = temp_model.from_map(m.get('weights'))

        return self

class ListAICoachScriptPageResponseBodyListWeights(DaraModel):
    def __init__(
        self,
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

class ListAICoachScriptPageResponseBodyListScoreConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        level_enabled: bool = None,
        levels: List[main_models.ListAICoachScriptPageResponseBodyListScoreConfigLevels] = None,
        pass_score: int = None,
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
                temp_model = main_models.ListAICoachScriptPageResponseBodyListScoreConfigLevels()
                self.levels.append(temp_model.from_map(k1))

        if m.get('passScore') is not None:
            self.pass_score = m.get('passScore')

        return self

class ListAICoachScriptPageResponseBodyListScoreConfigLevels(DaraModel):
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

class ListAICoachScriptPageResponseBodyListSampleDialogueList(DaraModel):
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

class ListAICoachScriptPageResponseBodyListCustomReplyRules(DaraModel):
    def __init__(
        self,
        action: main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesAction = None,
        logic: str = None,
        main_condition: main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesMainCondition = None,
        priority: int = None,
        sort_no: int = None,
        sub_condition: main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesSubCondition = None,
    ):
        self.action = action
        self.logic = logic
        self.main_condition = main_condition
        self.priority = priority
        self.sort_no = sort_no
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

        if self.sort_no is not None:
            result['sortNo'] = self.sort_no

        if self.sub_condition is not None:
            result['subCondition'] = self.sub_condition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            temp_model = main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesAction()
            self.action = temp_model.from_map(m.get('action'))

        if m.get('logic') is not None:
            self.logic = m.get('logic')

        if m.get('mainCondition') is not None:
            temp_model = main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesMainCondition()
            self.main_condition = temp_model.from_map(m.get('mainCondition'))

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('sortNo') is not None:
            self.sort_no = m.get('sortNo')

        if m.get('subCondition') is not None:
            temp_model = main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesSubCondition()
            self.sub_condition = temp_model.from_map(m.get('subCondition'))

        return self

class ListAICoachScriptPageResponseBodyListCustomReplyRulesSubCondition(DaraModel):
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

class ListAICoachScriptPageResponseBodyListCustomReplyRulesMainCondition(DaraModel):
    def __init__(
        self,
        parameters: main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesMainConditionParameters = None,
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
            temp_model = main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesMainConditionParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListAICoachScriptPageResponseBodyListCustomReplyRulesMainConditionParameters(DaraModel):
    def __init__(
        self,
        assess_point: str = None,
    ):
        self.assess_point = assess_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assess_point is not None:
            result['assessPoint'] = self.assess_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assessPoint') is not None:
            self.assess_point = m.get('assessPoint')

        return self

class ListAICoachScriptPageResponseBodyListCustomReplyRulesAction(DaraModel):
    def __init__(
        self,
        parameters: main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesActionParameters = None,
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
            temp_model = main_models.ListAICoachScriptPageResponseBodyListCustomReplyRulesActionParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListAICoachScriptPageResponseBodyListCustomReplyRulesActionParameters(DaraModel):
    def __init__(
        self,
        assess_point: str = None,
        custom_content: str = None,
    ):
        self.assess_point = assess_point
        self.custom_content = custom_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assess_point is not None:
            result['assessPoint'] = self.assess_point

        if self.custom_content is not None:
            result['customContent'] = self.custom_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assessPoint') is not None:
            self.assess_point = m.get('assessPoint')

        if m.get('customContent') is not None:
            self.custom_content = m.get('customContent')

        return self

class ListAICoachScriptPageResponseBodyListCompleteStrategy(DaraModel):
    def __init__(
        self,
        click_complete_auto_end: bool = None,
        duration: int = None,
        full_coverage_auto_end: bool = None,
    ):
        self.click_complete_auto_end = click_complete_auto_end
        self.duration = duration
        self.full_coverage_auto_end = full_coverage_auto_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.click_complete_auto_end is not None:
            result['clickCompleteAutoEnd'] = self.click_complete_auto_end

        if self.duration is not None:
            result['duration'] = self.duration

        if self.full_coverage_auto_end is not None:
            result['fullCoverageAutoEnd'] = self.full_coverage_auto_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clickCompleteAutoEnd') is not None:
            self.click_complete_auto_end = m.get('clickCompleteAutoEnd')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('fullCoverageAutoEnd') is not None:
            self.full_coverage_auto_end = m.get('fullCoverageAutoEnd')

        return self

