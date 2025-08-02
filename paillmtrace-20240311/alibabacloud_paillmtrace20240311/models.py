# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class EvaluationConfigAnswer(TeaModel):
    def __init__(
        self,
        json_path_in_span: str = None,
        json_path_in_span_value: str = None,
        span_name: str = None,
    ):
        self.json_path_in_span = json_path_in_span
        self.json_path_in_span_value = json_path_in_span_value
        self.span_name = span_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_path_in_span is not None:
            result['JsonPathInSpan'] = self.json_path_in_span
        if self.json_path_in_span_value is not None:
            result['JsonPathInSpanValue'] = self.json_path_in_span_value
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonPathInSpan') is not None:
            self.json_path_in_span = m.get('JsonPathInSpan')
        if m.get('JsonPathInSpanValue') is not None:
            self.json_path_in_span_value = m.get('JsonPathInSpanValue')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        return self


class EvaluationConfigContext(TeaModel):
    def __init__(
        self,
        json_path_in_span: str = None,
        json_path_in_span_value: str = None,
        span_name: str = None,
    ):
        self.json_path_in_span = json_path_in_span
        self.json_path_in_span_value = json_path_in_span_value
        self.span_name = span_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_path_in_span is not None:
            result['JsonPathInSpan'] = self.json_path_in_span
        if self.json_path_in_span_value is not None:
            result['JsonPathInSpanValue'] = self.json_path_in_span_value
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonPathInSpan') is not None:
            self.json_path_in_span = m.get('JsonPathInSpan')
        if m.get('JsonPathInSpanValue') is not None:
            self.json_path_in_span_value = m.get('JsonPathInSpanValue')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        return self


class EvaluationConfigQuery(TeaModel):
    def __init__(
        self,
        json_path_in_span: str = None,
        json_path_in_span_value: str = None,
        span_name: str = None,
    ):
        self.json_path_in_span = json_path_in_span
        self.json_path_in_span_value = json_path_in_span_value
        self.span_name = span_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_path_in_span is not None:
            result['JsonPathInSpan'] = self.json_path_in_span
        if self.json_path_in_span_value is not None:
            result['JsonPathInSpanValue'] = self.json_path_in_span_value
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonPathInSpan') is not None:
            self.json_path_in_span = m.get('JsonPathInSpan')
        if m.get('JsonPathInSpanValue') is not None:
            self.json_path_in_span_value = m.get('JsonPathInSpanValue')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        return self


class EvaluationConfig(TeaModel):
    def __init__(
        self,
        answer: EvaluationConfigAnswer = None,
        context: EvaluationConfigContext = None,
        query: EvaluationConfigQuery = None,
    ):
        self.answer = answer
        self.context = context
        self.query = query

    def validate(self):
        if self.answer:
            self.answer.validate()
        if self.context:
            self.context.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer.to_map()
        if self.context is not None:
            result['Context'] = self.context.to_map()
        if self.query is not None:
            result['Query'] = self.query.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            temp_model = EvaluationConfigAnswer()
            self.answer = temp_model.from_map(m['Answer'])
        if m.get('Context') is not None:
            temp_model = EvaluationConfigContext()
            self.context = temp_model.from_map(m['Context'])
        if m.get('Query') is not None:
            temp_model = EvaluationConfigQuery()
            self.query = temp_model.from_map(m['Query'])
        return self


