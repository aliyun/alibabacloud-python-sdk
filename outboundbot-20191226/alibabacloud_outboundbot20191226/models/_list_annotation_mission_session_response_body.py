# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListAnnotationMissionSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAnnotationMissionSessionResponseBodyData = None,
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
            temp_model = main_models.ListAnnotationMissionSessionResponseBodyData()
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

class ListAnnotationMissionSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        annotation_mission_id: str = None,
        annotation_mission_session_list: List[main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionList] = None,
        message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_list = annotation_mission_session_list
        self.message = message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.annotation_mission_session_list:
            for v1 in self.annotation_mission_session_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        result['AnnotationMissionSessionList'] = []
        if self.annotation_mission_session_list is not None:
            for k1 in self.annotation_mission_session_list:
                result['AnnotationMissionSessionList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        self.annotation_mission_session_list = []
        if m.get('AnnotationMissionSessionList') is not None:
            for k1 in m.get('AnnotationMissionSessionList'):
                temp_model = main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionList()
                self.annotation_mission_session_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionList(DaraModel):
    def __init__(
        self,
        annotation_mission_chat_list: List[main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatList] = None,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        annotation_status: int = None,
        create_time: int = None,
        debug_conversation: bool = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_id: str = None,
        modified_time: int = None,
        script_id: str = None,
        session_id: str = None,
        version: int = None,
    ):
        self.annotation_mission_chat_list = annotation_mission_chat_list
        self.annotation_mission_id = annotation_mission_id
        # ID
        self.annotation_mission_session_id = annotation_mission_session_id
        self.annotation_status = annotation_status
        self.create_time = create_time
        self.debug_conversation = debug_conversation
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.modified_time = modified_time
        self.script_id = script_id
        self.session_id = session_id
        self.version = version

    def validate(self):
        if self.annotation_mission_chat_list:
            for v1 in self.annotation_mission_chat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnnotationMissionChatList'] = []
        if self.annotation_mission_chat_list is not None:
            for k1 in self.annotation_mission_chat_list:
                result['AnnotationMissionChatList'].append(k1.to_map() if k1 else None)

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.annotation_status is not None:
            result['AnnotationStatus'] = self.annotation_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.debug_conversation is not None:
            result['DebugConversation'] = self.debug_conversation

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotation_mission_chat_list = []
        if m.get('AnnotationMissionChatList') is not None:
            for k1 in m.get('AnnotationMissionChatList'):
                temp_model = main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatList()
                self.annotation_mission_chat_list.append(temp_model.from_map(k1))

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('AnnotationStatus') is not None:
            self.annotation_status = m.get('AnnotationStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DebugConversation') is not None:
            self.debug_conversation = m.get('DebugConversation')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatList(DaraModel):
    def __init__(
        self,
        annotation_asr_result: str = None,
        annotation_mission_chat_customization_data_info_list: List[main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatCustomizationDataInfoList] = None,
        annotation_mission_chat_id: str = None,
        annotation_mission_chat_intent_user_say_info_list: List[main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatIntentUserSayInfoList] = None,
        annotation_mission_chat_tag_info_list: List[main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatTagInfoList] = None,
        annotation_mission_chat_vocabulary_info_list: List[main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatVocabularyInfoList] = None,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        annotation_status: int = None,
        answer: str = None,
        asr_annotation_status: int = None,
        create_time: int = None,
        instance_id: str = None,
        intent_annotation_status: int = None,
        modified_time: int = None,
        occur_time: int = None,
        original_asr_result: str = None,
        sequence_id: str = None,
        sub_status: int = None,
        tag_annotation_status: int = None,
        translation_error: int = None,
    ):
        self.annotation_asr_result = annotation_asr_result
        self.annotation_mission_chat_customization_data_info_list = annotation_mission_chat_customization_data_info_list
        # chat id
        self.annotation_mission_chat_id = annotation_mission_chat_id
        self.annotation_mission_chat_intent_user_say_info_list = annotation_mission_chat_intent_user_say_info_list
        self.annotation_mission_chat_tag_info_list = annotation_mission_chat_tag_info_list
        self.annotation_mission_chat_vocabulary_info_list = annotation_mission_chat_vocabulary_info_list
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_id = annotation_mission_session_id
        self.annotation_status = annotation_status
        self.answer = answer
        self.asr_annotation_status = asr_annotation_status
        self.create_time = create_time
        self.instance_id = instance_id
        self.intent_annotation_status = intent_annotation_status
        self.modified_time = modified_time
        self.occur_time = occur_time
        self.original_asr_result = original_asr_result
        self.sequence_id = sequence_id
        self.sub_status = sub_status
        self.tag_annotation_status = tag_annotation_status
        self.translation_error = translation_error

    def validate(self):
        if self.annotation_mission_chat_customization_data_info_list:
            for v1 in self.annotation_mission_chat_customization_data_info_list:
                 if v1:
                    v1.validate()
        if self.annotation_mission_chat_intent_user_say_info_list:
            for v1 in self.annotation_mission_chat_intent_user_say_info_list:
                 if v1:
                    v1.validate()
        if self.annotation_mission_chat_tag_info_list:
            for v1 in self.annotation_mission_chat_tag_info_list:
                 if v1:
                    v1.validate()
        if self.annotation_mission_chat_vocabulary_info_list:
            for v1 in self.annotation_mission_chat_vocabulary_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_asr_result is not None:
            result['AnnotationAsrResult'] = self.annotation_asr_result

        result['AnnotationMissionChatCustomizationDataInfoList'] = []
        if self.annotation_mission_chat_customization_data_info_list is not None:
            for k1 in self.annotation_mission_chat_customization_data_info_list:
                result['AnnotationMissionChatCustomizationDataInfoList'].append(k1.to_map() if k1 else None)

        if self.annotation_mission_chat_id is not None:
            result['AnnotationMissionChatId'] = self.annotation_mission_chat_id

        result['AnnotationMissionChatIntentUserSayInfoList'] = []
        if self.annotation_mission_chat_intent_user_say_info_list is not None:
            for k1 in self.annotation_mission_chat_intent_user_say_info_list:
                result['AnnotationMissionChatIntentUserSayInfoList'].append(k1.to_map() if k1 else None)

        result['AnnotationMissionChatTagInfoList'] = []
        if self.annotation_mission_chat_tag_info_list is not None:
            for k1 in self.annotation_mission_chat_tag_info_list:
                result['AnnotationMissionChatTagInfoList'].append(k1.to_map() if k1 else None)

        result['AnnotationMissionChatVocabularyInfoList'] = []
        if self.annotation_mission_chat_vocabulary_info_list is not None:
            for k1 in self.annotation_mission_chat_vocabulary_info_list:
                result['AnnotationMissionChatVocabularyInfoList'].append(k1.to_map() if k1 else None)

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.annotation_status is not None:
            result['AnnotationStatus'] = self.annotation_status

        if self.answer is not None:
            result['Answer'] = self.answer

        if self.asr_annotation_status is not None:
            result['AsrAnnotationStatus'] = self.asr_annotation_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_annotation_status is not None:
            result['IntentAnnotationStatus'] = self.intent_annotation_status

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time

        if self.original_asr_result is not None:
            result['OriginalAsrResult'] = self.original_asr_result

        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.tag_annotation_status is not None:
            result['TagAnnotationStatus'] = self.tag_annotation_status

        if self.translation_error is not None:
            result['TranslationError'] = self.translation_error

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationAsrResult') is not None:
            self.annotation_asr_result = m.get('AnnotationAsrResult')

        self.annotation_mission_chat_customization_data_info_list = []
        if m.get('AnnotationMissionChatCustomizationDataInfoList') is not None:
            for k1 in m.get('AnnotationMissionChatCustomizationDataInfoList'):
                temp_model = main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatCustomizationDataInfoList()
                self.annotation_mission_chat_customization_data_info_list.append(temp_model.from_map(k1))

        if m.get('AnnotationMissionChatId') is not None:
            self.annotation_mission_chat_id = m.get('AnnotationMissionChatId')

        self.annotation_mission_chat_intent_user_say_info_list = []
        if m.get('AnnotationMissionChatIntentUserSayInfoList') is not None:
            for k1 in m.get('AnnotationMissionChatIntentUserSayInfoList'):
                temp_model = main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatIntentUserSayInfoList()
                self.annotation_mission_chat_intent_user_say_info_list.append(temp_model.from_map(k1))

        self.annotation_mission_chat_tag_info_list = []
        if m.get('AnnotationMissionChatTagInfoList') is not None:
            for k1 in m.get('AnnotationMissionChatTagInfoList'):
                temp_model = main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatTagInfoList()
                self.annotation_mission_chat_tag_info_list.append(temp_model.from_map(k1))

        self.annotation_mission_chat_vocabulary_info_list = []
        if m.get('AnnotationMissionChatVocabularyInfoList') is not None:
            for k1 in m.get('AnnotationMissionChatVocabularyInfoList'):
                temp_model = main_models.ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatVocabularyInfoList()
                self.annotation_mission_chat_vocabulary_info_list.append(temp_model.from_map(k1))

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('AnnotationStatus') is not None:
            self.annotation_status = m.get('AnnotationStatus')

        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('AsrAnnotationStatus') is not None:
            self.asr_annotation_status = m.get('AsrAnnotationStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentAnnotationStatus') is not None:
            self.intent_annotation_status = m.get('IntentAnnotationStatus')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')

        if m.get('OriginalAsrResult') is not None:
            self.original_asr_result = m.get('OriginalAsrResult')

        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('TagAnnotationStatus') is not None:
            self.tag_annotation_status = m.get('TagAnnotationStatus')

        if m.get('TranslationError') is not None:
            self.translation_error = m.get('TranslationError')

        return self

class ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatVocabularyInfoList(DaraModel):
    def __init__(
        self,
        annotation_mission_chat_id: str = None,
        annotation_mission_chat_vocabulary_info_id: str = None,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        create: bool = None,
        create_time: int = None,
        delete: bool = None,
        instance_id: str = None,
        modified_time: int = None,
        vocabulary: str = None,
        vocabulary_description: str = None,
        vocabulary_id: str = None,
        vocabulary_name: str = None,
        vocabulary_weight: int = None,
    ):
        # chat id
        self.annotation_mission_chat_id = annotation_mission_chat_id
        # id
        self.annotation_mission_chat_vocabulary_info_id = annotation_mission_chat_vocabulary_info_id
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_id = annotation_mission_session_id
        self.create = create
        self.create_time = create_time
        self.delete = delete
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.vocabulary = vocabulary
        self.vocabulary_description = vocabulary_description
        self.vocabulary_id = vocabulary_id
        self.vocabulary_name = vocabulary_name
        self.vocabulary_weight = vocabulary_weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_chat_id is not None:
            result['AnnotationMissionChatId'] = self.annotation_mission_chat_id

        if self.annotation_mission_chat_vocabulary_info_id is not None:
            result['AnnotationMissionChatVocabularyInfoId'] = self.annotation_mission_chat_vocabulary_info_id

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.create is not None:
            result['Create'] = self.create

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.vocabulary is not None:
            result['Vocabulary'] = self.vocabulary

        if self.vocabulary_description is not None:
            result['VocabularyDescription'] = self.vocabulary_description

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        if self.vocabulary_name is not None:
            result['VocabularyName'] = self.vocabulary_name

        if self.vocabulary_weight is not None:
            result['VocabularyWeight'] = self.vocabulary_weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionChatId') is not None:
            self.annotation_mission_chat_id = m.get('AnnotationMissionChatId')

        if m.get('AnnotationMissionChatVocabularyInfoId') is not None:
            self.annotation_mission_chat_vocabulary_info_id = m.get('AnnotationMissionChatVocabularyInfoId')

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('Create') is not None:
            self.create = m.get('Create')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Vocabulary') is not None:
            self.vocabulary = m.get('Vocabulary')

        if m.get('VocabularyDescription') is not None:
            self.vocabulary_description = m.get('VocabularyDescription')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        if m.get('VocabularyName') is not None:
            self.vocabulary_name = m.get('VocabularyName')

        if m.get('VocabularyWeight') is not None:
            self.vocabulary_weight = m.get('VocabularyWeight')

        return self

class ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatTagInfoList(DaraModel):
    def __init__(
        self,
        annotation_mission_chat_id: str = None,
        annotation_mission_chat_tag_info_id: str = None,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        annotation_mission_tag_info_id: str = None,
        annotation_mission_tag_info_name: str = None,
        create: bool = None,
        create_time: int = None,
        delete: bool = None,
        instance_id: str = None,
        modified_time: int = None,
    ):
        # chat id
        self.annotation_mission_chat_id = annotation_mission_chat_id
        # id
        self.annotation_mission_chat_tag_info_id = annotation_mission_chat_tag_info_id
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_id = annotation_mission_session_id
        # tag id
        self.annotation_mission_tag_info_id = annotation_mission_tag_info_id
        self.annotation_mission_tag_info_name = annotation_mission_tag_info_name
        self.create = create
        self.create_time = create_time
        self.delete = delete
        self.instance_id = instance_id
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_chat_id is not None:
            result['AnnotationMissionChatId'] = self.annotation_mission_chat_id

        if self.annotation_mission_chat_tag_info_id is not None:
            result['AnnotationMissionChatTagInfoId'] = self.annotation_mission_chat_tag_info_id

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.annotation_mission_tag_info_id is not None:
            result['AnnotationMissionTagInfoId'] = self.annotation_mission_tag_info_id

        if self.annotation_mission_tag_info_name is not None:
            result['AnnotationMissionTagInfoName'] = self.annotation_mission_tag_info_name

        if self.create is not None:
            result['Create'] = self.create

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionChatId') is not None:
            self.annotation_mission_chat_id = m.get('AnnotationMissionChatId')

        if m.get('AnnotationMissionChatTagInfoId') is not None:
            self.annotation_mission_chat_tag_info_id = m.get('AnnotationMissionChatTagInfoId')

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('AnnotationMissionTagInfoId') is not None:
            self.annotation_mission_tag_info_id = m.get('AnnotationMissionTagInfoId')

        if m.get('AnnotationMissionTagInfoName') is not None:
            self.annotation_mission_tag_info_name = m.get('AnnotationMissionTagInfoName')

        if m.get('Create') is not None:
            self.create = m.get('Create')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        return self

class ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatIntentUserSayInfoList(DaraModel):
    def __init__(
        self,
        annotation_mission_chat_id: str = None,
        annotation_mission_chat_intent_user_say_info_id: str = None,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        bot_id: str = None,
        content: str = None,
        create: bool = None,
        create_time: int = None,
        delete: bool = None,
        dialog_id: int = None,
        instance_id: str = None,
        intent_id: int = None,
        modified_time: int = None,
    ):
        # chat id
        self.annotation_mission_chat_id = annotation_mission_chat_id
        # id
        self.annotation_mission_chat_intent_user_say_info_id = annotation_mission_chat_intent_user_say_info_id
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_id = annotation_mission_session_id
        self.bot_id = bot_id
        self.content = content
        self.create = create
        self.create_time = create_time
        self.delete = delete
        self.dialog_id = dialog_id
        self.instance_id = instance_id
        self.intent_id = intent_id
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_chat_id is not None:
            result['AnnotationMissionChatId'] = self.annotation_mission_chat_id

        if self.annotation_mission_chat_intent_user_say_info_id is not None:
            result['AnnotationMissionChatIntentUserSayInfoId'] = self.annotation_mission_chat_intent_user_say_info_id

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.content is not None:
            result['Content'] = self.content

        if self.create is not None:
            result['Create'] = self.create

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intent_id is not None:
            result['IntentId'] = self.intent_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionChatId') is not None:
            self.annotation_mission_chat_id = m.get('AnnotationMissionChatId')

        if m.get('AnnotationMissionChatIntentUserSayInfoId') is not None:
            self.annotation_mission_chat_intent_user_say_info_id = m.get('AnnotationMissionChatIntentUserSayInfoId')

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Create') is not None:
            self.create = m.get('Create')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        return self

class ListAnnotationMissionSessionResponseBodyDataAnnotationMissionSessionListAnnotationMissionChatListAnnotationMissionChatCustomizationDataInfoList(DaraModel):
    def __init__(
        self,
        annotation_mission_chat_customization_data_info_id: str = None,
        annotation_mission_chat_id: str = None,
        annotation_mission_id: str = None,
        annotation_mission_session_id: str = None,
        content: str = None,
        create: bool = None,
        create_time: int = None,
        customization_data_description: str = None,
        customization_data_id: str = None,
        customization_data_name: str = None,
        customization_data_weight: int = None,
        delete: bool = None,
        instance_id: str = None,
        modified_time: int = None,
    ):
        # id
        self.annotation_mission_chat_customization_data_info_id = annotation_mission_chat_customization_data_info_id
        # chat id
        self.annotation_mission_chat_id = annotation_mission_chat_id
        self.annotation_mission_id = annotation_mission_id
        self.annotation_mission_session_id = annotation_mission_session_id
        self.content = content
        self.create = create
        self.create_time = create_time
        self.customization_data_description = customization_data_description
        # id
        self.customization_data_id = customization_data_id
        self.customization_data_name = customization_data_name
        self.customization_data_weight = customization_data_weight
        self.delete = delete
        self.instance_id = instance_id
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_chat_customization_data_info_id is not None:
            result['AnnotationMissionChatCustomizationDataInfoId'] = self.annotation_mission_chat_customization_data_info_id

        if self.annotation_mission_chat_id is not None:
            result['AnnotationMissionChatId'] = self.annotation_mission_chat_id

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_session_id is not None:
            result['AnnotationMissionSessionId'] = self.annotation_mission_session_id

        if self.content is not None:
            result['Content'] = self.content

        if self.create is not None:
            result['Create'] = self.create

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.customization_data_description is not None:
            result['CustomizationDataDescription'] = self.customization_data_description

        if self.customization_data_id is not None:
            result['CustomizationDataId'] = self.customization_data_id

        if self.customization_data_name is not None:
            result['CustomizationDataName'] = self.customization_data_name

        if self.customization_data_weight is not None:
            result['CustomizationDataWeight'] = self.customization_data_weight

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionChatCustomizationDataInfoId') is not None:
            self.annotation_mission_chat_customization_data_info_id = m.get('AnnotationMissionChatCustomizationDataInfoId')

        if m.get('AnnotationMissionChatId') is not None:
            self.annotation_mission_chat_id = m.get('AnnotationMissionChatId')

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionSessionId') is not None:
            self.annotation_mission_session_id = m.get('AnnotationMissionSessionId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Create') is not None:
            self.create = m.get('Create')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomizationDataDescription') is not None:
            self.customization_data_description = m.get('CustomizationDataDescription')

        if m.get('CustomizationDataId') is not None:
            self.customization_data_id = m.get('CustomizationDataId')

        if m.get('CustomizationDataName') is not None:
            self.customization_data_name = m.get('CustomizationDataName')

        if m.get('CustomizationDataWeight') is not None:
            self.customization_data_weight = m.get('CustomizationDataWeight')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        return self

