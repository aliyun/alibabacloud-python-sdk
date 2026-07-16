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
        # - **true**: The request was successful.
        # - **false/null**: The request failed.
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
        input_tokens: str = None,
        llm_request_id: str = None,
        output_tokens: str = None,
        response: main_models.GetAgentTaskResultResponseBodyDataResponse = None,
        status: str = None,
        task_id: str = None,
        total_tokens: str = None,
        tyxm_plus_count: str = None,
        tyxm_turbo_count: str = None,
        vid: str = None,
    ):
        # The number of input tokens.
        self.input_tokens = input_tokens
        # The request ID returned by the large language model service.
        self.llm_request_id = llm_request_id
        # The number of output tokens.
        self.output_tokens = output_tokens
        # The result of the computing task.
        self.response = response
        # The task status. Valid values:
        # 
        # - 1: pending
        # - 2: running
        # - 3: succeeded
        # - 4: failed
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The total number of tokens.
        self.total_tokens = total_tokens
        # The number of times the plus model is used.
        self.tyxm_plus_count = tyxm_plus_count
        # The number of times the turbo model is used.
        self.tyxm_turbo_count = tyxm_turbo_count
        # The session ID.
        self.vid = vid

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.llm_request_id is not None:
            result['LlmRequestId'] = self.llm_request_id

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.response is not None:
            result['Response'] = self.response.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.tyxm_plus_count is not None:
            result['TyxmPlusCount'] = self.tyxm_plus_count

        if self.tyxm_turbo_count is not None:
            result['TyxmTurboCount'] = self.tyxm_turbo_count

        if self.vid is not None:
            result['Vid'] = self.vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('LlmRequestId') is not None:
            self.llm_request_id = m.get('LlmRequestId')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('Response') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponse()
            self.response = temp_model.from_map(m.get('Response'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('TyxmPlusCount') is not None:
            self.tyxm_plus_count = m.get('TyxmPlusCount')

        if m.get('TyxmTurboCount') is not None:
            self.tyxm_turbo_count = m.get('TyxmTurboCount')

        if m.get('Vid') is not None:
            self.vid = m.get('Vid')

        return self

class GetAgentTaskResultResponseBodyDataResponse(DaraModel):
    def __init__(
        self,
        customer_prompt_response: main_models.GetAgentTaskResultResponseBodyDataResponseCustomerPromptResponse = None,
        field_response: main_models.GetAgentTaskResultResponseBodyDataResponseFieldResponse = None,
        service_inspection_response: main_models.GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponse = None,
        tag_category_response: main_models.GetAgentTaskResultResponseBodyDataResponseTagCategoryResponse = None,
    ):
        # The result of the custom prompt.
        self.customer_prompt_response = customer_prompt_response
        # The property extraction result.
        self.field_response = field_response
        # The service quality inspection result.
        self.service_inspection_response = service_inspection_response
        # The tag categorization result.
        self.tag_category_response = tag_category_response

    def validate(self):
        if self.customer_prompt_response:
            self.customer_prompt_response.validate()
        if self.field_response:
            self.field_response.validate()
        if self.service_inspection_response:
            self.service_inspection_response.validate()
        if self.tag_category_response:
            self.tag_category_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_prompt_response is not None:
            result['CustomerPromptResponse'] = self.customer_prompt_response.to_map()

        if self.field_response is not None:
            result['FieldResponse'] = self.field_response.to_map()

        if self.service_inspection_response is not None:
            result['ServiceInspectionResponse'] = self.service_inspection_response.to_map()

        if self.tag_category_response is not None:
            result['TagCategoryResponse'] = self.tag_category_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerPromptResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseCustomerPromptResponse()
            self.customer_prompt_response = temp_model.from_map(m.get('CustomerPromptResponse'))

        if m.get('FieldResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseFieldResponse()
            self.field_response = temp_model.from_map(m.get('FieldResponse'))

        if m.get('ServiceInspectionResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseServiceInspectionResponse()
            self.service_inspection_response = temp_model.from_map(m.get('ServiceInspectionResponse'))

        if m.get('TagCategoryResponse') is not None:
            temp_model = main_models.GetAgentTaskResultResponseBodyDataResponseTagCategoryResponse()
            self.tag_category_response = temp_model.from_map(m.get('TagCategoryResponse'))

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
        # Indicates whether a match is found.
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
        # Indicates whether a match is found.
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

