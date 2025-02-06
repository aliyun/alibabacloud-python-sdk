# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class BusinessCategoryBasicInfo(TeaModel):
    def __init__(
        self,
        bid: int = None,
        name: str = None,
        original_id: int = None,
        service_type: int = None,
    ):
        self.bid = bid
        self.name = name
        self.original_id = original_id
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.name is not None:
            result['Name'] = self.name
        if self.original_id is not None:
            result['OriginalId'] = self.original_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ConditionBasicInfoCheckRangeAnchor(TeaModel):
    def __init__(
        self,
        cid: str = None,
        hit_time: int = None,
        location: str = None,
    ):
        self.cid = cid
        self.hit_time = hit_time
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ConditionBasicInfoCheckRangeRange(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ConditionBasicInfoCheckRange(TeaModel):
    def __init__(
        self,
        absolute: bool = None,
        all_sentences_satisfy: bool = None,
        anchor: ConditionBasicInfoCheckRangeAnchor = None,
        range: ConditionBasicInfoCheckRangeRange = None,
        role: str = None,
        role_id: int = None,
    ):
        self.absolute = absolute
        self.all_sentences_satisfy = all_sentences_satisfy
        self.anchor = anchor
        self.range = range
        self.role = role
        self.role_id = role_id

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.absolute is not None:
            result['Absolute'] = self.absolute
        if self.all_sentences_satisfy is not None:
            result['AllSentencesSatisfy'] = self.all_sentences_satisfy
        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()
        if self.range is not None:
            result['Range'] = self.range.to_map()
        if self.role is not None:
            result['Role'] = self.role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')
        if m.get('AllSentencesSatisfy') is not None:
            self.all_sentences_satisfy = m.get('AllSentencesSatisfy')
        if m.get('Anchor') is not None:
            temp_model = ConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m['Anchor'])
        if m.get('Range') is not None:
            temp_model = ConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class JudgeNodeMetaDesc(TeaModel):
    def __init__(
        self,
        actual_value: str = None,
        data_type: int = None,
        field: str = None,
        field_type: int = None,
        symbol: int = None,
        value: str = None,
    ):
        self.actual_value = actual_value
        self.data_type = data_type
        self.field = field
        self.field_type = field_type
        self.symbol = symbol
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.field is not None:
            result['Field'] = self.field
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OperatorBasicInfoParam(TeaModel):
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
        customer_param: JudgeNodeMetaDesc = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = JudgeNodeMetaDesc()
            self.customer_param = temp_model.from_map(m['CustomerParam'])
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