class ModelConfig(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        endpoint: str = None,
        is_self_host: bool = None,
        name: str = None,
        temperature: float = None,
        top_p: float = None,
        use_function_call: bool = None,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.is_self_host = is_self_host
        self.name = name
        self.temperature = temperature
        self.top_p = top_p
        self.use_function_call = use_function_call

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.is_self_host is not None:
            result['IsSelfHost'] = self.is_self_host
        if self.name is not None:
            result['Name'] = self.name
        if self.temperature is not None:
            result['Temperature'] = self.temperature
        if self.top_p is not None:
            result['TopP'] = self.top_p
        if self.use_function_call is not None:
            result['UseFunctionCall'] = self.use_function_call
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('IsSelfHost') is not None:
            self.is_self_host = m.get('IsSelfHost')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')
        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')
        if m.get('UseFunctionCall') is not None:
            self.use_function_call = m.get('UseFunctionCall')
        return self


class QuestionAnswerAnswer(TeaModel):
    def __init__(
        self,
        contexts: List[str] = None,
        text: str = None,
    ):
        self.contexts = contexts
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contexts is not None:
            result['Contexts'] = self.contexts
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contexts') is not None:
            self.contexts = m.get('Contexts')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QuestionAnswerGroundTruth(TeaModel):
    def __init__(
        self,
        contexts: List[str] = None,
        text: str = None,
    ):
        self.contexts = contexts
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contexts is not None:
            result['Contexts'] = self.contexts
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contexts') is not None:
            self.contexts = m.get('Contexts')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QuestionAnswer(TeaModel):
    def __init__(
        self,
        answer: QuestionAnswerAnswer = None,
        ground_truth: QuestionAnswerGroundTruth = None,
        question: str = None,
    ):
        self.answer = answer
        self.ground_truth = ground_truth
        self.question = question

    def validate(self):
        if self.answer:
            self.answer.validate()
        if self.ground_truth:
            self.ground_truth.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer.to_map()
        if self.ground_truth is not None:
            result['GroundTruth'] = self.ground_truth.to_map()
        if self.question is not None:
            result['Question'] = self.question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            temp_model = QuestionAnswerAnswer()
            self.answer = temp_model.from_map(m['Answer'])
        if m.get('GroundTruth') is not None:
            temp_model = QuestionAnswerGroundTruth()
            self.ground_truth = temp_model.from_map(m['GroundTruth'])
        if m.get('Question') is not None:
            self.question = m.get('Question')
        return self


class CreateOnlineEvalTaskRequestBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The key of the filter condition.
        # 
        # Valid values:
        # 
        # *   Status
        # *   SpanName
        # *   Input
        # *   TraceType
        # *   SpanType
        # *   ServiceName
        # *   Output
        # *   TraceName
        # *   ServiceId
        self.key = key
        # The matching operator of the filter condition.
        # 
        # Valid values:
        # 
        # *   Contains
        # *   \\=\
        # *   StartsWith
        self.operator = operator
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOnlineEvalTaskRequestBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        end_time: str = None,
        evaluation_config: EvaluationConfig = None,
        filters: List[CreateOnlineEvalTaskRequestBodyFilters] = None,
        model_config: ModelConfig = None,
        sampling_frequency_minutes: int = None,
        sampling_ratio: int = None,
        start_time: str = None,
        task_name: str = None,
    ):
        # The name of the user application in the trace data.
        self.app_name = app_name
        # The description of the task.
        self.description = description
        # The end time of the trace data, in UTC format.
        self.end_time = end_time
        # This configuration structure defines the JSON paths needed to extract specific values from trace data in JSON format. EvaluationConfig defines these JSON paths.
        self.evaluation_config = evaluation_config
        # The evaluation task must search for a certain amount of trace data generated by the user application as input data for the evaluation. This list defines the search filter conditions.
        self.filters = filters
        # The access configuration structure of the model used in the evaluation.
        self.model_config = model_config
        # The evaluation task must search for a certain amount of trace data generated by the user application as input data for the evaluation. This is the width of the time window for each search of input data.
        self.sampling_frequency_minutes = sampling_frequency_minutes
        # The percentage of data found in a time window that truly serves as evaluation input data. For example, 100 indicates that all data searched is used as evaluation input. 20 indicates that 20% of the found data is randomly selected as evaluation input.
        self.sampling_ratio = sampling_ratio
        # The start time of the trace data, in UTC format.
        self.start_time = start_time
        # The task name.
        self.task_name = task_name

    def validate(self):
        if self.evaluation_config:
            self.evaluation_config.validate()
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.evaluation_config is not None:
            result['EvaluationConfig'] = self.evaluation_config.to_map()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.sampling_frequency_minutes is not None:
            result['SamplingFrequencyMinutes'] = self.sampling_frequency_minutes
        if self.sampling_ratio is not None:
            result['SamplingRatio'] = self.sampling_ratio
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EvaluationConfig') is not None:
            temp_model = EvaluationConfig()
            self.evaluation_config = temp_model.from_map(m['EvaluationConfig'])
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = CreateOnlineEvalTaskRequestBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('ModelConfig') is not None:
            temp_model = ModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('SamplingFrequencyMinutes') is not None:
            self.sampling_frequency_minutes = m.get('SamplingFrequencyMinutes')
        if m.get('SamplingRatio') is not None:
            self.sampling_ratio = m.get('SamplingRatio')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateOnlineEvalTaskRequest(TeaModel):
    def __init__(
        self,
        body: CreateOnlineEvalTaskRequestBody = None,
    ):
        # The request data.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateOnlineEvalTaskRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOnlineEvalTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        # The request data.
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class CreateOnlineEvalTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The internal error code. This parameter is returned only when an error occurs.
        self.code = code
        # The error message. This parameter is returned only when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The ID of the created trace evaluation task.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateOnlineEvalTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOnlineEvalTaskResponseBody = None,
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
            temp_model = CreateOnlineEvalTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceIdentityRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        role_details: str = None,
        role_name: str = None,
    ):
        # The error code returned if the request fails.
        self.code = code
        # The error message returned if the request fails.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The role details.
        self.role_details = role_details
        # The name of the service-linked role. Default value: AliyunServiceRoleForPaiLLMTrace.
        self.role_name = role_name

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
        if self.role_details is not None:
            result['RoleDetails'] = self.role_details
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleDetails') is not None:
            self.role_details = m.get('RoleDetails')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateServiceIdentityRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceIdentityRoleResponseBody = None,
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
            temp_model = CreateServiceIdentityRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOnlineEvalTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Internal error code. Set only when the response is in error.
        self.code = code
        # Response error message. Set only when the response is in error.
        self.message = message
        # ID of the request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteOnlineEvalTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteOnlineEvalTaskResponseBody = None,
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
            temp_model = DeleteOnlineEvalTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateTraceRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        evaluation_config: EvaluationConfig = None,
        evaluation_id: str = None,
        max_time: str = None,
        min_time: str = None,
        model_config: ModelConfig = None,
    ):
        # The name of the application to which the trace belongs.
        self.app_name = app_name
        # If the value retrieved at the JSON path is itself a JSON string, further JSON path definitions within this JSON are necessary to get the actual value.
        # 
        # This parameter is required.
        self.evaluation_config = evaluation_config
        # The ID of the evaluation task. If not specified, the system randomly generates and returns an ID. You can use this ID to quickly search for evaluation results.
        self.evaluation_id = evaluation_id
        # The end time of the search time range, in UTC format.
        self.max_time = max_time
        # The start time of the search time range, in UTC format.
        self.min_time = min_time
        # The configuration structure to access the model used internally by the evaluation trace.
        self.model_config = model_config

    def validate(self):
        if self.evaluation_config:
            self.evaluation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.evaluation_config is not None:
            result['EvaluationConfig'] = self.evaluation_config.to_map()
        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EvaluationConfig') is not None:
            temp_model = EvaluationConfig()
            self.evaluation_config = temp_model.from_map(m['EvaluationConfig'])
        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        if m.get('ModelConfig') is not None:
            temp_model = ModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        return self


class EvaluateTraceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        evaluation_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The internal error code. This parameter is returned if an exception occurred.
        self.code = code
        # the task ID of the evaluation task to which the trace belongs.
        self.evaluation_id = evaluation_id
        # The error message. This parameter is returned if an exception occurred.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EvaluateTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EvaluateTraceResponseBody = None,
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
            temp_model = EvaluateTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEvaluationTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        evaluation_templates: List[Any] = None,
        message: str = None,
        request_id: str = None,
    ):
        # Internal error code. Set only when the response has an error.
        self.code = code
        # A series of templates used internally by the evaluation system to construct LLM interaction information.
        self.evaluation_templates = evaluation_templates
        # Response error message. Set only when the response has an error.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.evaluation_templates is not None:
            result['EvaluationTemplates'] = self.evaluation_templates
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EvaluationTemplates') is not None:
            self.evaluation_templates = m.get('EvaluationTemplates')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEvaluationTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEvaluationTemplatesResponseBody = None,
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
            temp_model = GetEvaluationTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOnlineEvalTaskResponseBodyTaskFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # Key of the filter condition.
        self.key = key
        # Filter condition match operator.
        self.operator = operator
        # Value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetOnlineEvalTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        app_name: str = None,
        description: str = None,
        eval_results: str = None,
        evaluation_config: EvaluationConfig = None,
        filters: List[GetOnlineEvalTaskResponseBodyTaskFilters] = None,
        gmt_create_time: str = None,
        gmt_end_time: str = None,
        gmt_last_sampling_window_end_time: str = None,
        gmt_last_sampling_window_start_time: str = None,
        gmt_start_time: str = None,
        id: str = None,
        model_config: ModelConfig = None,
        name: str = None,
        record_count: int = None,
        sampling_frequency_minutes: int = None,
        sampling_ratio: int = None,
        status: str = None,
        user_id: str = None,
    ):
        # The Alibaba Cloud account (primary account) of the task creator.
        self.aliyun_uid = aliyun_uid
        # The name of the user application targeted by this task.
        self.app_name = app_name
        # Task description information
        self.description = description
        # Deprecated. Will be removed.
        self.eval_results = eval_results
        # Extract specific path values from JSON-formatted trace data as input for the evaluation operation. These JSON paths are defined within this EvaluationConfig structure.
        self.evaluation_config = evaluation_config
        # The evaluation task needs to search for a certain amount of trace data generated by the user application as input data for the evaluation operation. This is a list that defines the search filter conditions.
        self.filters = filters
        # UTC creation time of the task.
        self.gmt_create_time = gmt_create_time
        # UTC end time of the trace data.
        self.gmt_end_time = gmt_end_time
        # UTC upper bound of the last sampling window
        self.gmt_last_sampling_window_end_time = gmt_last_sampling_window_end_time
        # UTC lower bound of the last sampling window.
        self.gmt_last_sampling_window_start_time = gmt_last_sampling_window_start_time
        # UTC start time of the trace data.
        self.gmt_start_time = gmt_start_time
        # Task ID
        self.id = id
        # Access configuration structure for the large model used internally by the evaluation task.
        self.model_config = model_config
        # Task name.
        self.name = name
        # Number of evaluation records
        self.record_count = record_count
        # The evaluation task needs to search for a certain amount of trace data generated by the user application as input data for the evaluation operation. This defines the width of the time window for each search of input data.
        self.sampling_frequency_minutes = sampling_frequency_minutes
        # The percentage of the data found within a time window that is actually used as input for the evaluation task. For example, 100 means all the found data is used as input, 20 means 20% of the found data is randomly selected as input.
        self.sampling_ratio = sampling_ratio
        # Task status
        self.status = status
        # The Alibaba Cloud sub-account of the task creator.
        self.user_id = user_id

    def validate(self):
        if self.evaluation_config:
            self.evaluation_config.validate()
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.eval_results is not None:
            result['EvalResults'] = self.eval_results
        if self.evaluation_config is not None:
            result['EvaluationConfig'] = self.evaluation_config.to_map()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_last_sampling_window_end_time is not None:
            result['GmtLastSamplingWindowEndTime'] = self.gmt_last_sampling_window_end_time
        if self.gmt_last_sampling_window_start_time is not None:
            result['GmtLastSamplingWindowStartTime'] = self.gmt_last_sampling_window_start_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.id is not None:
            result['Id'] = self.id
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.sampling_frequency_minutes is not None:
            result['SamplingFrequencyMinutes'] = self.sampling_frequency_minutes
        if self.sampling_ratio is not None:
            result['SamplingRatio'] = self.sampling_ratio
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EvalResults') is not None:
            self.eval_results = m.get('EvalResults')
        if m.get('EvaluationConfig') is not None:
            temp_model = EvaluationConfig()
            self.evaluation_config = temp_model.from_map(m['EvaluationConfig'])
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = GetOnlineEvalTaskResponseBodyTaskFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtLastSamplingWindowEndTime') is not None:
            self.gmt_last_sampling_window_end_time = m.get('GmtLastSamplingWindowEndTime')
        if m.get('GmtLastSamplingWindowStartTime') is not None:
            self.gmt_last_sampling_window_start_time = m.get('GmtLastSamplingWindowStartTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelConfig') is not None:
            temp_model = ModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('SamplingFrequencyMinutes') is not None:
            self.sampling_frequency_minutes = m.get('SamplingFrequencyMinutes')
        if m.get('SamplingRatio') is not None:
            self.sampling_ratio = m.get('SamplingRatio')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetOnlineEvalTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        task: GetOnlineEvalTaskResponseBodyTask = None,
    ):
        # Internal error code. Set only when the response is in error.
        self.code = code
        # Response error message. Set only when the response is in error.
        self.message = message
        # POP request ID
        self.request_id = request_id
        # Task information
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

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
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Task') is not None:
            temp_model = GetOnlineEvalTaskResponseBodyTask()
            self.task = temp_model.from_map(m['Task'])
        return self


class GetOnlineEvalTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOnlineEvalTaskResponseBody = None,
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
            temp_model = GetOnlineEvalTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceIdentityRoleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        role_detail: str = None,
        role_name: str = None,
    ):
        # The internal error code. This parameter is returned only when an error occurs.
        self.code = code
        # The error message. This parameter is returned only when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The role details.
        self.role_detail = role_detail
        # The name of the service-linked role. Default value: AliyunServiceRoleForPaiLLMTrace.
        self.role_name = role_name

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
        if self.role_detail is not None:
            result['RoleDetail'] = self.role_detail
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleDetail') is not None:
            self.role_detail = m.get('RoleDetail')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetServiceIdentityRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceIdentityRoleResponseBody = None,
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
            temp_model = GetServiceIdentityRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetXtraceTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        grpc_endpoint: str = None,
        grpc_internal_endpoint: str = None,
        http_endpoint: str = None,
        http_internal_endpoint: str = None,
        message: str = None,
        request_id: str = None,
        token: str = None,
    ):
        # The internal error code. This parameter is returned only when an error occurs.
        self.code = code
        # The gRPC endpoint used for uploading ARM traces.
        self.grpc_endpoint = grpc_endpoint
        # The internal gRPC endpoint used for uploading ARMS traces used by Alibaba Cloud.
        self.grpc_internal_endpoint = grpc_internal_endpoint
        # The endpoint used for uploading ARMS traces.
        self.http_endpoint = http_endpoint
        # The internal endpoint used for uploading ARMS traces used by Alibaba Cloud.
        self.http_internal_endpoint = http_internal_endpoint
        # The error message. This parameter is returned only when an error occurs.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The token used for uploading ARMS traces.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.grpc_endpoint is not None:
            result['GrpcEndpoint'] = self.grpc_endpoint
        if self.grpc_internal_endpoint is not None:
            result['GrpcInternalEndpoint'] = self.grpc_internal_endpoint
        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint
        if self.http_internal_endpoint is not None:
            result['HttpInternalEndpoint'] = self.http_internal_endpoint
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GrpcEndpoint') is not None:
            self.grpc_endpoint = m.get('GrpcEndpoint')
        if m.get('GrpcInternalEndpoint') is not None:
            self.grpc_internal_endpoint = m.get('GrpcInternalEndpoint')
        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')
        if m.get('HttpInternalEndpoint') is not None:
            self.http_internal_endpoint = m.get('HttpInternalEndpoint')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetXtraceTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetXtraceTokenResponseBody = None,
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
            temp_model = GetXtraceTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEvalResultsRequest(TeaModel):
    def __init__(
        self,
        evaluation_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        record_ids: List[str] = None,
    ):
        # The task ID of the evaluation task to which the trace belongs.
        self.evaluation_id = evaluation_id
        # The keyword to query from the evaluation inputs.
        self.keyword = keyword
        # The page number. Page starts from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 50. Default value: 10.
        self.page_size = page_size
        # The trace data IDs.
        self.record_ids = record_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.record_ids is not None:
            result['RecordIds'] = self.record_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordIds') is not None:
            self.record_ids = m.get('RecordIds')
        return self


class ListEvalResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        evaluation_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        record_ids_shrink: str = None,
    ):
        # The task ID of the evaluation task to which the trace belongs.
        self.evaluation_id = evaluation_id
        # The keyword to query from the evaluation inputs.
        self.keyword = keyword
        # The page number. Page starts from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 50. Default value: 10.
        self.page_size = page_size
        # The trace data IDs.
        self.record_ids_shrink = record_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.record_ids_shrink is not None:
            result['RecordIds'] = self.record_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecordIds') is not None:
            self.record_ids_shrink = m.get('RecordIds')
        return self


class ListEvalResultsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        evaluation_results: List[str] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The internal error code. This parameter is returned only when an error occurs.
        self.code = code
        # The evaluation results.
        self.evaluation_results = evaluation_results
        # The error message. This parameter is returned only when an error occurs.
        self.message = message
        # The ID of the POP request.
        self.request_id = request_id
        # The total number of results that meet the condition.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EvaluationResults') is not None:
            self.evaluation_results = m.get('EvaluationResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEvalResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEvalResultsResponseBody = None,
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
            temp_model = ListEvalResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnlineEvalTaskResultsRequest(TeaModel):
    def __init__(
        self,
        evaluation_id: str = None,
        most_recent_results_only: bool = None,
        page_number: int = None,
        page_size: int = None,
        trace_ids: List[str] = None,
    ):
        # The ID of the evaluation task. At least one of the trace ID or task ID must be set.
        self.evaluation_id = evaluation_id
        # The same trace data may have been evaluated by different tasks. If no task ID is specified and there are multiple evaluation results for the same trace ID, this parameter specifies whether to return only the most recent evaluation result.
        self.most_recent_results_only = most_recent_results_only
        # The current page number. Value range: integers greater than 0. Default value: 1.
        self.page_number = page_number
        # Page size, default is 10.
        self.page_size = page_size
        # Specify a set of trace IDs, and only return the evaluation results for these traces. At least one of the trace ID or task ID must be set.
        self.trace_ids = trace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id
        if self.most_recent_results_only is not None:
            result['MostRecentResultsOnly'] = self.most_recent_results_only
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.trace_ids is not None:
            result['TraceIds'] = self.trace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')
        if m.get('MostRecentResultsOnly') is not None:
            self.most_recent_results_only = m.get('MostRecentResultsOnly')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TraceIds') is not None:
            self.trace_ids = m.get('TraceIds')
        return self


class ListOnlineEvalTaskResultsShrinkRequest(TeaModel):
    def __init__(
        self,
        evaluation_id: str = None,
        most_recent_results_only: bool = None,
        page_number: int = None,
        page_size: int = None,
        trace_ids_shrink: str = None,
    ):
        # The ID of the evaluation task. At least one of the trace ID or task ID must be set.
        self.evaluation_id = evaluation_id
        # The same trace data may have been evaluated by different tasks. If no task ID is specified and there are multiple evaluation results for the same trace ID, this parameter specifies whether to return only the most recent evaluation result.
        self.most_recent_results_only = most_recent_results_only
        # The current page number. Value range: integers greater than 0. Default value: 1.
        self.page_number = page_number
        # Page size, default is 10.
        self.page_size = page_size
        # Specify a set of trace IDs, and only return the evaluation results for these traces. At least one of the trace ID or task ID must be set.
        self.trace_ids_shrink = trace_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_id is not None:
            result['EvaluationId'] = self.evaluation_id
        if self.most_recent_results_only is not None:
            result['MostRecentResultsOnly'] = self.most_recent_results_only
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.trace_ids_shrink is not None:
            result['TraceIds'] = self.trace_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationId') is not None:
            self.evaluation_id = m.get('EvaluationId')
        if m.get('MostRecentResultsOnly') is not None:
            self.most_recent_results_only = m.get('MostRecentResultsOnly')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TraceIds') is not None:
            self.trace_ids_shrink = m.get('TraceIds')
        return self


class ListOnlineEvalTaskResultsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        evaluation_results: List[str] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Internal error code. Set only when the response has an error.
        self.code = code
        # List of evaluation results.
        self.evaluation_results = evaluation_results
        # Response error message. Set only when the response has an error.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # Total number of evaluation results that meet the criteria.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.evaluation_results is not None:
            result['EvaluationResults'] = self.evaluation_results
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EvaluationResults') is not None:
            self.evaluation_results = m.get('EvaluationResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOnlineEvalTaskResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOnlineEvalTaskResultsResponseBody = None,
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
            temp_model = ListOnlineEvalTaskResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnlineEvalTasksRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        keyword: str = None,
        max_time: str = None,
        min_time: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
    ):
        self.app_name = app_name
        # Search keyword. It will match on fields such as task name, application name (appName), task description, and evaluation metric name.
        self.keyword = keyword
        # The UTC end time of the search time range
        self.max_time = max_time
        # The UTC start time of the search time range
        self.min_time = min_time
        # The current page number. Value range: integers greater than 0. Default value: 1.
        self.page_number = page_number
        # Page size, default is 10.
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOnlineEvalTasksResponseBodyTasksFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The matching operator of the filter condition.
        self.operator = operator
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListOnlineEvalTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        app_name: str = None,
        description: str = None,
        eval_results: str = None,
        evaluation_config: EvaluationConfig = None,
        filters: List[ListOnlineEvalTasksResponseBodyTasksFilters] = None,
        gmt_create_time: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        id: str = None,
        model_config: ModelConfig = None,
        name: str = None,
        record_count: int = None,
        sampling_frequency_minutes: int = None,
        sampling_ratio: int = None,
        status: str = None,
        user_id: str = None,
    ):
        # The Alibaba Cloud account (primary account) of the task creator.
        self.aliyun_uid = aliyun_uid
        # The name of the user application targeted by this task.
        self.app_name = app_name
        # Task description information
        self.description = description
        self.eval_results = eval_results
        # Extract specific path values from JSON-formatted trace data as input for the evaluation operation. These JSON paths are defined in this EvaluationConfig structure.
        self.evaluation_config = evaluation_config
        # The list define the search filter conditions for the evaluation task to search a certain amount of trace data generated by the user application, which serves as input data for the evaluation operation.
        self.filters = filters
        # The UTC creation time of the task.
        self.gmt_create_time = gmt_create_time
        # Task UTC end time.
        self.gmt_end_time = gmt_end_time
        # The UTC start time of the task.
        self.gmt_start_time = gmt_start_time
        # Task ID.
        self.id = id
        # Access configuration structure for the large model used internally by the evaluation task.
        self.model_config = model_config
        # Task name.
        self.name = name
        self.record_count = record_count
        # The evaluation task needs to search for a certain amount of trace data generated by the user\\"s application as input data for the evaluation operation. This defines the time window for each data search.
        self.sampling_frequency_minutes = sampling_frequency_minutes
        # The percentage of the data searched within a time window that is used as input data for the evaluation. For example, 100 means all the searched data is used as input, 20 means 20% of the searched data is randomly selected as input.
        self.sampling_ratio = sampling_ratio
        # Task status
        self.status = status
        # The Alibaba Cloud sub-account of the task creator.
        self.user_id = user_id

    def validate(self):
        if self.evaluation_config:
            self.evaluation_config.validate()
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.eval_results is not None:
            result['EvalResults'] = self.eval_results
        if self.evaluation_config is not None:
            result['EvaluationConfig'] = self.evaluation_config.to_map()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time
        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time
        if self.id is not None:
            result['Id'] = self.id
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.sampling_frequency_minutes is not None:
            result['SamplingFrequencyMinutes'] = self.sampling_frequency_minutes
        if self.sampling_ratio is not None:
            result['SamplingRatio'] = self.sampling_ratio
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EvalResults') is not None:
            self.eval_results = m.get('EvalResults')
        if m.get('EvaluationConfig') is not None:
            temp_model = EvaluationConfig()
            self.evaluation_config = temp_model.from_map(m['EvaluationConfig'])
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListOnlineEvalTasksResponseBodyTasksFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')
        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModelConfig') is not None:
            temp_model = ModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('SamplingFrequencyMinutes') is not None:
            self.sampling_frequency_minutes = m.get('SamplingFrequencyMinutes')
        if m.get('SamplingRatio') is not None:
            self.sampling_ratio = m.get('SamplingRatio')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListOnlineEvalTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        tasks: List[ListOnlineEvalTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # Internal error code. Set only when the response has an error.
        self.code = code
        # Response error message. Set only when the response has an error.
        self.message = message
        # ID of the request
        self.request_id = request_id
        # List of tasks.
        self.tasks = tasks
        # Total number of tasks that meet the criteria.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

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
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListOnlineEvalTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOnlineEvalTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOnlineEvalTasksResponseBody = None,
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
            temp_model = ListOnlineEvalTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTracesDatasRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The name of the filter parameter, case-insensitive. Supported parameters: \\"serviceid\\", \\"servicename\\", \\"input\\", \\"output\\", \\"status\\", \\"tracetype\\", and \\"tracename\\".
        # 
        # The otel span attributes corresponding to the parameters:
        # 
        # serviceid: resources.service.id
        # 
        # servicename: resources.service.name
        # 
        # input: attributes.input.value
        # 
        # output: attributes.output.value
        # 
        # status: statusCode
        # 
        # tracetype: the attributes.gen_ai.span.kind of span whose parentSpanId is 0
        # 
        # tracename: the spanName of span whose parentSpanId is 0
        # 
        # Valid values:
        # 
        # *   Status
        # *   SpanName
        # *   Input
        # *   TraceType
        # *   SpanType
        # *   ServiceName
        # *   Output
        # *   TraceName
        # *   ServiceId
        self.key = key
        # The parameter operator. Case-insensitive. Supported operators: \\"=\\", \\"contains\\", and \\"startswith\\".
        # 
        # Valid values:
        # 
        # *   contains
        # *   \\=\
        # *   startsWith
        self.operator = operator
        # The value of the filter parameter. For the contains operation, it is case-sensitive. For other operations, it is case-insensitive.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTracesDatasRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        filters: List[ListTracesDatasRequestFilters] = None,
        has_events: bool = None,
        has_status_message: bool = None,
        llm_app_name: str = None,
        max_duration: float = None,
        max_time: str = None,
        min_duration: float = None,
        min_time: str = None,
        opentelemetry_compatible: bool = None,
        owner_id: str = None,
        owner_sub_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        span_ids: List[str] = None,
        span_name: str = None,
        trace_ids: List[str] = None,
        trace_reduce_method: str = None,
    ):
        # The value of the attributes.service.app.user_id field in the trace record. It can contain upper and lower case letters, digits, dot (.), hyphen (-), and underscore (_). It is empty by default.
        self.end_user_id = end_user_id
        # Other filter parameters
        self.filters = filters
        # Whether to return only trace records containing spans with a non-empty events. Example: Suppose a trace has 3 spans. If this parameter is True, this trace meets the condition when any one of the 3 spans has a non-empty events. The default value is False. The events is not used for filtering.
        self.has_events = has_events
        # Whether to return only trace records containing spans with a non-empty statusMessage. Example: Suppose a trace has 3 spans. If this parameter is True, this trace meets the condition when any one of the 3 spans has a non-empty statusMessage. The default value is False. The statusMessage is not used for filtering.
        self.has_status_message = has_status_message
        # The value of the resources.service.app.name field in the trace record. It can contain upper and lower case letters, digits, dot (.), hyphen (-), and underscore (_). Must be an exact match. It is empty by default.
        self.llm_app_name = llm_app_name
        self.max_duration = max_duration
        # The upper limit of the search time range, in UTC format (YYYY-mm-dd or YYYY-MM-DD HH:mm:ss). By default, the value is (current time +10 minutes)
        self.max_time = max_time
        self.min_duration = min_duration
        # The lower limit of the search time range, in UTC format (YYYY-mm-dd or YYYY-MM-DD HH:mm:ss). By default, the value is (current time - 2 days).
        # 
        # This parameter is required.
        self.min_time = min_time
        # Whether the returned JSON data can be directly converted to OpenTelemetry TracesData protobuf object. Default value: False. JSON data that is compatible with OpenTelemetry is more complex. Such data is generally not required unless you want to generate a protobuf object of OpenTelemetry.
        self.opentelemetry_compatible = opentelemetry_compatible
        self.owner_id = owner_id
        # The value of the resources.service.owner.sub_id field in the trace record. It can contain upper and lower case letters, digits, dot (.), hyphen (-), and underscore (_). It is empty by default.
        self.owner_sub_id = owner_sub_id
        # The page number. Page starts from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The field used to sort the returned results. Valid values: StartTime and Duration.
        self.sort_by = sort_by
        # The sorting order. Valid values:
        # 
        # *   **ASC**\
        # *   **DESC** (default)
        self.sort_order = sort_order
        # The list of span IDs. Each trace record contains one or more spans.
        self.span_ids = span_ids
        self.span_name = span_name
        # The list of trace IDs.
        self.trace_ids = trace_ids
        # The content simplification method for returned trace data to reduce the data volume.
        # 
        # REMOVE_EMBEDDING: Removes all embedding array contents.
        # 
        # ROOT_ONLY: Returns only the root span for each trace, with the root span content also having the REMOVE_EMBEDDING applied.
        # 
        # Blank: Maintains the original data without simplification.
        self.trace_reduce_method = trace_reduce_method

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.has_events is not None:
            result['HasEvents'] = self.has_events
        if self.has_status_message is not None:
            result['HasStatusMessage'] = self.has_status_message
        if self.llm_app_name is not None:
            result['LlmAppName'] = self.llm_app_name
        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        if self.opentelemetry_compatible is not None:
            result['OpentelemetryCompatible'] = self.opentelemetry_compatible
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_sub_id is not None:
            result['OwnerSubId'] = self.owner_sub_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.span_ids is not None:
            result['SpanIds'] = self.span_ids
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.trace_ids is not None:
            result['TraceIds'] = self.trace_ids
        if self.trace_reduce_method is not None:
            result['TraceReduceMethod'] = self.trace_reduce_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListTracesDatasRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('HasEvents') is not None:
            self.has_events = m.get('HasEvents')
        if m.get('HasStatusMessage') is not None:
            self.has_status_message = m.get('HasStatusMessage')
        if m.get('LlmAppName') is not None:
            self.llm_app_name = m.get('LlmAppName')
        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        if m.get('OpentelemetryCompatible') is not None:
            self.opentelemetry_compatible = m.get('OpentelemetryCompatible')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerSubId') is not None:
            self.owner_sub_id = m.get('OwnerSubId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SpanIds') is not None:
            self.span_ids = m.get('SpanIds')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('TraceIds') is not None:
            self.trace_ids = m.get('TraceIds')
        if m.get('TraceReduceMethod') is not None:
            self.trace_reduce_method = m.get('TraceReduceMethod')
        return self


