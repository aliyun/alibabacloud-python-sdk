# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetRuleDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRuleDetailResponseBodyData = None,
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
            temp_model = main_models.GetRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRuleDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        conditions: main_models.GetRuleDetailResponseBodyDataConditions = None,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        rules: main_models.GetRuleDetailResponseBodyDataRules = None,
    ):
        self.conditions = conditions
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.rules = rules

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()

        if self.count is not None:
            result['Count'] = self.count

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditions()
            self.conditions = temp_model.from_map(m.get('Conditions'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Rules') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class GetRuleDetailResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        rule_basic_info: List[main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfo] = None,
    ):
        self.rule_basic_info = rule_basic_info

    def validate(self):
        if self.rule_basic_info:
            for v1 in self.rule_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RuleBasicInfo'] = []
        if self.rule_basic_info is not None:
            for k1 in self.rule_basic_info:
                result['RuleBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_basic_info = []
        if m.get('RuleBasicInfo') is not None:
            for k1 in m.get('RuleBasicInfo'):
                temp_model = main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k1))

        return self

class GetRuleDetailResponseBodyDataRulesRuleBasicInfo(DaraModel):
    def __init__(
        self,
        business_categories: main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories = None,
        rid: str = None,
        rule_lambda: str = None,
        triggers: main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers = None,
    ):
        self.business_categories = business_categories
        self.rid = rid
        self.rule_lambda = rule_lambda
        self.triggers = triggers

    def validate(self):
        if self.business_categories:
            self.business_categories.validate()
        if self.triggers:
            self.triggers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_categories is not None:
            result['BusinessCategories'] = self.business_categories.to_map()

        if self.rid is not None:
            result['Rid'] = self.rid

        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda

        if self.triggers is not None:
            result['Triggers'] = self.triggers.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessCategories') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories()
            self.business_categories = temp_model.from_map(m.get('BusinessCategories'))

        if m.get('Rid') is not None:
            self.rid = m.get('Rid')

        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')

        if m.get('Triggers') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers()
            self.triggers = temp_model.from_map(m.get('Triggers'))

        return self

class GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers(DaraModel):
    def __init__(
        self,
        trigger: List[str] = None,
    ):
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trigger is not None:
            result['Trigger'] = self.trigger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        return self

