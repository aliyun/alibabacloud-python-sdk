# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetAnnotationMissionSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAnnotationMissionSummaryResponseBodyData = None,
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
            temp_model = main_models.GetAnnotationMissionSummaryResponseBodyData()
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

class GetAnnotationMissionSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        annotation_mission_id: str = None,
        asr_summary_info: main_models.GetAnnotationMissionSummaryResponseBodyDataAsrSummaryInfo = None,
        intent_summary_info: main_models.GetAnnotationMissionSummaryResponseBodyDataIntentSummaryInfo = None,
        message: str = None,
        success: bool = None,
        tag_summary_info: main_models.GetAnnotationMissionSummaryResponseBodyDataTagSummaryInfo = None,
    ):
        self.annotation_mission_id = annotation_mission_id
        self.asr_summary_info = asr_summary_info
        self.intent_summary_info = intent_summary_info
        self.message = message
        self.success = success
        self.tag_summary_info = tag_summary_info

    def validate(self):
        if self.asr_summary_info:
            self.asr_summary_info.validate()
        if self.intent_summary_info:
            self.intent_summary_info.validate()
        if self.tag_summary_info:
            self.tag_summary_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.asr_summary_info is not None:
            result['AsrSummaryInfo'] = self.asr_summary_info.to_map()

        if self.intent_summary_info is not None:
            result['IntentSummaryInfo'] = self.intent_summary_info.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        if self.tag_summary_info is not None:
            result['TagSummaryInfo'] = self.tag_summary_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AsrSummaryInfo') is not None:
            temp_model = main_models.GetAnnotationMissionSummaryResponseBodyDataAsrSummaryInfo()
            self.asr_summary_info = temp_model.from_map(m.get('AsrSummaryInfo'))

        if m.get('IntentSummaryInfo') is not None:
            temp_model = main_models.GetAnnotationMissionSummaryResponseBodyDataIntentSummaryInfo()
            self.intent_summary_info = temp_model.from_map(m.get('IntentSummaryInfo'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TagSummaryInfo') is not None:
            temp_model = main_models.GetAnnotationMissionSummaryResponseBodyDataTagSummaryInfo()
            self.tag_summary_info = temp_model.from_map(m.get('TagSummaryInfo'))

        return self

class GetAnnotationMissionSummaryResponseBodyDataTagSummaryInfo(DaraModel):
    def __init__(
        self,
        tag_summary_info_detail_list: List[main_models.GetAnnotationMissionSummaryResponseBodyDataTagSummaryInfoTagSummaryInfoDetailList] = None,
    ):
        self.tag_summary_info_detail_list = tag_summary_info_detail_list

    def validate(self):
        if self.tag_summary_info_detail_list:
            for v1 in self.tag_summary_info_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagSummaryInfoDetailList'] = []
        if self.tag_summary_info_detail_list is not None:
            for k1 in self.tag_summary_info_detail_list:
                result['TagSummaryInfoDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_summary_info_detail_list = []
        if m.get('TagSummaryInfoDetailList') is not None:
            for k1 in m.get('TagSummaryInfoDetailList'):
                temp_model = main_models.GetAnnotationMissionSummaryResponseBodyDataTagSummaryInfoTagSummaryInfoDetailList()
                self.tag_summary_info_detail_list.append(temp_model.from_map(k1))

        return self

class GetAnnotationMissionSummaryResponseBodyDataTagSummaryInfoTagSummaryInfoDetailList(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        self.count = count
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetAnnotationMissionSummaryResponseBodyDataIntentSummaryInfo(DaraModel):
    def __init__(
        self,
        annotation_correct_count: int = None,
        annotation_invalid: int = None,
        chat_total_count: int = None,
        intent_user_say_count: int = None,
        intention_not_covered_count: int = None,
        match_error_count: int = None,
        no_annotation: int = None,
        translation_unrecognized_count: int = None,
    ):
        self.annotation_correct_count = annotation_correct_count
        self.annotation_invalid = annotation_invalid
        self.chat_total_count = chat_total_count
        self.intent_user_say_count = intent_user_say_count
        self.intention_not_covered_count = intention_not_covered_count
        self.match_error_count = match_error_count
        self.no_annotation = no_annotation
        self.translation_unrecognized_count = translation_unrecognized_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_correct_count is not None:
            result['AnnotationCorrectCount'] = self.annotation_correct_count

        if self.annotation_invalid is not None:
            result['AnnotationInvalid'] = self.annotation_invalid

        if self.chat_total_count is not None:
            result['ChatTotalCount'] = self.chat_total_count

        if self.intent_user_say_count is not None:
            result['IntentUserSayCount'] = self.intent_user_say_count

        if self.intention_not_covered_count is not None:
            result['IntentionNotCoveredCount'] = self.intention_not_covered_count

        if self.match_error_count is not None:
            result['MatchErrorCount'] = self.match_error_count

        if self.no_annotation is not None:
            result['NoAnnotation'] = self.no_annotation

        if self.translation_unrecognized_count is not None:
            result['TranslationUnrecognizedCount'] = self.translation_unrecognized_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationCorrectCount') is not None:
            self.annotation_correct_count = m.get('AnnotationCorrectCount')

        if m.get('AnnotationInvalid') is not None:
            self.annotation_invalid = m.get('AnnotationInvalid')

        if m.get('ChatTotalCount') is not None:
            self.chat_total_count = m.get('ChatTotalCount')

        if m.get('IntentUserSayCount') is not None:
            self.intent_user_say_count = m.get('IntentUserSayCount')

        if m.get('IntentionNotCoveredCount') is not None:
            self.intention_not_covered_count = m.get('IntentionNotCoveredCount')

        if m.get('MatchErrorCount') is not None:
            self.match_error_count = m.get('MatchErrorCount')

        if m.get('NoAnnotation') is not None:
            self.no_annotation = m.get('NoAnnotation')

        if m.get('TranslationUnrecognizedCount') is not None:
            self.translation_unrecognized_count = m.get('TranslationUnrecognizedCount')

        return self

class GetAnnotationMissionSummaryResponseBodyDataAsrSummaryInfo(DaraModel):
    def __init__(
        self,
        add_customization_data_count: int = None,
        add_vocabulary_data_count: int = None,
        annotation_invalid: int = None,
        character_correct_rate: int = None,
        character_error_rate: int = None,
        chat_total_count: int = None,
        no_annotation: int = None,
        sentence_error_rate: int = None,
        word_error_rate: int = None,
    ):
        self.add_customization_data_count = add_customization_data_count
        self.add_vocabulary_data_count = add_vocabulary_data_count
        self.annotation_invalid = annotation_invalid
        self.character_correct_rate = character_correct_rate
        self.character_error_rate = character_error_rate
        self.chat_total_count = chat_total_count
        self.no_annotation = no_annotation
        self.sentence_error_rate = sentence_error_rate
        self.word_error_rate = word_error_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_customization_data_count is not None:
            result['AddCustomizationDataCount'] = self.add_customization_data_count

        if self.add_vocabulary_data_count is not None:
            result['AddVocabularyDataCount'] = self.add_vocabulary_data_count

        if self.annotation_invalid is not None:
            result['AnnotationInvalid'] = self.annotation_invalid

        if self.character_correct_rate is not None:
            result['CharacterCorrectRate'] = self.character_correct_rate

        if self.character_error_rate is not None:
            result['CharacterErrorRate'] = self.character_error_rate

        if self.chat_total_count is not None:
            result['ChatTotalCount'] = self.chat_total_count

        if self.no_annotation is not None:
            result['NoAnnotation'] = self.no_annotation

        if self.sentence_error_rate is not None:
            result['SentenceErrorRate'] = self.sentence_error_rate

        if self.word_error_rate is not None:
            result['WordErrorRate'] = self.word_error_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCustomizationDataCount') is not None:
            self.add_customization_data_count = m.get('AddCustomizationDataCount')

        if m.get('AddVocabularyDataCount') is not None:
            self.add_vocabulary_data_count = m.get('AddVocabularyDataCount')

        if m.get('AnnotationInvalid') is not None:
            self.annotation_invalid = m.get('AnnotationInvalid')

        if m.get('CharacterCorrectRate') is not None:
            self.character_correct_rate = m.get('CharacterCorrectRate')

        if m.get('CharacterErrorRate') is not None:
            self.character_error_rate = m.get('CharacterErrorRate')

        if m.get('ChatTotalCount') is not None:
            self.chat_total_count = m.get('ChatTotalCount')

        if m.get('NoAnnotation') is not None:
            self.no_annotation = m.get('NoAnnotation')

        if m.get('SentenceErrorRate') is not None:
            self.sentence_error_rate = m.get('SentenceErrorRate')

        if m.get('WordErrorRate') is not None:
            self.word_error_rate = m.get('WordErrorRate')

        return self

