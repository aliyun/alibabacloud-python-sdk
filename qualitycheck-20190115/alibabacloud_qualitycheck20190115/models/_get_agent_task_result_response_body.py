# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetAgentTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentTaskResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The returned result.
        self.data = data
        # The error message returned when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. You can use this field to determine whether the request was successful:
        # 
        # - **true**: successful.
        # - **false/null**: failed.
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
            temp_model = main_models.GetAgentTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgentTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        dialogues: List[main_models.GetAgentTaskResultResponseBodyDataDialogues] = None,
        error_message: str = None,
        llm_request_id: str = None,
        response: main_models.GetAgentTaskResultResponseBodyDataResponse = None,
        status: str = None,
        task_id: str = None,
        usage: main_models.GetAgentTaskResultResponseBodyDataUsage = None,
        vid: str = None,
    ):
        self.dialogues = dialogues
        self.error_message = error_message
        # The request ID returned by the large language model service.
        self.llm_request_id = llm_request_id
        # The result of the computation task.
        self.response = response
        # The task status. Valid values:
        # 
        # - 1: pending.
        # - 2: running.
        # - 3: succeeded.
        # - 4: failed.
        self.status = status
        # The task ID.
        self.task_id = task_id
        self.usage = usage
        # The session ID.
        self.vid = vid

    def validate(self):
        if self.dialogues:
            for v1 in self.dialogues:
                 if v1:
                    v1.validate()
        if self.response:
            self.response.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dialogues'] = []
        if self.dialogues is not None:
            for k1 in self.dialogues:
                result['Dialogues'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.llm_request_id is not None:
            result['LlmRequestId'] = self.llm_request_id

        if self.response is not None:
            result['Response'] = self.response.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        if self.vid is not None:
            result['Vid'] = self.vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogues = []
        if m.get('Dialogues') is not None:
            for k1 in m.get('Dialogues'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataDialogues()
                self.dialogues.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('LlmRequestId') is not None:
            self.llm_request_id = m.get('LlmRequestId')

        if m.get('Response') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponse()
            self.response = temp_model.from_map(m.get('Response'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Usage') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        if m.get('Vid') is not None:
            self.vid = m.get('Vid')

        return self

class GetAgentTaskResultResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        input_tokens: str = None,
        output_tokens: str = None,
        total_tokens: str = None,
        tymx_plus_count: str = None,
        tymx_turbo_count: str = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens
        self.tymx_plus_count = tymx_plus_count
        self.tymx_turbo_count = tymx_turbo_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.tymx_plus_count is not None:
            result['TymxPlusCount'] = self.tymx_plus_count

        if self.tymx_turbo_count is not None:
            result['TymxTurboCount'] = self.tymx_turbo_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('TymxPlusCount') is not None:
            self.tymx_plus_count = m.get('TymxPlusCount')

        if m.get('TymxTurboCount') is not None:
            self.tymx_turbo_count = m.get('TymxTurboCount')

        return self

class GetAgentTaskResultResponseBodyDataResponse(DaraModel):
    def __init__(
        self,
        customer_prompt_response: main_models.GetAgentTaskResultResponseBodyDataResponseCustomerPromptResponse = None,
        field_response: main_models.GetAgentTaskResultResponseBodyDataResponseFieldResponse = None,
        multi_level_tag_response: main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponse = None,
        service_inspection_response: main_models.GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponse = None,
        tag_category_response: main_models.GetAgentTaskResultResponseBodyDataResponseTagCategoryResponse = None,
        voiceprint_response: main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponse = None,
    ):
        # The result of the custom prompt.
        self.customer_prompt_response = customer_prompt_response
        # The property extraction result.
        self.field_response = field_response
        self.multi_level_tag_response = multi_level_tag_response
        # The service quality inspection result.
        self.service_inspection_response = service_inspection_response
        # The tag categorization result.
        self.tag_category_response = tag_category_response
        self.voiceprint_response = voiceprint_response

    def validate(self):
        if self.customer_prompt_response:
            self.customer_prompt_response.validate()
        if self.field_response:
            self.field_response.validate()
        if self.multi_level_tag_response:
            self.multi_level_tag_response.validate()
        if self.service_inspection_response:
            self.service_inspection_response.validate()
        if self.tag_category_response:
            self.tag_category_response.validate()
        if self.voiceprint_response:
            self.voiceprint_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_prompt_response is not None:
            result['CustomerPromptResponse'] = self.customer_prompt_response.to_map()

        if self.field_response is not None:
            result['FieldResponse'] = self.field_response.to_map()

        if self.multi_level_tag_response is not None:
            result['MultiLevelTagResponse'] = self.multi_level_tag_response.to_map()

        if self.service_inspection_response is not None:
            result['ServiceInspectionResponse'] = self.service_inspection_response.to_map()

        if self.tag_category_response is not None:
            result['TagCategoryResponse'] = self.tag_category_response.to_map()

        if self.voiceprint_response is not None:
            result['VoiceprintResponse'] = self.voiceprint_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerPromptResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseCustomerPromptResponse()
            self.customer_prompt_response = temp_model.from_map(m.get('CustomerPromptResponse'))

        if m.get('FieldResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseFieldResponse()
            self.field_response = temp_model.from_map(m.get('FieldResponse'))

        if m.get('MultiLevelTagResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponse()
            self.multi_level_tag_response = temp_model.from_map(m.get('MultiLevelTagResponse'))

        if m.get('ServiceInspectionResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponse()
            self.service_inspection_response = temp_model.from_map(m.get('ServiceInspectionResponse'))

        if m.get('TagCategoryResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseTagCategoryResponse()
            self.tag_category_response = temp_model.from_map(m.get('TagCategoryResponse'))

        if m.get('VoiceprintResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponse()
            self.voiceprint_response = temp_model.from_map(m.get('VoiceprintResponse'))

        return self

class GetAgentTaskResultResponseBodyDataResponseVoiceprintResponse(DaraModel):
    def __init__(
        self,
        dialogue: List[main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseDialogue] = None,
        errors: List[main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseErrors] = None,
    ):
        self.dialogue = dialogue
        self.errors = errors

    def validate(self):
        if self.dialogue:
            for v1 in self.dialogue:
                 if v1:
                    v1.validate()
        if self.errors:
            for v1 in self.errors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dialogue'] = []
        if self.dialogue is not None:
            for k1 in self.dialogue:
                result['Dialogue'].append(k1.to_map() if k1 else None)

        result['Errors'] = []
        if self.errors is not None:
            for k1 in self.errors:
                result['Errors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogue = []
        if m.get('Dialogue') is not None:
            for k1 in m.get('Dialogue'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseDialogue()
                self.dialogue.append(temp_model.from_map(k1))

        self.errors = []
        if m.get('Errors') is not None:
            for k1 in m.get('Errors'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseErrors()
                self.errors.append(temp_model.from_map(k1))

        return self

class GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseErrors(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseDialogue(DaraModel):
    def __init__(
        self,
        additions: main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseDialogueAdditions = None,
        begin: int = None,
        end: int = None,
        words: str = None,
    ):
        self.additions = additions
        self.begin = begin
        self.end = end
        self.words = words

    def validate(self):
        if self.additions:
            self.additions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additions is not None:
            result['Additions'] = self.additions.to_map()

        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Additions') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseDialogueAdditions()
            self.additions = temp_model.from_map(m.get('Additions'))

        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

class GetAgentTaskResultResponseBodyDataResponseVoiceprintResponseDialogueAdditions(DaraModel):
    def __init__(
        self,
        age: str = None,
        age_group: str = None,
        age_score: float = None,
        best_voiceprint_score: float = None,
        emotion: str = None,
        emotion_score: float = None,
        gender: str = None,
        gender_score: float = None,
        is_known_voiceprint: bool = None,
        speaker: str = None,
    ):
        self.age = age
        self.age_group = age_group
        self.age_score = age_score
        self.best_voiceprint_score = best_voiceprint_score
        self.emotion = emotion
        self.emotion_score = emotion_score
        self.gender = gender
        self.gender_score = gender_score
        self.is_known_voiceprint = is_known_voiceprint
        self.speaker = speaker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.age is not None:
            result['Age'] = self.age

        if self.age_group is not None:
            result['AgeGroup'] = self.age_group

        if self.age_score is not None:
            result['AgeScore'] = self.age_score

        if self.best_voiceprint_score is not None:
            result['BestVoiceprintScore'] = self.best_voiceprint_score

        if self.emotion is not None:
            result['Emotion'] = self.emotion

        if self.emotion_score is not None:
            result['EmotionScore'] = self.emotion_score

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.gender_score is not None:
            result['GenderScore'] = self.gender_score

        if self.is_known_voiceprint is not None:
            result['IsKnownVoiceprint'] = self.is_known_voiceprint

        if self.speaker is not None:
            result['Speaker'] = self.speaker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')

        if m.get('AgeGroup') is not None:
            self.age_group = m.get('AgeGroup')

        if m.get('AgeScore') is not None:
            self.age_score = m.get('AgeScore')

        if m.get('BestVoiceprintScore') is not None:
            self.best_voiceprint_score = m.get('BestVoiceprintScore')

        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')

        if m.get('EmotionScore') is not None:
            self.emotion_score = m.get('EmotionScore')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('GenderScore') is not None:
            self.gender_score = m.get('GenderScore')

        if m.get('IsKnownVoiceprint') is not None:
            self.is_known_voiceprint = m.get('IsKnownVoiceprint')

        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')

        return self

class GetAgentTaskResultResponseBodyDataResponseTagCategoryResponse(DaraModel):
    def __init__(
        self,
        tag_category_vo_list: List[main_models.GetAgentTaskResultResponseBodyDataResponseTagCategoryResponseTagCategoryVoList] = None,
    ):
        # The list of labels.
        self.tag_category_vo_list = tag_category_vo_list

    def validate(self):
        if self.tag_category_vo_list:
            for v1 in self.tag_category_vo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagCategoryVoList'] = []
        if self.tag_category_vo_list is not None:
            for k1 in self.tag_category_vo_list:
                result['TagCategoryVoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_category_vo_list = []
        if m.get('TagCategoryVoList') is not None:
            for k1 in m.get('TagCategoryVoList'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseTagCategoryResponseTagCategoryVoList()
                self.tag_category_vo_list.append(temp_model.from_map(k1))

        return self

class GetAgentTaskResultResponseBodyDataResponseTagCategoryResponseTagCategoryVoList(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        is_match: bool = None,
        original_utterances: List[str] = None,
        remarks: str = None,
        result_labels: List[str] = None,
    ):
        # The label dimension.
        self.dimension = dimension
        # Indicates whether the label is matched.
        self.is_match = is_match
        # The sentences referenced in the reasoning.
        self.original_utterances = original_utterances
        # The reasoning for the judgment.
        self.remarks = remarks
        # The list of matched labels.
        self.result_labels = result_labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.is_match is not None:
            result['IsMatch'] = self.is_match

        if self.original_utterances is not None:
            result['OriginalUtterances'] = self.original_utterances

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.result_labels is not None:
            result['ResultLabels'] = self.result_labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('IsMatch') is not None:
            self.is_match = m.get('IsMatch')

        if m.get('OriginalUtterances') is not None:
            self.original_utterances = m.get('OriginalUtterances')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('ResultLabels') is not None:
            self.result_labels = m.get('ResultLabels')

        return self

class GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponse(DaraModel):
    def __init__(
        self,
        service_inspection_vo_list: List[main_models.GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponseServiceInspectionVoList] = None,
    ):
        # The list of inspection items.
        self.service_inspection_vo_list = service_inspection_vo_list

    def validate(self):
        if self.service_inspection_vo_list:
            for v1 in self.service_inspection_vo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceInspectionVoList'] = []
        if self.service_inspection_vo_list is not None:
            for k1 in self.service_inspection_vo_list:
                result['ServiceInspectionVoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_inspection_vo_list = []
        if m.get('ServiceInspectionVoList') is not None:
            for k1 in m.get('ServiceInspectionVoList'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponseServiceInspectionVoList()
                self.service_inspection_vo_list.append(temp_model.from_map(k1))

        return self

class GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponseServiceInspectionVoList(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        is_match: bool = None,
        original_utterances: List[str] = None,
        remarks: str = None,
    ):
        # The inspection dimension.
        self.dimension = dimension
        # Indicates whether the label is matched.
        self.is_match = is_match
        # The sentences referenced in the reasoning.
        self.original_utterances = original_utterances
        # The reasoning for the judgment.
        self.remarks = remarks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.is_match is not None:
            result['IsMatch'] = self.is_match

        if self.original_utterances is not None:
            result['OriginalUtterances'] = self.original_utterances

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('IsMatch') is not None:
            self.is_match = m.get('IsMatch')

        if m.get('OriginalUtterances') is not None:
            self.original_utterances = m.get('OriginalUtterances')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        return self

class GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponse(DaraModel):
    def __init__(
        self,
        tag_list: List[main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagList] = None,
    ):
        self.tag_list = tag_list

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagList()
                self.tag_list.append(temp_model.from_map(k1))

        return self

class GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagList(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        self.children = children
        self.remarks = remarks
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        self.children = children
        self.remarks = remarks
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildrenChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        self.children = children
        self.remarks = remarks
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildrenChildren(DaraModel):
    def __init__(
        self,
        children: List[main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildrenChildrenChildren] = None,
        remarks: str = None,
        tag_name: str = None,
    ):
        self.children = children
        self.remarks = remarks
        self.tag_name = tag_name

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildrenChildrenChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetAgentTaskResultResponseBodyDataResponseMultiLevelTagResponseTagListChildrenChildrenChildrenChildren(DaraModel):
    def __init__(
        self,
        remarks: str = None,
        tag_name: str = None,
    ):
        self.remarks = remarks
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class GetAgentTaskResultResponseBodyDataResponseFieldResponse(DaraModel):
    def __init__(
        self,
        field_vo_list: List[main_models.GetAgentTaskResultResponseBodyDataResponseFieldResponseFieldVoList] = None,
    ):
        # The list of properties.
        self.field_vo_list = field_vo_list

    def validate(self):
        if self.field_vo_list:
            for v1 in self.field_vo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FieldVoList'] = []
        if self.field_vo_list is not None:
            for k1 in self.field_vo_list:
                result['FieldVoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_vo_list = []
        if m.get('FieldVoList') is not None:
            for k1 in m.get('FieldVoList'):
                temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseFieldResponseFieldVoList()
                self.field_vo_list.append(temp_model.from_map(k1))

        return self

class GetAgentTaskResultResponseBodyDataResponseFieldResponseFieldVoList(DaraModel):
    def __init__(
        self,
        name: str = None,
        original_utterances: List[int] = None,
        remarks: str = None,
        value: str = None,
    ):
        # The property name.
        self.name = name
        # The sentences referenced in the reasoning.
        self.original_utterances = original_utterances
        # The reasoning for the judgment.
        self.remarks = remarks
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.original_utterances is not None:
            result['OriginalUtterances'] = self.original_utterances

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OriginalUtterances') is not None:
            self.original_utterances = m.get('OriginalUtterances')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetAgentTaskResultResponseBodyDataResponseCustomerPromptResponse(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        # The result returned by the large language model.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class GetAgentTaskResultResponseBodyDataDialogues(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        hour_min_sec: str = None,
        role: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.hour_min_sec = hour_min_sec
        self.role = role
        self.speech_rate = speech_rate
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

        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value

        if self.end is not None:
            result['End'] = self.end

        if self.hour_min_sec is not None:
            result['HourMinSec'] = self.hour_min_sec

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

        if m.get('HourMinSec') is not None:
            self.hour_min_sec = m.get('HourMinSec')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