class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories(DaraModel):
    def __init__(
        self,
        business_category_basic_info: List[main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo] = None,
    ):
        self.business_category_basic_info = business_category_basic_info

    def validate(self):
        if self.business_category_basic_info:
            for v1 in self.business_category_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BusinessCategoryBasicInfo'] = []
        if self.business_category_basic_info is not None:
            for k1 in self.business_category_basic_info:
                result['BusinessCategoryBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business_category_basic_info = []
        if m.get('BusinessCategoryBasicInfo') is not None:
            for k1 in m.get('BusinessCategoryBasicInfo'):
                temp_model = main_models.GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo()
                self.business_category_basic_info.append(temp_model.from_map(k1))

        return self

class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo(DaraModel):
    def __init__(
        self,
        bid: int = None,
        business_name: str = None,
        service_type: int = None,
    ):
        self.bid = bid
        self.business_name = business_name
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

class GetRuleDetailResponseBodyDataConditions(DaraModel):
    def __init__(
        self,
        condition_basic_info: List[main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfo] = None,
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
                temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k1))

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfo(DaraModel):
    def __init__(
        self,
        check_range: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange = None,
        condition_info_cid: str = None,
        oper_lambda: str = None,
        operators: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators = None,
    ):
        self.check_range = check_range
        self.condition_info_cid = condition_info_cid
        self.oper_lambda = oper_lambda
        self.operators = operators

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            self.operators.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_range is not None:
            result['CheckRange'] = self.check_range.to_map()

        if self.condition_info_cid is not None:
            result['ConditionInfoCid'] = self.condition_info_cid

        if self.oper_lambda is not None:
            result['OperLambda'] = self.oper_lambda

        if self.operators is not None:
            result['Operators'] = self.operators.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRange') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m.get('CheckRange'))

        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')

        if m.get('OperLambda') is not None:
            self.oper_lambda = m.get('OperLambda')

        if m.get('Operators') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators()
            self.operators = temp_model.from_map(m.get('Operators'))

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators(DaraModel):
    def __init__(
        self,
        operator_basic_info: List[main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo] = None,
    ):
        self.operator_basic_info = operator_basic_info

    def validate(self):
        if self.operator_basic_info:
            for v1 in self.operator_basic_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperatorBasicInfo'] = []
        if self.operator_basic_info is not None:
            for k1 in self.operator_basic_info:
                result['OperatorBasicInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator_basic_info = []
        if m.get('OperatorBasicInfo') is not None:
            for k1 in m.get('OperatorBasicInfo'):
                temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo()
                self.operator_basic_info.append(temp_model.from_map(k1))

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo(DaraModel):
    def __init__(
        self,
        oid: str = None,
        oper_name: str = None,
        param: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam = None,
        type: str = None,
    ):
        self.oid = oid
        self.oper_name = oper_name
        self.param = param
        self.type = type

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oid is not None:
            result['Oid'] = self.oid

        if self.oper_name is not None:
            result['OperName'] = self.oper_name

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oid') is not None:
            self.oid = m.get('Oid')

        if m.get('OperName') is not None:
            self.oper_name = m.get('OperName')

        if m.get('Param') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam(DaraModel):
    def __init__(
        self,
        ant_model_info: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo = None,
        average: bool = None,
        begin_type: str = None,
        check_type: int = None,
        compare_operator: str = None,
        context_chat_match: bool = None,
        delay_time: int = None,
        different_role: bool = None,
        excludes: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes = None,
        from_: int = None,
        from_end: bool = None,
        hit_time: int = None,
        in_sentence: bool = None,
        interval: int = None,
        keyword_extension: bool = None,
        keyword_match_size: int = None,
        max_emotion_change_value: int = None,
        min_word_size: int = None,
        not_regex: str = None,
        oper_key_words: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords = None,
        phrase: str = None,
        pvalues: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues = None,
        references: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences = None,
        regex: str = None,
        score: int = None,
        similarity_threshold: float = None,
        similarly_sentences: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences = None,
        target: int = None,
        target_role: str = None,
        threshold: float = None,
        velocity_in_mint: int = None,
    ):
        self.ant_model_info = ant_model_info
        self.average = average
        self.begin_type = begin_type
        self.check_type = check_type
        self.compare_operator = compare_operator
        self.context_chat_match = context_chat_match
        self.delay_time = delay_time
        self.different_role = different_role
        self.excludes = excludes
        self.from_ = from_
        self.from_end = from_end
        self.hit_time = hit_time
        self.in_sentence = in_sentence
        self.interval = interval
        self.keyword_extension = keyword_extension
        self.keyword_match_size = keyword_match_size
        self.max_emotion_change_value = max_emotion_change_value
        self.min_word_size = min_word_size
        self.not_regex = not_regex
        self.oper_key_words = oper_key_words
        self.phrase = phrase
        self.pvalues = pvalues
        self.references = references
        self.regex = regex
        self.score = score
        self.similarity_threshold = similarity_threshold
        self.similarly_sentences = similarly_sentences
        self.target = target
        self.target_role = target_role
        self.threshold = threshold
        self.velocity_in_mint = velocity_in_mint

    def validate(self):
        if self.ant_model_info:
            self.ant_model_info.validate()
        if self.excludes:
            self.excludes.validate()
        if self.oper_key_words:
            self.oper_key_words.validate()
        if self.pvalues:
            self.pvalues.validate()
        if self.references:
            self.references.validate()
        if self.similarly_sentences:
            self.similarly_sentences.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ant_model_info is not None:
            result['AntModelInfo'] = self.ant_model_info.to_map()

        if self.average is not None:
            result['Average'] = self.average

        if self.begin_type is not None:
            result['BeginType'] = self.begin_type

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.compare_operator is not None:
            result['CompareOperator'] = self.compare_operator

        if self.context_chat_match is not None:
            result['ContextChatMatch'] = self.context_chat_match

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.different_role is not None:
            result['DifferentRole'] = self.different_role

        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()

        if self.from_ is not None:
            result['From'] = self.from_

        if self.from_end is not None:
            result['FromEnd'] = self.from_end

        if self.hit_time is not None:
            result['HitTime'] = self.hit_time

        if self.in_sentence is not None:
            result['InSentence'] = self.in_sentence

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.keyword_extension is not None:
            result['KeywordExtension'] = self.keyword_extension

        if self.keyword_match_size is not None:
            result['KeywordMatchSize'] = self.keyword_match_size

        if self.max_emotion_change_value is not None:
            result['MaxEmotionChangeValue'] = self.max_emotion_change_value

        if self.min_word_size is not None:
            result['MinWordSize'] = self.min_word_size

        if self.not_regex is not None:
            result['NotRegex'] = self.not_regex

        if self.oper_key_words is not None:
            result['OperKeyWords'] = self.oper_key_words.to_map()

        if self.phrase is not None:
            result['Phrase'] = self.phrase

        if self.pvalues is not None:
            result['Pvalues'] = self.pvalues.to_map()

        if self.references is not None:
            result['References'] = self.references.to_map()

        if self.regex is not None:
            result['Regex'] = self.regex

        if self.score is not None:
            result['Score'] = self.score

        if self.similarity_threshold is not None:
            result['Similarity_threshold'] = self.similarity_threshold

        if self.similarly_sentences is not None:
            result['SimilarlySentences'] = self.similarly_sentences.to_map()

        if self.target is not None:
            result['Target'] = self.target

        if self.target_role is not None:
            result['TargetRole'] = self.target_role

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.velocity_in_mint is not None:
            result['VelocityInMint'] = self.velocity_in_mint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntModelInfo') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo()
            self.ant_model_info = temp_model.from_map(m.get('AntModelInfo'))

        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('BeginType') is not None:
            self.begin_type = m.get('BeginType')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CompareOperator') is not None:
            self.compare_operator = m.get('CompareOperator')

        if m.get('ContextChatMatch') is not None:
            self.context_chat_match = m.get('ContextChatMatch')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DifferentRole') is not None:
            self.different_role = m.get('DifferentRole')

        if m.get('Excludes') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes()
            self.excludes = temp_model.from_map(m.get('Excludes'))

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('FromEnd') is not None:
            self.from_end = m.get('FromEnd')

        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')

        if m.get('InSentence') is not None:
            self.in_sentence = m.get('InSentence')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('KeywordExtension') is not None:
            self.keyword_extension = m.get('KeywordExtension')

        if m.get('KeywordMatchSize') is not None:
            self.keyword_match_size = m.get('KeywordMatchSize')

        if m.get('MaxEmotionChangeValue') is not None:
            self.max_emotion_change_value = m.get('MaxEmotionChangeValue')

        if m.get('MinWordSize') is not None:
            self.min_word_size = m.get('MinWordSize')

        if m.get('NotRegex') is not None:
            self.not_regex = m.get('NotRegex')

        if m.get('OperKeyWords') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords()
            self.oper_key_words = temp_model.from_map(m.get('OperKeyWords'))

        if m.get('Phrase') is not None:
            self.phrase = m.get('Phrase')

        if m.get('Pvalues') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues()
            self.pvalues = temp_model.from_map(m.get('Pvalues'))

        if m.get('References') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences()
            self.references = temp_model.from_map(m.get('References'))

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Similarity_threshold') is not None:
            self.similarity_threshold = m.get('Similarity_threshold')

        if m.get('SimilarlySentences') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences()
            self.similarly_sentences = temp_model.from_map(m.get('SimilarlySentences'))

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('VelocityInMint') is not None:
            self.velocity_in_mint = m.get('VelocityInMint')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences(DaraModel):
    def __init__(
        self,
        similarly_sentence: List[str] = None,
    ):
        self.similarly_sentence = similarly_sentence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.similarly_sentence is not None:
            result['SimilarlySentence'] = self.similarly_sentence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimilarlySentence') is not None:
            self.similarly_sentence = m.get('SimilarlySentence')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences(DaraModel):
    def __init__(
        self,
        reference: List[str] = None,
    ):
        self.reference = reference

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference is not None:
            result['Reference'] = self.reference

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues(DaraModel):
    def __init__(
        self,
        pvalues: List[str] = None,
    ):
        self.pvalues = pvalues

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pvalues is not None:
            result['Pvalues'] = self.pvalues

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pvalues') is not None:
            self.pvalues = m.get('Pvalues')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords(DaraModel):
    def __init__(
        self,
        oper_key_word: List[str] = None,
    ):
        self.oper_key_word = oper_key_word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oper_key_word is not None:
            result['OperKeyWord'] = self.oper_key_word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperKeyWord') is not None:
            self.oper_key_word = m.get('OperKeyWord')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes(DaraModel):
    def __init__(
        self,
        excludes: List[str] = None,
    ):
        self.excludes = excludes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.excludes is not None:
            result['Excludes'] = self.excludes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo(DaraModel):
    def __init__(
        self,
        ant_model_info: List[str] = None,
    ):
        self.ant_model_info = ant_model_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ant_model_info is not None:
            result['AntModelInfo'] = self.ant_model_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntModelInfo') is not None:
            self.ant_model_info = m.get('AntModelInfo')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange(DaraModel):
    def __init__(
        self,
        absolute: bool = None,
        anchor: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor = None,
        range: main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange = None,
        role: str = None,
    ):
        self.absolute = absolute
        self.anchor = anchor
        self.range = range
        self.role = role

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.absolute is not None:
            result['Absolute'] = self.absolute

        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()

        if self.range is not None:
            result['Range'] = self.range.to_map()

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')

        if m.get('Anchor') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m.get('Anchor'))

        if m.get('Range') is not None:
            temp_model = main_models.GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m.get('Range'))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor(DaraModel):
    def __init__(
        self,
        anchor_cid: str = None,
        hit_time: int = None,
        location: str = None,
    ):
        self.anchor_cid = anchor_cid
        self.hit_time = hit_time
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_cid is not None:
            result['AnchorCid'] = self.anchor_cid

        if self.hit_time is not None:
            result['HitTime'] = self.hit_time

        if self.location is not None:
            result['Location'] = self.location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorCid') is not None:
            self.anchor_cid = m.get('AnchorCid')

        if m.get('HitTime') is not None:
            self.hit_time = m.get('HitTime')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        return self