class ListTracesDatasShrinkRequest(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        filters_shrink: str = None,
        has_events: bool = None,
        has_status_message: bool = None,
        llm_app_name: str = None,
        max_duration: float = None,
        max_time: str = None,
        min_duration: float = None,
        min_time: str = None,
        opentelemetry_compatible: bool = None,
        owner_id: str = None,
        owner_sub_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        span_ids_shrink: str = None,
        span_name: str = None,
        trace_ids_shrink: str = None,
        trace_reduce_method: str = None,
    ):
        # The value of the attributes.service.app.user_id field in the trace record. It can contain upper and lower case letters, digits, dot (.), hyphen (-), and underscore (_). It is empty by default.
        self.end_user_id = end_user_id
        # Other filter parameters
        self.filters_shrink = filters_shrink
        # Whether to return only trace records containing spans with a non-empty events. Example: Suppose a trace has 3 spans. If this parameter is True, this trace meets the condition when any one of the 3 spans has a non-empty events. The default value is False. The events is not used for filtering.
        self.has_events = has_events
        # Whether to return only trace records containing spans with a non-empty statusMessage. Example: Suppose a trace has 3 spans. If this parameter is True, this trace meets the condition when any one of the 3 spans has a non-empty statusMessage. The default value is False. The statusMessage is not used for filtering.
        self.has_status_message = has_status_message
        # The value of the resources.service.app.name field in the trace record. It can contain upper and lower case letters, digits, dot (.), hyphen (-), and underscore (_). Must be an exact match. It is empty by default.
        self.llm_app_name = llm_app_name
        self.max_duration = max_duration
        # The upper limit of the search time range, in UTC format (YYYY-mm-dd or YYYY-MM-DD HH:mm:ss). By default, the value is (current time +10 minutes)
        self.max_time = max_time
        self.min_duration = min_duration
        # The lower limit of the search time range, in UTC format (YYYY-mm-dd or YYYY-MM-DD HH:mm:ss). By default, the value is (current time - 2 days).
        # 
        # This parameter is required.
        self.min_time = min_time
        # Whether the returned JSON data can be directly converted to OpenTelemetry TracesData protobuf object. Default value: False. JSON data that is compatible with OpenTelemetry is more complex. Such data is generally not required unless you want to generate a protobuf object of OpenTelemetry.
        self.opentelemetry_compatible = opentelemetry_compatible
        self.owner_id = owner_id
        # The value of the resources.service.owner.sub_id field in the trace record. It can contain upper and lower case letters, digits, dot (.), hyphen (-), and underscore (_). It is empty by default.
        self.owner_sub_id = owner_sub_id
        # The page number. Page starts from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The field used to sort the returned results. Valid values: StartTime and Duration.
        self.sort_by = sort_by
        # The sorting order. Valid values:
        # 
        # *   **ASC**\
        # *   **DESC** (default)
        self.sort_order = sort_order
        # The list of span IDs. Each trace record contains one or more spans.
        self.span_ids_shrink = span_ids_shrink
        self.span_name = span_name
        # The list of trace IDs.
        self.trace_ids_shrink = trace_ids_shrink
        # The content simplification method for returned trace data to reduce the data volume.
        # 
        # REMOVE_EMBEDDING: Removes all embedding array contents.
        # 
        # ROOT_ONLY: Returns only the root span for each trace, with the root span content also having the REMOVE_EMBEDDING applied.
        # 
        # Blank: Maintains the original data without simplification.
        self.trace_reduce_method = trace_reduce_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.filters_shrink is not None:
            result['Filters'] = self.filters_shrink
        if self.has_events is not None:
            result['HasEvents'] = self.has_events
        if self.has_status_message is not None:
            result['HasStatusMessage'] = self.has_status_message
        if self.llm_app_name is not None:
            result['LlmAppName'] = self.llm_app_name
        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        if self.opentelemetry_compatible is not None:
            result['OpentelemetryCompatible'] = self.opentelemetry_compatible
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_sub_id is not None:
            result['OwnerSubId'] = self.owner_sub_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.span_ids_shrink is not None:
            result['SpanIds'] = self.span_ids_shrink
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.trace_ids_shrink is not None:
            result['TraceIds'] = self.trace_ids_shrink
        if self.trace_reduce_method is not None:
            result['TraceReduceMethod'] = self.trace_reduce_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Filters') is not None:
            self.filters_shrink = m.get('Filters')
        if m.get('HasEvents') is not None:
            self.has_events = m.get('HasEvents')
        if m.get('HasStatusMessage') is not None:
            self.has_status_message = m.get('HasStatusMessage')
        if m.get('LlmAppName') is not None:
            self.llm_app_name = m.get('LlmAppName')
        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        if m.get('OpentelemetryCompatible') is not None:
            self.opentelemetry_compatible = m.get('OpentelemetryCompatible')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerSubId') is not None:
            self.owner_sub_id = m.get('OwnerSubId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SpanIds') is not None:
            self.span_ids_shrink = m.get('SpanIds')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('TraceIds') is not None:
            self.trace_ids_shrink = m.get('TraceIds')
        if m.get('TraceReduceMethod') is not None:
            self.trace_reduce_method = m.get('TraceReduceMethod')
        return self


class ListTracesDatasResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
        traces: List[Any] = None,
    ):
        # The internal error code. This parameter is returned only when an error occurs.
        self.code = code
        # The error message. This parameter is returned only when an error occurs.
        self.message = message
        # POP request id
        self.request_id = request_id
        # The total number of traces that meet the condition.
        self.total_count = total_count
        # The JSON array with each element being a trace\\"s JSON string. Length of the array is equal to or less than the page size parameter value.
        self.traces = traces

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.traces is not None:
            result['Traces'] = self.traces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Traces') is not None:
            self.traces = m.get('Traces')
        return self


class ListTracesDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTracesDatasResponseBody = None,
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
            temp_model = ListTracesDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopOnlineEvalTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Internal error code. Set only when the response is in error.
        self.code = code
        # Response error message. Set only when the response is in error.
        self.message = message
        # ID of the POP request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopOnlineEvalTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopOnlineEvalTaskResponseBody = None,
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
            temp_model = StopOnlineEvalTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOnlineEvalTaskRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The key of the filter condition.
        # 
        # Valid values:
        # 
        # *   Status
        # *   SpanName
        # *   Input
        # *   TraceType
        # *   SpanType
        # *   ServiceName
        # *   Output
        # *   TraceName
        # *   ServiceId
        self.key = key
        # The matching operator of the filter condition.
        # 
        # Valid values:
        # 
        # *   Contains
        # *   \\=\
        # *   StartsWith
        self.operator = operator
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateOnlineEvalTaskRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        end_time: str = None,
        evaluation_config: EvaluationConfig = None,
        filters: List[UpdateOnlineEvalTaskRequestFilters] = None,
        model_config: ModelConfig = None,
        sampling_frequency_minutes: int = None,
        sampling_ratio: int = None,
        start_time: str = None,
        task_name: str = None,
    ):
        # The user-defined name of the LLM application.
        self.app_name = app_name
        # The description of the task.
        self.description = description
        # The end time of the trace data, in UTC format.
        self.end_time = end_time
        # This configuration structure defines the JSON paths needed to extract specific values from trace data in JSON format. EvaluationConfig defines these JSON paths.
        self.evaluation_config = evaluation_config
        # The evaluation task must search for a certain amount of trace data generated by the user application as input data for the evaluation. This list defines the search filter conditions.
        self.filters = filters
        # The access configuration structure of the model used in the evaluation.
        self.model_config = model_config
        # The evaluation task must search for a certain amount of trace data generated by the user application as input data for the evaluation. This is the width of the time window for each search of input data.
        self.sampling_frequency_minutes = sampling_frequency_minutes
        # The percentage of data found in a time window that truly serves as evaluation input data. For example, 100 indicates that all data searched is used as evaluation input. 20 indicates that 20% of the found data is randomly selected as evaluation input.
        self.sampling_ratio = sampling_ratio
        # The start time of the trace data, in UTC format.
        self.start_time = start_time
        # The task name.
        self.task_name = task_name

    def validate(self):
        if self.evaluation_config:
            self.evaluation_config.validate()
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.evaluation_config is not None:
            result['EvaluationConfig'] = self.evaluation_config.to_map()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()
        if self.sampling_frequency_minutes is not None:
            result['SamplingFrequencyMinutes'] = self.sampling_frequency_minutes
        if self.sampling_ratio is not None:
            result['SamplingRatio'] = self.sampling_ratio
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EvaluationConfig') is not None:
            temp_model = EvaluationConfig()
            self.evaluation_config = temp_model.from_map(m['EvaluationConfig'])
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = UpdateOnlineEvalTaskRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('ModelConfig') is not None:
            temp_model = ModelConfig()
            self.model_config = temp_model.from_map(m['ModelConfig'])
        if m.get('SamplingFrequencyMinutes') is not None:
            self.sampling_frequency_minutes = m.get('SamplingFrequencyMinutes')
        if m.get('SamplingRatio') is not None:
            self.sampling_ratio = m.get('SamplingRatio')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateOnlineEvalTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The internal error code. This parameter is returned only when an error occurs.
        self.code = code
        # The error message. This parameter is returned only when an error occurs.
        self.message = message
        # Id of the POP request
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOnlineEvalTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOnlineEvalTaskResponseBody = None,
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
            temp_model = UpdateOnlineEvalTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


