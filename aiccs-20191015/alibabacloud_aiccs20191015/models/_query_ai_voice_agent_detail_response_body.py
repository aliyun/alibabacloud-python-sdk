# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryAiVoiceAgentDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryAiVoiceAgentDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAiVoiceAgentDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_name: str = None,
        ai_voice_agent_call_config: main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfig = None,
        ai_voice_agent_model_config: main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfig = None,
        business_type_name: str = None,
        description: str = None,
        knowledge_name: str = None,
        status: int = None,
        voice_style_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.ai_voice_agent_call_config = ai_voice_agent_call_config
        self.ai_voice_agent_model_config = ai_voice_agent_model_config
        self.business_type_name = business_type_name
        self.description = description
        self.knowledge_name = knowledge_name
        self.status = status
        self.voice_style_name = voice_style_name

    def validate(self):
        if self.ai_voice_agent_call_config:
            self.ai_voice_agent_call_config.validate()
        if self.ai_voice_agent_model_config:
            self.ai_voice_agent_model_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.ai_voice_agent_call_config is not None:
            result['AiVoiceAgentCallConfig'] = self.ai_voice_agent_call_config.to_map()

        if self.ai_voice_agent_model_config is not None:
            result['AiVoiceAgentModelConfig'] = self.ai_voice_agent_model_config.to_map()

        if self.business_type_name is not None:
            result['BusinessTypeName'] = self.business_type_name

        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_name is not None:
            result['KnowledgeName'] = self.knowledge_name

        if self.status is not None:
            result['Status'] = self.status

        if self.voice_style_name is not None:
            result['VoiceStyleName'] = self.voice_style_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AiVoiceAgentCallConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfig()
            self.ai_voice_agent_call_config = temp_model.from_map(m.get('AiVoiceAgentCallConfig'))

        if m.get('AiVoiceAgentModelConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfig()
            self.ai_voice_agent_model_config = temp_model.from_map(m.get('AiVoiceAgentModelConfig'))

        if m.get('BusinessTypeName') is not None:
            self.business_type_name = m.get('BusinessTypeName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeName') is not None:
            self.knowledge_name = m.get('KnowledgeName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VoiceStyleName') is not None:
            self.voice_style_name = m.get('VoiceStyleName')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfig(DaraModel):
    def __init__(
        self,
        basic_task_description: str = None,
        business_type: int = None,
        child_task_list: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigChildTaskList] = None,
        custom_exception_enable: bool = None,
        custom_exception_file_id: str = None,
        custom_exception_file_name: str = None,
        custom_exception_list: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigCustomExceptionList] = None,
        custom_exception_url_path: str = None,
        custom_exception_voice_style: int = None,
        flow_desc: str = None,
        knowledge_doc_id_list: List[str] = None,
        knowledge_doc_name_list: List[str] = None,
        knowledge_doc_original_name_list: List[str] = None,
        knowledge_enable: bool = None,
        knowledge_id: str = None,
        main_purpose: main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigMainPurpose = None,
        output_tag_config: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigOutputTagConfig] = None,
        phone_tag_config: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigPhoneTagConfig] = None,
        prologue: str = None,
        recording_file: str = None,
        start_word_type: int = None,
        sys_role: str = None,
        task_type: str = None,
        user_role: str = None,
    ):
        self.basic_task_description = basic_task_description
        self.business_type = business_type
        self.child_task_list = child_task_list
        self.custom_exception_enable = custom_exception_enable
        self.custom_exception_file_id = custom_exception_file_id
        self.custom_exception_file_name = custom_exception_file_name
        self.custom_exception_list = custom_exception_list
        self.custom_exception_url_path = custom_exception_url_path
        self.custom_exception_voice_style = custom_exception_voice_style
        self.flow_desc = flow_desc
        self.knowledge_doc_id_list = knowledge_doc_id_list
        self.knowledge_doc_name_list = knowledge_doc_name_list
        self.knowledge_doc_original_name_list = knowledge_doc_original_name_list
        self.knowledge_enable = knowledge_enable
        self.knowledge_id = knowledge_id
        self.main_purpose = main_purpose
        self.output_tag_config = output_tag_config
        self.phone_tag_config = phone_tag_config
        self.prologue = prologue
        self.recording_file = recording_file
        self.start_word_type = start_word_type
        self.sys_role = sys_role
        self.task_type = task_type
        self.user_role = user_role

    def validate(self):
        if self.child_task_list:
            for v1 in self.child_task_list:
                 if v1:
                    v1.validate()
        if self.custom_exception_list:
            for v1 in self.custom_exception_list:
                 if v1:
                    v1.validate()
        if self.main_purpose:
            self.main_purpose.validate()
        if self.output_tag_config:
            for v1 in self.output_tag_config:
                 if v1:
                    v1.validate()
        if self.phone_tag_config:
            for v1 in self.phone_tag_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_task_description is not None:
            result['BasicTaskDescription'] = self.basic_task_description

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        result['ChildTaskList'] = []
        if self.child_task_list is not None:
            for k1 in self.child_task_list:
                result['ChildTaskList'].append(k1.to_map() if k1 else None)

        if self.custom_exception_enable is not None:
            result['CustomExceptionEnable'] = self.custom_exception_enable

        if self.custom_exception_file_id is not None:
            result['CustomExceptionFileId'] = self.custom_exception_file_id

        if self.custom_exception_file_name is not None:
            result['CustomExceptionFileName'] = self.custom_exception_file_name

        result['CustomExceptionList'] = []
        if self.custom_exception_list is not None:
            for k1 in self.custom_exception_list:
                result['CustomExceptionList'].append(k1.to_map() if k1 else None)

        if self.custom_exception_url_path is not None:
            result['CustomExceptionUrlPath'] = self.custom_exception_url_path

        if self.custom_exception_voice_style is not None:
            result['CustomExceptionVoiceStyle'] = self.custom_exception_voice_style

        if self.flow_desc is not None:
            result['FlowDesc'] = self.flow_desc

        if self.knowledge_doc_id_list is not None:
            result['KnowledgeDocIdList'] = self.knowledge_doc_id_list

        if self.knowledge_doc_name_list is not None:
            result['KnowledgeDocNameList'] = self.knowledge_doc_name_list

        if self.knowledge_doc_original_name_list is not None:
            result['KnowledgeDocOriginalNameList'] = self.knowledge_doc_original_name_list

        if self.knowledge_enable is not None:
            result['KnowledgeEnable'] = self.knowledge_enable

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.main_purpose is not None:
            result['MainPurpose'] = self.main_purpose.to_map()

        result['OutputTagConfig'] = []
        if self.output_tag_config is not None:
            for k1 in self.output_tag_config:
                result['OutputTagConfig'].append(k1.to_map() if k1 else None)

        result['PhoneTagConfig'] = []
        if self.phone_tag_config is not None:
            for k1 in self.phone_tag_config:
                result['PhoneTagConfig'].append(k1.to_map() if k1 else None)

        if self.prologue is not None:
            result['Prologue'] = self.prologue

        if self.recording_file is not None:
            result['RecordingFile'] = self.recording_file

        if self.start_word_type is not None:
            result['StartWordType'] = self.start_word_type

        if self.sys_role is not None:
            result['SysRole'] = self.sys_role

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_role is not None:
            result['UserRole'] = self.user_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicTaskDescription') is not None:
            self.basic_task_description = m.get('BasicTaskDescription')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        self.child_task_list = []
        if m.get('ChildTaskList') is not None:
            for k1 in m.get('ChildTaskList'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigChildTaskList()
                self.child_task_list.append(temp_model.from_map(k1))

        if m.get('CustomExceptionEnable') is not None:
            self.custom_exception_enable = m.get('CustomExceptionEnable')

        if m.get('CustomExceptionFileId') is not None:
            self.custom_exception_file_id = m.get('CustomExceptionFileId')

        if m.get('CustomExceptionFileName') is not None:
            self.custom_exception_file_name = m.get('CustomExceptionFileName')

        self.custom_exception_list = []
        if m.get('CustomExceptionList') is not None:
            for k1 in m.get('CustomExceptionList'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigCustomExceptionList()
                self.custom_exception_list.append(temp_model.from_map(k1))

        if m.get('CustomExceptionUrlPath') is not None:
            self.custom_exception_url_path = m.get('CustomExceptionUrlPath')

        if m.get('CustomExceptionVoiceStyle') is not None:
            self.custom_exception_voice_style = m.get('CustomExceptionVoiceStyle')

        if m.get('FlowDesc') is not None:
            self.flow_desc = m.get('FlowDesc')

        if m.get('KnowledgeDocIdList') is not None:
            self.knowledge_doc_id_list = m.get('KnowledgeDocIdList')

        if m.get('KnowledgeDocNameList') is not None:
            self.knowledge_doc_name_list = m.get('KnowledgeDocNameList')

        if m.get('KnowledgeDocOriginalNameList') is not None:
            self.knowledge_doc_original_name_list = m.get('KnowledgeDocOriginalNameList')

        if m.get('KnowledgeEnable') is not None:
            self.knowledge_enable = m.get('KnowledgeEnable')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('MainPurpose') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigMainPurpose()
            self.main_purpose = temp_model.from_map(m.get('MainPurpose'))

        self.output_tag_config = []
        if m.get('OutputTagConfig') is not None:
            for k1 in m.get('OutputTagConfig'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigOutputTagConfig()
                self.output_tag_config.append(temp_model.from_map(k1))

        self.phone_tag_config = []
        if m.get('PhoneTagConfig') is not None:
            for k1 in m.get('PhoneTagConfig'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigPhoneTagConfig()
                self.phone_tag_config.append(temp_model.from_map(k1))

        if m.get('Prologue') is not None:
            self.prologue = m.get('Prologue')

        if m.get('RecordingFile') is not None:
            self.recording_file = m.get('RecordingFile')

        if m.get('StartWordType') is not None:
            self.start_word_type = m.get('StartWordType')

        if m.get('SysRole') is not None:
            self.sys_role = m.get('SysRole')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigPhoneTagConfig(DaraModel):
    def __init__(
        self,
        id: str = None,
        phone_tag_description: str = None,
        phone_tag_enum: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigPhoneTagConfigPhoneTagEnum] = None,
        phone_tag_key: str = None,
        phone_tag_name: str = None,
        phone_tag_required: bool = None,
        phone_tag_source: str = None,
        phone_tag_type: str = None,
    ):
        self.id = id
        self.phone_tag_description = phone_tag_description
        self.phone_tag_enum = phone_tag_enum
        self.phone_tag_key = phone_tag_key
        self.phone_tag_name = phone_tag_name
        self.phone_tag_required = phone_tag_required
        self.phone_tag_source = phone_tag_source
        self.phone_tag_type = phone_tag_type

    def validate(self):
        if self.phone_tag_enum:
            for v1 in self.phone_tag_enum:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.phone_tag_description is not None:
            result['PhoneTagDescription'] = self.phone_tag_description

        result['PhoneTagEnum'] = []
        if self.phone_tag_enum is not None:
            for k1 in self.phone_tag_enum:
                result['PhoneTagEnum'].append(k1.to_map() if k1 else None)

        if self.phone_tag_key is not None:
            result['PhoneTagKey'] = self.phone_tag_key

        if self.phone_tag_name is not None:
            result['PhoneTagName'] = self.phone_tag_name

        if self.phone_tag_required is not None:
            result['PhoneTagRequired'] = self.phone_tag_required

        if self.phone_tag_source is not None:
            result['PhoneTagSource'] = self.phone_tag_source

        if self.phone_tag_type is not None:
            result['PhoneTagType'] = self.phone_tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PhoneTagDescription') is not None:
            self.phone_tag_description = m.get('PhoneTagDescription')

        self.phone_tag_enum = []
        if m.get('PhoneTagEnum') is not None:
            for k1 in m.get('PhoneTagEnum'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigPhoneTagConfigPhoneTagEnum()
                self.phone_tag_enum.append(temp_model.from_map(k1))

        if m.get('PhoneTagKey') is not None:
            self.phone_tag_key = m.get('PhoneTagKey')

        if m.get('PhoneTagName') is not None:
            self.phone_tag_name = m.get('PhoneTagName')

        if m.get('PhoneTagRequired') is not None:
            self.phone_tag_required = m.get('PhoneTagRequired')

        if m.get('PhoneTagSource') is not None:
            self.phone_tag_source = m.get('PhoneTagSource')

        if m.get('PhoneTagType') is not None:
            self.phone_tag_type = m.get('PhoneTagType')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigPhoneTagConfigPhoneTagEnum(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        value: str = None,
    ):
        self.description = description
        self.id = id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigOutputTagConfig(DaraModel):
    def __init__(
        self,
        id: str = None,
        output_tag_description: str = None,
        output_tag_enum: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigOutputTagConfigOutputTagEnum] = None,
        output_tag_name: str = None,
        output_tag_type: str = None,
    ):
        self.id = id
        self.output_tag_description = output_tag_description
        self.output_tag_enum = output_tag_enum
        self.output_tag_name = output_tag_name
        self.output_tag_type = output_tag_type

    def validate(self):
        if self.output_tag_enum:
            for v1 in self.output_tag_enum:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.output_tag_description is not None:
            result['OutputTagDescription'] = self.output_tag_description

        result['OutputTagEnum'] = []
        if self.output_tag_enum is not None:
            for k1 in self.output_tag_enum:
                result['OutputTagEnum'].append(k1.to_map() if k1 else None)

        if self.output_tag_name is not None:
            result['OutputTagName'] = self.output_tag_name

        if self.output_tag_type is not None:
            result['OutputTagType'] = self.output_tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OutputTagDescription') is not None:
            self.output_tag_description = m.get('OutputTagDescription')

        self.output_tag_enum = []
        if m.get('OutputTagEnum') is not None:
            for k1 in m.get('OutputTagEnum'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigOutputTagConfigOutputTagEnum()
                self.output_tag_enum.append(temp_model.from_map(k1))

        if m.get('OutputTagName') is not None:
            self.output_tag_name = m.get('OutputTagName')

        if m.get('OutputTagType') is not None:
            self.output_tag_type = m.get('OutputTagType')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigOutputTagConfigOutputTagEnum(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        value: str = None,
    ):
        self.description = description
        self.id = id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigMainPurpose(DaraModel):
    def __init__(
        self,
        id: str = None,
        main_purpose_description: str = None,
        main_purpose_enum: List[main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigMainPurposeMainPurposeEnum] = None,
        main_purpose_name: str = None,
        main_purpose_type: str = None,
    ):
        self.id = id
        self.main_purpose_description = main_purpose_description
        self.main_purpose_enum = main_purpose_enum
        self.main_purpose_name = main_purpose_name
        self.main_purpose_type = main_purpose_type

    def validate(self):
        if self.main_purpose_enum:
            for v1 in self.main_purpose_enum:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.main_purpose_description is not None:
            result['MainPurposeDescription'] = self.main_purpose_description

        result['MainPurposeEnum'] = []
        if self.main_purpose_enum is not None:
            for k1 in self.main_purpose_enum:
                result['MainPurposeEnum'].append(k1.to_map() if k1 else None)

        if self.main_purpose_name is not None:
            result['MainPurposeName'] = self.main_purpose_name

        if self.main_purpose_type is not None:
            result['MainPurposeType'] = self.main_purpose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MainPurposeDescription') is not None:
            self.main_purpose_description = m.get('MainPurposeDescription')

        self.main_purpose_enum = []
        if m.get('MainPurposeEnum') is not None:
            for k1 in m.get('MainPurposeEnum'):
                temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigMainPurposeMainPurposeEnum()
                self.main_purpose_enum.append(temp_model.from_map(k1))

        if m.get('MainPurposeName') is not None:
            self.main_purpose_name = m.get('MainPurposeName')

        if m.get('MainPurposeType') is not None:
            self.main_purpose_type = m.get('MainPurposeType')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigMainPurposeMainPurposeEnum(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        value: str = None,
    ):
        self.description = description
        self.id = id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigCustomExceptionList(DaraModel):
    def __init__(
        self,
        exception_sign: bool = None,
        exception_type: str = None,
        reply: str = None,
        support_break: bool = None,
    ):
        self.exception_sign = exception_sign
        self.exception_type = exception_type
        self.reply = reply
        self.support_break = support_break

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_sign is not None:
            result['ExceptionSign'] = self.exception_sign

        if self.exception_type is not None:
            result['ExceptionType'] = self.exception_type

        if self.reply is not None:
            result['Reply'] = self.reply

        if self.support_break is not None:
            result['SupportBreak'] = self.support_break

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionSign') is not None:
            self.exception_sign = m.get('ExceptionSign')

        if m.get('ExceptionType') is not None:
            self.exception_type = m.get('ExceptionType')

        if m.get('Reply') is not None:
            self.reply = m.get('Reply')

        if m.get('SupportBreak') is not None:
            self.support_break = m.get('SupportBreak')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentModelConfigChildTaskList(DaraModel):
    def __init__(
        self,
        child_task_description: str = None,
        child_task_name: str = None,
        id: str = None,
    ):
        self.child_task_description = child_task_description
        self.child_task_name = child_task_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_task_description is not None:
            result['ChildTaskDescription'] = self.child_task_description

        if self.child_task_name is not None:
            result['ChildTaskName'] = self.child_task_name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildTaskDescription') is not None:
            self.child_task_description = m.get('ChildTaskDescription')

        if m.get('ChildTaskName') is not None:
            self.child_task_name = m.get('ChildTaskName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfig(DaraModel):
    def __init__(
        self,
        event_config: main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfigEventConfig = None,
        tts_config: main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfigTtsConfig = None,
        vocab_id: str = None,
    ):
        self.event_config = event_config
        self.tts_config = tts_config
        self.vocab_id = vocab_id

    def validate(self):
        if self.event_config:
            self.event_config.validate()
        if self.tts_config:
            self.tts_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_config is not None:
            result['EventConfig'] = self.event_config.to_map()

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config.to_map()

        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfigEventConfig()
            self.event_config = temp_model.from_map(m.get('EventConfig'))

        if m.get('TtsConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfigTtsConfig()
            self.tts_config = temp_model.from_map(m.get('TtsConfig'))

        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfigTtsConfig(DaraModel):
    def __init__(
        self,
        background_enabled: bool = None,
        background_sound: int = None,
        background_volume: int = None,
        mixing_enabled: bool = None,
        mixing_template: int = None,
        tts_speed: int = None,
        tts_style: str = None,
        tts_volume: int = None,
        voice_code: str = None,
        voice_type: str = None,
    ):
        self.background_enabled = background_enabled
        self.background_sound = background_sound
        self.background_volume = background_volume
        self.mixing_enabled = mixing_enabled
        self.mixing_template = mixing_template
        self.tts_speed = tts_speed
        self.tts_style = tts_style
        self.tts_volume = tts_volume
        self.voice_code = voice_code
        self.voice_type = voice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_enabled is not None:
            result['BackgroundEnabled'] = self.background_enabled

        if self.background_sound is not None:
            result['BackgroundSound'] = self.background_sound

        if self.background_volume is not None:
            result['BackgroundVolume'] = self.background_volume

        if self.mixing_enabled is not None:
            result['MixingEnabled'] = self.mixing_enabled

        if self.mixing_template is not None:
            result['MixingTemplate'] = self.mixing_template

        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed

        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style

        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume

        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code

        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundEnabled') is not None:
            self.background_enabled = m.get('BackgroundEnabled')

        if m.get('BackgroundSound') is not None:
            self.background_sound = m.get('BackgroundSound')

        if m.get('BackgroundVolume') is not None:
            self.background_volume = m.get('BackgroundVolume')

        if m.get('MixingEnabled') is not None:
            self.mixing_enabled = m.get('MixingEnabled')

        if m.get('MixingTemplate') is not None:
            self.mixing_template = m.get('MixingTemplate')

        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')

        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')

        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')

        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')

        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')

        return self

class QueryAiVoiceAgentDetailResponseBodyDataAiVoiceAgentCallConfigEventConfig(DaraModel):
    def __init__(
        self,
        call_assistant_hangup: bool = None,
        call_assistant_recognize: bool = None,
        mute_active: bool = None,
        mute_duration: int = None,
        mute_hangup_num: int = None,
        session_timeout: int = None,
    ):
        self.call_assistant_hangup = call_assistant_hangup
        self.call_assistant_recognize = call_assistant_recognize
        self.mute_active = mute_active
        self.mute_duration = mute_duration
        self.mute_hangup_num = mute_hangup_num
        self.session_timeout = session_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_assistant_hangup is not None:
            result['CallAssistantHangup'] = self.call_assistant_hangup

        if self.call_assistant_recognize is not None:
            result['CallAssistantRecognize'] = self.call_assistant_recognize

        if self.mute_active is not None:
            result['MuteActive'] = self.mute_active

        if self.mute_duration is not None:
            result['MuteDuration'] = self.mute_duration

        if self.mute_hangup_num is not None:
            result['MuteHangupNum'] = self.mute_hangup_num

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallAssistantHangup') is not None:
            self.call_assistant_hangup = m.get('CallAssistantHangup')

        if m.get('CallAssistantRecognize') is not None:
            self.call_assistant_recognize = m.get('CallAssistantRecognize')

        if m.get('MuteActive') is not None:
            self.mute_active = m.get('MuteActive')

        if m.get('MuteDuration') is not None:
            self.mute_duration = m.get('MuteDuration')

        if m.get('MuteHangupNum') is not None:
            self.mute_hangup_num = m.get('MuteHangupNum')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        return self