class OperatorBasicInfo(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        oid: str = None,
        param: OperatorBasicInfoParam = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = OperatorBasicInfoParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        return self


class ConditionBasicInfo(TeaModel):
    def __init__(
        self,
        check_range: ConditionBasicInfoCheckRange = None,
        cid: str = None,
        exclusion: int = None,
        id: int = None,
        lambda_: str = None,
        name: str = None,
        operators: List[OperatorBasicInfo] = None,
        rid: str = None,
        user_group: str = None,
    ):
        self.check_range = check_range
        self.cid = cid
        self.exclusion = exclusion
        self.id = id
        self.lambda_ = lambda_
        self.name = name
        self.operators = operators
        self.rid = rid
        self.user_group = user_group

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            for k in self.operators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_range is not None:
            result['Check_range'] = self.check_range.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.exclusion is not None:
            result['Exclusion'] = self.exclusion
        if self.id is not None:
            result['Id'] = self.id
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.name is not None:
            result['Name'] = self.name
        result['Operators'] = []
        if self.operators is not None:
            for k in self.operators:
                result['Operators'].append(k.to_map() if k else None)
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.user_group is not None:
            result['UserGroup'] = self.user_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check_range') is not None:
            temp_model = ConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m['Check_range'])
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Exclusion') is not None:
            self.exclusion = m.get('Exclusion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.operators = []
        if m.get('Operators') is not None:
            for k in m.get('Operators'):
                temp_model = OperatorBasicInfo()
                self.operators.append(temp_model.from_map(k))
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        return self


class GraphFlowNodeNextNodes(TeaModel):
    def __init__(
        self,
        check_type: int = None,
        index: int = None,
        lambda_: str = None,
        name: str = None,
        next_node_id: int = None,
        triggers: List[str] = None,
    ):
        self.check_type = check_type
        self.index = index
        self.lambda_ = lambda_
        self.name = name
        self.next_node_id = next_node_id
        self.triggers = triggers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')
        return self


class GraphFlowNodeProperties(TeaModel):
    def __init__(
        self,
        auto_review: int = None,
        branch_judge: bool = None,
        check_more_size: int = None,
        check_type: int = None,
        lambda_: str = None,
        role: str = None,
        rule_score_type: int = None,
        say_type: str = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_type: int = None,
        triggers: List[str] = None,
        type: str = None,
    ):
        self.auto_review = auto_review
        self.branch_judge = branch_judge
        self.check_more_size = check_more_size
        self.check_type = check_type
        self.lambda_ = lambda_
        self.role = role
        self.rule_score_type = rule_score_type
        self.say_type = say_type
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_rule_hit_type = score_rule_hit_type
        self.score_type = score_type
        self.triggers = triggers
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.branch_judge is not None:
            result['BranchJudge'] = self.branch_judge
        if self.check_more_size is not None:
            result['CheckMoreSize'] = self.check_more_size
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.role is not None:
            result['Role'] = self.role
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.say_type is not None:
            result['SayType'] = self.say_type
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type
        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.triggers is not None:
            result['Triggers'] = self.triggers
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('BranchJudge') is not None:
            self.branch_judge = m.get('BranchJudge')
        if m.get('CheckMoreSize') is not None:
            self.check_more_size = m.get('CheckMoreSize')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('SayType') is not None:
            self.say_type = m.get('SayType')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')
        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GraphFlowNode(TeaModel):
    def __init__(
        self,
        conditions: List[ConditionBasicInfo] = None,
        content: str = None,
        id: int = None,
        index: int = None,
        name: str = None,
        next_nodes: List[GraphFlowNodeNextNodes] = None,
        node_type: str = None,
        properties: GraphFlowNodeProperties = None,
        rid: int = None,
        use_conditions: bool = None,
    ):
        self.conditions = conditions
        self.content = content
        self.id = id
        self.index = index
        self.name = name
        self.next_nodes = next_nodes
        self.node_type = node_type
        self.properties = properties
        self.rid = rid
        self.use_conditions = use_conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.next_nodes:
            for k in self.next_nodes:
                if k:
                    k.validate()
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.index is not None:
            result['Index'] = self.index
        if self.name is not None:
            result['Name'] = self.name
        result['NextNodes'] = []
        if self.next_nodes is not None:
            for k in self.next_nodes:
                result['NextNodes'].append(k.to_map() if k else None)
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.use_conditions is not None:
            result['UseConditions'] = self.use_conditions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = ConditionBasicInfo()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.next_nodes = []
        if m.get('NextNodes') is not None:
            for k in m.get('NextNodes'):
                temp_model = GraphFlowNodeNextNodes()
                self.next_nodes.append(temp_model.from_map(k))
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Properties') is not None:
            temp_model = GraphFlowNodeProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('UseConditions') is not None:
            self.use_conditions = m.get('UseConditions')
        return self


class NextNodeSituationsConditionGroup(TeaModel):
    def __init__(
        self,
        conditions: List[JudgeNodeMetaDesc] = None,
        type: str = None,
    ):
        self.conditions = conditions
        self.type = type

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = JudgeNodeMetaDesc()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class NextNodeSituations(TeaModel):
    def __init__(
        self,
        condition_group: List[NextNodeSituationsConditionGroup] = None,
        type: str = None,
    ):
        self.condition_group = condition_group
        self.type = type

    def validate(self):
        if self.condition_group:
            for k in self.condition_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionGroup'] = []
        if self.condition_group is not None:
            for k in self.condition_group:
                result['ConditionGroup'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_group = []
        if m.get('ConditionGroup') is not None:
            for k in m.get('ConditionGroup'):
                temp_model = NextNodeSituationsConditionGroup()
                self.condition_group.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RuleCountInfo(TeaModel):
    def __init__(
        self,
        auto_review: int = None,
        business_category_basic_info_list: List[BusinessCategoryBasicInfo] = None,
        business_category_name_list: List[str] = None,
        business_range: List[int] = None,
        check_number: int = None,
        comments: str = None,
        create_emp_name: str = None,
        create_empid: str = None,
        create_time: str = None,
        deny: int = None,
        effective: int = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        end_time: str = None,
        full_cycle: int = None,
        graph_flow: Any = None,
        hit_number: int = None,
        hit_rate: float = None,
        hit_real_violation_rate: float = None,
        is_delete: int = None,
        is_select: bool = None,
        job_name: str = None,
        last_update_emp_name: str = None,
        last_update_empid: str = None,
        last_update_time: str = None,
        name: str = None,
        operation_mode: int = None,
        pre_review_number: int = None,
        problem_number: int = None,
        quality_check_type: int = None,
        real_violation_number: int = None,
        review_accuracy_rate: float = None,
        review_number: int = None,
        review_rate: float = None,
        review_status_name: str = None,
        rid: int = None,
        rule_score_single_type: int = None,
        rule_score_type: int = None,
        rule_type: int = None,
        score_sub_id: int = None,
        start_time: str = None,
        status: int = None,
        target_type: int = None,
        type: int = None,
        type_name: str = None,
        un_review_number: int = None,
        user_group: str = None,
    ):
        self.auto_review = auto_review
        self.business_category_basic_info_list = business_category_basic_info_list
        self.business_category_name_list = business_category_name_list
        self.business_range = business_range
        self.check_number = check_number
        self.comments = comments
        self.create_emp_name = create_emp_name
        self.create_empid = create_empid
        self.create_time = create_time
        self.deny = deny
        self.effective = effective
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.end_time = end_time
        self.full_cycle = full_cycle
        self.graph_flow = graph_flow
        self.hit_number = hit_number
        self.hit_rate = hit_rate
        self.hit_real_violation_rate = hit_real_violation_rate
        self.is_delete = is_delete
        self.is_select = is_select
        self.job_name = job_name
        self.last_update_emp_name = last_update_emp_name
        self.last_update_empid = last_update_empid
        self.last_update_time = last_update_time
        self.name = name
        self.operation_mode = operation_mode
        self.pre_review_number = pre_review_number
        self.problem_number = problem_number
        self.quality_check_type = quality_check_type
        self.real_violation_number = real_violation_number
        self.review_accuracy_rate = review_accuracy_rate
        self.review_number = review_number
        self.review_rate = review_rate
        self.review_status_name = review_status_name
        self.rid = rid
        self.rule_score_single_type = rule_score_single_type
        self.rule_score_type = rule_score_type
        self.rule_type = rule_type
        self.score_sub_id = score_sub_id
        self.start_time = start_time
        self.status = status
        self.target_type = target_type
        self.type = type
        self.type_name = type_name
        self.un_review_number = un_review_number
        self.user_group = user_group

    def validate(self):
        if self.business_category_basic_info_list:
            for k in self.business_category_basic_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        result['BusinessCategoryBasicInfoList'] = []
        if self.business_category_basic_info_list is not None:
            for k in self.business_category_basic_info_list:
                result['BusinessCategoryBasicInfoList'].append(k.to_map() if k else None)
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        if self.business_range is not None:
            result['BusinessRange'] = self.business_range
        if self.check_number is not None:
            result['CheckNumber'] = self.check_number
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_emp_name is not None:
            result['CreateEmpName'] = self.create_emp_name
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deny is not None:
            result['Deny'] = self.deny
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.full_cycle is not None:
            result['FullCycle'] = self.full_cycle
        if self.graph_flow is not None:
            result['GraphFlow'] = self.graph_flow
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.hit_rate is not None:
            result['HitRate'] = self.hit_rate
        if self.hit_real_violation_rate is not None:
            result['HitRealViolationRate'] = self.hit_real_violation_rate
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.is_select is not None:
            result['IsSelect'] = self.is_select
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.last_update_emp_name is not None:
            result['LastUpdateEmpName'] = self.last_update_emp_name
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode
        if self.pre_review_number is not None:
            result['PreReviewNumber'] = self.pre_review_number
        if self.problem_number is not None:
            result['ProblemNumber'] = self.problem_number
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.real_violation_number is not None:
            result['RealViolationNumber'] = self.real_violation_number
        if self.review_accuracy_rate is not None:
            result['ReviewAccuracyRate'] = self.review_accuracy_rate
        if self.review_number is not None:
            result['ReviewNumber'] = self.review_number
        if self.review_rate is not None:
            result['ReviewRate'] = self.review_rate
        if self.review_status_name is not None:
            result['ReviewStatusName'] = self.review_status_name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_score_single_type is not None:
            result['RuleScoreSingleType'] = self.rule_score_single_type
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.un_review_number is not None:
            result['UnReviewNumber'] = self.un_review_number
        if self.user_group is not None:
            result['UserGroup'] = self.user_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        self.business_category_basic_info_list = []
        if m.get('BusinessCategoryBasicInfoList') is not None:
            for k in m.get('BusinessCategoryBasicInfoList'):
                temp_model = BusinessCategoryBasicInfo()
                self.business_category_basic_info_list.append(temp_model.from_map(k))
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        if m.get('BusinessRange') is not None:
            self.business_range = m.get('BusinessRange')
        if m.get('CheckNumber') is not None:
            self.check_number = m.get('CheckNumber')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateEmpName') is not None:
            self.create_emp_name = m.get('CreateEmpName')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deny') is not None:
            self.deny = m.get('Deny')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FullCycle') is not None:
            self.full_cycle = m.get('FullCycle')
        if m.get('GraphFlow') is not None:
            self.graph_flow = m.get('GraphFlow')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('HitRate') is not None:
            self.hit_rate = m.get('HitRate')
        if m.get('HitRealViolationRate') is not None:
            self.hit_real_violation_rate = m.get('HitRealViolationRate')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('IsSelect') is not None:
            self.is_select = m.get('IsSelect')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('LastUpdateEmpName') is not None:
            self.last_update_emp_name = m.get('LastUpdateEmpName')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')
        if m.get('PreReviewNumber') is not None:
            self.pre_review_number = m.get('PreReviewNumber')
        if m.get('ProblemNumber') is not None:
            self.problem_number = m.get('ProblemNumber')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('RealViolationNumber') is not None:
            self.real_violation_number = m.get('RealViolationNumber')
        if m.get('ReviewAccuracyRate') is not None:
            self.review_accuracy_rate = m.get('ReviewAccuracyRate')
        if m.get('ReviewNumber') is not None:
            self.review_number = m.get('ReviewNumber')
        if m.get('ReviewRate') is not None:
            self.review_rate = m.get('ReviewRate')
        if m.get('ReviewStatusName') is not None:
            self.review_status_name = m.get('ReviewStatusName')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleScoreSingleType') is not None:
            self.rule_score_single_type = m.get('RuleScoreSingleType')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UnReviewNumber') is not None:
            self.un_review_number = m.get('UnReviewNumber')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        return self


class RuleTestDialogueContent(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: int = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.role = role
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
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
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
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


class RuleTestDialogue(TeaModel):
    def __init__(
        self,
        content: List[RuleTestDialogueContent] = None,
        id: int = None,
        name: str = None,
        user_group: str = None,
    ):
        self.content = content
        self.id = id
        self.name = name
        self.user_group = user_group

    def validate(self):
        if self.content:
            for k in self.content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Content'] = []
        if self.content is not None:
            for k in self.content:
                result['Content'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.user_group is not None:
            result['UserGroup'] = self.user_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k in m.get('Content'):
                temp_model = RuleTestDialogueContent()
                self.content.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        return self


class SchemeCheckTypeSchemeScoreInfoList(TeaModel):
    def __init__(
        self,
        name: str = None,
        rid: int = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_type: int = None,
        task_flow_id: int = None,
        task_flow_name: str = None,
    ):
        self.name = name
        self.rid = rid
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_rule_hit_type = score_rule_hit_type
        self.score_type = score_type
        self.task_flow_id = task_flow_id
        self.task_flow_name = task_flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type
        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        if self.task_flow_name is not None:
            result['TaskFlowName'] = self.task_flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')
        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        if m.get('TaskFlowName') is not None:
            self.task_flow_name = m.get('TaskFlowName')
        return self


class SchemeCheckTypeTaskFlowScoreInfoListSchemeScoreInfoList(TeaModel):
    def __init__(
        self,
        name: str = None,
        rid: int = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_type: int = None,
        task_flow_id: int = None,
        task_flow_name: str = None,
    ):
        self.name = name
        self.rid = rid
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_rule_hit_type = score_rule_hit_type
        self.score_type = score_type
        self.task_flow_id = task_flow_id
        self.task_flow_name = task_flow_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type
        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        if self.task_flow_name is not None:
            result['TaskFlowName'] = self.task_flow_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')
        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        if m.get('TaskFlowName') is not None:
            self.task_flow_name = m.get('TaskFlowName')
        return self


class SchemeCheckTypeTaskFlowScoreInfoList(TeaModel):
    def __init__(
        self,
        scheme_score_info_list: List[SchemeCheckTypeTaskFlowScoreInfoListSchemeScoreInfoList] = None,
        task_flow_id: int = None,
        task_flow_name: str = None,
        task_flow_type: int = None,
    ):
        self.scheme_score_info_list = scheme_score_info_list
        self.task_flow_id = task_flow_id
        self.task_flow_name = task_flow_name
        self.task_flow_type = task_flow_type

    def validate(self):
        if self.scheme_score_info_list:
            for k in self.scheme_score_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SchemeScoreInfoList'] = []
        if self.scheme_score_info_list is not None:
            for k in self.scheme_score_info_list:
                result['SchemeScoreInfoList'].append(k.to_map() if k else None)
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        if self.task_flow_name is not None:
            result['TaskFlowName'] = self.task_flow_name
        if self.task_flow_type is not None:
            result['TaskFlowType'] = self.task_flow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheme_score_info_list = []
        if m.get('SchemeScoreInfoList') is not None:
            for k in m.get('SchemeScoreInfoList'):
                temp_model = SchemeCheckTypeTaskFlowScoreInfoListSchemeScoreInfoList()
                self.scheme_score_info_list.append(temp_model.from_map(k))
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        if m.get('TaskFlowName') is not None:
            self.task_flow_name = m.get('TaskFlowName')
        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')
        return self


class SchemeCheckType(TeaModel):
    def __init__(
        self,
        check_name: str = None,
        check_type: int = None,
        enable: int = None,
        scheme_id: int = None,
        scheme_score_info_list: List[SchemeCheckTypeSchemeScoreInfoList] = None,
        score: int = None,
        source_score: int = None,
        task_flow_score_info_list: List[SchemeCheckTypeTaskFlowScoreInfoList] = None,
    ):
        self.check_name = check_name
        self.check_type = check_type
        self.enable = enable
        self.scheme_id = scheme_id
        self.scheme_score_info_list = scheme_score_info_list
        self.score = score
        self.source_score = source_score
        self.task_flow_score_info_list = task_flow_score_info_list

    def validate(self):
        if self.scheme_score_info_list:
            for k in self.scheme_score_info_list:
                if k:
                    k.validate()
        if self.task_flow_score_info_list:
            for k in self.task_flow_score_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        result['SchemeScoreInfoList'] = []
        if self.scheme_score_info_list is not None:
            for k in self.scheme_score_info_list:
                result['SchemeScoreInfoList'].append(k.to_map() if k else None)
        if self.score is not None:
            result['Score'] = self.score
        if self.source_score is not None:
            result['SourceScore'] = self.source_score
        result['TaskFlowScoreInfoList'] = []
        if self.task_flow_score_info_list is not None:
            for k in self.task_flow_score_info_list:
                result['TaskFlowScoreInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        self.scheme_score_info_list = []
        if m.get('SchemeScoreInfoList') is not None:
            for k in m.get('SchemeScoreInfoList'):
                temp_model = SchemeCheckTypeSchemeScoreInfoList()
                self.scheme_score_info_list.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SourceScore') is not None:
            self.source_score = m.get('SourceScore')
        self.task_flow_score_info_list = []
        if m.get('TaskFlowScoreInfoList') is not None:
            for k in m.get('TaskFlowScoreInfoList'):
                temp_model = SchemeCheckTypeTaskFlowScoreInfoList()
                self.task_flow_score_info_list.append(temp_model.from_map(k))
        return self


class RuleInfo(TeaModel):
    def __init__(
        self,
        auto_review: int = None,
        business_category_name_list: List[str] = None,
        check_type: int = None,
        comments: str = None,
        config_type: int = None,
        create_emp_name: str = None,
        create_empid: str = None,
        create_time: str = None,
        deny: int = None,
        dialogues: List[RuleTestDialogue] = None,
        effective: int = None,
        effective_end_time: str = None,
        effective_start_time: str = None,
        end_time: str = None,
        external_property: int = None,
        full_cycle: int = None,
        graph_flow: Any = None,
        is_delete: int = None,
        is_online: int = None,
        lambda_: str = None,
        last_update_emp_name: str = None,
        last_update_empid: str = None,
        last_update_time: str = None,
        level: int = None,
        meet: int = None,
        modify_type: int = None,
        name: str = None,
        operation_mode: int = None,
        quality_check_type: int = None,
        rid: str = None,
        rule_category_name: str = None,
        rule_score_type: int = None,
        rule_type: int = None,
        scheme_check_type: SchemeCheckType = None,
        scheme_id: int = None,
        scheme_name: str = None,
        scheme_rule_mapping_id: int = None,
        score_deleted: bool = None,
        score_id: int = None,
        score_name: str = None,
        score_num: int = None,
        score_num_type: int = None,
        score_rule_hit_type: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
        score_type: int = None,
        sort_index: int = None,
        start_time: str = None,
        status: int = None,
        target_type: int = None,
        task_flow_id: int = None,
        task_flow_type: int = None,
        triggers: List[str] = None,
        type: int = None,
        weight: str = None,
    ):
        self.auto_review = auto_review
        self.business_category_name_list = business_category_name_list
        self.check_type = check_type
        self.comments = comments
        self.config_type = config_type
        self.create_emp_name = create_emp_name
        self.create_empid = create_empid
        self.create_time = create_time
        self.deny = deny
        self.dialogues = dialogues
        self.effective = effective
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.end_time = end_time
        self.external_property = external_property
        self.full_cycle = full_cycle
        self.graph_flow = graph_flow
        self.is_delete = is_delete
        self.is_online = is_online
        self.lambda_ = lambda_
        self.last_update_emp_name = last_update_emp_name
        self.last_update_empid = last_update_empid
        self.last_update_time = last_update_time
        self.level = level
        self.meet = meet
        self.modify_type = modify_type
        self.name = name
        self.operation_mode = operation_mode
        self.quality_check_type = quality_check_type
        self.rid = rid
        self.rule_category_name = rule_category_name
        self.rule_score_type = rule_score_type
        self.rule_type = rule_type
        self.scheme_check_type = scheme_check_type
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.scheme_rule_mapping_id = scheme_rule_mapping_id
        self.score_deleted = score_deleted
        self.score_id = score_id
        self.score_name = score_name
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_rule_hit_type = score_rule_hit_type
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name
        self.score_type = score_type
        self.sort_index = sort_index
        self.start_time = start_time
        self.status = status
        self.target_type = target_type
        self.task_flow_id = task_flow_id
        self.task_flow_type = task_flow_type
        self.triggers = triggers
        self.type = type
        self.weight = weight

    def validate(self):
        if self.dialogues:
            for k in self.dialogues:
                if k:
                    k.validate()
        if self.scheme_check_type:
            self.scheme_check_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.create_emp_name is not None:
            result['CreateEmpName'] = self.create_emp_name
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deny is not None:
            result['Deny'] = self.deny
        result['Dialogues'] = []
        if self.dialogues is not None:
            for k in self.dialogues:
                result['Dialogues'].append(k.to_map() if k else None)
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_property is not None:
            result['ExternalProperty'] = self.external_property
        if self.full_cycle is not None:
            result['FullCycle'] = self.full_cycle
        if self.graph_flow is not None:
            result['GraphFlow'] = self.graph_flow
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.last_update_emp_name is not None:
            result['LastUpdateEmpName'] = self.last_update_emp_name
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.level is not None:
            result['Level'] = self.level
        if self.meet is not None:
            result['Meet'] = self.meet
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_mode is not None:
            result['OperationMode'] = self.operation_mode
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_category_name is not None:
            result['RuleCategoryName'] = self.rule_category_name
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scheme_check_type is not None:
            result['SchemeCheckType'] = self.scheme_check_type.to_map()
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.scheme_rule_mapping_id is not None:
            result['SchemeRuleMappingId'] = self.scheme_rule_mapping_id
        if self.score_deleted is not None:
            result['ScoreDeleted'] = self.score_deleted
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type
        if self.score_rule_hit_type is not None:
            result['ScoreRuleHitType'] = self.score_rule_hit_type
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.sort_index is not None:
            result['SortIndex'] = self.sort_index
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.task_flow_id is not None:
            result['TaskFlowId'] = self.task_flow_id
        if self.task_flow_type is not None:
            result['TaskFlowType'] = self.task_flow_type
        if self.triggers is not None:
            result['Triggers'] = self.triggers
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('CreateEmpName') is not None:
            self.create_emp_name = m.get('CreateEmpName')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Deny') is not None:
            self.deny = m.get('Deny')
        self.dialogues = []
        if m.get('Dialogues') is not None:
            for k in m.get('Dialogues'):
                temp_model = RuleTestDialogue()
                self.dialogues.append(temp_model.from_map(k))
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalProperty') is not None:
            self.external_property = m.get('ExternalProperty')
        if m.get('FullCycle') is not None:
            self.full_cycle = m.get('FullCycle')
        if m.get('GraphFlow') is not None:
            self.graph_flow = m.get('GraphFlow')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('LastUpdateEmpName') is not None:
            self.last_update_emp_name = m.get('LastUpdateEmpName')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Meet') is not None:
            self.meet = m.get('Meet')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationMode') is not None:
            self.operation_mode = m.get('OperationMode')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleCategoryName') is not None:
            self.rule_category_name = m.get('RuleCategoryName')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SchemeCheckType') is not None:
            temp_model = SchemeCheckType()
            self.scheme_check_type = temp_model.from_map(m['SchemeCheckType'])
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('SchemeRuleMappingId') is not None:
            self.scheme_rule_mapping_id = m.get('SchemeRuleMappingId')
        if m.get('ScoreDeleted') is not None:
            self.score_deleted = m.get('ScoreDeleted')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')
        if m.get('ScoreRuleHitType') is not None:
            self.score_rule_hit_type = m.get('ScoreRuleHitType')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('SortIndex') is not None:
            self.sort_index = m.get('SortIndex')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TaskFlowId') is not None:
            self.task_flow_id = m.get('TaskFlowId')
        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')
        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class RulesInfo(TeaModel):
    def __init__(
        self,
        conditions: List[ConditionBasicInfo] = None,
        count: int = None,
        dialogues: List[RuleTestDialogue] = None,
        page_number: int = None,
        page_size: int = None,
        rules: List[RuleInfo] = None,
    ):
        self.conditions = conditions
        self.count = count
        self.dialogues = dialogues
        self.page_number = page_number
        self.page_size = page_size
        self.rules = rules

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.dialogues:
            for k in self.dialogues:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        result['Dialogues'] = []
        if self.dialogues is not None:
            for k in self.dialogues:
                result['Dialogues'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = ConditionBasicInfo()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.dialogues = []
        if m.get('Dialogues') is not None:
            for k in m.get('Dialogues'):
                temp_model = RuleTestDialogue()
                self.dialogues.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = RuleInfo()
                self.rules.append(temp_model.from_map(k))
        return self


class TaskGraphFlow(TeaModel):
    def __init__(
        self,
        flow_rule_score_type: int = None,
        id: int = None,
        nodes: List[GraphFlowNode] = None,
        rid: int = None,
        rule_name: str = None,
        show_properties: str = None,
        skip_when_first_session_node_miss: bool = None,
    ):
        self.flow_rule_score_type = flow_rule_score_type
        self.id = id
        self.nodes = nodes
        self.rid = rid
        self.rule_name = rule_name
        self.show_properties = show_properties
        self.skip_when_first_session_node_miss = skip_when_first_session_node_miss

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_rule_score_type is not None:
            result['FlowRuleScoreType'] = self.flow_rule_score_type
        if self.id is not None:
            result['Id'] = self.id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.show_properties is not None:
            result['ShowProperties'] = self.show_properties
        if self.skip_when_first_session_node_miss is not None:
            result['SkipWhenFirstSessionNodeMiss'] = self.skip_when_first_session_node_miss
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowRuleScoreType') is not None:
            self.flow_rule_score_type = m.get('FlowRuleScoreType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GraphFlowNode()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ShowProperties') is not None:
            self.show_properties = m.get('ShowProperties')
        if m.get('SkipWhenFirstSessionNodeMiss') is not None:
            self.skip_when_first_session_node_miss = m.get('SkipWhenFirstSessionNodeMiss')
        return self


class AddBusinessCategoryRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddBusinessCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddBusinessCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddBusinessCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddBusinessCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRuleCategoryRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AddRuleCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        select: bool = None,
        type: int = None,
    ):
        self.select = select
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddRuleCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddRuleCategoryResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AddRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRuleCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRuleCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddRuleCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRuleV4Request(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        is_copy: bool = None,
        json_str_for_rule: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.is_copy = is_copy
        # This parameter is required.
        self.json_str_for_rule = json_str_for_rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy
        if self.json_str_for_rule is not None:
            result['JsonStrForRule'] = self.json_str_for_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')
        if m.get('JsonStrForRule') is not None:
            self.json_str_for_rule = m.get('JsonStrForRule')
        return self


class AddRuleV4ResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddRuleV4ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: AddRuleV4ResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = AddRuleV4ResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRuleV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRuleV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddRuleV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyWsTokenRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ApplyWsTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        token: str = None,
        ws_endpoint: str = None,
    ):
        self.session_id = session_id
        self.token = token
        self.ws_endpoint = ws_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token is not None:
            result['Token'] = self.token
        if self.ws_endpoint is not None:
            result['WsEndpoint'] = self.ws_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('WsEndpoint') is not None:
            self.ws_endpoint = m.get('WsEndpoint')
        return self


class ApplyWsTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ApplyWsTokenResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ApplyWsTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyWsTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyWsTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyWsTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignReviewerRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class AssignReviewerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignReviewerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssignReviewerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssignReviewerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignReviewerBySessionGroupRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class AssignReviewerBySessionGroupResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AssignReviewerBySessionGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: AssignReviewerBySessionGroupResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = AssignReviewerBySessionGroupResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignReviewerBySessionGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssignReviewerBySessionGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssignReviewerBySessionGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSubmitReviewInfoRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class BatchSubmitReviewInfoResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class BatchSubmitReviewInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: BatchSubmitReviewInfoResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = BatchSubmitReviewInfoResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchSubmitReviewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSubmitReviewInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchSubmitReviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsrVocabRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateAsrVocabResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAsrVocabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAsrVocabResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCheckTypeToSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class CreateCheckTypeToSchemeResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateCheckTypeToSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: CreateCheckTypeToSchemeResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = CreateCheckTypeToSchemeResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCheckTypeToSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCheckTypeToSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCheckTypeToSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQualityCheckSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class CreateQualityCheckSchemeResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateQualityCheckSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: CreateQualityCheckSchemeResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = CreateQualityCheckSchemeResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQualityCheckSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQualityCheckSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQualityCheckSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchemeTaskConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class CreateSchemeTaskConfigResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateSchemeTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: CreateSchemeTaskConfigResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = CreateSchemeTaskConfigResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSchemeTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSchemeTaskConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSchemeTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSkillGroupConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateSkillGroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSkillGroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSkillGroupConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskAssignRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateTaskAssignRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTaskAssignRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskAssignRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskAssignRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWarningConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateWarningConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateWarningConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWarningConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWarningStrategyConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class CreateWarningStrategyConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateWarningStrategyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWarningStrategyConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWarningStrategyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelRuleCategoryRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DelRuleCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        select: bool = None,
    ):
        self.select = select

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        return self


class DelRuleCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DelRuleCategoryResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DelRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelRuleCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DelRuleCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DelRuleCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAsrVocabRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteAsrVocabResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAsrVocabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAsrVocabResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBusinessCategoryRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteBusinessCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteBusinessCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBusinessCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBusinessCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCheckTypeToSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteCheckTypeToSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        messages: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCheckTypeToSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCheckTypeToSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCheckTypeToSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomizationConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteCustomizationConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomizationConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomizationConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomizationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSetRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrecisionTaskRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeletePrecisionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePrecisionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrecisionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQualityCheckSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class DeleteQualityCheckSchemeResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteQualityCheckSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: DeleteQualityCheckSchemeResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = DeleteQualityCheckSchemeResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQualityCheckSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQualityCheckSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQualityCheckSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        force_delete: bool = None,
        is_scheme_data: int = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.force_delete = force_delete
        self.is_scheme_data = is_scheme_data
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete
        if self.is_scheme_data is not None:
            result['IsSchemeData'] = self.is_scheme_data
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')
        if m.get('IsSchemeData') is not None:
            self.is_scheme_data = m.get('IsSchemeData')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteRuleResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: DeleteRuleResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = DeleteRuleResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleV4Request(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        force_delete: bool = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.force_delete = force_delete
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteRuleV4ResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteRuleV4ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: DeleteRuleV4ResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = DeleteRuleV4ResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRuleV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRuleV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRuleV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchemeTaskConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class DeleteSchemeTaskConfigResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DeleteSchemeTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: DeleteSchemeTaskConfigResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = DeleteSchemeTaskConfigResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSchemeTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSchemeTaskConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSchemeTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSkillGroupConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteSkillGroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSkillGroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSkillGroupConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskAssignRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteTaskAssignRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTaskAssignRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTaskAssignRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskAssignRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWarningConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteWarningConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWarningConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWarningConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWarningStrategyConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class DeleteWarningStrategyConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWarningStrategyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWarningStrategyConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWarningStrategyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsrVocabRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetAsrVocabResponseBodyDataWordsWord(TeaModel):
    def __init__(
        self,
        weight: int = None,
        word: str = None,
    ):
        self.weight = weight
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class GetAsrVocabResponseBodyDataWords(TeaModel):
    def __init__(
        self,
        word: List[GetAsrVocabResponseBodyDataWordsWord] = None,
    ):
        self.word = word

    def validate(self):
        if self.word:
            for k in self.word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Word'] = []
        if self.word is not None:
            for k in self.word:
                result['Word'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.word = []
        if m.get('Word') is not None:
            for k in m.get('Word'):
                temp_model = GetAsrVocabResponseBodyDataWordsWord()
                self.word.append(temp_model.from_map(k))
        return self


class GetAsrVocabResponseBodyData(TeaModel):
    def __init__(
        self,
        asr_version: int = None,
        model_customization_id: str = None,
        name: str = None,
        words: GetAsrVocabResponseBodyDataWords = None,
    ):
        self.asr_version = asr_version
        self.model_customization_id = model_customization_id
        self.name = name
        self.words = words

    def validate(self):
        if self.words:
            self.words.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version
        if self.model_customization_id is not None:
            result['ModelCustomizationId'] = self.model_customization_id
        if self.name is not None:
            result['Name'] = self.name
        if self.words is not None:
            result['Words'] = self.words.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')
        if m.get('ModelCustomizationId') is not None:
            self.model_customization_id = m.get('ModelCustomizationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Words') is not None:
            temp_model = GetAsrVocabResponseBodyDataWords()
            self.words = temp_model.from_map(m['Words'])
        return self


class GetAsrVocabResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAsrVocabResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsrVocabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsrVocabResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBusinessCategoryListRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetBusinessCategoryListResponseBodyData(TeaModel):
    def __init__(
        self,
        business_category_basic_info: List[GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo] = None,
    ):
        self.business_category_basic_info = business_category_basic_info

    def validate(self):
        if self.business_category_basic_info:
            for k in self.business_category_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BusinessCategoryBasicInfo'] = []
        if self.business_category_basic_info is not None:
            for k in self.business_category_basic_info:
                result['BusinessCategoryBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business_category_basic_info = []
        if m.get('BusinessCategoryBasicInfo') is not None:
            for k in m.get('BusinessCategoryBasicInfo'):
                temp_model = GetBusinessCategoryListResponseBodyDataBusinessCategoryBasicInfo()
                self.business_category_basic_info.append(temp_model.from_map(k))
        return self


class GetBusinessCategoryListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetBusinessCategoryListResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetBusinessCategoryListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBusinessCategoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBusinessCategoryListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBusinessCategoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomizationConfigListRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo(TeaModel):
    def __init__(
        self,
        asr_version: int = None,
        create_time: str = None,
        mode_customization_id: str = None,
        model_id: int = None,
        model_name: str = None,
        model_status: int = None,
        task_type: int = None,
    ):
        self.asr_version = asr_version
        self.create_time = create_time
        self.mode_customization_id = mode_customization_id
        self.model_id = model_id
        self.model_name = model_name
        self.model_status = model_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_status is not None:
            result['ModelStatus'] = self.model_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelStatus') is not None:
            self.model_status = m.get('ModelStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetCustomizationConfigListResponseBodyData(TeaModel):
    def __init__(
        self,
        model_customization_data_set_po: List[GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo] = None,
    ):
        self.model_customization_data_set_po = model_customization_data_set_po

    def validate(self):
        if self.model_customization_data_set_po:
            for k in self.model_customization_data_set_po:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelCustomizationDataSetPo'] = []
        if self.model_customization_data_set_po is not None:
            for k in self.model_customization_data_set_po:
                result['ModelCustomizationDataSetPo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_customization_data_set_po = []
        if m.get('ModelCustomizationDataSetPo') is not None:
            for k in m.get('ModelCustomizationDataSetPo'):
                temp_model = GetCustomizationConfigListResponseBodyDataModelCustomizationDataSetPo()
                self.model_customization_data_set_po.append(temp_model.from_map(k))
        return self


class GetCustomizationConfigListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCustomizationConfigListResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetCustomizationConfigListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomizationConfigListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomizationConfigListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCustomizationConfigListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNextResultToVerifyRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine(TeaModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource(TeaModel):
    def __init__(
        self,
        line: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSourceLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine(TeaModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget(TeaModel):
    def __init__(
        self,
        line: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTargetLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta(TeaModel):
    def __init__(
        self,
        source: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource = None,
        target: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget = None,
        type: str = None,
    ):
        self.source = source
        self.target = target
        self.type = type

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDeltaTarget()
            self.target = temp_model.from_map(m['Target'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas(TeaModel):
    def __init__(
        self,
        delta: List[GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta] = None,
    ):
        self.delta = delta

    def validate(self):
        if self.delta:
            for k in self.delta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delta'] = []
        if self.delta is not None:
            for k in self.delta:
                result['Delta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delta = []
        if m.get('Delta') is not None:
            for k in m.get('Delta'):
                temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltasDelta()
                self.delta.append(temp_model.from_map(k))
        return self


class GetNextResultToVerifyResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        deltas: GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        incorrect_words: int = None,
        role: str = None,
        silence_duration: int = None,
        source_role: str = None,
        source_words: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.deltas = deltas
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.incorrect_words = incorrect_words
        self.role = role
        self.silence_duration = silence_duration
        self.source_role = source_role
        self.source_words = source_words
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        if self.deltas:
            self.deltas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.deltas is not None:
            result['Deltas'] = self.deltas.to_map()
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.role is not None:
            result['Role'] = self.role
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.source_role is not None:
            result['SourceRole'] = self.source_role
        if self.source_words is not None:
            result['SourceWords'] = self.source_words
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.words is not None:
            result['Words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Deltas') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogueDeltas()
            self.deltas = temp_model.from_map(m['Deltas'])
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')
        if m.get('SourceWords') is not None:
            self.source_words = m.get('SourceWords')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetNextResultToVerifyResponseBodyDataDialogues(TeaModel):
    def __init__(
        self,
        dialogue: List[GetNextResultToVerifyResponseBodyDataDialoguesDialogue] = None,
    ):
        self.dialogue = dialogue

    def validate(self):
        if self.dialogue:
            for k in self.dialogue:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k in self.dialogue:
                result['Dialogue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k in m.get('Dialogue'):
                temp_model = GetNextResultToVerifyResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k))
        return self


class GetNextResultToVerifyResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_scheme: str = None,
        audio_url: str = None,
        dialogues: GetNextResultToVerifyResponseBodyDataDialogues = None,
        duration: int = None,
        file_id: str = None,
        file_name: str = None,
        incorrect_words: int = None,
        index: int = None,
        precision: float = None,
        status: int = None,
        total_count: int = None,
        update_time: str = None,
        verified: bool = None,
        verified_count: int = None,
    ):
        self.audio_scheme = audio_scheme
        self.audio_url = audio_url
        self.dialogues = dialogues
        self.duration = duration
        self.file_id = file_id
        self.file_name = file_name
        self.incorrect_words = incorrect_words
        self.index = index
        self.precision = precision
        self.status = status
        self.total_count = total_count
        self.update_time = update_time
        self.verified = verified
        self.verified_count = verified_count

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.index is not None:
            result['Index'] = self.index
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verified is not None:
            result['Verified'] = self.verified
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('Dialogues') is not None:
            temp_model = GetNextResultToVerifyResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Verified') is not None:
            self.verified = m.get('Verified')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        return self


class GetNextResultToVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetNextResultToVerifyResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetNextResultToVerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNextResultToVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNextResultToVerifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNextResultToVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrecisionTaskRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetPrecisionTaskResponseBodyDataPrecisionsPrecision(TeaModel):
    def __init__(
        self,
        model_id: int = None,
        model_name: str = None,
        precision: float = None,
        status: int = None,
        task_id: str = None,
    ):
        self.model_id = model_id
        self.model_name = model_name
        self.precision = precision
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetPrecisionTaskResponseBodyDataPrecisions(TeaModel):
    def __init__(
        self,
        precision: List[GetPrecisionTaskResponseBodyDataPrecisionsPrecision] = None,
    ):
        self.precision = precision

    def validate(self):
        if self.precision:
            for k in self.precision:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Precision'] = []
        if self.precision is not None:
            for k in self.precision:
                result['Precision'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precision = []
        if m.get('Precision') is not None:
            for k in m.get('Precision'):
                temp_model = GetPrecisionTaskResponseBodyDataPrecisionsPrecision()
                self.precision.append(temp_model.from_map(k))
        return self


class GetPrecisionTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        data_set_id: int = None,
        data_set_name: str = None,
        duration: int = None,
        incorrect_words: int = None,
        name: str = None,
        precisions: GetPrecisionTaskResponseBodyDataPrecisions = None,
        source: int = None,
        status: int = None,
        task_id: str = None,
        total_count: int = None,
        update_time: str = None,
        verified_count: int = None,
    ):
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.duration = duration
        self.incorrect_words = incorrect_words
        self.name = name
        self.precisions = precisions
        self.source = source
        self.status = status
        self.task_id = task_id
        self.total_count = total_count
        self.update_time = update_time
        self.verified_count = verified_count

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.name is not None:
            result['Name'] = self.name
        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Precisions') is not None:
            temp_model = GetPrecisionTaskResponseBodyDataPrecisions()
            self.precisions = temp_model.from_map(m['Precisions'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        return self


class GetPrecisionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPrecisionTaskResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPrecisionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPrecisionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityCheckSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class GetQualityCheckSchemeResponseBodyDataSchemeCheckTypeList(TeaModel):
    def __init__(
        self,
        check_name: str = None,
        check_type: int = None,
        enable: int = None,
        scheme_id: int = None,
        score: int = None,
        source_score: int = None,
    ):
        self.check_name = check_name
        self.check_type = check_type
        self.enable = enable
        self.scheme_id = scheme_id
        self.score = score
        self.source_score = source_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.score is not None:
            result['Score'] = self.score
        if self.source_score is not None:
            result['SourceScore'] = self.source_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SourceScore') is not None:
            self.source_score = m.get('SourceScore')
        return self


class GetQualityCheckSchemeResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_name: str = None,
        data_type: int = None,
        description: str = None,
        init_score: str = None,
        name: str = None,
        rule_ids: List[str] = None,
        rule_list: List[RulesInfo] = None,
        scheme_check_type_list: List[GetQualityCheckSchemeResponseBodyDataSchemeCheckTypeList] = None,
        scheme_id: int = None,
        scheme_template_id: int = None,
        status: int = None,
        template_type: int = None,
        type: int = None,
        update_time: str = None,
        update_user_name: str = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.data_type = data_type
        self.description = description
        self.init_score = init_score
        self.name = name
        self.rule_ids = rule_ids
        self.rule_list = rule_list
        self.scheme_check_type_list = scheme_check_type_list
        self.scheme_id = scheme_id
        self.scheme_template_id = scheme_template_id
        self.status = status
        self.template_type = template_type
        self.type = type
        self.update_time = update_time
        self.update_user_name = update_user_name
        self.version = version

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()
        if self.scheme_check_type_list:
            for k in self.scheme_check_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.init_score is not None:
            result['InitScore'] = self.init_score
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        result['SchemeCheckTypeList'] = []
        if self.scheme_check_type_list is not None:
            for k in self.scheme_check_type_list:
                result['SchemeCheckTypeList'].append(k.to_map() if k else None)
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.scheme_template_id is not None:
            result['SchemeTemplateId'] = self.scheme_template_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InitScore') is not None:
            self.init_score = m.get('InitScore')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = RulesInfo()
                self.rule_list.append(temp_model.from_map(k))
        self.scheme_check_type_list = []
        if m.get('SchemeCheckTypeList') is not None:
            for k in m.get('SchemeCheckTypeList'):
                temp_model = GetQualityCheckSchemeResponseBodyDataSchemeCheckTypeList()
                self.scheme_check_type_list.append(temp_model.from_map(k))
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SchemeTemplateId') is not None:
            self.scheme_template_id = m.get('SchemeTemplateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetQualityCheckSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQualityCheckSchemeResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        messages: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages
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
            temp_model = GetQualityCheckSchemeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityCheckSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQualityCheckSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQualityCheckSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResultRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultResponseBodyDataResultInfoAgent(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        skill_group: str = None,
    ):
        self.id = id
        self.name = name
        self.skill_group = skill_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        return self


class GetResultResponseBodyDataResultInfoAsrResultAsrResult(TeaModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        identity: str = None,
        role: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.identity = identity
        self.role = role
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultResponseBodyDataResultInfoAsrResult(TeaModel):
    def __init__(
        self,
        asr_result: List[GetResultResponseBodyDataResultInfoAsrResultAsrResult] = None,
    ):
        self.asr_result = asr_result

    def validate(self):
        if self.asr_result:
            for k in self.asr_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AsrResult'] = []
        if self.asr_result is not None:
            for k in self.asr_result:
                result['AsrResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k in m.get('AsrResult'):
                temp_model = GetResultResponseBodyDataResultInfoAsrResultAsrResult()
                self.asr_result.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeAnchor(TeaModel):
    def __init__(
        self,
        cid: str = None,
        hit_time: int = None,
        location: str = None,
    ):
        # 条件ID
        self.cid = cid
        # 命中次数
        self.hit_time = hit_time
        # 位置
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeRange(TeaModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        # 对话开始索引
        self.from_ = from_
        # 对话结束索引
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeTimeRange(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRange(TeaModel):
    def __init__(
        self,
        absolute: bool = None,
        all_sentences_satisfy: bool = None,
        anchor: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeAnchor = None,
        range: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeRange = None,
        role: str = None,
        role_id: int = None,
        time_range: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeTimeRange = None,
    ):
        # false: 相对位置; 会结合anchor以及角色来决定句子位置
        self.absolute = absolute
        # true: 每句话都必须满足条件；
        self.all_sentences_satisfy = all_sentences_satisfy
        # 前置后置条件
        self.anchor = anchor
        # 相对范围
        self.range = range
        # 对应 RoleType.type
        self.role = role
        # 对应 RoleType.id
        self.role_id = role_id
        self.time_range = time_range

    def validate(self):
        if self.anchor:
            self.anchor.validate()
        if self.range:
            self.range.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.absolute is not None:
            result['Absolute'] = self.absolute
        if self.all_sentences_satisfy is not None:
            result['AllSentencesSatisfy'] = self.all_sentences_satisfy
        if self.anchor is not None:
            result['Anchor'] = self.anchor.to_map()
        if self.range is not None:
            result['Range'] = self.range.to_map()
        if self.role is not None:
            result['Role'] = self.role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Absolute') is not None:
            self.absolute = m.get('Absolute')
        if m.get('AllSentencesSatisfy') is not None:
            self.all_sentences_satisfy = m.get('AllSentencesSatisfy')
        if m.get('Anchor') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeAnchor()
            self.anchor = temp_model.from_map(m['Anchor'])
        if m.get('Range') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('TimeRange') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRangeTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamExcludes(TeaModel):
    def __init__(
        self,
        exclude: List[str] = None,
    ):
        self.exclude = exclude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamFlowNodePrerequisiteParam(TeaModel):
    def __init__(
        self,
        node_id: int = None,
        node_match_status: int = None,
        node_name: str = None,
    ):
        # 节点id
        self.node_id = node_id
        # 节点匹配状态。
        self.node_match_status = node_match_status
        # 冗余的节点名称
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_match_status is not None:
            result['NodeMatchStatus'] = self.node_match_status
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeMatchStatus') is not None:
            self.node_match_status = m.get('NodeMatchStatus')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntentsIntent(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # 意图模型ID
        self.id = id
        # 意图模型名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntents(TeaModel):
    def __init__(
        self,
        intent: List[GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntentsIntent] = None,
    ):
        self.intent = intent

    def validate(self):
        if self.intent:
            for k in self.intent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intent'] = []
        if self.intent is not None:
            for k in self.intent:
                result['Intent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intent = []
        if m.get('Intent') is not None:
            for k in m.get('Intent'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntentsIntent()
                self.intent.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParm(TeaModel):
    def __init__(
        self,
        intents: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntents = None,
        model_scene: str = None,
    ):
        # 引用的意图模型
        self.intents = intents
        # 模型应用的场景 AGENT:客户场景、CUSTOMER:客服场景 (CUSTOMER: 客户场景, AGENT: 坐席场景)
        self.model_scene = model_scene

    def validate(self):
        if self.intents:
            self.intents.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intents is not None:
            result['Intents'] = self.intents.to_map()
        if self.model_scene is not None:
            result['ModelScene'] = self.model_scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Intents') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParmIntents()
            self.intents = temp_model.from_map(m['Intents'])
        if m.get('ModelScene') is not None:
            self.model_scene = m.get('ModelScene')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamKeywords(TeaModel):
    def __init__(
        self,
        keyword: List[str] = None,
    ):
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParam(TeaModel):
    def __init__(
        self,
        average: bool = None,
        begin_type: str = None,
        case_sensitive: bool = None,
        check_first_sentence: bool = None,
        check_type: int = None,
        compare_operator: str = None,
        context_chat_match: bool = None,
        delay_time: int = None,
        end_type: str = None,
        excludes: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamExcludes = None,
        flow_node_prerequisite_param: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamFlowNodePrerequisiteParam = None,
        from_: int = None,
        from_end: bool = None,
        hit_time: int = None,
        in_sentence: bool = None,
        intent_model_check_parm: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParm = None,
        interval: int = None,
        interval_end: int = None,
        keyword_extension: int = None,
        keyword_match_size: int = None,
        keywords: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamKeywords = None,
        max_emotion_change_value: int = None,
        min_word_size: int = None,
        near_dialogue: bool = None,
        not_regex: str = None,
        phrase: str = None,
        regex: str = None,
        target: int = None,
        threshold: float = None,
    ):
        # 语速检测，是否计算整个对话平均语速，默认false
        self.average = average
        # 时长算子，时长计算开始类型，录音开始，还是某句对话开始
        self.begin_type = begin_type
        # 区分大小写
        self.case_sensitive = case_sensitive
        # 静音检测：要不要检测第一句话
        self.check_first_sentence = check_first_sentence
        # 检测方式，1 相邻句能量波动 2 最大能量跨度 默认1
        self.check_type = check_type
        # 大于，还是小于，gt/lt
        self.compare_operator = compare_operator
        # 是否单句话匹配；
        self.context_chat_match = context_chat_match
        # 抢话算子 延时时长
        self.delay_time = delay_time
        # 时长算子，时长计算结束类型，录音结束，还是某句对话结束
        self.end_type = end_type
        # 上下文重复算子：排除掉某些对话
        self.excludes = excludes
        # 流程节点前置条件参数
        self.flow_node_prerequisite_param = flow_node_prerequisite_param
        # 上下文重复算子：检测当前句的前from句是否有重复；0表示前面的所有句
        self.from_ = from_
        # from_end
        self.from_end = from_end
        # 上下文重复算子：重复几次
        self.hit_time = hit_time
        # 生效句子， true单个句子，false多个句子
        self.in_sentence = in_sentence
        # 意图模型检查参数
        self.intent_model_check_parm = intent_model_check_parm
        # interval代表区间范围开始
        self.interval = interval
        # intervalEnd 代表区间范围结束
        self.interval_end = interval_end
        # 关键字扩展
        self.keyword_extension = keyword_extension
        # 匹配到的关键字数量
        self.keyword_match_size = keyword_match_size
        # 关键词
        self.keywords = keywords
        # 能量值变化，默认3, 1~9
        self.max_emotion_change_value = max_emotion_change_value
        # 句子中最少字数，小于此字数的句子不检查
        self.min_word_size = min_word_size
        # true表示取不同角色相邻的两句话，false表示取不同角色的第一句话比较响应时间（默认）
        self.near_dialogue = near_dialogue
        # 排除的正则表达式
        self.not_regex = not_regex
        # 语句
        self.phrase = phrase
        # 正则表达式
        self.regex = regex
        # target
        self.target = target
        # 阈值
        self.threshold = threshold

    def validate(self):
        if self.excludes:
            self.excludes.validate()
        if self.flow_node_prerequisite_param:
            self.flow_node_prerequisite_param.validate()
        if self.intent_model_check_parm:
            self.intent_model_check_parm.validate()
        if self.keywords:
            self.keywords.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.begin_type is not None:
            result['BeginType'] = self.begin_type
        if self.case_sensitive is not None:
            result['Case_sensitive'] = self.case_sensitive
        if self.check_first_sentence is not None:
            result['CheckFirstSentence'] = self.check_first_sentence
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.compare_operator is not None:
            result['CompareOperator'] = self.compare_operator
        if self.context_chat_match is not None:
            result['ContextChatMatch'] = self.context_chat_match
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.end_type is not None:
            result['EndType'] = self.end_type
        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()
        if self.flow_node_prerequisite_param is not None:
            result['FlowNodePrerequisiteParam'] = self.flow_node_prerequisite_param.to_map()
        if self.from_ is not None:
            result['From'] = self.from_
        if self.from_end is not None:
            result['From_end'] = self.from_end
        if self.hit_time is not None:
            result['Hit_time'] = self.hit_time
        if self.in_sentence is not None:
            result['In_sentence'] = self.in_sentence
        if self.intent_model_check_parm is not None:
            result['IntentModelCheckParm'] = self.intent_model_check_parm.to_map()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.interval_end is not None:
            result['IntervalEnd'] = self.interval_end
        if self.keyword_extension is not None:
            result['KeywordExtension'] = self.keyword_extension
        if self.keyword_match_size is not None:
            result['KeywordMatchSize'] = self.keyword_match_size
        if self.keywords is not None:
            result['Keywords'] = self.keywords.to_map()
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
        if self.regex is not None:
            result['Regex'] = self.regex
        if self.target is not None:
            result['Target'] = self.target
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('BeginType') is not None:
            self.begin_type = m.get('BeginType')
        if m.get('Case_sensitive') is not None:
            self.case_sensitive = m.get('Case_sensitive')
        if m.get('CheckFirstSentence') is not None:
            self.check_first_sentence = m.get('CheckFirstSentence')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('CompareOperator') is not None:
            self.compare_operator = m.get('CompareOperator')
        if m.get('ContextChatMatch') is not None:
            self.context_chat_match = m.get('ContextChatMatch')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('EndType') is not None:
            self.end_type = m.get('EndType')
        if m.get('Excludes') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamExcludes()
            self.excludes = temp_model.from_map(m['Excludes'])
        if m.get('FlowNodePrerequisiteParam') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamFlowNodePrerequisiteParam()
            self.flow_node_prerequisite_param = temp_model.from_map(m['FlowNodePrerequisiteParam'])
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('From_end') is not None:
            self.from_end = m.get('From_end')
        if m.get('Hit_time') is not None:
            self.hit_time = m.get('Hit_time')
        if m.get('In_sentence') is not None:
            self.in_sentence = m.get('In_sentence')
        if m.get('IntentModelCheckParm') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamIntentModelCheckParm()
            self.intent_model_check_parm = temp_model.from_map(m['IntentModelCheckParm'])
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IntervalEnd') is not None:
            self.interval_end = m.get('IntervalEnd')
        if m.get('KeywordExtension') is not None:
            self.keyword_extension = m.get('KeywordExtension')
        if m.get('KeywordMatchSize') is not None:
            self.keyword_match_size = m.get('KeywordMatchSize')
        if m.get('Keywords') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParamKeywords()
            self.keywords = temp_model.from_map(m['Keywords'])
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
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperator(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        oid: str = None,
        param: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParam = None,
        type: str = None,
    ):
        # 主键id
        self.id = id
        # 算子名
        self.name = name
        # 可能是主键id，也可能是前端生成的id
        self.oid = oid
        # 算子参数
        self.param = param
        # 算子类别
        self.type = type

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.oid is not None:
            result['Oid'] = self.oid
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.type is not None:
            result['Type'] = self.type
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
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperatorParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperators(TeaModel):
    def __init__(
        self,
        operator: List[GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperator] = None,
    ):
        self.operator = operator

    def validate(self):
        if self.operator:
            for k in self.operator:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Operator'] = []
        if self.operator is not None:
            for k in self.operator:
                result['Operator'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator = []
        if m.get('Operator') is not None:
            for k in m.get('Operator'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperatorsOperator()
                self.operator.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditions(TeaModel):
    def __init__(
        self,
        check_range: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRange = None,
        cid: str = None,
        exclusion: int = None,
        id: int = None,
        lambda_: str = None,
        operators: GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperators = None,
        rid: str = None,
    ):
        # 检测范围
        self.check_range = check_range
        # 条件id，可能是db中的主键，也可能是转换成的a, b, c
        self.cid = cid
        # 排除
        self.exclusion = exclusion
        # 在db中的主键
        self.id = id
        # Lambda表达式：例如:a&&b
        self.lambda_ = lambda_
        # 算子列表
        self.operators = operators
        # 条件所属的规则id
        self.rid = rid

    def validate(self):
        if self.check_range:
            self.check_range.validate()
        if self.operators:
            self.operators.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_range is not None:
            result['Check_range'] = self.check_range.to_map()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.exclusion is not None:
            result['Exclusion'] = self.exclusion
        if self.id is not None:
            result['Id'] = self.id
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.operators is not None:
            result['Operators'] = self.operators.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Check_range') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsCheckRange()
            self.check_range = temp_model.from_map(m['Check_range'])
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Exclusion') is not None:
            self.exclusion = m.get('Exclusion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('Operators') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditionsOperators()
            self.operators = temp_model.from_map(m['Operators'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultConditions(TeaModel):
    def __init__(
        self,
        conditions: List[GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditions] = None,
    ):
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditionsConditions()
                self.conditions.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid(TeaModel):
    def __init__(
        self,
        cid: List[str] = None,
    ):
        self.cid = cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord(TeaModel):
    def __init__(
        self,
        cid: str = None,
        from_: int = None,
        to: int = None,
        val: str = None,
    ):
        self.cid = cid
        self.from_ = from_
        self.to = to
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.from_ is not None:
            result['From'] = self.from_
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
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords(TeaModel):
    def __init__(
        self,
        key_word: List[GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord] = None,
    ):
        self.key_word = key_word

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyWord'] = []
        if self.key_word is not None:
            for k in self.key_word:
                result['KeyWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_word = []
        if m.get('KeyWord') is not None:
            for k in m.get('KeyWord'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase(TeaModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.role = role
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.role is not None:
            result['Role'] = self.role
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
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit(TeaModel):
    def __init__(
        self,
        cid: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid = None,
        key_words: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords = None,
        phrase: GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase = None,
    ):
        self.cid = cid
        self.key_words = key_words
        self.phrase = phrase

    def validate(self):
        if self.cid:
            self.cid.validate()
        if self.key_words:
            self.key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitCid()
            self.cid = temp_model.from_map(m['Cid'])
        if m.get('KeyWords') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Phrase') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHitPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResultHits(TeaModel):
    def __init__(
        self,
        hit: List[GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit] = None,
    ):
        self.hit = hit

    def validate(self):
        if self.hit:
            for k in self.hit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hit'] = []
        if self.hit is not None:
            for k in self.hit:
                result['Hit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit = []
        if m.get('Hit') is not None:
            for k in m.get('Hit'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHitsHit()
                self.hit.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitResultHitResult(TeaModel):
    def __init__(
        self,
        conditions: GetResultResponseBodyDataResultInfoHitResultHitResultConditions = None,
        hits: GetResultResponseBodyDataResultInfoHitResultHitResultHits = None,
        name: str = None,
        review_result: int = None,
        rid: str = None,
        scheme_id: int = None,
        scheme_version: int = None,
        score: int = None,
        type: str = None,
    ):
        self.conditions = conditions
        self.hits = hits
        self.name = name
        self.review_result = review_result
        self.rid = rid
        self.scheme_id = scheme_id
        self.scheme_version = scheme_version
        self.score = score
        self.type = type

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.hits:
            self.hits.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions.to_map()
        if self.hits is not None:
            result['Hits'] = self.hits.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.scheme_version is not None:
            result['SchemeVersion'] = self.scheme_version
        if self.score is not None:
            result['Score'] = self.score
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultConditions()
            self.conditions = temp_model.from_map(m['Conditions'])
        if m.get('Hits') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResultHitResultHits()
            self.hits = temp_model.from_map(m['Hits'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SchemeVersion') is not None:
            self.scheme_version = m.get('SchemeVersion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResultResponseBodyDataResultInfoHitResult(TeaModel):
    def __init__(
        self,
        hit_result: List[GetResultResponseBodyDataResultInfoHitResultHitResult] = None,
    ):
        self.hit_result = hit_result

    def validate(self):
        if self.hit_result:
            for k in self.hit_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitResult'] = []
        if self.hit_result is not None:
            for k in self.hit_result:
                result['HitResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_result = []
        if m.get('HitResult') is not None:
            for k in m.get('HitResult'):
                temp_model = GetResultResponseBodyDataResultInfoHitResultHitResult()
                self.hit_result.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoHitScoreHitScore(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        score_id: str = None,
        score_name: str = None,
        score_number: str = None,
    ):
        self.rule_id = rule_id
        self.score_id = score_id
        self.score_name = score_name
        self.score_number = score_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_number is not None:
            result['ScoreNumber'] = self.score_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreNumber') is not None:
            self.score_number = m.get('ScoreNumber')
        return self


class GetResultResponseBodyDataResultInfoHitScore(TeaModel):
    def __init__(
        self,
        hit_score: List[GetResultResponseBodyDataResultInfoHitScoreHitScore] = None,
    ):
        self.hit_score = hit_score

    def validate(self):
        if self.hit_score:
            for k in self.hit_score:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitScore'] = []
        if self.hit_score is not None:
            for k in self.hit_score:
                result['HitScore'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_score = []
        if m.get('HitScore') is not None:
            for k in m.get('HitScore'):
                temp_model = GetResultResponseBodyDataResultInfoHitScoreHitScore()
                self.hit_score.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoRecording(TeaModel):
    def __init__(
        self,
        business: str = None,
        call_id: str = None,
        call_time: str = None,
        call_type: int = None,
        callee: str = None,
        caller: str = None,
        customer_name: str = None,
        data_set_name: str = None,
        dialogue_size: int = None,
        duration: int = None,
        id: str = None,
        name: str = None,
        primary_id: str = None,
        remark_1: str = None,
        remark_10: str = None,
        remark_11: str = None,
        remark_12: str = None,
        remark_13: str = None,
        remark_2: str = None,
        remark_3: str = None,
        remark_4: str = None,
        remark_5: int = None,
        remark_6: str = None,
        remark_7: str = None,
        remark_8: str = None,
        remark_9: str = None,
        task_config_id: int = None,
        task_config_name: str = None,
        url: str = None,
    ):
        self.business = business
        self.call_id = call_id
        self.call_time = call_time
        self.call_type = call_type
        self.callee = callee
        self.caller = caller
        self.customer_name = customer_name
        self.data_set_name = data_set_name
        self.dialogue_size = dialogue_size
        self.duration = duration
        self.id = id
        self.name = name
        self.primary_id = primary_id
        self.remark_1 = remark_1
        self.remark_10 = remark_10
        self.remark_11 = remark_11
        self.remark_12 = remark_12
        self.remark_13 = remark_13
        self.remark_2 = remark_2
        self.remark_3 = remark_3
        self.remark_4 = remark_4
        self.remark_5 = remark_5
        self.remark_6 = remark_6
        self.remark_7 = remark_7
        self.remark_8 = remark_8
        self.remark_9 = remark_9
        self.task_config_id = task_config_id
        self.task_config_name = task_config_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.dialogue_size is not None:
            result['DialogueSize'] = self.dialogue_size
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1
        if self.remark_10 is not None:
            result['Remark10'] = self.remark_10
        if self.remark_11 is not None:
            result['Remark11'] = self.remark_11
        if self.remark_12 is not None:
            result['Remark12'] = self.remark_12
        if self.remark_13 is not None:
            result['Remark13'] = self.remark_13
        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2
        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3
        if self.remark_4 is not None:
            result['Remark4'] = self.remark_4
        if self.remark_5 is not None:
            result['Remark5'] = self.remark_5
        if self.remark_6 is not None:
            result['Remark6'] = self.remark_6
        if self.remark_7 is not None:
            result['Remark7'] = self.remark_7
        if self.remark_8 is not None:
            result['Remark8'] = self.remark_8
        if self.remark_9 is not None:
            result['Remark9'] = self.remark_9
        if self.task_config_id is not None:
            result['TaskConfigId'] = self.task_config_id
        if self.task_config_name is not None:
            result['TaskConfigName'] = self.task_config_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('DialogueSize') is not None:
            self.dialogue_size = m.get('DialogueSize')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')
        if m.get('Remark10') is not None:
            self.remark_10 = m.get('Remark10')
        if m.get('Remark11') is not None:
            self.remark_11 = m.get('Remark11')
        if m.get('Remark12') is not None:
            self.remark_12 = m.get('Remark12')
        if m.get('Remark13') is not None:
            self.remark_13 = m.get('Remark13')
        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')
        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')
        if m.get('Remark4') is not None:
            self.remark_4 = m.get('Remark4')
        if m.get('Remark5') is not None:
            self.remark_5 = m.get('Remark5')
        if m.get('Remark6') is not None:
            self.remark_6 = m.get('Remark6')
        if m.get('Remark7') is not None:
            self.remark_7 = m.get('Remark7')
        if m.get('Remark8') is not None:
            self.remark_8 = m.get('Remark8')
        if m.get('Remark9') is not None:
            self.remark_9 = m.get('Remark9')
        if m.get('TaskConfigId') is not None:
            self.task_config_id = m.get('TaskConfigId')
        if m.get('TaskConfigName') is not None:
            self.task_config_name = m.get('TaskConfigName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['rid'] = self.rid
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rid') is not None:
            self.rid = m.get('rid')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRule(TeaModel):
    def __init__(
        self,
        review_right_rule: List[GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule] = None,
    ):
        self.review_right_rule = review_right_rule

    def validate(self):
        if self.review_right_rule:
            for k in self.review_right_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewRightRule'] = []
        if self.review_right_rule is not None:
            for k in self.review_right_rule:
                result['ReviewRightRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_right_rule = []
        if m.get('ReviewRightRule') is not None:
            for k in m.get('ReviewRightRule'):
                temp_model = GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule()
                self.review_right_rule.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistory(TeaModel):
    def __init__(
        self,
        comments: str = None,
        complain_result: int = None,
        old_score: int = None,
        operator: int = None,
        operator_name: str = None,
        review_manager_type: str = None,
        review_result: int = None,
        review_right_rule: GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRule = None,
        score: int = None,
        time: int = None,
        time_str: str = None,
        type: int = None,
    ):
        self.comments = comments
        self.complain_result = complain_result
        self.old_score = old_score
        self.operator = operator
        self.operator_name = operator_name
        self.review_manager_type = review_manager_type
        self.review_result = review_result
        self.review_right_rule = review_right_rule
        self.score = score
        self.time = time
        self.time_str = time_str
        self.type = type

    def validate(self):
        if self.review_right_rule:
            self.review_right_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.complain_result is not None:
            result['ComplainResult'] = self.complain_result
        if self.old_score is not None:
            result['OldScore'] = self.old_score
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.review_manager_type is not None:
            result['ReviewManagerType'] = self.review_manager_type
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_right_rule is not None:
            result['ReviewRightRule'] = self.review_right_rule.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.time is not None:
            result['Time'] = self.time
        if self.time_str is not None:
            result['TimeStr'] = self.time_str
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ComplainResult') is not None:
            self.complain_result = m.get('ComplainResult')
        if m.get('OldScore') is not None:
            self.old_score = m.get('OldScore')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('ReviewManagerType') is not None:
            self.review_manager_type = m.get('ReviewManagerType')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewRightRule') is not None:
            temp_model = GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistoryReviewRightRule()
            self.review_right_rule = temp_model.from_map(m['ReviewRightRule'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TimeStr') is not None:
            self.time_str = m.get('TimeStr')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResultResponseBodyDataResultInfoReviewHistoryList(TeaModel):
    def __init__(
        self,
        review_history: List[GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistory] = None,
    ):
        self.review_history = review_history

    def validate(self):
        if self.review_history:
            for k in self.review_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewHistory'] = []
        if self.review_history is not None:
            for k in self.review_history:
                result['ReviewHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_history = []
        if m.get('ReviewHistory') is not None:
            for k in m.get('ReviewHistory'):
                temp_model = GetResultResponseBodyDataResultInfoReviewHistoryListReviewHistory()
                self.review_history.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdListReviewKeyIdList(TeaModel):
    def __init__(
        self,
        review_key_id_list: List[int] = None,
    ):
        self.review_key_id_list = review_key_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_key_id_list is not None:
            result['ReviewKeyIdList'] = self.review_key_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeyIdList') is not None:
            self.review_key_id_list = m.get('ReviewKeyIdList')
        return self


class GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdList(TeaModel):
    def __init__(
        self,
        review_key_id_list: GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdListReviewKeyIdList = None,
        review_type_id: int = None,
    ):
        self.review_key_id_list = review_key_id_list
        self.review_type_id = review_type_id

    def validate(self):
        if self.review_key_id_list:
            self.review_key_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_key_id_list is not None:
            result['ReviewKeyIdList'] = self.review_key_id_list.to_map()
        if self.review_type_id is not None:
            result['ReviewTypeId'] = self.review_type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeyIdList') is not None:
            temp_model = GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdListReviewKeyIdList()
            self.review_key_id_list = temp_model.from_map(m['ReviewKeyIdList'])
        if m.get('ReviewTypeId') is not None:
            self.review_type_id = m.get('ReviewTypeId')
        return self


class GetResultResponseBodyDataResultInfoReviewTypeIdList(TeaModel):
    def __init__(
        self,
        review_type_id_list: List[GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdList] = None,
    ):
        self.review_type_id_list = review_type_id_list

    def validate(self):
        if self.review_type_id_list:
            for k in self.review_type_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewTypeIdList'] = []
        if self.review_type_id_list is not None:
            for k in self.review_type_id_list:
                result['ReviewTypeIdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_type_id_list = []
        if m.get('ReviewTypeIdList') is not None:
            for k in m.get('ReviewTypeIdList'):
                temp_model = GetResultResponseBodyDataResultInfoReviewTypeIdListReviewTypeIdList()
                self.review_type_id_list.append(temp_model.from_map(k))
        return self


class GetResultResponseBodyDataResultInfoSchemeIdList(TeaModel):
    def __init__(
        self,
        scheme_id_list: List[int] = None,
    ):
        self.scheme_id_list = scheme_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeIdList') is not None:
            self.scheme_id_list = m.get('SchemeIdList')
        return self


class GetResultResponseBodyDataResultInfoSchemeNameList(TeaModel):
    def __init__(
        self,
        scheme_name_list: List[str] = None,
    ):
        self.scheme_name_list = scheme_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_name_list is not None:
            result['SchemeNameList'] = self.scheme_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeNameList') is not None:
            self.scheme_name_list = m.get('SchemeNameList')
        return self


class GetResultResponseBodyDataResultInfo(TeaModel):
    def __init__(
        self,
        agent: GetResultResponseBodyDataResultInfoAgent = None,
        asr_result: GetResultResponseBodyDataResultInfoAsrResult = None,
        assignment_time: str = None,
        comments: str = None,
        create_time: str = None,
        create_time_long: str = None,
        error_message: str = None,
        hit_result: GetResultResponseBodyDataResultInfoHitResult = None,
        hit_score: GetResultResponseBodyDataResultInfoHitScore = None,
        last_data_id: str = None,
        recording: GetResultResponseBodyDataResultInfoRecording = None,
        resolver: str = None,
        review_history_list: GetResultResponseBodyDataResultInfoReviewHistoryList = None,
        review_result: int = None,
        review_status: int = None,
        review_time: str = None,
        review_time_long: str = None,
        review_type: int = None,
        review_type_id_list: GetResultResponseBodyDataResultInfoReviewTypeIdList = None,
        reviewer: str = None,
        scheme_id_list: GetResultResponseBodyDataResultInfoSchemeIdList = None,
        scheme_name_list: GetResultResponseBodyDataResultInfoSchemeNameList = None,
        score: int = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
        vid: str = None,
    ):
        self.agent = agent
        self.asr_result = asr_result
        self.assignment_time = assignment_time
        self.comments = comments
        self.create_time = create_time
        self.create_time_long = create_time_long
        self.error_message = error_message
        self.hit_result = hit_result
        self.hit_score = hit_score
        self.last_data_id = last_data_id
        self.recording = recording
        self.resolver = resolver
        self.review_history_list = review_history_list
        self.review_result = review_result
        self.review_status = review_status
        self.review_time = review_time
        self.review_time_long = review_time_long
        self.review_type = review_type
        self.review_type_id_list = review_type_id_list
        self.reviewer = reviewer
        self.scheme_id_list = scheme_id_list
        self.scheme_name_list = scheme_name_list
        self.score = score
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.vid = vid

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            self.asr_result.validate()
        if self.hit_result:
            self.hit_result.validate()
        if self.hit_score:
            self.hit_score.validate()
        if self.recording:
            self.recording.validate()
        if self.review_history_list:
            self.review_history_list.validate()
        if self.review_type_id_list:
            self.review_type_id_list.validate()
        if self.scheme_id_list:
            self.scheme_id_list.validate()
        if self.scheme_name_list:
            self.scheme_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        if self.asr_result is not None:
            result['AsrResult'] = self.asr_result.to_map()
        if self.assignment_time is not None:
            result['AssignmentTime'] = self.assignment_time
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.hit_result is not None:
            result['HitResult'] = self.hit_result.to_map()
        if self.hit_score is not None:
            result['HitScore'] = self.hit_score.to_map()
        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id
        if self.recording is not None:
            result['Recording'] = self.recording.to_map()
        if self.resolver is not None:
            result['Resolver'] = self.resolver
        if self.review_history_list is not None:
            result['ReviewHistoryList'] = self.review_history_list.to_map()
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.review_time_long is not None:
            result['ReviewTimeLong'] = self.review_time_long
        if self.review_type is not None:
            result['ReviewType'] = self.review_type
        if self.review_type_id_list is not None:
            result['ReviewTypeIdList'] = self.review_type_id_list.to_map()
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list.to_map()
        if self.scheme_name_list is not None:
            result['SchemeNameList'] = self.scheme_name_list.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = GetResultResponseBodyDataResultInfoAgent()
            self.agent = temp_model.from_map(m['Agent'])
        if m.get('AsrResult') is not None:
            temp_model = GetResultResponseBodyDataResultInfoAsrResult()
            self.asr_result = temp_model.from_map(m['AsrResult'])
        if m.get('AssignmentTime') is not None:
            self.assignment_time = m.get('AssignmentTime')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HitResult') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitResult()
            self.hit_result = temp_model.from_map(m['HitResult'])
        if m.get('HitScore') is not None:
            temp_model = GetResultResponseBodyDataResultInfoHitScore()
            self.hit_score = temp_model.from_map(m['HitScore'])
        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')
        if m.get('Recording') is not None:
            temp_model = GetResultResponseBodyDataResultInfoRecording()
            self.recording = temp_model.from_map(m['Recording'])
        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')
        if m.get('ReviewHistoryList') is not None:
            temp_model = GetResultResponseBodyDataResultInfoReviewHistoryList()
            self.review_history_list = temp_model.from_map(m['ReviewHistoryList'])
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('ReviewTimeLong') is not None:
            self.review_time_long = m.get('ReviewTimeLong')
        if m.get('ReviewType') is not None:
            self.review_type = m.get('ReviewType')
        if m.get('ReviewTypeIdList') is not None:
            temp_model = GetResultResponseBodyDataResultInfoReviewTypeIdList()
            self.review_type_id_list = temp_model.from_map(m['ReviewTypeIdList'])
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('SchemeIdList') is not None:
            temp_model = GetResultResponseBodyDataResultInfoSchemeIdList()
            self.scheme_id_list = temp_model.from_map(m['SchemeIdList'])
        if m.get('SchemeNameList') is not None:
            temp_model = GetResultResponseBodyDataResultInfoSchemeNameList()
            self.scheme_name_list = temp_model.from_map(m['SchemeNameList'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetResultResponseBodyData(TeaModel):
    def __init__(
        self,
        result_info: List[GetResultResponseBodyDataResultInfo] = None,
    ):
        self.result_info = result_info

    def validate(self):
        if self.result_info:
            for k in self.result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k in self.result_info:
                result['ResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k in m.get('ResultInfo'):
                temp_model = GetResultResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k))
        return self


class GetResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: GetResultResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = GetResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResultToReviewRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetResultToReviewResponseBodyDataDialoguesDialogue(TeaModel):
    def __init__(
        self,
        begin: int = None,
        begin_time: str = None,
        begin_time_ms: int = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        identity: str = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.begin_time = begin_time
        self.begin_time_ms = begin_time_ms
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.identity = identity
        self.role = role
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.begin_time_ms is not None:
            result['BeginTimeMs'] = self.begin_time_ms
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec
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
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('BeginTimeMs') is not None:
            self.begin_time_ms = m.get('BeginTimeMs')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')
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


class GetResultToReviewResponseBodyDataDialogues(TeaModel):
    def __init__(
        self,
        dialogue: List[GetResultToReviewResponseBodyDataDialoguesDialogue] = None,
    ):
        self.dialogue = dialogue

    def validate(self):
        if self.dialogue:
            for k in self.dialogue:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k in self.dialogue:
                result['Dialogue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k in m.get('Dialogue'):
                temp_model = GetResultToReviewResponseBodyDataDialoguesDialogue()
                self.dialogue.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories(TeaModel):
    def __init__(
        self,
        comments: str = None,
        operation_time: str = None,
        operation_type: int = None,
        operator: int = None,
        operator_name: str = None,
    ):
        self.comments = comments
        self.operation_time = operation_time
        self.operation_type = operation_type
        self.operator = operator
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories(TeaModel):
    def __init__(
        self,
        complain_histories: List[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories] = None,
    ):
        self.complain_histories = complain_histories

    def validate(self):
        if self.complain_histories:
            for k in self.complain_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplainHistories'] = []
        if self.complain_histories is not None:
            for k in self.complain_histories:
                result['ComplainHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.complain_histories = []
        if m.get('ComplainHistories') is not None:
            for k in m.get('ComplainHistories'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistoriesComplainHistories()
                self.complain_histories.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid(TeaModel):
    def __init__(
        self,
        cid: List[str] = None,
    ):
        self.cid = cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord(TeaModel):
    def __init__(
        self,
        cid: str = None,
        customize_code: str = None,
        from_: int = None,
        pid: int = None,
        tid: str = None,
        to: int = None,
        val: str = None,
    ):
        self.cid = cid
        self.customize_code = customize_code
        self.from_ = from_
        self.pid = pid
        self.tid = tid
        self.to = to
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.customize_code is not None:
            result['CustomizeCode'] = self.customize_code
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
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('CustomizeCode') is not None:
            self.customize_code = m.get('CustomizeCode')
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


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords(TeaModel):
    def __init__(
        self,
        key_word: List[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord] = None,
    ):
        self.key_word = key_word

    def validate(self):
        if self.key_word:
            for k in self.key_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyWord'] = []
        if self.key_word is not None:
            for k in self.key_word:
                result['KeyWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_word = []
        if m.get('KeyWord') is not None:
            for k in m.get('KeyWord'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWordsKeyWord()
                self.key_word.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase(TeaModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        identity: str = None,
        pid: int = None,
        role: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.identity = identity
        self.pid = pid
        self.role = role
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
        if self.identity is not None:
            result['Identity'] = self.identity
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.role is not None:
            result['Role'] = self.role
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
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo(TeaModel):
    def __init__(
        self,
        cid: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid = None,
        key_words: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords = None,
        phrase: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase = None,
    ):
        self.cid = cid
        self.key_words = key_words
        self.phrase = phrase

    def validate(self):
        if self.cid:
            self.cid.validate()
        if self.key_words:
            self.key_words.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid.to_map()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words.to_map()
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoCid()
            self.cid = temp_model.from_map(m['Cid'])
        if m.get('KeyWords') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoKeyWords()
            self.key_words = temp_model.from_map(m['KeyWords'])
        if m.get('Phrase') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList(TeaModel):
    def __init__(
        self,
        condition_hit_info: List[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo] = None,
    ):
        self.condition_hit_info = condition_hit_info

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionHitInfo'] = []
        if self.condition_hit_info is not None:
            for k in self.condition_hit_info:
                result['ConditionHitInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_hit_info = []
        if m.get('ConditionHitInfo') is not None:
            for k in m.get('ConditionHitInfo'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoListConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo(TeaModel):
    def __init__(
        self,
        hit_id: str = None,
        review_result: int = None,
        review_time: str = None,
        reviewer: str = None,
        rid: int = None,
    ):
        self.hit_id = hit_id
        self.review_result = review_result
        self.review_time = review_time
        self.reviewer = reviewer
        self.rid = rid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_id is not None:
            result['HitId'] = self.hit_id
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_time is not None:
            result['ReviewTime'] = self.review_time
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitId') is not None:
            self.hit_id = m.get('HitId')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo(TeaModel):
    def __init__(
        self,
        auto_review: int = None,
        complain_histories: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories = None,
        complainable: bool = None,
        condition_hit_info_list: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList = None,
        review_info: GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo = None,
        rid: int = None,
        rule_name: str = None,
        score_id: int = None,
        score_num: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
    ):
        self.auto_review = auto_review
        self.complain_histories = complain_histories
        self.complainable = complainable
        self.condition_hit_info_list = condition_hit_info_list
        self.review_info = review_info
        self.rid = rid
        self.rule_name = rule_name
        self.score_id = score_id
        self.score_num = score_num
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()
        if self.condition_hit_info_list:
            self.condition_hit_info_list.validate()
        if self.review_info:
            self.review_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()
        if self.complainable is not None:
            result['Complainable'] = self.complainable
        if self.condition_hit_info_list is not None:
            result['ConditionHitInfoList'] = self.condition_hit_info_list.to_map()
        if self.review_info is not None:
            result['ReviewInfo'] = self.review_info.to_map()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('ComplainHistories') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m['ComplainHistories'])
        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')
        if m.get('ConditionHitInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoConditionHitInfoList()
            self.condition_hit_info_list = temp_model.from_map(m['ConditionHitInfoList'])
        if m.get('ReviewInfo') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfoReviewInfo()
            self.review_info = temp_model.from_map(m['ReviewInfo'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        return self


class GetResultToReviewResponseBodyDataHitRuleReviewInfoList(TeaModel):
    def __init__(
        self,
        hit_rule_review_info: List[GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo] = None,
    ):
        self.hit_rule_review_info = hit_rule_review_info

    def validate(self):
        if self.hit_rule_review_info:
            for k in self.hit_rule_review_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitRuleReviewInfo'] = []
        if self.hit_rule_review_info is not None:
            for k in self.hit_rule_review_info:
                result['HitRuleReviewInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_rule_review_info = []
        if m.get('HitRuleReviewInfo') is not None:
            for k in m.get('HitRuleReviewInfo'):
                temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoListHitRuleReviewInfo()
                self.hit_rule_review_info.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories(TeaModel):
    def __init__(
        self,
        comments: str = None,
        operation_time: str = None,
        operation_type: int = None,
        operator: int = None,
        operator_name: str = None,
    ):
        self.comments = comments
        self.operation_time = operation_time
        self.operation_type = operation_type
        self.operator = operator
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories(TeaModel):
    def __init__(
        self,
        complain_histories: List[GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories] = None,
    ):
        self.complain_histories = complain_histories

    def validate(self):
        if self.complain_histories:
            for k in self.complain_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComplainHistories'] = []
        if self.complain_histories is not None:
            for k in self.complain_histories:
                result['ComplainHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.complain_histories = []
        if m.get('ComplainHistories') is not None:
            for k in m.get('ComplainHistories'):
                temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistoriesComplainHistories()
                self.complain_histories.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo(TeaModel):
    def __init__(
        self,
        complain_histories: GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories = None,
        complainable: bool = None,
        score_id: int = None,
        score_num: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
    ):
        self.complain_histories = complain_histories
        self.complainable = complainable
        self.score_id = score_id
        self.score_num = score_num
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name

    def validate(self):
        if self.complain_histories:
            self.complain_histories.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complain_histories is not None:
            result['ComplainHistories'] = self.complain_histories.to_map()
        if self.complainable is not None:
            result['Complainable'] = self.complainable
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplainHistories') is not None:
            temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfoComplainHistories()
            self.complain_histories = temp_model.from_map(m['ComplainHistories'])
        if m.get('Complainable') is not None:
            self.complainable = m.get('Complainable')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        return self


class GetResultToReviewResponseBodyDataManualScoreInfoList(TeaModel):
    def __init__(
        self,
        manual_score_info: List[GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo] = None,
    ):
        self.manual_score_info = manual_score_info

    def validate(self):
        if self.manual_score_info:
            for k in self.manual_score_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManualScoreInfo'] = []
        if self.manual_score_info is not None:
            for k in self.manual_score_info:
                result['ManualScoreInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.manual_score_info = []
        if m.get('ManualScoreInfo') is not None:
            for k in m.get('ManualScoreInfo'):
                temp_model = GetResultToReviewResponseBodyDataManualScoreInfoListManualScoreInfo()
                self.manual_score_info.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['rid'] = self.rid
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rid') is not None:
            self.rid = m.get('rid')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRule(TeaModel):
    def __init__(
        self,
        review_right_rule: List[GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule] = None,
    ):
        self.review_right_rule = review_right_rule

    def validate(self):
        if self.review_right_rule:
            for k in self.review_right_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewRightRule'] = []
        if self.review_right_rule is not None:
            for k in self.review_right_rule:
                result['ReviewRightRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_right_rule = []
        if m.get('ReviewRightRule') is not None:
            for k in m.get('ReviewRightRule'):
                temp_model = GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRuleReviewRightRule()
                self.review_right_rule.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory(TeaModel):
    def __init__(
        self,
        comments: str = None,
        complain_result: int = None,
        old_score: int = None,
        operator: int = None,
        operator_name: str = None,
        review_manager_type: str = None,
        review_result: int = None,
        review_right_rule: GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRule = None,
        score: int = None,
        time: int = None,
        time_str: str = None,
        type: int = None,
    ):
        self.comments = comments
        self.complain_result = complain_result
        self.old_score = old_score
        self.operator = operator
        self.operator_name = operator_name
        self.review_manager_type = review_manager_type
        self.review_result = review_result
        self.review_right_rule = review_right_rule
        self.score = score
        self.time = time
        self.time_str = time_str
        self.type = type

    def validate(self):
        if self.review_right_rule:
            self.review_right_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.complain_result is not None:
            result['ComplainResult'] = self.complain_result
        if self.old_score is not None:
            result['OldScore'] = self.old_score
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.review_manager_type is not None:
            result['ReviewManagerType'] = self.review_manager_type
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_right_rule is not None:
            result['ReviewRightRule'] = self.review_right_rule.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.time is not None:
            result['Time'] = self.time
        if self.time_str is not None:
            result['TimeStr'] = self.time_str
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ComplainResult') is not None:
            self.complain_result = m.get('ComplainResult')
        if m.get('OldScore') is not None:
            self.old_score = m.get('OldScore')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('ReviewManagerType') is not None:
            self.review_manager_type = m.get('ReviewManagerType')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewRightRule') is not None:
            temp_model = GetResultToReviewResponseBodyDataReviewHistoryListReviewHistoryReviewRightRule()
            self.review_right_rule = temp_model.from_map(m['ReviewRightRule'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TimeStr') is not None:
            self.time_str = m.get('TimeStr')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResultToReviewResponseBodyDataReviewHistoryList(TeaModel):
    def __init__(
        self,
        review_history: List[GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory] = None,
    ):
        self.review_history = review_history

    def validate(self):
        if self.review_history:
            for k in self.review_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewHistory'] = []
        if self.review_history is not None:
            for k in self.review_history:
                result['ReviewHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_history = []
        if m.get('ReviewHistory') is not None:
            for k in m.get('ReviewHistory'):
                temp_model = GetResultToReviewResponseBodyDataReviewHistoryListReviewHistory()
                self.review_history.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdListReviewKeyIdList(TeaModel):
    def __init__(
        self,
        review_key_id_list: List[int] = None,
    ):
        self.review_key_id_list = review_key_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_key_id_list is not None:
            result['ReviewKeyIdList'] = self.review_key_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeyIdList') is not None:
            self.review_key_id_list = m.get('ReviewKeyIdList')
        return self


class GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdList(TeaModel):
    def __init__(
        self,
        review_key_id_list: GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdListReviewKeyIdList = None,
        review_type_id: int = None,
    ):
        self.review_key_id_list = review_key_id_list
        self.review_type_id = review_type_id

    def validate(self):
        if self.review_key_id_list:
            self.review_key_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_key_id_list is not None:
            result['ReviewKeyIdList'] = self.review_key_id_list.to_map()
        if self.review_type_id is not None:
            result['ReviewTypeId'] = self.review_type_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeyIdList') is not None:
            temp_model = GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdListReviewKeyIdList()
            self.review_key_id_list = temp_model.from_map(m['ReviewKeyIdList'])
        if m.get('ReviewTypeId') is not None:
            self.review_type_id = m.get('ReviewTypeId')
        return self


class GetResultToReviewResponseBodyDataReviewTypeIdList(TeaModel):
    def __init__(
        self,
        review_type_id_list: List[GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdList] = None,
    ):
        self.review_type_id_list = review_type_id_list

    def validate(self):
        if self.review_type_id_list:
            for k in self.review_type_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReviewTypeIdList'] = []
        if self.review_type_id_list is not None:
            for k in self.review_type_id_list:
                result['ReviewTypeIdList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.review_type_id_list = []
        if m.get('ReviewTypeIdList') is not None:
            for k in m.get('ReviewTypeIdList'):
                temp_model = GetResultToReviewResponseBodyDataReviewTypeIdListReviewTypeIdList()
                self.review_type_id_list.append(temp_model.from_map(k))
        return self


class GetResultToReviewResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_scheme: str = None,
        audio_url: str = None,
        comments: str = None,
        dialogues: GetResultToReviewResponseBodyDataDialogues = None,
        file_id: str = None,
        file_merge_name: str = None,
        hit_rule_review_info_list: GetResultToReviewResponseBodyDataHitRuleReviewInfoList = None,
        manual_score_info_list: GetResultToReviewResponseBodyDataManualScoreInfoList = None,
        review_history_list: GetResultToReviewResponseBodyDataReviewHistoryList = None,
        review_type_id_list: GetResultToReviewResponseBodyDataReviewTypeIdList = None,
        status: int = None,
        total_score: int = None,
        vid: str = None,
    ):
        self.audio_scheme = audio_scheme
        self.audio_url = audio_url
        self.comments = comments
        self.dialogues = dialogues
        self.file_id = file_id
        self.file_merge_name = file_merge_name
        self.hit_rule_review_info_list = hit_rule_review_info_list
        self.manual_score_info_list = manual_score_info_list
        self.review_history_list = review_history_list
        self.review_type_id_list = review_type_id_list
        self.status = status
        self.total_score = total_score
        self.vid = vid

    def validate(self):
        if self.dialogues:
            self.dialogues.validate()
        if self.hit_rule_review_info_list:
            self.hit_rule_review_info_list.validate()
        if self.manual_score_info_list:
            self.manual_score_info_list.validate()
        if self.review_history_list:
            self.review_history_list.validate()
        if self.review_type_id_list:
            self.review_type_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_scheme is not None:
            result['AudioScheme'] = self.audio_scheme
        if self.audio_url is not None:
            result['AudioURL'] = self.audio_url
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.dialogues is not None:
            result['Dialogues'] = self.dialogues.to_map()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_merge_name is not None:
            result['FileMergeName'] = self.file_merge_name
        if self.hit_rule_review_info_list is not None:
            result['HitRuleReviewInfoList'] = self.hit_rule_review_info_list.to_map()
        if self.manual_score_info_list is not None:
            result['ManualScoreInfoList'] = self.manual_score_info_list.to_map()
        if self.review_history_list is not None:
            result['ReviewHistoryList'] = self.review_history_list.to_map()
        if self.review_type_id_list is not None:
            result['ReviewTypeIdList'] = self.review_type_id_list.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.total_score is not None:
            result['TotalScore'] = self.total_score
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioScheme') is not None:
            self.audio_scheme = m.get('AudioScheme')
        if m.get('AudioURL') is not None:
            self.audio_url = m.get('AudioURL')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Dialogues') is not None:
            temp_model = GetResultToReviewResponseBodyDataDialogues()
            self.dialogues = temp_model.from_map(m['Dialogues'])
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileMergeName') is not None:
            self.file_merge_name = m.get('FileMergeName')
        if m.get('HitRuleReviewInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataHitRuleReviewInfoList()
            self.hit_rule_review_info_list = temp_model.from_map(m['HitRuleReviewInfoList'])
        if m.get('ManualScoreInfoList') is not None:
            temp_model = GetResultToReviewResponseBodyDataManualScoreInfoList()
            self.manual_score_info_list = temp_model.from_map(m['ManualScoreInfoList'])
        if m.get('ReviewHistoryList') is not None:
            temp_model = GetResultToReviewResponseBodyDataReviewHistoryList()
            self.review_history_list = temp_model.from_map(m['ReviewHistoryList'])
        if m.get('ReviewTypeIdList') is not None:
            temp_model = GetResultToReviewResponseBodyDataReviewTypeIdList()
            self.review_type_id_list = temp_model.from_map(m['ReviewTypeIdList'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalScore') is not None:
            self.total_score = m.get('TotalScore')
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetResultToReviewResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetResultToReviewResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetResultToReviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResultToReviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResultToReviewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResultToReviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList(TeaModel):
    def __init__(
        self,
        business_category_name_list: List[str] = None,
    ):
        self.business_category_name_list = business_category_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        return self


class GetRuleResponseBodyDataRulesRuleInfo(TeaModel):
    def __init__(
        self,
        auto_review: int = None,
        business_category_name_list: GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList = None,
        comments: str = None,
        create_empid: str = None,
        create_time: str = None,
        end_time: str = None,
        is_delete: int = None,
        is_online: int = None,
        last_update_empid: str = None,
        last_update_time: str = None,
        name: str = None,
        rid: str = None,
        rule_lambda: str = None,
        rule_score_type: int = None,
        score_id: int = None,
        score_name: str = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
        start_time: str = None,
        status: int = None,
        type: int = None,
        weight: str = None,
    ):
        self.auto_review = auto_review
        self.business_category_name_list = business_category_name_list
        self.comments = comments
        self.create_empid = create_empid
        self.create_time = create_time
        self.end_time = end_time
        self.is_delete = is_delete
        self.is_online = is_online
        self.last_update_empid = last_update_empid
        self.last_update_time = last_update_time
        self.name = name
        self.rid = rid
        self.rule_lambda = rule_lambda
        self.rule_score_type = rule_score_type
        self.score_id = score_id
        self.score_name = score_name
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name
        self.start_time = start_time
        self.status = status
        self.type = type
        self.weight = weight

    def validate(self):
        if self.business_category_name_list:
            self.business_category_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_review is not None:
            result['AutoReview'] = self.auto_review
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list.to_map()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.is_online is not None:
            result['IsOnline'] = self.is_online
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_lambda is not None:
            result['RuleLambda'] = self.rule_lambda
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReview') is not None:
            self.auto_review = m.get('AutoReview')
        if m.get('BusinessCategoryNameList') is not None:
            temp_model = GetRuleResponseBodyDataRulesRuleInfoBusinessCategoryNameList()
            self.business_category_name_list = temp_model.from_map(m['BusinessCategoryNameList'])
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('IsOnline') is not None:
            self.is_online = m.get('IsOnline')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class GetRuleResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        rule_info: List[GetRuleResponseBodyDataRulesRuleInfo] = None,
    ):
        self.rule_info = rule_info

    def validate(self):
        if self.rule_info:
            for k in self.rule_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleInfo'] = []
        if self.rule_info is not None:
            for k in self.rule_info:
                result['RuleInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_info = []
        if m.get('RuleInfo') is not None:
            for k in m.get('RuleInfo'):
                temp_model = GetRuleResponseBodyDataRulesRuleInfo()
                self.rule_info.append(temp_model.from_map(k))
        return self


class GetRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rules: GetRuleResponseBodyDataRules = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rules') is not None:
            temp_model = GetRuleResponseBodyDataRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class GetRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRuleResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleByIdRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetRuleByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RulesInfo = None,
        http_status_code: int = None,
        message: str = None,
        messages: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages
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
            temp_model = RulesInfo()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleCategoryRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleCategoryResponseBodyDataRuleCountInfo(TeaModel):
    def __init__(
        self,
        select: bool = None,
        type: int = None,
        type_name: str = None,
    ):
        self.select = select
        self.type = type
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetRuleCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_count_info: List[GetRuleCategoryResponseBodyDataRuleCountInfo] = None,
    ):
        self.rule_count_info = rule_count_info

    def validate(self):
        if self.rule_count_info:
            for k in self.rule_count_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleCountInfo'] = []
        if self.rule_count_info is not None:
            for k in self.rule_count_info:
                result['RuleCountInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_count_info = []
        if m.get('RuleCountInfo') is not None:
            for k in m.get('RuleCountInfo'):
                temp_model = GetRuleCategoryResponseBodyDataRuleCountInfo()
                self.rule_count_info.append(temp_model.from_map(k))
        return self


class GetRuleCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRuleCategoryResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleCategoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleDetailRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange(TeaModel):
    def __init__(
        self,
        absolute: bool = None,
        anchor: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor = None,
        range: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeAnchor()
            self.anchor = temp_model.from_map(m['Anchor'])
        if m.get('Range') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRangeRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo(TeaModel):
    def __init__(
        self,
        ant_model_info: List[str] = None,
    ):
        self.ant_model_info = ant_model_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ant_model_info is not None:
            result['AntModelInfo'] = self.ant_model_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntModelInfo') is not None:
            self.ant_model_info = m.get('AntModelInfo')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes(TeaModel):
    def __init__(
        self,
        excludes: List[str] = None,
    ):
        self.excludes = excludes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Excludes') is not None:
            self.excludes = m.get('Excludes')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords(TeaModel):
    def __init__(
        self,
        oper_key_word: List[str] = None,
    ):
        self.oper_key_word = oper_key_word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oper_key_word is not None:
            result['OperKeyWord'] = self.oper_key_word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperKeyWord') is not None:
            self.oper_key_word = m.get('OperKeyWord')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues(TeaModel):
    def __init__(
        self,
        pvalues: List[str] = None,
    ):
        self.pvalues = pvalues

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pvalues is not None:
            result['Pvalues'] = self.pvalues
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pvalues') is not None:
            self.pvalues = m.get('Pvalues')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences(TeaModel):
    def __init__(
        self,
        reference: List[str] = None,
    ):
        self.reference = reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference is not None:
            result['Reference'] = self.reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reference') is not None:
            self.reference = m.get('Reference')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences(TeaModel):
    def __init__(
        self,
        similarly_sentence: List[str] = None,
    ):
        self.similarly_sentence = similarly_sentence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.similarly_sentence is not None:
            result['SimilarlySentence'] = self.similarly_sentence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SimilarlySentence') is not None:
            self.similarly_sentence = m.get('SimilarlySentence')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam(TeaModel):
    def __init__(
        self,
        ant_model_info: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo = None,
        average: bool = None,
        begin_type: str = None,
        check_type: int = None,
        compare_operator: str = None,
        context_chat_match: bool = None,
        delay_time: int = None,
        different_role: bool = None,
        excludes: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes = None,
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
        oper_key_words: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords = None,
        phrase: str = None,
        pvalues: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues = None,
        references: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences = None,
        regex: str = None,
        score: int = None,
        similarity_threshold: float = None,
        similarly_sentences: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamAntModelInfo()
            self.ant_model_info = temp_model.from_map(m['AntModelInfo'])
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
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamExcludes()
            self.excludes = temp_model.from_map(m['Excludes'])
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
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamOperKeyWords()
            self.oper_key_words = temp_model.from_map(m['OperKeyWords'])
        if m.get('Phrase') is not None:
            self.phrase = m.get('Phrase')
        if m.get('Pvalues') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamPvalues()
            self.pvalues = temp_model.from_map(m['Pvalues'])
        if m.get('References') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamReferences()
            self.references = temp_model.from_map(m['References'])
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Similarity_threshold') is not None:
            self.similarity_threshold = m.get('Similarity_threshold')
        if m.get('SimilarlySentences') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParamSimilarlySentences()
            self.similarly_sentences = temp_model.from_map(m['SimilarlySentences'])
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VelocityInMint') is not None:
            self.velocity_in_mint = m.get('VelocityInMint')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo(TeaModel):
    def __init__(
        self,
        oid: str = None,
        oper_name: str = None,
        param: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfoParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators(TeaModel):
    def __init__(
        self,
        operator_basic_info: List[GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo] = None,
    ):
        self.operator_basic_info = operator_basic_info

    def validate(self):
        if self.operator_basic_info:
            for k in self.operator_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperatorBasicInfo'] = []
        if self.operator_basic_info is not None:
            for k in self.operator_basic_info:
                result['OperatorBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operator_basic_info = []
        if m.get('OperatorBasicInfo') is not None:
            for k in m.get('OperatorBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperatorsOperatorBasicInfo()
                self.operator_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyDataConditionsConditionBasicInfo(TeaModel):
    def __init__(
        self,
        check_range: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange = None,
        condition_info_cid: str = None,
        oper_lambda: str = None,
        operators: GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoCheckRange()
            self.check_range = temp_model.from_map(m['CheckRange'])
        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')
        if m.get('OperLambda') is not None:
            self.oper_lambda = m.get('OperLambda')
        if m.get('Operators') is not None:
            temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfoOperators()
            self.operators = temp_model.from_map(m['Operators'])
        return self


class GetRuleDetailResponseBodyDataConditions(TeaModel):
    def __init__(
        self,
        condition_basic_info: List[GetRuleDetailResponseBodyDataConditionsConditionBasicInfo] = None,
    ):
        self.condition_basic_info = condition_basic_info

    def validate(self):
        if self.condition_basic_info:
            for k in self.condition_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionBasicInfo'] = []
        if self.condition_basic_info is not None:
            for k in self.condition_basic_info:
                result['ConditionBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_basic_info = []
        if m.get('ConditionBasicInfo') is not None:
            for k in m.get('ConditionBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataConditionsConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories(TeaModel):
    def __init__(
        self,
        business_category_basic_info: List[GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo] = None,
    ):
        self.business_category_basic_info = business_category_basic_info

    def validate(self):
        if self.business_category_basic_info:
            for k in self.business_category_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BusinessCategoryBasicInfo'] = []
        if self.business_category_basic_info is not None:
            for k in self.business_category_basic_info:
                result['BusinessCategoryBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.business_category_basic_info = []
        if m.get('BusinessCategoryBasicInfo') is not None:
            for k in m.get('BusinessCategoryBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategoriesBusinessCategoryBasicInfo()
                self.business_category_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers(TeaModel):
    def __init__(
        self,
        trigger: List[str] = None,
    ):
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        return self


class GetRuleDetailResponseBodyDataRulesRuleBasicInfo(TeaModel):
    def __init__(
        self,
        business_categories: GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories = None,
        rid: str = None,
        rule_lambda: str = None,
        triggers: GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoBusinessCategories()
            self.business_categories = temp_model.from_map(m['BusinessCategories'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleLambda') is not None:
            self.rule_lambda = m.get('RuleLambda')
        if m.get('Triggers') is not None:
            temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfoTriggers()
            self.triggers = temp_model.from_map(m['Triggers'])
        return self


class GetRuleDetailResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        rule_basic_info: List[GetRuleDetailResponseBodyDataRulesRuleBasicInfo] = None,
    ):
        self.rule_basic_info = rule_basic_info

    def validate(self):
        if self.rule_basic_info:
            for k in self.rule_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleBasicInfo'] = []
        if self.rule_basic_info is not None:
            for k in self.rule_basic_info:
                result['RuleBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_basic_info = []
        if m.get('RuleBasicInfo') is not None:
            for k in m.get('RuleBasicInfo'):
                temp_model = GetRuleDetailResponseBodyDataRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k))
        return self


class GetRuleDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        conditions: GetRuleDetailResponseBodyDataConditions = None,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        rules: GetRuleDetailResponseBodyDataRules = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyDataConditions()
            self.conditions = temp_model.from_map(m['Conditions'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rules') is not None:
            temp_model = GetRuleDetailResponseBodyDataRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class GetRuleDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRuleDetailResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleV4Request(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetRuleV4ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RulesInfo = None,
        http_status_code: int = None,
        message: str = None,
        messages: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages
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
            temp_model = RulesInfo()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRuleV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRuleV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRuleV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRulesCountListRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        business_name: str = None,
        business_range: int = None,
        category_name: str = None,
        count_total: bool = None,
        create_empid: str = None,
        create_user_id: int = None,
        current_page: int = None,
        end_time: str = None,
        last_update_empid: str = None,
        page_number: int = None,
        page_size: int = None,
        require_infos: List[str] = None,
        rid: int = None,
        rule_id_or_rule_name: str = None,
        rule_score_single_type: int = None,
        rule_type: int = None,
        scheme_id: int = None,
        source_type: int = None,
        start_time: str = None,
        status: int = None,
        type: int = None,
        type_name: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        update_user_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.business_name = business_name
        self.business_range = business_range
        self.category_name = category_name
        self.count_total = count_total
        self.create_empid = create_empid
        self.create_user_id = create_user_id
        self.current_page = current_page
        self.end_time = end_time
        self.last_update_empid = last_update_empid
        self.page_number = page_number
        self.page_size = page_size
        self.require_infos = require_infos
        self.rid = rid
        self.rule_id_or_rule_name = rule_id_or_rule_name
        self.rule_score_single_type = rule_score_single_type
        self.rule_type = rule_type
        self.scheme_id = scheme_id
        self.source_type = source_type
        self.start_time = start_time
        self.status = status
        self.type = type
        self.type_name = type_name
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.update_user_id = update_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.business_range is not None:
            result['BusinessRange'] = self.business_range
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.count_total is not None:
            result['CountTotal'] = self.count_total
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.require_infos is not None:
            result['RequireInfos'] = self.require_infos
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_id_or_rule_name is not None:
            result['RuleIdOrRuleName'] = self.rule_id_or_rule_name
        if self.rule_score_single_type is not None:
            result['RuleScoreSingleType'] = self.rule_score_single_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.update_end_time is not None:
            result['UpdateEndTime'] = self.update_end_time
        if self.update_start_time is not None:
            result['UpdateStartTime'] = self.update_start_time
        if self.update_user_id is not None:
            result['UpdateUserId'] = self.update_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('BusinessRange') is not None:
            self.business_range = m.get('BusinessRange')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CountTotal') is not None:
            self.count_total = m.get('CountTotal')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequireInfos') is not None:
            self.require_infos = m.get('RequireInfos')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleIdOrRuleName') is not None:
            self.rule_id_or_rule_name = m.get('RuleIdOrRuleName')
        if m.get('RuleScoreSingleType') is not None:
            self.rule_score_single_type = m.get('RuleScoreSingleType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UpdateEndTime') is not None:
            self.update_end_time = m.get('UpdateEndTime')
        if m.get('UpdateStartTime') is not None:
            self.update_start_time = m.get('UpdateStartTime')
        if m.get('UpdateUserId') is not None:
            self.update_user_id = m.get('UpdateUserId')
        return self


class GetRulesCountListResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetRulesCountListResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class GetRulesCountListResponseBody(TeaModel):
    def __init__(
        self,
        business_type: int = None,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: GetRulesCountListResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        messages: GetRulesCountListResponseBodyMessages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.business_type = business_type
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = GetRulesCountListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = GetRulesCountListResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetRulesCountListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRulesCountListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRulesCountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScoreInfoRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam(TeaModel):
    def __init__(
        self,
        score_num: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
        score_type: int = None,
    ):
        self.score_num = score_num
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name
        self.score_type = score_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id
        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')
        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        return self


class GetScoreInfoResponseBodyDataScorePoScoreInfos(TeaModel):
    def __init__(
        self,
        score_param: List[GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam] = None,
    ):
        self.score_param = score_param

    def validate(self):
        if self.score_param:
            for k in self.score_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScoreParam'] = []
        if self.score_param is not None:
            for k in self.score_param:
                result['ScoreParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.score_param = []
        if m.get('ScoreParam') is not None:
            for k in m.get('ScoreParam'):
                temp_model = GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam()
                self.score_param.append(temp_model.from_map(k))
        return self


class GetScoreInfoResponseBodyDataScorePo(TeaModel):
    def __init__(
        self,
        score_id: int = None,
        score_infos: GetScoreInfoResponseBodyDataScorePoScoreInfos = None,
        score_name: str = None,
    ):
        self.score_id = score_id
        self.score_infos = score_infos
        self.score_name = score_name

    def validate(self):
        if self.score_infos:
            self.score_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score_id is not None:
            result['ScoreId'] = self.score_id
        if self.score_infos is not None:
            result['ScoreInfos'] = self.score_infos.to_map()
        if self.score_name is not None:
            result['ScoreName'] = self.score_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')
        if m.get('ScoreInfos') is not None:
            temp_model = GetScoreInfoResponseBodyDataScorePoScoreInfos()
            self.score_infos = temp_model.from_map(m['ScoreInfos'])
        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')
        return self


class GetScoreInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        score_po: List[GetScoreInfoResponseBodyDataScorePo] = None,
    ):
        self.score_po = score_po

    def validate(self):
        if self.score_po:
            for k in self.score_po:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScorePo'] = []
        if self.score_po is not None:
            for k in self.score_po:
                result['ScorePo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.score_po = []
        if m.get('ScorePo') is not None:
            for k in m.get('ScorePo'):
                temp_model = GetScoreInfoResponseBodyDataScorePo()
                self.score_po.append(temp_model.from_map(k))
        return self


class GetScoreInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetScoreInfoResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetScoreInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScoreInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetScoreInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetScoreInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetSkillGroupConfigResponseBodyDataAllRuleList(TeaModel):
    def __init__(
        self,
        rule_name_info: List[GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo] = None,
    ):
        self.rule_name_info = rule_name_info

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = GetSkillGroupConfigResponseBodyDataAllRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetSkillGroupConfigResponseBodyDataRuleList(TeaModel):
    def __init__(
        self,
        rule_name_info: List[GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo] = None,
    ):
        self.rule_name_info = rule_name_info

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = GetSkillGroupConfigResponseBodyDataRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class GetSkillGroupConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        all_content_quality_check: int = None,
        all_rids: str = None,
        all_rule_list: GetSkillGroupConfigResponseBodyDataAllRuleList = None,
        create_time: str = None,
        id: int = None,
        instance_id: str = None,
        model_id: int = None,
        model_name: str = None,
        name: str = None,
        quality_check_type: int = None,
        rid: str = None,
        rule_list: GetSkillGroupConfigResponseBodyDataRuleList = None,
        skill_group_from: int = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
        status: int = None,
        type: int = None,
        update_time: str = None,
        vocab_id: int = None,
        vocab_name: str = None,
    ):
        self.all_content_quality_check = all_content_quality_check
        self.all_rids = all_rids
        self.all_rule_list = all_rule_list
        self.create_time = create_time
        self.id = id
        self.instance_id = instance_id
        self.model_id = model_id
        self.model_name = model_name
        self.name = name
        self.quality_check_type = quality_check_type
        self.rid = rid
        self.rule_list = rule_list
        self.skill_group_from = skill_group_from
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.status = status
        self.type = type
        self.update_time = update_time
        self.vocab_id = vocab_id
        self.vocab_name = vocab_name

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check
        if self.all_rids is not None:
            result['AllRids'] = self.all_rids
        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')
        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')
        if m.get('AllRuleList') is not None:
            temp_model = GetSkillGroupConfigResponseBodyDataAllRuleList()
            self.all_rule_list = temp_model.from_map(m['AllRuleList'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleList') is not None:
            temp_model = GetSkillGroupConfigResponseBodyDataRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')
        return self


class GetSkillGroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSkillGroupConfigResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSkillGroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSkillGroupConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSyncResultRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetSyncResultResponseBodyDataAgent(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        skill_group: str = None,
    ):
        self.id = id
        self.name = name
        self.skill_group = skill_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        return self


class GetSyncResultResponseBodyDataAsrResult(TeaModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.role = role
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
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
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetSyncResultResponseBodyDataHitResultHitsKeyWords(TeaModel):
    def __init__(
        self,
        cid: str = None,
        from_: int = None,
        to: int = None,
        val: str = None,
    ):
        self.cid = cid
        self.from_ = from_
        self.to = to
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.from_ is not None:
            result['From'] = self.from_
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
        if m.get('To') is not None:
            self.to = m.get('To')
        if m.get('Val') is not None:
            self.val = m.get('Val')
        return self


class GetSyncResultResponseBodyDataHitResultHitsPhrase(TeaModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        silence_duration: int = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.role = role
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end is not None:
            result['End'] = self.end
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
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Words') is not None:
            self.words = m.get('Words')
        return self


class GetSyncResultResponseBodyDataHitResultHits(TeaModel):
    def __init__(
        self,
        cid: List[str] = None,
        key_words: List[GetSyncResultResponseBodyDataHitResultHitsKeyWords] = None,
        phrase: GetSyncResultResponseBodyDataHitResultHitsPhrase = None,
    ):
        self.cid = cid
        self.key_words = key_words
        self.phrase = phrase

    def validate(self):
        if self.key_words:
            for k in self.key_words:
                if k:
                    k.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        result['KeyWords'] = []
        if self.key_words is not None:
            for k in self.key_words:
                result['KeyWords'].append(k.to_map() if k else None)
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        self.key_words = []
        if m.get('KeyWords') is not None:
            for k in m.get('KeyWords'):
                temp_model = GetSyncResultResponseBodyDataHitResultHitsKeyWords()
                self.key_words.append(temp_model.from_map(k))
        if m.get('Phrase') is not None:
            temp_model = GetSyncResultResponseBodyDataHitResultHitsPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class GetSyncResultResponseBodyDataHitResult(TeaModel):
    def __init__(
        self,
        hits: List[GetSyncResultResponseBodyDataHitResultHits] = None,
        name: str = None,
        review_result: int = None,
        rid: str = None,
        type: str = None,
    ):
        self.hits = hits
        self.name = name
        self.review_result = review_result
        self.rid = rid
        self.type = type

    def validate(self):
        if self.hits:
            for k in self.hits:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hits'] = []
        if self.hits is not None:
            for k in self.hits:
                result['Hits'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hits = []
        if m.get('Hits') is not None:
            for k in m.get('Hits'):
                temp_model = GetSyncResultResponseBodyDataHitResultHits()
                self.hits.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSyncResultResponseBodyDataRecording(TeaModel):
    def __init__(
        self,
        business: str = None,
        call_id: str = None,
        call_time: str = None,
        call_type: int = None,
        callee: str = None,
        caller: str = None,
        data_set_name: str = None,
        duration: int = None,
        duration_audio: int = None,
        id: str = None,
        name: str = None,
        primary_id: str = None,
        remark_1: str = None,
        remark_2: str = None,
        remark_3: str = None,
        url: str = None,
    ):
        self.business = business
        self.call_id = call_id
        self.call_time = call_time
        self.call_type = call_type
        self.callee = callee
        self.caller = caller
        self.data_set_name = data_set_name
        self.duration = duration
        self.duration_audio = duration_audio
        self.id = id
        self.name = name
        self.primary_id = primary_id
        self.remark_1 = remark_1
        self.remark_2 = remark_2
        self.remark_3 = remark_3
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.duration_audio is not None:
            result['DurationAudio'] = self.duration_audio
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.primary_id is not None:
            result['PrimaryId'] = self.primary_id
        if self.remark_1 is not None:
            result['Remark1'] = self.remark_1
        if self.remark_2 is not None:
            result['Remark2'] = self.remark_2
        if self.remark_3 is not None:
            result['Remark3'] = self.remark_3
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DurationAudio') is not None:
            self.duration_audio = m.get('DurationAudio')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrimaryId') is not None:
            self.primary_id = m.get('PrimaryId')
        if m.get('Remark1') is not None:
            self.remark_1 = m.get('Remark1')
        if m.get('Remark2') is not None:
            self.remark_2 = m.get('Remark2')
        if m.get('Remark3') is not None:
            self.remark_3 = m.get('Remark3')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetSyncResultResponseBodyData(TeaModel):
    def __init__(
        self,
        agent: GetSyncResultResponseBodyDataAgent = None,
        asr_result: List[GetSyncResultResponseBodyDataAsrResult] = None,
        comments: str = None,
        create_time: str = None,
        error_message: str = None,
        hit_result: List[GetSyncResultResponseBodyDataHitResult] = None,
        recording: GetSyncResultResponseBodyDataRecording = None,
        resolver: str = None,
        review_result: int = None,
        review_status: int = None,
        reviewer: str = None,
        score: int = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.agent = agent
        self.asr_result = asr_result
        self.comments = comments
        self.create_time = create_time
        self.error_message = error_message
        self.hit_result = hit_result
        self.recording = recording
        self.resolver = resolver
        self.review_result = review_result
        self.review_status = review_status
        self.reviewer = reviewer
        self.score = score
        self.status = status
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.asr_result:
            for k in self.asr_result:
                if k:
                    k.validate()
        if self.hit_result:
            for k in self.hit_result:
                if k:
                    k.validate()
        if self.recording:
            self.recording.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        result['AsrResult'] = []
        if self.asr_result is not None:
            for k in self.asr_result:
                result['AsrResult'].append(k.to_map() if k else None)
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['HitResult'] = []
        if self.hit_result is not None:
            for k in self.hit_result:
                result['HitResult'].append(k.to_map() if k else None)
        if self.recording is not None:
            result['Recording'] = self.recording.to_map()
        if self.resolver is not None:
            result['Resolver'] = self.resolver
        if self.review_result is not None:
            result['ReviewResult'] = self.review_result
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.reviewer is not None:
            result['Reviewer'] = self.reviewer
        if self.score is not None:
            result['Score'] = self.score
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = GetSyncResultResponseBodyDataAgent()
            self.agent = temp_model.from_map(m['Agent'])
        self.asr_result = []
        if m.get('AsrResult') is not None:
            for k in m.get('AsrResult'):
                temp_model = GetSyncResultResponseBodyDataAsrResult()
                self.asr_result.append(temp_model.from_map(k))
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.hit_result = []
        if m.get('HitResult') is not None:
            for k in m.get('HitResult'):
                temp_model = GetSyncResultResponseBodyDataHitResult()
                self.hit_result.append(temp_model.from_map(k))
        if m.get('Recording') is not None:
            temp_model = GetSyncResultResponseBodyDataRecording()
            self.recording = temp_model.from_map(m['Recording'])
        if m.get('Resolver') is not None:
            self.resolver = m.get('Resolver')
        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('Reviewer') is not None:
            self.reviewer = m.get('Reviewer')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[GetSyncResultResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSyncResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSyncResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWarningStrategyConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyListRange(TeaModel):
    def __init__(
        self,
        range_num: int = None,
        type: int = None,
    ):
        self.range_num = range_num
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.range_num is not None:
            result['RangeNum'] = self.range_num
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RangeNum') is not None:
            self.range_num = m.get('RangeNum')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyList(TeaModel):
    def __init__(
        self,
        code: str = None,
        duration: int = None,
        duration_expression: int = None,
        hit_number: int = None,
        hit_number_expression: int = None,
        hit_rule_list: str = None,
        hit_type: int = None,
        id: int = None,
        range: GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyListRange = None,
        status: int = None,
    ):
        self.code = code
        self.duration = duration
        self.duration_expression = duration_expression
        self.hit_number = hit_number
        self.hit_number_expression = hit_number_expression
        self.hit_rule_list = hit_rule_list
        self.hit_type = hit_type
        self.id = id
        self.range = range
        self.status = status

    def validate(self):
        if self.range:
            self.range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.duration_expression is not None:
            result['DurationExpression'] = self.duration_expression
        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number
        if self.hit_number_expression is not None:
            result['HitNumberExpression'] = self.hit_number_expression
        if self.hit_rule_list is not None:
            result['HitRuleList'] = self.hit_rule_list
        if self.hit_type is not None:
            result['HitType'] = self.hit_type
        if self.id is not None:
            result['Id'] = self.id
        if self.range is not None:
            result['Range'] = self.range.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DurationExpression') is not None:
            self.duration_expression = m.get('DurationExpression')
        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')
        if m.get('HitNumberExpression') is not None:
            self.hit_number_expression = m.get('HitNumberExpression')
        if m.get('HitRuleList') is not None:
            self.hit_rule_list = m.get('HitRuleList')
        if m.get('HitType') is not None:
            self.hit_type = m.get('HitType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Range') is not None:
            temp_model = GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyListRange()
            self.range = temp_model.from_map(m['Range'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetWarningStrategyConfigResponseBodyDataWarningStrategyList(TeaModel):
    def __init__(
        self,
        warning_strategy_list: List[GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyList] = None,
    ):
        self.warning_strategy_list = warning_strategy_list

    def validate(self):
        if self.warning_strategy_list:
            for k in self.warning_strategy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['warningStrategyList'] = []
        if self.warning_strategy_list is not None:
            for k in self.warning_strategy_list:
                result['warningStrategyList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_strategy_list = []
        if m.get('warningStrategyList') is not None:
            for k in m.get('warningStrategyList'):
                temp_model = GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyList()
                self.warning_strategy_list.append(temp_model.from_map(k))
        return self


class GetWarningStrategyConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        interval_time: int = None,
        lambda_: str = None,
        level: int = None,
        max_number: int = None,
        name: str = None,
        warning_strategy_list: GetWarningStrategyConfigResponseBodyDataWarningStrategyList = None,
    ):
        self.id = id
        self.interval_time = interval_time
        self.lambda_ = lambda_
        self.level = level
        self.max_number = max_number
        self.name = name
        self.warning_strategy_list = warning_strategy_list

    def validate(self):
        if self.warning_strategy_list:
            self.warning_strategy_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.level is not None:
            result['Level'] = self.level
        if self.max_number is not None:
            result['MaxNumber'] = self.max_number
        if self.name is not None:
            result['Name'] = self.name
        if self.warning_strategy_list is not None:
            result['WarningStrategyList'] = self.warning_strategy_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MaxNumber') is not None:
            self.max_number = m.get('MaxNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WarningStrategyList') is not None:
            temp_model = GetWarningStrategyConfigResponseBodyDataWarningStrategyList()
            self.warning_strategy_list = temp_model.from_map(m['WarningStrategyList'])
        return self


class GetWarningStrategyConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetWarningStrategyConfigResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetWarningStrategyConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWarningStrategyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWarningStrategyConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWarningStrategyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleComplaintRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class HandleComplaintResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HandleComplaintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HandleComplaintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HandleComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvalidRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class InvalidRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvalidRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvalidRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InvalidRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsrVocabRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListAsrVocabResponseBodyDataAsrVocab(TeaModel):
    def __init__(
        self,
        asr_version: int = None,
        create_time: str = None,
        id: str = None,
        model_customization_id: str = None,
        name: str = None,
        update_time: str = None,
        vocabulary_id: str = None,
    ):
        self.asr_version = asr_version
        self.create_time = create_time
        self.id = id
        self.model_customization_id = model_customization_id
        self.name = name
        self.update_time = update_time
        self.vocabulary_id = vocabulary_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.model_customization_id is not None:
            result['ModelCustomizationId'] = self.model_customization_id
        if self.name is not None:
            result['Name'] = self.name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelCustomizationId') is not None:
            self.model_customization_id = m.get('ModelCustomizationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')
        return self


class ListAsrVocabResponseBodyData(TeaModel):
    def __init__(
        self,
        asr_vocab: List[ListAsrVocabResponseBodyDataAsrVocab] = None,
    ):
        self.asr_vocab = asr_vocab

    def validate(self):
        if self.asr_vocab:
            for k in self.asr_vocab:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AsrVocab'] = []
        if self.asr_vocab is not None:
            for k in self.asr_vocab:
                result['AsrVocab'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_vocab = []
        if m.get('AsrVocab') is not None:
            for k in m.get('AsrVocab'):
                temp_model = ListAsrVocabResponseBodyDataAsrVocab()
                self.asr_vocab.append(temp_model.from_map(k))
        return self


class ListAsrVocabResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListAsrVocabResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListAsrVocabResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAsrVocabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAsrVocabResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListDataSetResponseBodyDataData(TeaModel):
    def __init__(
        self,
        auto_transcoding: int = None,
        channel_id_0: int = None,
        channel_id_1: int = None,
        channel_type: int = None,
        create_time: str = None,
        create_type: int = None,
        data_set_type: int = None,
        is_delete: int = None,
        role_config_prop: str = None,
        role_config_status: int = None,
        role_config_task: str = None,
        set_bucket_name: str = None,
        set_domain: str = None,
        set_folder_name: str = None,
        set_id: int = None,
        set_name: str = None,
        set_number: int = None,
        set_role_arn: str = None,
        set_type: int = None,
        source_data_type: int = None,
        sub_dir: str = None,
        update_time: str = None,
        user_group: str = None,
    ):
        self.auto_transcoding = auto_transcoding
        self.channel_id_0 = channel_id_0
        self.channel_id_1 = channel_id_1
        self.channel_type = channel_type
        self.create_time = create_time
        self.create_type = create_type
        self.data_set_type = data_set_type
        self.is_delete = is_delete
        self.role_config_prop = role_config_prop
        self.role_config_status = role_config_status
        self.role_config_task = role_config_task
        self.set_bucket_name = set_bucket_name
        self.set_domain = set_domain
        self.set_folder_name = set_folder_name
        self.set_id = set_id
        self.set_name = set_name
        self.set_number = set_number
        self.set_role_arn = set_role_arn
        self.set_type = set_type
        self.source_data_type = source_data_type
        self.sub_dir = sub_dir
        self.update_time = update_time
        self.user_group = user_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_transcoding is not None:
            result['AutoTranscoding'] = self.auto_transcoding
        if self.channel_id_0 is not None:
            result['ChannelId0'] = self.channel_id_0
        if self.channel_id_1 is not None:
            result['ChannelId1'] = self.channel_id_1
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.data_set_type is not None:
            result['DataSetType'] = self.data_set_type
        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete
        if self.role_config_prop is not None:
            result['RoleConfigProp'] = self.role_config_prop
        if self.role_config_status is not None:
            result['RoleConfigStatus'] = self.role_config_status
        if self.role_config_task is not None:
            result['RoleConfigTask'] = self.role_config_task
        if self.set_bucket_name is not None:
            result['SetBucketName'] = self.set_bucket_name
        if self.set_domain is not None:
            result['SetDomain'] = self.set_domain
        if self.set_folder_name is not None:
            result['SetFolderName'] = self.set_folder_name
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.set_number is not None:
            result['SetNumber'] = self.set_number
        if self.set_role_arn is not None:
            result['SetRoleArn'] = self.set_role_arn
        if self.set_type is not None:
            result['SetType'] = self.set_type
        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type
        if self.sub_dir is not None:
            result['SubDir'] = self.sub_dir
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_group is not None:
            result['UserGroup'] = self.user_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoTranscoding') is not None:
            self.auto_transcoding = m.get('AutoTranscoding')
        if m.get('ChannelId0') is not None:
            self.channel_id_0 = m.get('ChannelId0')
        if m.get('ChannelId1') is not None:
            self.channel_id_1 = m.get('ChannelId1')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DataSetType') is not None:
            self.data_set_type = m.get('DataSetType')
        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')
        if m.get('RoleConfigProp') is not None:
            self.role_config_prop = m.get('RoleConfigProp')
        if m.get('RoleConfigStatus') is not None:
            self.role_config_status = m.get('RoleConfigStatus')
        if m.get('RoleConfigTask') is not None:
            self.role_config_task = m.get('RoleConfigTask')
        if m.get('SetBucketName') is not None:
            self.set_bucket_name = m.get('SetBucketName')
        if m.get('SetDomain') is not None:
            self.set_domain = m.get('SetDomain')
        if m.get('SetFolderName') is not None:
            self.set_folder_name = m.get('SetFolderName')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('SetNumber') is not None:
            self.set_number = m.get('SetNumber')
        if m.get('SetRoleArn') is not None:
            self.set_role_arn = m.get('SetRoleArn')
        if m.get('SetType') is not None:
            self.set_type = m.get('SetType')
        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')
        if m.get('SubDir') is not None:
            self.sub_dir = m.get('SubDir')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        return self


class ListDataSetResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListDataSetResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDataSetResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListDataSetResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: ListDataSetResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        messages: ListDataSetResponseBodyMessages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListDataSetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = ListDataSetResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrecisionTaskRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        model_id: int = None,
        model_name: str = None,
        precision: float = None,
        status: int = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.model_id = model_id
        self.model_name = model_name
        self.precision = precision
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.precision is not None:
            result['Precision'] = self.precision
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Precision') is not None:
            self.precision = m.get('Precision')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions(TeaModel):
    def __init__(
        self,
        precision: List[ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision] = None,
    ):
        self.precision = precision

    def validate(self):
        if self.precision:
            for k in self.precision:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Precision'] = []
        if self.precision is not None:
            for k in self.precision:
                result['Precision'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precision = []
        if m.get('Precision') is not None:
            for k in m.get('Precision'):
                temp_model = ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisionsPrecision()
                self.precision.append(temp_model.from_map(k))
        return self


class ListPrecisionTaskResponseBodyDataPrecisionTask(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_set_id: int = None,
        data_set_name: str = None,
        duration: int = None,
        incorrect_words: int = None,
        name: str = None,
        precisions: ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions = None,
        source: int = None,
        status: int = None,
        task_id: str = None,
        total_count: int = None,
        update_time: str = None,
        verified_count: int = None,
    ):
        self.create_time = create_time
        self.data_set_id = data_set_id
        self.data_set_name = data_set_name
        self.duration = duration
        self.incorrect_words = incorrect_words
        self.name = name
        self.precisions = precisions
        self.source = source
        self.status = status
        self.task_id = task_id
        self.total_count = total_count
        self.update_time = update_time
        self.verified_count = verified_count

    def validate(self):
        if self.precisions:
            self.precisions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id
        if self.data_set_name is not None:
            result['DataSetName'] = self.data_set_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.name is not None:
            result['Name'] = self.name
        if self.precisions is not None:
            result['Precisions'] = self.precisions.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.verified_count is not None:
            result['VerifiedCount'] = self.verified_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')
        if m.get('DataSetName') is not None:
            self.data_set_name = m.get('DataSetName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Precisions') is not None:
            temp_model = ListPrecisionTaskResponseBodyDataPrecisionTaskPrecisions()
            self.precisions = temp_model.from_map(m['Precisions'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VerifiedCount') is not None:
            self.verified_count = m.get('VerifiedCount')
        return self


class ListPrecisionTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        precision_task: List[ListPrecisionTaskResponseBodyDataPrecisionTask] = None,
    ):
        self.precision_task = precision_task

    def validate(self):
        if self.precision_task:
            for k in self.precision_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrecisionTask'] = []
        if self.precision_task is not None:
            for k in self.precision_task:
                result['PrecisionTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precision_task = []
        if m.get('PrecisionTask') is not None:
            for k in m.get('PrecisionTask'):
                temp_model = ListPrecisionTaskResponseBodyDataPrecisionTask()
                self.precision_task.append(temp_model.from_map(k))
        return self


class ListPrecisionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: ListPrecisionTaskResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListPrecisionTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPrecisionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrecisionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQualityCheckSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListQualityCheckSchemeResponseBodyDataRuleListRules(TeaModel):
    def __init__(
        self,
        check_type: int = None,
        name: str = None,
        rid: int = None,
        rule_score_type: int = None,
        score_num: int = None,
        score_num_type: int = None,
        score_type: int = None,
        target_type: int = None,
    ):
        self.check_type = check_type
        self.name = name
        self.rid = rid
        self.rule_score_type = rule_score_type
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_type = score_type
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_score_type is not None:
            result['RuleScoreType'] = self.rule_score_type
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num
        if self.score_num_type is not None:
            result['ScoreNumType'] = self.score_num_type
        if self.score_type is not None:
            result['ScoreType'] = self.score_type
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleScoreType') is not None:
            self.rule_score_type = m.get('RuleScoreType')
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')
        if m.get('ScoreNumType') is not None:
            self.score_num_type = m.get('ScoreNumType')
        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListQualityCheckSchemeResponseBodyDataRuleList(TeaModel):
    def __init__(
        self,
        rules: List[ListQualityCheckSchemeResponseBodyDataRuleListRules] = None,
    ):
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListQualityCheckSchemeResponseBodyDataRuleListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class ListQualityCheckSchemeResponseBodyDataSchemeCheckTypeList(TeaModel):
    def __init__(
        self,
        check_name: str = None,
        check_type: int = None,
        enable: int = None,
        score: int = None,
        target_type: int = None,
    ):
        self.check_name = check_name
        self.check_type = check_type
        self.enable = enable
        self.score = score
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name is not None:
            result['CheckName'] = self.check_name
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.score is not None:
            result['Score'] = self.score
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListQualityCheckSchemeResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user_name: str = None,
        data_type: int = None,
        description: str = None,
        name: str = None,
        rule_list: List[ListQualityCheckSchemeResponseBodyDataRuleList] = None,
        scheme_check_type_list: List[ListQualityCheckSchemeResponseBodyDataSchemeCheckTypeList] = None,
        scheme_id: int = None,
        status: int = None,
        template_type: int = None,
        type: int = None,
        update_time: str = None,
        update_user_name: str = None,
        version: int = None,
    ):
        self.create_time = create_time
        self.create_user_name = create_user_name
        self.data_type = data_type
        self.description = description
        self.name = name
        self.rule_list = rule_list
        self.scheme_check_type_list = scheme_check_type_list
        self.scheme_id = scheme_id
        self.status = status
        self.template_type = template_type
        self.type = type
        self.update_time = update_time
        self.update_user_name = update_user_name
        self.version = version

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()
        if self.scheme_check_type_list:
            for k in self.scheme_check_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        result['SchemeCheckTypeList'] = []
        if self.scheme_check_type_list is not None:
            for k in self.scheme_check_type_list:
                result['SchemeCheckTypeList'].append(k.to_map() if k else None)
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = ListQualityCheckSchemeResponseBodyDataRuleList()
                self.rule_list.append(temp_model.from_map(k))
        self.scheme_check_type_list = []
        if m.get('SchemeCheckTypeList') is not None:
            for k in m.get('SchemeCheckTypeList'):
                temp_model = ListQualityCheckSchemeResponseBodyDataSchemeCheckTypeList()
                self.scheme_check_type_list.append(temp_model.from_map(k))
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListQualityCheckSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[ListQualityCheckSchemeResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListQualityCheckSchemeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQualityCheckSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQualityCheckSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQualityCheckSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        business_category_name_list: List[str] = None,
        comments: str = None,
        create_time: str = None,
        name: str = None,
        rid: int = None,
        rule_type: int = None,
        type: int = None,
        type_name: str = None,
    ):
        self.business_category_name_list = business_category_name_list
        self.comments = comments
        self.create_time = create_time
        self.name = name
        self.rid = rid
        self.rule_type = rule_type
        self.type = type
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_category_name_list is not None:
            result['BusinessCategoryNameList'] = self.business_category_name_list
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessCategoryNameList') is not None:
            self.business_category_name_list = m.get('BusinessCategoryNameList')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[ListRulesResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesV4Request(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        business_name: str = None,
        business_range: int = None,
        category_name: str = None,
        count_total: bool = None,
        create_empid: str = None,
        create_user_id: int = None,
        current_page: int = None,
        end_time: str = None,
        last_update_empid: str = None,
        page_number: int = None,
        page_size: int = None,
        require_infos: List[str] = None,
        rid: int = None,
        rule_id_or_rule_name: str = None,
        rule_score_single_type: int = None,
        rule_type: int = None,
        scheme_id: int = None,
        source_type: int = None,
        start_time: str = None,
        status: int = None,
        type: int = None,
        type_name: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        update_user_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.business_name = business_name
        self.business_range = business_range
        self.category_name = category_name
        self.count_total = count_total
        self.create_empid = create_empid
        self.create_user_id = create_user_id
        self.current_page = current_page
        self.end_time = end_time
        self.last_update_empid = last_update_empid
        self.page_number = page_number
        self.page_size = page_size
        self.require_infos = require_infos
        self.rid = rid
        self.rule_id_or_rule_name = rule_id_or_rule_name
        self.rule_score_single_type = rule_score_single_type
        self.rule_type = rule_type
        self.scheme_id = scheme_id
        self.source_type = source_type
        self.start_time = start_time
        self.status = status
        self.type = type
        self.type_name = type_name
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.update_user_id = update_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.business_range is not None:
            result['BusinessRange'] = self.business_range
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.count_total is not None:
            result['CountTotal'] = self.count_total
        if self.create_empid is not None:
            result['CreateEmpid'] = self.create_empid
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.last_update_empid is not None:
            result['LastUpdateEmpid'] = self.last_update_empid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.require_infos is not None:
            result['RequireInfos'] = self.require_infos
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_id_or_rule_name is not None:
            result['RuleIdOrRuleName'] = self.rule_id_or_rule_name
        if self.rule_score_single_type is not None:
            result['RuleScoreSingleType'] = self.rule_score_single_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.update_end_time is not None:
            result['UpdateEndTime'] = self.update_end_time
        if self.update_start_time is not None:
            result['UpdateStartTime'] = self.update_start_time
        if self.update_user_id is not None:
            result['UpdateUserId'] = self.update_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('BusinessRange') is not None:
            self.business_range = m.get('BusinessRange')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CountTotal') is not None:
            self.count_total = m.get('CountTotal')
        if m.get('CreateEmpid') is not None:
            self.create_empid = m.get('CreateEmpid')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LastUpdateEmpid') is not None:
            self.last_update_empid = m.get('LastUpdateEmpid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequireInfos') is not None:
            self.require_infos = m.get('RequireInfos')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleIdOrRuleName') is not None:
            self.rule_id_or_rule_name = m.get('RuleIdOrRuleName')
        if m.get('RuleScoreSingleType') is not None:
            self.rule_score_single_type = m.get('RuleScoreSingleType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('UpdateEndTime') is not None:
            self.update_end_time = m.get('UpdateEndTime')
        if m.get('UpdateStartTime') is not None:
            self.update_start_time = m.get('UpdateStartTime')
        if m.get('UpdateUserId') is not None:
            self.update_user_id = m.get('UpdateUserId')
        return self


class ListRulesV4ResponseBody(TeaModel):
    def __init__(
        self,
        business_type: int = None,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: List[RuleCountInfo] = None,
        http_status_code: int = None,
        message: str = None,
        messages: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.business_type = business_type
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = RuleCountInfo()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRulesV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRulesV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRulesV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchemeTaskConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContestListObject(TeaModel):
    def __init__(
        self,
        list_object: List[Any] = None,
    ):
        self.list_object = list_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_object is not None:
            result['ListObject'] = self.list_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListObject') is not None:
            self.list_object = m.get('ListObject')
        return self


class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContest(TeaModel):
    def __init__(
        self,
        data_type: int = None,
        list_object: ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContestListObject = None,
        name: str = None,
        symbol: int = None,
        value: str = None,
    ):
        self.data_type = data_type
        self.list_object = list_object
        self.name = name
        self.symbol = symbol
        self.value = value

    def validate(self):
        if self.list_object:
            self.list_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.list_object is not None:
            result['ListObject'] = self.list_object.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('ListObject') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContestListObject()
            self.list_object = temp_model.from_map(m['ListObject'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContests(TeaModel):
    def __init__(
        self,
        assign_config_contest: List[ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContest] = None,
    ):
        self.assign_config_contest = assign_config_contest

    def validate(self):
        if self.assign_config_contest:
            for k in self.assign_config_contest:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssignConfigContest'] = []
        if self.assign_config_contest is not None:
            for k in self.assign_config_contest:
                result['AssignConfigContest'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_config_contest = []
        if m.get('AssignConfigContest') is not None:
            for k in m.get('AssignConfigContest'):
                temp_model = ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContest()
                self.assign_config_contest.append(temp_model.from_map(k))
        return self


class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfig(TeaModel):
    def __init__(
        self,
        assign_config_contests: ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContests = None,
    ):
        self.assign_config_contests = assign_config_contests

    def validate(self):
        if self.assign_config_contests:
            self.assign_config_contests.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_config_contests is not None:
            result['AssignConfigContests'] = self.assign_config_contests.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignConfigContests') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContests()
            self.assign_config_contests = temp_model.from_map(m['AssignConfigContests'])
        return self


class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigs(TeaModel):
    def __init__(
        self,
        assign_config: List[ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfig] = None,
    ):
        self.assign_config = assign_config

    def validate(self):
        if self.assign_config:
            for k in self.assign_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssignConfig'] = []
        if self.assign_config is not None:
            for k in self.assign_config:
                result['AssignConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_config = []
        if m.get('AssignConfig') is not None:
            for k in m.get('AssignConfig'):
                temp_model = ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfig()
                self.assign_config.append(temp_model.from_map(k))
        return self


class ListSchemeTaskConfigResponseBodyDataDataDataConfig(TeaModel):
    def __init__(
        self,
        assign_configs: ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigs = None,
        data_sets: str = None,
        index: int = None,
        result_param: str = None,
    ):
        self.assign_configs = assign_configs
        self.data_sets = data_sets
        self.index = index
        self.result_param = result_param

    def validate(self):
        if self.assign_configs:
            self.assign_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_configs is not None:
            result['AssignConfigs'] = self.assign_configs.to_map()
        if self.data_sets is not None:
            result['DataSets'] = self.data_sets
        if self.index is not None:
            result['Index'] = self.index
        if self.result_param is not None:
            result['ResultParam'] = self.result_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignConfigs') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigs()
            self.assign_configs = temp_model.from_map(m['AssignConfigs'])
        if m.get('DataSets') is not None:
            self.data_sets = m.get('DataSets')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('ResultParam') is not None:
            self.result_param = m.get('ResultParam')
        return self


class ListSchemeTaskConfigResponseBodyDataDataSchemeIdList(TeaModel):
    def __init__(
        self,
        scheme_id_list: List[int] = None,
    ):
        self.scheme_id_list = scheme_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeIdList') is not None:
            self.scheme_id_list = m.get('SchemeIdList')
        return self


class ListSchemeTaskConfigResponseBodyDataDataSchemeListSchemeList(TeaModel):
    def __init__(
        self,
        name: str = None,
        scheme_id: int = None,
    ):
        self.name = name
        self.scheme_id = scheme_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        return self


class ListSchemeTaskConfigResponseBodyDataDataSchemeList(TeaModel):
    def __init__(
        self,
        scheme_list: List[ListSchemeTaskConfigResponseBodyDataDataSchemeListSchemeList] = None,
    ):
        self.scheme_list = scheme_list

    def validate(self):
        if self.scheme_list:
            for k in self.scheme_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SchemeList'] = []
        if self.scheme_list is not None:
            for k in self.scheme_list:
                result['SchemeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheme_list = []
        if m.get('SchemeList') is not None:
            for k in m.get('SchemeList'):
                temp_model = ListSchemeTaskConfigResponseBodyDataDataSchemeListSchemeList()
                self.scheme_list.append(temp_model.from_map(k))
        return self


class ListSchemeTaskConfigResponseBodyDataData(TeaModel):
    def __init__(
        self,
        asr_task_priority: int = None,
        asr_version: int = None,
        assign_type: int = None,
        create_time: str = None,
        create_user: int = None,
        data_config: ListSchemeTaskConfigResponseBodyDataDataDataConfig = None,
        finish_rate: float = None,
        id: int = None,
        manual_review: int = None,
        mode_customization_id: str = None,
        model_name: str = None,
        name: str = None,
        number_executing: int = None,
        number_fail: int = None,
        number_success: int = None,
        number_sum: int = None,
        scheme_id_list: ListSchemeTaskConfigResponseBodyDataDataSchemeIdList = None,
        scheme_list: ListSchemeTaskConfigResponseBodyDataDataSchemeList = None,
        scheme_task_config_id: int = None,
        source_data_type: int = None,
        status: int = None,
        type: int = None,
        update_time: str = None,
        update_user: int = None,
        user_group: str = None,
        vocab_id: str = None,
        vocab_name: str = None,
    ):
        self.asr_task_priority = asr_task_priority
        self.asr_version = asr_version
        self.assign_type = assign_type
        self.create_time = create_time
        self.create_user = create_user
        self.data_config = data_config
        self.finish_rate = finish_rate
        self.id = id
        self.manual_review = manual_review
        self.mode_customization_id = mode_customization_id
        self.model_name = model_name
        self.name = name
        self.number_executing = number_executing
        self.number_fail = number_fail
        self.number_success = number_success
        self.number_sum = number_sum
        self.scheme_id_list = scheme_id_list
        self.scheme_list = scheme_list
        self.scheme_task_config_id = scheme_task_config_id
        self.source_data_type = source_data_type
        self.status = status
        self.type = type
        self.update_time = update_time
        self.update_user = update_user
        self.user_group = user_group
        self.vocab_id = vocab_id
        self.vocab_name = vocab_name

    def validate(self):
        if self.data_config:
            self.data_config.validate()
        if self.scheme_id_list:
            self.scheme_id_list.validate()
        if self.scheme_list:
            self.scheme_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_task_priority is not None:
            result['AsrTaskPriority'] = self.asr_task_priority
        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version
        if self.assign_type is not None:
            result['AssignType'] = self.assign_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.data_config is not None:
            result['DataConfig'] = self.data_config.to_map()
        if self.finish_rate is not None:
            result['FinishRate'] = self.finish_rate
        if self.id is not None:
            result['Id'] = self.id
        if self.manual_review is not None:
            result['ManualReview'] = self.manual_review
        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.number_executing is not None:
            result['NumberExecuting'] = self.number_executing
        if self.number_fail is not None:
            result['NumberFail'] = self.number_fail
        if self.number_success is not None:
            result['NumberSuccess'] = self.number_success
        if self.number_sum is not None:
            result['NumberSum'] = self.number_sum
        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list.to_map()
        if self.scheme_list is not None:
            result['SchemeList'] = self.scheme_list.to_map()
        if self.scheme_task_config_id is not None:
            result['SchemeTaskConfigId'] = self.scheme_task_config_id
        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.user_group is not None:
            result['UserGroup'] = self.user_group
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrTaskPriority') is not None:
            self.asr_task_priority = m.get('AsrTaskPriority')
        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')
        if m.get('AssignType') is not None:
            self.assign_type = m.get('AssignType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DataConfig') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyDataDataDataConfig()
            self.data_config = temp_model.from_map(m['DataConfig'])
        if m.get('FinishRate') is not None:
            self.finish_rate = m.get('FinishRate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ManualReview') is not None:
            self.manual_review = m.get('ManualReview')
        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NumberExecuting') is not None:
            self.number_executing = m.get('NumberExecuting')
        if m.get('NumberFail') is not None:
            self.number_fail = m.get('NumberFail')
        if m.get('NumberSuccess') is not None:
            self.number_success = m.get('NumberSuccess')
        if m.get('NumberSum') is not None:
            self.number_sum = m.get('NumberSum')
        if m.get('SchemeIdList') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyDataDataSchemeIdList()
            self.scheme_id_list = temp_model.from_map(m['SchemeIdList'])
        if m.get('SchemeList') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyDataDataSchemeList()
            self.scheme_list = temp_model.from_map(m['SchemeList'])
        if m.get('SchemeTaskConfigId') is not None:
            self.scheme_task_config_id = m.get('SchemeTaskConfigId')
        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')
        return self


class ListSchemeTaskConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListSchemeTaskConfigResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSchemeTaskConfigResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListSchemeTaskConfigResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListSchemeTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: ListSchemeTaskConfigResponseBodyData = None,
        http_status_code: int = None,
        last_data_id: str = None,
        message: str = None,
        messages: ListSchemeTaskConfigResponseBodyMessages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.last_data_id = last_data_id
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = ListSchemeTaskConfigResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSchemeTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSchemeTaskConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSchemeTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSessionGroupRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class ListSessionGroupResponseBodyDataDataCallerList(TeaModel):
    def __init__(
        self,
        caller_list: List[str] = None,
    ):
        self.caller_list = caller_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_list is not None:
            result['CallerList'] = self.caller_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerList') is not None:
            self.caller_list = m.get('CallerList')
        return self


class ListSessionGroupResponseBodyDataDataCustomerIdList(TeaModel):
    def __init__(
        self,
        customer_id_list: List[str] = None,
    ):
        self.customer_id_list = customer_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id_list is not None:
            result['CustomerIdList'] = self.customer_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerIdList') is not None:
            self.customer_id_list = m.get('CustomerIdList')
        return self


class ListSessionGroupResponseBodyDataDataCustomerNameList(TeaModel):
    def __init__(
        self,
        customer_name_list: List[str] = None,
    ):
        self.customer_name_list = customer_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_name_list is not None:
            result['CustomerNameList'] = self.customer_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerNameList') is not None:
            self.customer_name_list = m.get('CustomerNameList')
        return self


class ListSessionGroupResponseBodyDataDataCustomerServiceIdList(TeaModel):
    def __init__(
        self,
        customer_service_id_list: List[str] = None,
    ):
        self.customer_service_id_list = customer_service_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_service_id_list is not None:
            result['CustomerServiceIdList'] = self.customer_service_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerServiceIdList') is not None:
            self.customer_service_id_list = m.get('CustomerServiceIdList')
        return self


class ListSessionGroupResponseBodyDataDataCustomerServiceNameList(TeaModel):
    def __init__(
        self,
        customer_service_name_list: List[str] = None,
    ):
        self.customer_service_name_list = customer_service_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_service_name_list is not None:
            result['CustomerServiceNameList'] = self.customer_service_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerServiceNameList') is not None:
            self.customer_service_name_list = m.get('CustomerServiceNameList')
        return self


class ListSessionGroupResponseBodyDataDataReviewerList(TeaModel):
    def __init__(
        self,
        reviewer_list: List[str] = None,
    ):
        self.reviewer_list = reviewer_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reviewer_list is not None:
            result['ReviewerList'] = self.reviewer_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewerList') is not None:
            self.reviewer_list = m.get('ReviewerList')
        return self


class ListSessionGroupResponseBodyDataDataSkillGroupNameList(TeaModel):
    def __init__(
        self,
        skill_group_name_list: List[str] = None,
    ):
        self.skill_group_name_list = skill_group_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skill_group_name_list is not None:
            result['SkillGroupNameList'] = self.skill_group_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillGroupNameList') is not None:
            self.skill_group_name_list = m.get('SkillGroupNameList')
        return self


class ListSessionGroupResponseBodyDataData(TeaModel):
    def __init__(
        self,
        assign_status: int = None,
        call_start_time: str = None,
        caller_list: ListSessionGroupResponseBodyDataDataCallerList = None,
        customer_id_list: ListSessionGroupResponseBodyDataDataCustomerIdList = None,
        customer_name_list: ListSessionGroupResponseBodyDataDataCustomerNameList = None,
        customer_service_id_list: ListSessionGroupResponseBodyDataDataCustomerServiceIdList = None,
        customer_service_name_list: ListSessionGroupResponseBodyDataDataCustomerServiceNameList = None,
        hit_session_count: int = None,
        last_data_id: str = None,
        review_status: int = None,
        reviewer_list: ListSessionGroupResponseBodyDataDataReviewerList = None,
        scheme_task_config_id: int = None,
        scheme_task_config_name: str = None,
        score: int = None,
        session_count: int = None,
        session_group_id: str = None,
        session_group_reviewed_or_complained: bool = None,
        skill_group_name_list: ListSessionGroupResponseBodyDataDataSkillGroupNameList = None,
    ):
        self.assign_status = assign_status
        self.call_start_time = call_start_time
        self.caller_list = caller_list
        self.customer_id_list = customer_id_list
        self.customer_name_list = customer_name_list
        self.customer_service_id_list = customer_service_id_list
        self.customer_service_name_list = customer_service_name_list
        self.hit_session_count = hit_session_count
        self.last_data_id = last_data_id
        self.review_status = review_status
        self.reviewer_list = reviewer_list
        self.scheme_task_config_id = scheme_task_config_id
        self.scheme_task_config_name = scheme_task_config_name
        self.score = score
        self.session_count = session_count
        self.session_group_id = session_group_id
        self.session_group_reviewed_or_complained = session_group_reviewed_or_complained
        self.skill_group_name_list = skill_group_name_list

    def validate(self):
        if self.caller_list:
            self.caller_list.validate()
        if self.customer_id_list:
            self.customer_id_list.validate()
        if self.customer_name_list:
            self.customer_name_list.validate()
        if self.customer_service_id_list:
            self.customer_service_id_list.validate()
        if self.customer_service_name_list:
            self.customer_service_name_list.validate()
        if self.reviewer_list:
            self.reviewer_list.validate()
        if self.skill_group_name_list:
            self.skill_group_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_status is not None:
            result['AssignStatus'] = self.assign_status
        if self.call_start_time is not None:
            result['CallStartTime'] = self.call_start_time
        if self.caller_list is not None:
            result['CallerList'] = self.caller_list.to_map()
        if self.customer_id_list is not None:
            result['CustomerIdList'] = self.customer_id_list.to_map()
        if self.customer_name_list is not None:
            result['CustomerNameList'] = self.customer_name_list.to_map()
        if self.customer_service_id_list is not None:
            result['CustomerServiceIdList'] = self.customer_service_id_list.to_map()
        if self.customer_service_name_list is not None:
            result['CustomerServiceNameList'] = self.customer_service_name_list.to_map()
        if self.hit_session_count is not None:
            result['HitSessionCount'] = self.hit_session_count
        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id
        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status
        if self.reviewer_list is not None:
            result['ReviewerList'] = self.reviewer_list.to_map()
        if self.scheme_task_config_id is not None:
            result['SchemeTaskConfigId'] = self.scheme_task_config_id
        if self.scheme_task_config_name is not None:
            result['SchemeTaskConfigName'] = self.scheme_task_config_name
        if self.score is not None:
            result['Score'] = self.score
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.session_group_id is not None:
            result['SessionGroupId'] = self.session_group_id
        if self.session_group_reviewed_or_complained is not None:
            result['SessionGroupReviewedOrComplained'] = self.session_group_reviewed_or_complained
        if self.skill_group_name_list is not None:
            result['SkillGroupNameList'] = self.skill_group_name_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignStatus') is not None:
            self.assign_status = m.get('AssignStatus')
        if m.get('CallStartTime') is not None:
            self.call_start_time = m.get('CallStartTime')
        if m.get('CallerList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataCallerList()
            self.caller_list = temp_model.from_map(m['CallerList'])
        if m.get('CustomerIdList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataCustomerIdList()
            self.customer_id_list = temp_model.from_map(m['CustomerIdList'])
        if m.get('CustomerNameList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataCustomerNameList()
            self.customer_name_list = temp_model.from_map(m['CustomerNameList'])
        if m.get('CustomerServiceIdList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataCustomerServiceIdList()
            self.customer_service_id_list = temp_model.from_map(m['CustomerServiceIdList'])
        if m.get('CustomerServiceNameList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataCustomerServiceNameList()
            self.customer_service_name_list = temp_model.from_map(m['CustomerServiceNameList'])
        if m.get('HitSessionCount') is not None:
            self.hit_session_count = m.get('HitSessionCount')
        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')
        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')
        if m.get('ReviewerList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataReviewerList()
            self.reviewer_list = temp_model.from_map(m['ReviewerList'])
        if m.get('SchemeTaskConfigId') is not None:
            self.scheme_task_config_id = m.get('SchemeTaskConfigId')
        if m.get('SchemeTaskConfigName') is not None:
            self.scheme_task_config_name = m.get('SchemeTaskConfigName')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('SessionGroupId') is not None:
            self.session_group_id = m.get('SessionGroupId')
        if m.get('SessionGroupReviewedOrComplained') is not None:
            self.session_group_reviewed_or_complained = m.get('SessionGroupReviewedOrComplained')
        if m.get('SkillGroupNameList') is not None:
            temp_model = ListSessionGroupResponseBodyDataDataSkillGroupNameList()
            self.skill_group_name_list = temp_model.from_map(m['SkillGroupNameList'])
        return self


class ListSessionGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListSessionGroupResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSessionGroupResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListSessionGroupResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListSessionGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: ListSessionGroupResponseBodyData = None,
        http_status_code: int = None,
        last_data_id: str = None,
        message: str = None,
        messages: ListSessionGroupResponseBodyMessages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.last_data_id = last_data_id
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListSessionGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = ListSessionGroupResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSessionGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSessionGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSessionGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSkillGroupConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList(TeaModel):
    def __init__(
        self,
        rule_name_info: List[ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo] = None,
    ):
        self.rule_name_info = rule_name_info

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList(TeaModel):
    def __init__(
        self,
        rule_name_info: List[ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo] = None,
    ):
        self.rule_name_info = rule_name_info

    def validate(self):
        if self.rule_name_info:
            for k in self.rule_name_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleNameInfo'] = []
        if self.rule_name_info is not None:
            for k in self.rule_name_info:
                result['RuleNameInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_name_info = []
        if m.get('RuleNameInfo') is not None:
            for k in m.get('RuleNameInfo'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleListRuleNameInfo()
                self.rule_name_info.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen(TeaModel):
    def __init__(
        self,
        data_type: int = None,
        name: str = None,
        symbol: int = None,
        value: str = None,
    ):
        self.data_type = data_type
        self.name = name
        self.symbol = symbol
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.name is not None:
            result['Name'] = self.name
        if self.symbol is not None:
            result['Symbol'] = self.symbol
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens(TeaModel):
    def __init__(
        self,
        skill_group_screen: List[ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen] = None,
    ):
        self.skill_group_screen = skill_group_screen

    def validate(self):
        if self.skill_group_screen:
            for k in self.skill_group_screen:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SkillGroupScreen'] = []
        if self.skill_group_screen is not None:
            for k in self.skill_group_screen:
                result['SkillGroupScreen'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.skill_group_screen = []
        if m.get('SkillGroupScreen') is not None:
            for k in m.get('SkillGroupScreen'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreensSkillGroupScreen()
                self.skill_group_screen.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBodyDataSkillGroupConfig(TeaModel):
    def __init__(
        self,
        all_content_quality_check: int = None,
        all_rids: str = None,
        all_rule_list: ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList = None,
        create_time: str = None,
        id: int = None,
        instance_id: str = None,
        model_id: int = None,
        model_name: str = None,
        name: str = None,
        quality_check_type: int = None,
        rid: str = None,
        rule_list: ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList = None,
        screen_switch: bool = None,
        skill_group_from: int = None,
        skill_group_id: str = None,
        skill_group_name: str = None,
        skill_group_screens: ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens = None,
        status: int = None,
        type: int = None,
        update_time: str = None,
        vocab_id: int = None,
        vocab_name: str = None,
    ):
        self.all_content_quality_check = all_content_quality_check
        self.all_rids = all_rids
        self.all_rule_list = all_rule_list
        self.create_time = create_time
        self.id = id
        self.instance_id = instance_id
        self.model_id = model_id
        self.model_name = model_name
        self.name = name
        self.quality_check_type = quality_check_type
        self.rid = rid
        self.rule_list = rule_list
        self.screen_switch = screen_switch
        self.skill_group_from = skill_group_from
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.skill_group_screens = skill_group_screens
        self.status = status
        self.type = type
        self.update_time = update_time
        self.vocab_id = vocab_id
        self.vocab_name = vocab_name

    def validate(self):
        if self.all_rule_list:
            self.all_rule_list.validate()
        if self.rule_list:
            self.rule_list.validate()
        if self.skill_group_screens:
            self.skill_group_screens.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_content_quality_check is not None:
            result['AllContentQualityCheck'] = self.all_content_quality_check
        if self.all_rids is not None:
            result['AllRids'] = self.all_rids
        if self.all_rule_list is not None:
            result['AllRuleList'] = self.all_rule_list.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.name is not None:
            result['Name'] = self.name
        if self.quality_check_type is not None:
            result['QualityCheckType'] = self.quality_check_type
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.screen_switch is not None:
            result['ScreenSwitch'] = self.screen_switch
        if self.skill_group_from is not None:
            result['SkillGroupFrom'] = self.skill_group_from
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.skill_group_screens is not None:
            result['SkillGroupScreens'] = self.skill_group_screens.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id
        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllContentQualityCheck') is not None:
            self.all_content_quality_check = m.get('AllContentQualityCheck')
        if m.get('AllRids') is not None:
            self.all_rids = m.get('AllRids')
        if m.get('AllRuleList') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigAllRuleList()
            self.all_rule_list = temp_model.from_map(m['AllRuleList'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QualityCheckType') is not None:
            self.quality_check_type = m.get('QualityCheckType')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleList') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('ScreenSwitch') is not None:
            self.screen_switch = m.get('ScreenSwitch')
        if m.get('SkillGroupFrom') is not None:
            self.skill_group_from = m.get('SkillGroupFrom')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('SkillGroupScreens') is not None:
            temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfigSkillGroupScreens()
            self.skill_group_screens = temp_model.from_map(m['SkillGroupScreens'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')
        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')
        return self


class ListSkillGroupConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        skill_group_config: List[ListSkillGroupConfigResponseBodyDataSkillGroupConfig] = None,
    ):
        self.skill_group_config = skill_group_config

    def validate(self):
        if self.skill_group_config:
            for k in self.skill_group_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SkillGroupConfig'] = []
        if self.skill_group_config is not None:
            for k in self.skill_group_config:
                result['SkillGroupConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.skill_group_config = []
        if m.get('SkillGroupConfig') is not None:
            for k in m.get('SkillGroupConfig'):
                temp_model = ListSkillGroupConfigResponseBodyDataSkillGroupConfig()
                self.skill_group_config.append(temp_model.from_map(k))
        return self


class ListSkillGroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSkillGroupConfigResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListSkillGroupConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSkillGroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSkillGroupConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskAssignRulesRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents(TeaModel):
    def __init__(
        self,
        agent: List[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent] = None,
    ):
        self.agent = agent

    def validate(self):
        if self.agent:
            for k in self.agent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agent'] = []
        if self.agent is not None:
            for k in self.agent:
                result['Agent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent = []
        if m.get('Agent') is not None:
            for k in m.get('Agent'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgentsAgent()
                self.agent.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer(TeaModel):
    def __init__(
        self,
        reviewer_id: str = None,
        reviewer_name: str = None,
    ):
        self.reviewer_id = reviewer_id
        self.reviewer_name = reviewer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reviewer_id is not None:
            result['ReviewerId'] = self.reviewer_id
        if self.reviewer_name is not None:
            result['ReviewerName'] = self.reviewer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewerId') is not None:
            self.reviewer_id = m.get('ReviewerId')
        if m.get('ReviewerName') is not None:
            self.reviewer_name = m.get('ReviewerName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers(TeaModel):
    def __init__(
        self,
        reviewer: List[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer] = None,
    ):
        self.reviewer = reviewer

    def validate(self):
        if self.reviewer:
            for k in self.reviewer:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Reviewer'] = []
        if self.reviewer is not None:
            for k in self.reviewer:
                result['Reviewer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reviewer = []
        if m.get('Reviewer') is not None:
            for k in m.get('Reviewer'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewersReviewer()
                self.reviewer.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        rid: str = None,
    ):
        self.name = name
        self.rid = rid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rid is not None:
            result['Rid'] = self.rid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules(TeaModel):
    def __init__(
        self,
        rule_basic_info: List[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo] = None,
    ):
        self.rule_basic_info = rule_basic_info

    def validate(self):
        if self.rule_basic_info:
            for k in self.rule_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleBasicInfo'] = []
        if self.rule_basic_info is not None:
            for k in self.rule_basic_info:
                result['RuleBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_basic_info = []
        if m.get('RuleBasicInfo') is not None:
            for k in m.get('RuleBasicInfo'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRulesRuleBasicInfo()
                self.rule_basic_info.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents(TeaModel):
    def __init__(
        self,
        sampling_mode_agent: List[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent] = None,
    ):
        self.sampling_mode_agent = sampling_mode_agent

    def validate(self):
        if self.sampling_mode_agent:
            for k in self.sampling_mode_agent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SamplingModeAgent'] = []
        if self.sampling_mode_agent is not None:
            for k in self.sampling_mode_agent:
                result['SamplingModeAgent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sampling_mode_agent = []
        if m.get('SamplingModeAgent') is not None:
            for k in m.get('SamplingModeAgent'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgentsSamplingModeAgent()
                self.sampling_mode_agent.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode(TeaModel):
    def __init__(
        self,
        any_number_of_draws: int = None,
        designated: bool = None,
        dimension: int = None,
        limit: int = None,
        number_of_draws: int = None,
        proportion: float = None,
        random_inspection_number: int = None,
        sampling_mode_agents: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents = None,
    ):
        self.any_number_of_draws = any_number_of_draws
        self.designated = designated
        self.dimension = dimension
        self.limit = limit
        self.number_of_draws = number_of_draws
        self.proportion = proportion
        self.random_inspection_number = random_inspection_number
        self.sampling_mode_agents = sampling_mode_agents

    def validate(self):
        if self.sampling_mode_agents:
            self.sampling_mode_agents.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.any_number_of_draws is not None:
            result['AnyNumberOfDraws'] = self.any_number_of_draws
        if self.designated is not None:
            result['Designated'] = self.designated
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.number_of_draws is not None:
            result['NumberOfDraws'] = self.number_of_draws
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.random_inspection_number is not None:
            result['RandomInspectionNumber'] = self.random_inspection_number
        if self.sampling_mode_agents is not None:
            result['SamplingModeAgents'] = self.sampling_mode_agents.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnyNumberOfDraws') is not None:
            self.any_number_of_draws = m.get('AnyNumberOfDraws')
        if m.get('Designated') is not None:
            self.designated = m.get('Designated')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NumberOfDraws') is not None:
            self.number_of_draws = m.get('NumberOfDraws')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('RandomInspectionNumber') is not None:
            self.random_inspection_number = m.get('RandomInspectionNumber')
        if m.get('SamplingModeAgents') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingModeSamplingModeAgents()
            self.sampling_mode_agents = temp_model.from_map(m['SamplingModeAgents'])
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup(TeaModel):
    def __init__(
        self,
        skill_id: str = None,
        skill_name: str = None,
    ):
        self.skill_id = skill_id
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skill_id is not None:
            result['SkillId'] = self.skill_id
        if self.skill_name is not None:
            result['SkillName'] = self.skill_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')
        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups(TeaModel):
    def __init__(
        self,
        skill_group: List[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup] = None,
    ):
        self.skill_group = skill_group

    def validate(self):
        if self.skill_group:
            for k in self.skill_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SkillGroup'] = []
        if self.skill_group is not None:
            for k in self.skill_group:
                result['SkillGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.skill_group = []
        if m.get('SkillGroup') is not None:
            for k in m.get('SkillGroup'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroupsSkillGroup()
                self.skill_group.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo(TeaModel):
    def __init__(
        self,
        agents: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents = None,
        agents_str: str = None,
        assignment_type: int = None,
        call_time_end: int = None,
        call_time_start: int = None,
        call_type: int = None,
        create_time: str = None,
        duration_max: int = None,
        duration_min: int = None,
        enabled: int = None,
        priority: int = None,
        reviewers: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers = None,
        rule_id: int = None,
        rule_name: str = None,
        rules: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules = None,
        sampling_mode: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode = None,
        skill_groups: ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups = None,
        skill_groups_str: str = None,
        update_time: str = None,
    ):
        self.agents = agents
        self.agents_str = agents_str
        self.assignment_type = assignment_type
        self.call_time_end = call_time_end
        self.call_time_start = call_time_start
        self.call_type = call_type
        self.create_time = create_time
        self.duration_max = duration_max
        self.duration_min = duration_min
        self.enabled = enabled
        self.priority = priority
        self.reviewers = reviewers
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rules = rules
        self.sampling_mode = sampling_mode
        self.skill_groups = skill_groups
        self.skill_groups_str = skill_groups_str
        self.update_time = update_time

    def validate(self):
        if self.agents:
            self.agents.validate()
        if self.reviewers:
            self.reviewers.validate()
        if self.rules:
            self.rules.validate()
        if self.sampling_mode:
            self.sampling_mode.validate()
        if self.skill_groups:
            self.skill_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agents is not None:
            result['Agents'] = self.agents.to_map()
        if self.agents_str is not None:
            result['AgentsStr'] = self.agents_str
        if self.assignment_type is not None:
            result['AssignmentType'] = self.assignment_type
        if self.call_time_end is not None:
            result['CallTimeEnd'] = self.call_time_end
        if self.call_time_start is not None:
            result['CallTimeStart'] = self.call_time_start
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.duration_max is not None:
            result['DurationMax'] = self.duration_max
        if self.duration_min is not None:
            result['DurationMin'] = self.duration_min
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.reviewers is not None:
            result['Reviewers'] = self.reviewers.to_map()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        if self.sampling_mode is not None:
            result['SamplingMode'] = self.sampling_mode.to_map()
        if self.skill_groups is not None:
            result['SkillGroups'] = self.skill_groups.to_map()
        if self.skill_groups_str is not None:
            result['SkillGroupsStr'] = self.skill_groups_str
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agents') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoAgents()
            self.agents = temp_model.from_map(m['Agents'])
        if m.get('AgentsStr') is not None:
            self.agents_str = m.get('AgentsStr')
        if m.get('AssignmentType') is not None:
            self.assignment_type = m.get('AssignmentType')
        if m.get('CallTimeEnd') is not None:
            self.call_time_end = m.get('CallTimeEnd')
        if m.get('CallTimeStart') is not None:
            self.call_time_start = m.get('CallTimeStart')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DurationMax') is not None:
            self.duration_max = m.get('DurationMax')
        if m.get('DurationMin') is not None:
            self.duration_min = m.get('DurationMin')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Reviewers') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoReviewers()
            self.reviewers = temp_model.from_map(m['Reviewers'])
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Rules') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('SamplingMode') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSamplingMode()
            self.sampling_mode = temp_model.from_map(m['SamplingMode'])
        if m.get('SkillGroups') is not None:
            temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfoSkillGroups()
            self.skill_groups = temp_model.from_map(m['SkillGroups'])
        if m.get('SkillGroupsStr') is not None:
            self.skill_groups_str = m.get('SkillGroupsStr')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTaskAssignRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        task_assign_rule_info: List[ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo] = None,
    ):
        self.task_assign_rule_info = task_assign_rule_info

    def validate(self):
        if self.task_assign_rule_info:
            for k in self.task_assign_rule_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskAssignRuleInfo'] = []
        if self.task_assign_rule_info is not None:
            for k in self.task_assign_rule_info:
                result['TaskAssignRuleInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_assign_rule_info = []
        if m.get('TaskAssignRuleInfo') is not None:
            for k in m.get('TaskAssignRuleInfo'):
                temp_model = ListTaskAssignRulesResponseBodyDataTaskAssignRuleInfo()
                self.task_assign_rule_info.append(temp_model.from_map(k))
        return self


class ListTaskAssignRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: ListTaskAssignRulesResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListTaskAssignRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTaskAssignRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaskAssignRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaskAssignRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListUsersResponseBodyDataUser(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        id: int = None,
        login_user_type: int = None,
        role_name: str = None,
        update_time: str = None,
        user_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.id = id
        self.login_user_type = login_user_type
        self.role_name = role_name
        self.update_time = update_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.login_user_type is not None:
            result['LoginUserType'] = self.login_user_type
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LoginUserType') is not None:
            self.login_user_type = m.get('LoginUserType')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        user: List[ListUsersResponseBodyDataUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersResponseBodyDataUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: ListUsersResponseBodyData = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWarningConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel(TeaModel):
    def __init__(
        self,
        type: int = None,
        url: str = None,
    ):
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoChannels(TeaModel):
    def __init__(
        self,
        channel: List[ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel] = None,
    ):
        self.channel = channel

    def validate(self):
        if self.channel:
            for k in self.channel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Channel'] = []
        if self.channel is not None:
            for k in self.channel:
                result['Channel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel = []
        if m.get('Channel') is not None:
            for k in m.get('Channel'):
                temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoChannelsChannel()
                self.channel.append(temp_model.from_map(k))
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRidList(TeaModel):
    def __init__(
        self,
        rid_list: List[str] = None,
    ):
        self.rid_list = rid_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid_list is not None:
            result['RidList'] = self.rid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RidList') is not None:
            self.rid_list = m.get('RidList')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule(TeaModel):
    def __init__(
        self,
        rid: int = None,
        rule_name: str = None,
    ):
        self.rid = rid
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfoRuleList(TeaModel):
    def __init__(
        self,
        warning_rule: List[ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule] = None,
    ):
        self.warning_rule = warning_rule

    def validate(self):
        if self.warning_rule:
            for k in self.warning_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WarningRule'] = []
        if self.warning_rule is not None:
            for k in self.warning_rule:
                result['WarningRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_rule = []
        if m.get('WarningRule') is not None:
            for k in m.get('WarningRule'):
                temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRuleListWarningRule()
                self.warning_rule.append(temp_model.from_map(k))
        return self


class ListWarningConfigResponseBodyDataWarningConfigInfo(TeaModel):
    def __init__(
        self,
        channels: ListWarningConfigResponseBodyDataWarningConfigInfoChannels = None,
        config_id: int = None,
        config_name: str = None,
        create_time: str = None,
        rid_list: ListWarningConfigResponseBodyDataWarningConfigInfoRidList = None,
        rule_list: ListWarningConfigResponseBodyDataWarningConfigInfoRuleList = None,
        status: int = None,
        update_time: str = None,
    ):
        self.channels = channels
        self.config_id = config_id
        self.config_name = config_name
        self.create_time = create_time
        self.rid_list = rid_list
        self.rule_list = rule_list
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.channels:
            self.channels.validate()
        if self.rid_list:
            self.rid_list.validate()
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.rid_list is not None:
            result['RidList'] = self.rid_list.to_map()
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RidList') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRidList()
            self.rid_list = temp_model.from_map(m['RidList'])
        if m.get('RuleList') is not None:
            temp_model = ListWarningConfigResponseBodyDataWarningConfigInfoRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListWarningConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        warning_config_info: List[ListWarningConfigResponseBodyDataWarningConfigInfo] = None,
    ):
        self.warning_config_info = warning_config_info

    def validate(self):
        if self.warning_config_info:
            for k in self.warning_config_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WarningConfigInfo'] = []
        if self.warning_config_info is not None:
            for k in self.warning_config_info:
                result['WarningConfigInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_config_info = []
        if m.get('WarningConfigInfo') is not None:
            for k in m.get('WarningConfigInfo'):
                temp_model = ListWarningConfigResponseBodyDataWarningConfigInfo()
                self.warning_config_info.append(temp_model.from_map(k))
        return self


class ListWarningConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListWarningConfigResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ListWarningConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWarningConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWarningConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWarningStrategyConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class ListWarningStrategyConfigResponseBodyDataData(TeaModel):
    def __init__(
        self,
        id: int = None,
        interval_time: int = None,
        lambda_: str = None,
        level: int = None,
        max_number: int = None,
        name: str = None,
    ):
        self.id = id
        self.interval_time = interval_time
        self.lambda_ = lambda_
        self.level = level
        self.max_number = max_number
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time
        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_
        if self.level is not None:
            result['Level'] = self.level
        if self.max_number is not None:
            result['MaxNumber'] = self.max_number
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')
        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MaxNumber') is not None:
            self.max_number = m.get('MaxNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListWarningStrategyConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListWarningStrategyConfigResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListWarningStrategyConfigResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListWarningStrategyConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: ListWarningStrategyConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
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
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = ListWarningStrategyConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWarningStrategyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWarningStrategyConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWarningStrategyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevertAssignedSessionRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class RevertAssignedSessionResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RevertAssignedSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: RevertAssignedSessionResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = RevertAssignedSessionResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevertAssignedSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevertAssignedSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevertAssignedSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevertAssignedSessionGroupRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class RevertAssignedSessionGroupResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RevertAssignedSessionGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: RevertAssignedSessionGroupResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = RevertAssignedSessionGroupResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevertAssignedSessionGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevertAssignedSessionGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevertAssignedSessionGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveConfigDataSetRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SaveConfigDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveConfigDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveConfigDataSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SaveConfigDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitComplaintRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitComplaintResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitComplaintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitComplaintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPrecisionTaskRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitPrecisionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitPrecisionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitPrecisionTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitPrecisionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitQualityCheckTaskRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitQualityCheckTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitQualityCheckTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitQualityCheckTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitQualityCheckTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitReviewInfoRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SubmitReviewInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitReviewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitReviewInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitReviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncQualityCheckRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class SyncQualityCheckResponseBodyDataRulesHitHitKeyWords(TeaModel):
    def __init__(
        self,
        cid: int = None,
        from_: int = None,
        pid: int = None,
        to: int = None,
        val: str = None,
    ):
        self.cid = cid
        self.from_ = from_
        self.pid = pid
        self.to = to
        self.val = val

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SyncQualityCheckResponseBodyDataRulesHitPhrase(TeaModel):
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
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.identity = identity
        self.role = role
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SyncQualityCheckResponseBodyDataRulesHit(TeaModel):
    def __init__(
        self,
        hit_key_words: List[SyncQualityCheckResponseBodyDataRulesHitHitKeyWords] = None,
        phrase: SyncQualityCheckResponseBodyDataRulesHitPhrase = None,
    ):
        self.hit_key_words = hit_key_words
        self.phrase = phrase

    def validate(self):
        if self.hit_key_words:
            for k in self.hit_key_words:
                if k:
                    k.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitKeyWords'] = []
        if self.hit_key_words is not None:
            for k in self.hit_key_words:
                result['HitKeyWords'].append(k.to_map() if k else None)
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_key_words = []
        if m.get('HitKeyWords') is not None:
            for k in m.get('HitKeyWords'):
                temp_model = SyncQualityCheckResponseBodyDataRulesHitHitKeyWords()
                self.hit_key_words.append(temp_model.from_map(k))
        if m.get('Phrase') is not None:
            temp_model = SyncQualityCheckResponseBodyDataRulesHitPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class SyncQualityCheckResponseBodyDataRulesRuleInfoBase(TeaModel):
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
        self.comments = comments
        self.level = level
        self.rule_category_name = rule_category_name
        self.score_num = score_num
        self.score_num_type = score_num_type
        self.score_type = score_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class SyncQualityCheckResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        hit: List[SyncQualityCheckResponseBodyDataRulesHit] = None,
        rid: str = None,
        rule_info_base: SyncQualityCheckResponseBodyDataRulesRuleInfoBase = None,
        rule_name: str = None,
    ):
        self.hit = hit
        self.rid = rid
        self.rule_info_base = rule_info_base
        self.rule_name = rule_name

    def validate(self):
        if self.hit:
            for k in self.hit:
                if k:
                    k.validate()
        if self.rule_info_base:
            self.rule_info_base.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hit'] = []
        if self.hit is not None:
            for k in self.hit:
                result['Hit'].append(k.to_map() if k else None)
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
            for k in m.get('Hit'):
                temp_model = SyncQualityCheckResponseBodyDataRulesHit()
                self.hit.append(temp_model.from_map(k))
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('RuleInfoBase') is not None:
            temp_model = SyncQualityCheckResponseBodyDataRulesRuleInfoBase()
            self.rule_info_base = temp_model.from_map(m['RuleInfoBase'])
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class SyncQualityCheckResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        rules: List[SyncQualityCheckResponseBodyDataRules] = None,
        score: int = None,
        task_id: str = None,
        tid: str = None,
    ):
        self.begin_time = begin_time
        self.rules = rules
        self.score = score
        self.task_id = task_id
        self.tid = tid

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
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
            for k in m.get('Rules'):
                temp_model = SyncQualityCheckResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SyncQualityCheckResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SyncQualityCheckResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = SyncQualityCheckResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncQualityCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncQualityCheckResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncQualityCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestRuleV4Request(TeaModel):
    def __init__(
        self,
        is_scheme_data: int = None,
        test_json: str = None,
    ):
        self.is_scheme_data = is_scheme_data
        # This parameter is required.
        self.test_json = test_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_scheme_data is not None:
            result['IsSchemeData'] = self.is_scheme_data
        if self.test_json is not None:
            result['TestJson'] = self.test_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSchemeData') is not None:
            self.is_scheme_data = m.get('IsSchemeData')
        if m.get('TestJson') is not None:
            self.test_json = m.get('TestJson')
        return self


class TestRuleV4ResponseBodyDataHitRuleReviewInfoListBranchInfoList(TeaModel):
    def __init__(
        self,
        check_type: int = None,
        index: int = None,
        lambda_: str = None,
        name: str = None,
        next_node_id: int = None,
        situation: NextNodeSituations = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = NextNodeSituations()
            self.situation = temp_model.from_map(m['Situation'])
        if m.get('Triggers') is not None:
            self.triggers = m.get('Triggers')
        return self


class TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListKeyWords(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListPhrase(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoList(TeaModel):
    def __init__(
        self,
        cid: List[str] = None,
        key_words: List[TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListKeyWords] = None,
        phrase: TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListPhrase = None,
    ):
        self.cid = cid
        self.key_words = key_words
        self.phrase = phrase

    def validate(self):
        if self.key_words:
            for k in self.key_words:
                if k:
                    k.validate()
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid is not None:
            result['Cid'] = self.cid
        result['KeyWords'] = []
        if self.key_words is not None:
            for k in self.key_words:
                result['KeyWords'].append(k.to_map() if k else None)
        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        self.key_words = []
        if m.get('KeyWords') is not None:
            for k in m.get('KeyWords'):
                temp_model = TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListKeyWords()
                self.key_words.append(temp_model.from_map(k))
        if m.get('Phrase') is not None:
            temp_model = TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoListPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class TestRuleV4ResponseBodyDataHitRuleReviewInfoList(TeaModel):
    def __init__(
        self,
        branch_hit_id: int = None,
        branch_info_list: List[TestRuleV4ResponseBodyDataHitRuleReviewInfoListBranchInfoList] = None,
        condition_hit_info_list: List[TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoList] = None,
        condition_info_list: List[ConditionBasicInfo] = None,
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
            for k in self.branch_info_list:
                if k:
                    k.validate()
        if self.condition_hit_info_list:
            for k in self.condition_hit_info_list:
                if k:
                    k.validate()
        if self.condition_info_list:
            for k in self.condition_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch_hit_id is not None:
            result['BranchHitId'] = self.branch_hit_id
        result['BranchInfoList'] = []
        if self.branch_info_list is not None:
            for k in self.branch_info_list:
                result['BranchInfoList'].append(k.to_map() if k else None)
        result['ConditionHitInfoList'] = []
        if self.condition_hit_info_list is not None:
            for k in self.condition_hit_info_list:
                result['ConditionHitInfoList'].append(k.to_map() if k else None)
        result['ConditionInfoList'] = []
        if self.condition_info_list is not None:
            for k in self.condition_info_list:
                result['ConditionInfoList'].append(k.to_map() if k else None)
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
            for k in m.get('BranchInfoList'):
                temp_model = TestRuleV4ResponseBodyDataHitRuleReviewInfoListBranchInfoList()
                self.branch_info_list.append(temp_model.from_map(k))
        self.condition_hit_info_list = []
        if m.get('ConditionHitInfoList') is not None:
            for k in m.get('ConditionHitInfoList'):
                temp_model = TestRuleV4ResponseBodyDataHitRuleReviewInfoListConditionHitInfoList()
                self.condition_hit_info_list.append(temp_model.from_map(k))
        self.condition_info_list = []
        if m.get('ConditionInfoList') is not None:
            for k in m.get('ConditionInfoList'):
                temp_model = ConditionBasicInfo()
                self.condition_info_list.append(temp_model.from_map(k))
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


class TestRuleV4ResponseBodyDataHitTaskFlowList(TeaModel):
    def __init__(
        self,
        graph_flow: TaskGraphFlow = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = TaskGraphFlow()
            self.graph_flow = temp_model.from_map(m['GraphFlow'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')
        return self


class TestRuleV4ResponseBodyDataUnhitRuleReviewInfoList(TeaModel):
    def __init__(
        self,
        condition_info_list: List[ConditionBasicInfo] = None,
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
            for k in self.condition_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionInfoList'] = []
        if self.condition_info_list is not None:
            for k in self.condition_info_list:
                result['ConditionInfoList'].append(k.to_map() if k else None)
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
            for k in m.get('ConditionInfoList'):
                temp_model = ConditionBasicInfo()
                self.condition_info_list.append(temp_model.from_map(k))
        if m.get('Matched') is not None:
            self.matched = m.get('Matched')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('TaskFlowType') is not None:
            self.task_flow_type = m.get('TaskFlowType')
        return self


class TestRuleV4ResponseBodyData(TeaModel):
    def __init__(
        self,
        hit_rule_review_info_list: List[TestRuleV4ResponseBodyDataHitRuleReviewInfoList] = None,
        hit_task_flow_list: List[TestRuleV4ResponseBodyDataHitTaskFlowList] = None,
        unhit_rule_review_info_list: List[TestRuleV4ResponseBodyDataUnhitRuleReviewInfoList] = None,
    ):
        self.hit_rule_review_info_list = hit_rule_review_info_list
        self.hit_task_flow_list = hit_task_flow_list
        self.unhit_rule_review_info_list = unhit_rule_review_info_list

    def validate(self):
        if self.hit_rule_review_info_list:
            for k in self.hit_rule_review_info_list:
                if k:
                    k.validate()
        if self.hit_task_flow_list:
            for k in self.hit_task_flow_list:
                if k:
                    k.validate()
        if self.unhit_rule_review_info_list:
            for k in self.unhit_rule_review_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitRuleReviewInfoList'] = []
        if self.hit_rule_review_info_list is not None:
            for k in self.hit_rule_review_info_list:
                result['HitRuleReviewInfoList'].append(k.to_map() if k else None)
        result['HitTaskFlowList'] = []
        if self.hit_task_flow_list is not None:
            for k in self.hit_task_flow_list:
                result['HitTaskFlowList'].append(k.to_map() if k else None)
        result['UnhitRuleReviewInfoList'] = []
        if self.unhit_rule_review_info_list is not None:
            for k in self.unhit_rule_review_info_list:
                result['UnhitRuleReviewInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_rule_review_info_list = []
        if m.get('HitRuleReviewInfoList') is not None:
            for k in m.get('HitRuleReviewInfoList'):
                temp_model = TestRuleV4ResponseBodyDataHitRuleReviewInfoList()
                self.hit_rule_review_info_list.append(temp_model.from_map(k))
        self.hit_task_flow_list = []
        if m.get('HitTaskFlowList') is not None:
            for k in m.get('HitTaskFlowList'):
                temp_model = TestRuleV4ResponseBodyDataHitTaskFlowList()
                self.hit_task_flow_list.append(temp_model.from_map(k))
        self.unhit_rule_review_info_list = []
        if m.get('UnhitRuleReviewInfoList') is not None:
            for k in m.get('UnhitRuleReviewInfoList'):
                temp_model = TestRuleV4ResponseBodyDataUnhitRuleReviewInfoList()
                self.unhit_rule_review_info_list.append(temp_model.from_map(k))
        return self


class TestRuleV4ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TestRuleV4ResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = TestRuleV4ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TestRuleV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestRuleV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TestRuleV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAsrVocabRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateAsrVocabResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAsrVocabResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAsrVocabResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAsrVocabResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCheckTypeToSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class UpdateCheckTypeToSchemeResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateCheckTypeToSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: UpdateCheckTypeToSchemeResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = UpdateCheckTypeToSchemeResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCheckTypeToSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCheckTypeToSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCheckTypeToSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQualityCheckDataRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateQualityCheckDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateQualityCheckDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQualityCheckDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateQualityCheckDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQualityCheckSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class UpdateQualityCheckSchemeResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateQualityCheckSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: UpdateQualityCheckSchemeResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = UpdateQualityCheckSchemeResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateQualityCheckSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQualityCheckSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateQualityCheckSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleByIdRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        is_copy: bool = None,
        json_str_for_rule: str = None,
        return_related_schemes: bool = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.is_copy = is_copy
        # This parameter is required.
        self.json_str_for_rule = json_str_for_rule
        self.return_related_schemes = return_related_schemes
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy
        if self.json_str_for_rule is not None:
            result['JsonStrForRule'] = self.json_str_for_rule
        if self.return_related_schemes is not None:
            result['ReturnRelatedSchemes'] = self.return_related_schemes
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')
        if m.get('JsonStrForRule') is not None:
            self.json_str_for_rule = m.get('JsonStrForRule')
        if m.get('ReturnRelatedSchemes') is not None:
            self.return_related_schemes = m.get('ReturnRelatedSchemes')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class UpdateRuleByIdResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateRuleByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: UpdateRuleByIdResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = UpdateRuleByIdResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleToSchemeRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class UpdateRuleToSchemeResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateRuleToSchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: UpdateRuleToSchemeResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = UpdateRuleToSchemeResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleToSchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleToSchemeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleToSchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRuleV4Request(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str_for_rule: str = None,
        rule_id: int = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str_for_rule = json_str_for_rule
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str_for_rule is not None:
            result['JsonStrForRule'] = self.json_str_for_rule
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStrForRule') is not None:
            self.json_str_for_rule = m.get('JsonStrForRule')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class UpdateRuleV4ResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateRuleV4ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        messages: UpdateRuleV4ResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = UpdateRuleV4ResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRuleV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRuleV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRuleV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSchemeTaskConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['jsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')
        return self


class UpdateSchemeTaskConfigResponseBodyMessages(TeaModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateSchemeTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        messages: UpdateSchemeTaskConfigResponseBodyMessages = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.messages = messages
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.messages:
            self.messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.messages is not None:
            result['Messages'] = self.messages.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Messages') is not None:
            temp_model = UpdateSchemeTaskConfigResponseBodyMessages()
            self.messages = temp_model.from_map(m['Messages'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSchemeTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSchemeTaskConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSchemeTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSkillGroupConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSkillGroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSkillGroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSkillGroupConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSkillGroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSyncQualityCheckDataRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateSyncQualityCheckDataResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        tid: str = None,
    ):
        self.task_id = task_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class UpdateSyncQualityCheckDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateSyncQualityCheckDataResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UpdateSyncQualityCheckDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSyncQualityCheckDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSyncQualityCheckDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSyncQualityCheckDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskAssignRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateTaskAssignRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTaskAssignRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTaskAssignRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskAssignRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWarningConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateWarningConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWarningConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWarningConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWarningConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWarningStrategyConfigRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UpdateWarningStrategyConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWarningStrategyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWarningStrategyConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWarningStrategyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadAudioDataRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadAudioDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadAudioDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadAudioDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadAudioDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDataRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDataSyncRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataSyncResponseBodyDataResultInfoHandScoreIdList(TeaModel):
    def __init__(
        self,
        hand_score_id_list: List[str] = None,
    ):
        self.hand_score_id_list = hand_score_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hand_score_id_list is not None:
            result['HandScoreIdList'] = self.hand_score_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HandScoreIdList') is not None:
            self.hand_score_id_list = m.get('HandScoreIdList')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo(TeaModel):
    def __init__(
        self,
        condition_info_cid: str = None,
    ):
        self.condition_info_cid = condition_info_cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_info_cid is not None:
            result['ConditionInfoCid'] = self.condition_info_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionInfoCid') is not None:
            self.condition_info_cid = m.get('ConditionInfoCid')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo(TeaModel):
    def __init__(
        self,
        condition_basic_info: List[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo] = None,
    ):
        self.condition_basic_info = condition_basic_info

    def validate(self):
        if self.condition_basic_info:
            for k in self.condition_basic_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionBasicInfo'] = []
        if self.condition_basic_info is not None:
            for k in self.condition_basic_info:
                result['ConditionBasicInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_basic_info = []
        if m.get('ConditionBasicInfo') is not None:
            for k in m.get('ConditionBasicInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfoConditionBasicInfo()
                self.condition_basic_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids(TeaModel):
    def __init__(
        self,
        cid_item: List[str] = None,
    ):
        self.cid_item = cid_item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cid_item is not None:
            result['CidItem'] = self.cid_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidItem') is not None:
            self.cid_item = m.get('CidItem')
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords(TeaModel):
    def __init__(
        self,
        hit_key_word: List[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord] = None,
    ):
        self.hit_key_word = hit_key_word

    def validate(self):
        if self.hit_key_word:
            for k in self.hit_key_word:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HitKeyWord'] = []
        if self.hit_key_word is not None:
            for k in self.hit_key_word:
                result['HitKeyWord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_key_word = []
        if m.get('HitKeyWord') is not None:
            for k in m.get('HitKeyWord'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWordsHitKeyWord()
                self.hit_key_word.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo(TeaModel):
    def __init__(
        self,
        hit_cids: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids = None,
        hit_key_words: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords = None,
        phrase: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitCids()
            self.hit_cids = temp_model.from_map(m['HitCids'])
        if m.get('HitKeyWords') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoHitKeyWords()
            self.hit_key_words = temp_model.from_map(m['HitKeyWords'])
        if m.get('Phrase') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfoPhrase()
            self.phrase = temp_model.from_map(m['Phrase'])
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit(TeaModel):
    def __init__(
        self,
        condition_hit_info: List[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo] = None,
    ):
        self.condition_hit_info = condition_hit_info

    def validate(self):
        if self.condition_hit_info:
            for k in self.condition_hit_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConditionHitInfo'] = []
        if self.condition_hit_info is not None:
            for k in self.condition_hit_info:
                result['ConditionHitInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_hit_info = []
        if m.get('ConditionHitInfo') is not None:
            for k in m.get('ConditionHitInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHitConditionHitInfo()
                self.condition_hit_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo(TeaModel):
    def __init__(
        self,
        condition_info: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo = None,
        hit: UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoConditionInfo()
            self.condition_info = temp_model.from_map(m['ConditionInfo'])
        if m.get('Hit') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfoHit()
            self.hit = temp_model.from_map(m['Hit'])
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class UploadDataSyncResponseBodyDataResultInfoRules(TeaModel):
    def __init__(
        self,
        rule_hit_info: List[UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo] = None,
    ):
        self.rule_hit_info = rule_hit_info

    def validate(self):
        if self.rule_hit_info:
            for k in self.rule_hit_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RuleHitInfo'] = []
        if self.rule_hit_info is not None:
            for k in self.rule_hit_info:
                result['RuleHitInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_hit_info = []
        if m.get('RuleHitInfo') is not None:
            for k in m.get('RuleHitInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfoRulesRuleHitInfo()
                self.rule_hit_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBodyDataResultInfo(TeaModel):
    def __init__(
        self,
        hand_score_id_list: UploadDataSyncResponseBodyDataResultInfoHandScoreIdList = None,
        rules: UploadDataSyncResponseBodyDataResultInfoRules = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UploadDataSyncResponseBodyDataResultInfoHandScoreIdList()
            self.hand_score_id_list = temp_model.from_map(m['HandScoreIdList'])
        if m.get('Rules') is not None:
            temp_model = UploadDataSyncResponseBodyDataResultInfoRules()
            self.rules = temp_model.from_map(m['Rules'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class UploadDataSyncResponseBodyData(TeaModel):
    def __init__(
        self,
        result_info: List[UploadDataSyncResponseBodyDataResultInfo] = None,
    ):
        self.result_info = result_info

    def validate(self):
        if self.result_info:
            for k in self.result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultInfo'] = []
        if self.result_info is not None:
            for k in self.result_info:
                result['ResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_info = []
        if m.get('ResultInfo') is not None:
            for k in m.get('ResultInfo'):
                temp_model = UploadDataSyncResponseBodyDataResultInfo()
                self.result_info.append(temp_model.from_map(k))
        return self


class UploadDataSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UploadDataSyncResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UploadDataSyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDataSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadDataSyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadDataSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDataV4Request(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadDataV4ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDataV4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadDataV4ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadDataV4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRuleRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class UploadRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rid_info: List[str] = None,
    ):
        self.rid_info = rid_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rid_info is not None:
            result['RidInfo'] = self.rid_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RidInfo') is not None:
            self.rid_info = m.get('RidInfo')
        return self


class UploadRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UploadRuleResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UploadRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UploadRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyFileRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class VerifyFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: float = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifySentenceRequest(TeaModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        # This parameter is required.
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id
        if self.json_str is not None:
            result['JsonStr'] = self.json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')
        if m.get('JsonStr') is not None:
            self.json_str = m.get('JsonStr')
        return self


class VerifySentenceResponseBodyDataDeltaSourceLine(TeaModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class VerifySentenceResponseBodyDataDeltaSource(TeaModel):
    def __init__(
        self,
        line: VerifySentenceResponseBodyDataDeltaSourceLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaSourceLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class VerifySentenceResponseBodyDataDeltaTargetLine(TeaModel):
    def __init__(
        self,
        line: List[str] = None,
    ):
        self.line = line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class VerifySentenceResponseBodyDataDeltaTarget(TeaModel):
    def __init__(
        self,
        line: VerifySentenceResponseBodyDataDeltaTargetLine = None,
        position: int = None,
    ):
        self.line = line
        self.position = position

    def validate(self):
        if self.line:
            self.line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line is not None:
            result['Line'] = self.line.to_map()
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaTargetLine()
            self.line = temp_model.from_map(m['Line'])
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class VerifySentenceResponseBodyDataDelta(TeaModel):
    def __init__(
        self,
        source: VerifySentenceResponseBodyDataDeltaSource = None,
        target: VerifySentenceResponseBodyDataDeltaTarget = None,
        type: str = None,
    ):
        self.source = source
        self.target = target
        self.type = type

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = VerifySentenceResponseBodyDataDeltaTarget()
            self.target = temp_model.from_map(m['Target'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class VerifySentenceResponseBodyData(TeaModel):
    def __init__(
        self,
        delta: List[VerifySentenceResponseBodyDataDelta] = None,
    ):
        self.delta = delta

    def validate(self):
        if self.delta:
            for k in self.delta:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Delta'] = []
        if self.delta is not None:
            for k in self.delta:
                result['Delta'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delta = []
        if m.get('Delta') is not None:
            for k in m.get('Delta'):
                temp_model = VerifySentenceResponseBodyDataDelta()
                self.delta.append(temp_model.from_map(k))
        return self


class VerifySentenceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: VerifySentenceResponseBodyData = None,
        incorrect_words: int = None,
        message: str = None,
        request_id: str = None,
        source_role: int = None,
        success: bool = None,
        target_role: int = None,
    ):
        self.code = code
        self.data = data
        self.incorrect_words = incorrect_words
        self.message = message
        self.request_id = request_id
        self.source_role = source_role
        self.success = success
        self.target_role = target_role

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.incorrect_words is not None:
            result['IncorrectWords'] = self.incorrect_words
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_role is not None:
            result['SourceRole'] = self.source_role
        if self.success is not None:
            result['Success'] = self.success
        if self.target_role is not None:
            result['TargetRole'] = self.target_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VerifySentenceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('IncorrectWords') is not None:
            self.incorrect_words = m.get('IncorrectWords')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceRole') is not None:
            self.source_role = m.get('SourceRole')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TargetRole') is not None:
            self.target_role = m.get('TargetRole')
        return self


class VerifySentenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifySentenceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifySentenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


