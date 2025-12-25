# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class OperatorBasicInfo(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        oid: str = None,
        param: main_models.OperatorBasicInfoParam = None,
        quality_check_type: int = None,
        type: str = None,
        user_group: str = None,
    ):
        self.id = id
        self.name = name
        self.oid = oid
        self.param = param
        self.quality_check_type = quality_check_type
        self.type = type
        self.user_group = user_group

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.oid is not None:
            result['Oid'] = self.oid

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type

        if self.type is not None:
            result['Type'] = self.type

        if self.user_group is not None:
            result['UserGroup'] = self.user_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Oid') is not None:
            self.oid = m.get('Oid')

        if m.get('Param') is not None:
            temp_model = main_models.OperatorBasicInfoParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')

        return self

class OperatorBasicInfoParam(DaraModel):
    def __init__(
        self,
        answer_threshold: str = None,
        ant_model_info: Dict[str, str] = None,
        average: bool = None,
        begin_type: str = None,
        bot_id: str = None,
        case_sensitive: bool = None,
        category_path_code: str = None,
        check_first_sentence: bool = None,
        check_type: int = None,
        compare_operator: str = None,
        context_chat_match: bool = None,
        customer_param: main_models.JudgeNodeMetaDesc = None,
        delay_time: int = None,
        different_role: bool = None,
        end_type: str = None,
        excludes: List[str] = None,
        from_: int = None,
        from_end: bool = None,
        hit_time: int = None,
        in_sentence: bool = None,
        interval: int = None,
        interval_end: int = None,
        keyword_extension: int = None,
        keyword_match_size: int = None,
        keywords: List[str] = None,
        knowledge_info: str = None,
        knowledge_sentence_num: int = None,
        knowledge_target_id: str = None,
        knowledge_target_name: str = None,
        knowledge_target_type: int = None,
        lgf_sentences: List[str] = None,
        max_emotion_change_value: int = None,
        min_word_size: int = None,
        near_dialogue: bool = None,
        not_regex: str = None,
        phrase: str = None,
        pkey: str = None,
        poutput_type: int = None,
        pvalues: List[str] = None,
        question_threshold: str = None,
        references: List[str] = None,
        regex: str = None,
        role_id: int = None,
        score: int = None,
        similarity_threshold: float = None,
        similarly_sentences: List[str] = None,
        synonyms: Dict[str, List[str]] = None,
        target: int = None,
        target_role: str = None,
        threshold: float = None,
        use_eas_algorithm: bool = None,
        velocity: float = None,
        velocity_in_mint: int = None,
    ):
        self.answer_threshold = answer_threshold
        self.ant_model_info = ant_model_info
        self.average = average
        self.begin_type = begin_type
        self.bot_id = bot_id
        self.case_sensitive = case_sensitive
        self.category_path_code = category_path_code
        self.check_first_sentence = check_first_sentence
        self.check_type = check_type
        self.compare_operator = compare_operator
        self.context_chat_match = context_chat_match
        self.customer_param = customer_param
        self.delay_time = delay_time
        self.different_role = different_role
        self.end_type = end_type
        self.excludes = excludes
        self.from_ = from_
        self.from_end = from_end
        self.hit_time = hit_time
        self.in_sentence = in_sentence
        self.interval = interval
        self.interval_end = interval_end
        self.keyword_extension = keyword_extension
        self.keyword_match_size = keyword_match_size
        self.keywords = keywords
        self.knowledge_info = knowledge_info
        self.knowledge_sentence_num = knowledge_sentence_num
        self.knowledge_target_id = knowledge_target_id
        self.knowledge_target_name = knowledge_target_name
        self.knowledge_target_type = knowledge_target_type
        self.lgf_sentences = lgf_sentences
        self.max_emotion_change_value = max_emotion_change_value
        self.min_word_size = min_word_size
        self.near_dialogue = near_dialogue
        self.not_regex = not_regex
        self.phrase = phrase
        self.pkey = pkey
        self.poutput_type = poutput_type
        self.pvalues = pvalues
        self.question_threshold = question_threshold
        self.references = references
        self.regex = regex
        self.role_id = role_id
        self.score = score
        self.similarity_threshold = similarity_threshold
        self.similarly_sentences = similarly_sentences
        self.synonyms = synonyms
        self.target = target
        self.target_role = target_role
        self.threshold = threshold
        self.use_eas_algorithm = use_eas_algorithm
        self.velocity = velocity
        self.velocity_in_mint = velocity_in_mint

    def validate(self):
        if self.customer_param:
            self.customer_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_threshold is not None:
            result['AnswerThreshold'] = self.answer_threshold

        if self.ant_model_info is not None:
            result['AntModelInfo'] = self.ant_model_info

        if self.average is not None:
            result['Average'] = self.average

        if self.begin_type is not None:
            result['BeginType'] = self.begin_type

        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.case_sensitive is not None:
            result['Case_sensitive'] = self.case_sensitive

        if self.category_path_code is not None:
            result['CategoryPathCode'] = self.category_path_code

        if self.check_first_sentence is not None:
            result['CheckFirstSentence'] = self.check_first_sentence

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.compare_operator is not None:
            result['CompareOperator'] = self.compare_operator

        if self.context_chat_match is not None:
            result['ContextChatMatch'] = self.context_chat_match

        if self.customer_param is not None:
            result['CustomerParam'] = self.customer_param.to_map()

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.different_role is not None:
            result['Different_role'] = self.different_role

        if self.end_type is not None:
            result['EndType'] = self.end_type

        if self.excludes is not None:
            result['Excludes'] = self.excludes

        if self.from_ is not None:
            result['From'] = self.from_

        if self.from_end is not None:
            result['From_end'] = self.from_end

        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time

        if self.in_sentence is not None:
            result['In_sentence'] = self.in_sentence

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.interval_end is not None:
            result['IntervalEnd'] = self.interval_end

        if self.keyword_extension is not None:
            result['KeywordExtension'] = self.keyword_extension

        if self.keyword_match_size is not None:
            result['KeywordMatchSize'] = self.keyword_match_size

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.knowledge_info is not None:
            result['KnowledgeInfo'] = self.knowledge_info

        if self.knowledge_sentence_num is not None:
            result['KnowledgeSentenceNum'] = self.knowledge_sentence_num

        if self.knowledge_target_id is not None:
            result['KnowledgeTargetId'] = self.knowledge_target_id

        if self.knowledge_target_name is not None:
            result['KnowledgeTargetName'] = self.knowledge_target_name

        if self.knowledge_target_type is not None:
            result['KnowledgeTargetType'] = self.knowledge_target_type

        if self.lgf_sentences is not None:
            result['LgfSentences'] = self.lgf_sentences

        if self.max_emotion_change_value is not None:
            result['MaxEmotionChangeValue'] = self.max_emotion_change_value

        if self.min_word_size is not None:
            result['MinWordSize'] = self.min_word_size

        if self.near_dialogue is not None:
            result['Near_dialogue'] = self.near_dialogue

        if self.not_regex is not None:
            result['NotRegex'] = self.not_regex

        if self.phrase is not None:
            result['Phrase'] = self.phrase

        if self.pkey is not None:
            result['Pkey'] = self.pkey

        if self.poutput_type is not None:
            result['Poutput_type'] = self.poutput_type

        if self.pvalues is not None:
            result['Pvalues'] = self.pvalues

        if self.question_threshold is not None:
            result['QuestionThreshold'] = self.question_threshold

        if self.references is not None:
            result['References'] = self.references

        if self.regex is not None:
            result['Regex'] = self.regex

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.score is not None:
            result['Score'] = self.score

        if self.similarity_threshold is not None:
            result['Similarity_threshold'] = self.similarity_threshold

        if self.similarly_sentences is not None:
            result['SimilarlySentences'] = self.similarly_sentences

        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms

        if self.target is not None:
            result['Target'] = self.target

        if self.target_role is not None:
            result['Target_role'] = self.target_role

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.use_eas_algorithm is not None:
            result['UseEasAlgorithm'] = self.use_eas_algorithm

        if self.velocity is not None:
            result['Velocity'] = self.velocity

        if self.velocity_in_mint is not None:
            result['VelocityInMint'] = self.velocity_in_mint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerThreshold') is not None:
            self.answer_threshold = m.get('AnswerThreshold')

        if m.get('AntModelInfo') is not None:
            self.ant_model_info = m.get('AntModelInfo')

        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('BeginType') is not None:
            self.begin_type = m.get('BeginType')

        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('Case_sensitive') is not None:
            self.case_sensitive = m.get('Case_sensitive')

        if m.get('CategoryPathCode') is not None:
            self.category_path_code = m.get('CategoryPathCode')

        if m.get('CheckFirstSentence') is not None:
            self.check_first_sentence = m.get('CheckFirstSentence')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CompareOperator') is not None:
            self.compare_operator = m.get('CompareOperator')

        if m.get('ContextChatMatch') is not None:
            self.context_chat_match = m.get('ContextChatMatch')

        if m.get('CustomerParam') is not None:
            temp_model = main_models.JudgeNodeMetaDesc()
            self.customer_param = temp_model.from_map(m.get('CustomerParam'))

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('Different_role') is not None:
            self.different_role = m.get('Different_role')

        if m.get('EndType') is not None:
            self.end_type = m.get('EndType')

        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('From_end') is not None:
            self.from_end = m.get('From_end')

        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')

        if m.get('In_sentence') is not None:
            self.in_sentence = m.get('In_sentence')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IntervalEnd') is not None:
            self.interval_end = m.get('IntervalEnd')

        if m.get('KeywordExtension') is not None:
            self.keyword_extension = m.get('KeywordExtension')

        if m.get('KeywordMatchSize') is not None:
            self.keyword_match_size = m.get('KeywordMatchSize')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('KnowledgeInfo') is not None:
            self.knowledge_info = m.get('KnowledgeInfo')

        if m.get('KnowledgeSentenceNum') is not None:
            self.knowledge_sentence_num = m.get('KnowledgeSentenceNum')

        if m.get('KnowledgeTargetId') is not None:
            self.knowledge_target_id = m.get('KnowledgeTargetId')

        if m.get('KnowledgeTargetName') is not None:
            self.knowledge_target_name = m.get('KnowledgeTargetName')

        if m.get('KnowledgeTargetType') is not None:
            self.knowledge_target_type = m.get('KnowledgeTargetType')

        if m.get('LgfSentences') is not None:
            self.lgf_sentences = m.get('LgfSentences')

        if m.get('MaxEmotionChangeValue') is not None:
            self.max_emotion_change_value = m.get('MaxEmotionChangeValue')

        if m.get('MinWordSize') is not None:
            self.min_word_size = m.get('MinWordSize')

        if m.get('Near_dialogue') is not None:
            self.near_dialogue = m.get('Near_dialogue')

        if m.get('NotRegex') is not None:
            self.not_regex = m.get('NotRegex')

        if m.get('Phrase') is not None:
            self.phrase = m.get('Phrase')

        if m.get('Pkey') is not None:
            self.pkey = m.get('Pkey')

        if m.get('Poutput_type') is not None:
            self.poutput_type = m.get('Poutput_type')

        if m.get('Pvalues') is not None:
            self.pvalues = m.get('Pvalues')

        if m.get('QuestionThreshold') is not None:
            self.question_threshold = m.get('QuestionThreshold')

        if m.get('References') is not None:
            self.references = m.get('References')

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Similarity_threshold') is not None:
            self.similarity_threshold = m.get('Similarity_threshold')

        if m.get('SimilarlySentences') is not None:
            self.similarly_sentences = m.get('SimilarlySentences')

        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Target_role') is not None:
            self.target_role = m.get('Target_role')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('UseEasAlgorithm') is not None:
            self.use_eas_algorithm = m.get('UseEasAlgorithm')

        if m.get('Velocity') is not None:
            self.velocity = m.get('Velocity')

        if m.get('VelocityInMint') is not None:
            self.velocity_in_mint = m.get('VelocityInMint')

        return self

