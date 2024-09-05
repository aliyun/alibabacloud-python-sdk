# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class RunMarketingInformationExtractRequest(TeaModel):
    def __init__(
        self,
        custom_prompt: str = None,
        extract_type: str = None,
        model_id: str = None,
        source_materials: List[str] = None,
    ):
        self.custom_prompt = custom_prompt
        self.extract_type = extract_type
        self.model_id = model_id
        self.source_materials = source_materials

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt
        if self.extract_type is not None:
            result['extractType'] = self.extract_type
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.source_materials is not None:
            result['sourceMaterials'] = self.source_materials
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')
        if m.get('extractType') is not None:
            self.extract_type = m.get('extractType')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('sourceMaterials') is not None:
            self.source_materials = m.get('sourceMaterials')
        return self


class RunMarketingInformationExtractShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_prompt: str = None,
        extract_type: str = None,
        model_id: str = None,
        source_materials_shrink: str = None,
    ):
        self.custom_prompt = custom_prompt
        self.extract_type = extract_type
        self.model_id = model_id
        self.source_materials_shrink = source_materials_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt
        if self.extract_type is not None:
            result['extractType'] = self.extract_type
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.source_materials_shrink is not None:
            result['sourceMaterials'] = self.source_materials_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')
        if m.get('extractType') is not None:
            self.extract_type = m.get('extractType')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('sourceMaterials') is not None:
            self.source_materials_shrink = m.get('sourceMaterials')
        return self


class RunMarketingInformationExtractResponseBodyHeader(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_info: str = None,
        request_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.event = event
        self.event_info = event_info
        self.request_id = request_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['event'] = self.event
        if self.event_info is not None:
            result['eventInfo'] = self.event_info
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunMarketingInformationExtractResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunMarketingInformationExtractResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunMarketingInformationExtractResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunMarketingInformationExtractResponseBodyPayloadOutput = None,
        usage: RunMarketingInformationExtractResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = RunMarketingInformationExtractResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunMarketingInformationExtractResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunMarketingInformationExtractResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunMarketingInformationExtractResponseBodyHeader = None,
        payload: RunMarketingInformationExtractResponseBodyPayload = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('header') is not None:
            temp_model = RunMarketingInformationExtractResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunMarketingInformationExtractResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunMarketingInformationExtractResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunMarketingInformationExtractResponseBody = None,
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
            temp_model = RunMarketingInformationExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunMarketingInformationWritingRequest(TeaModel):
    def __init__(
        self,
        custom_prompt: str = None,
        model_id: str = None,
        source_material: str = None,
        writing_type: str = None,
    ):
        self.custom_prompt = custom_prompt
        self.model_id = model_id
        self.source_material = source_material
        self.writing_type = writing_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.source_material is not None:
            result['sourceMaterial'] = self.source_material
        if self.writing_type is not None:
            result['writingType'] = self.writing_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('sourceMaterial') is not None:
            self.source_material = m.get('sourceMaterial')
        if m.get('writingType') is not None:
            self.writing_type = m.get('writingType')
        return self


class RunMarketingInformationWritingResponseBodyHeader(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_info: str = None,
        request_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.event = event
        self.event_info = event_info
        self.request_id = request_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['event'] = self.event
        if self.event_info is not None:
            result['eventInfo'] = self.event_info
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunMarketingInformationWritingResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunMarketingInformationWritingResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunMarketingInformationWritingResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunMarketingInformationWritingResponseBodyPayloadOutput = None,
        usage: RunMarketingInformationWritingResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = RunMarketingInformationWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunMarketingInformationWritingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunMarketingInformationWritingResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunMarketingInformationWritingResponseBodyHeader = None,
        payload: RunMarketingInformationWritingResponseBodyPayload = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('header') is not None:
            temp_model = RunMarketingInformationWritingResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunMarketingInformationWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunMarketingInformationWritingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunMarketingInformationWritingResponseBody = None,
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
            temp_model = RunMarketingInformationWritingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunScriptContinueRequest(TeaModel):
    def __init__(
        self,
        script_summary: str = None,
        script_type_keyword: str = None,
        user_provided_content: str = None,
    ):
        self.script_summary = script_summary
        self.script_type_keyword = script_type_keyword
        # This parameter is required.
        self.user_provided_content = user_provided_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_summary is not None:
            result['scriptSummary'] = self.script_summary
        if self.script_type_keyword is not None:
            result['scriptTypeKeyword'] = self.script_type_keyword
        if self.user_provided_content is not None:
            result['userProvidedContent'] = self.user_provided_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptSummary') is not None:
            self.script_summary = m.get('scriptSummary')
        if m.get('scriptTypeKeyword') is not None:
            self.script_type_keyword = m.get('scriptTypeKeyword')
        if m.get('userProvidedContent') is not None:
            self.user_provided_content = m.get('userProvidedContent')
        return self


class RunScriptContinueResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        request_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.request_id = request_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.event_info is not None:
            result['eventInfo'] = self.event_info
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunScriptContinueResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunScriptContinueResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunScriptContinueResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunScriptContinueResponseBodyPayloadOutput = None,
        usage: RunScriptContinueResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = RunScriptContinueResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunScriptContinueResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunScriptContinueResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunScriptContinueResponseBodyHeader = None,
        payload: RunScriptContinueResponseBodyPayload = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('header') is not None:
            temp_model = RunScriptContinueResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunScriptContinueResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunScriptContinueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunScriptContinueResponseBody = None,
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
            temp_model = RunScriptContinueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunScriptPlanningRequest(TeaModel):
    def __init__(
        self,
        additional_note: str = None,
        dialogue_in_scene: bool = None,
        plot_conflict: bool = None,
        script_name: str = None,
        script_shot_count: int = None,
        script_summary: str = None,
        script_type_keyword: str = None,
    ):
        self.additional_note = additional_note
        self.dialogue_in_scene = dialogue_in_scene
        self.plot_conflict = plot_conflict
        self.script_name = script_name
        self.script_shot_count = script_shot_count
        # This parameter is required.
        self.script_summary = script_summary
        self.script_type_keyword = script_type_keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_note is not None:
            result['additionalNote'] = self.additional_note
        if self.dialogue_in_scene is not None:
            result['dialogueInScene'] = self.dialogue_in_scene
        if self.plot_conflict is not None:
            result['plotConflict'] = self.plot_conflict
        if self.script_name is not None:
            result['scriptName'] = self.script_name
        if self.script_shot_count is not None:
            result['scriptShotCount'] = self.script_shot_count
        if self.script_summary is not None:
            result['scriptSummary'] = self.script_summary
        if self.script_type_keyword is not None:
            result['scriptTypeKeyword'] = self.script_type_keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalNote') is not None:
            self.additional_note = m.get('additionalNote')
        if m.get('dialogueInScene') is not None:
            self.dialogue_in_scene = m.get('dialogueInScene')
        if m.get('plotConflict') is not None:
            self.plot_conflict = m.get('plotConflict')
        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')
        if m.get('scriptShotCount') is not None:
            self.script_shot_count = m.get('scriptShotCount')
        if m.get('scriptSummary') is not None:
            self.script_summary = m.get('scriptSummary')
        if m.get('scriptTypeKeyword') is not None:
            self.script_type_keyword = m.get('scriptTypeKeyword')
        return self


class RunScriptPlanningResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        request_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.request_id = request_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.event_info is not None:
            result['eventInfo'] = self.event_info
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunScriptPlanningResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunScriptPlanningResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunScriptPlanningResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunScriptPlanningResponseBodyPayloadOutput = None,
        usage: RunScriptPlanningResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = RunScriptPlanningResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunScriptPlanningResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunScriptPlanningResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunScriptPlanningResponseBodyHeader = None,
        payload: RunScriptPlanningResponseBodyPayload = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('header') is not None:
            temp_model = RunScriptPlanningResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunScriptPlanningResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunScriptPlanningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunScriptPlanningResponseBody = None,
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
            temp_model = RunScriptPlanningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunStyleWritingRequest(TeaModel):
    def __init__(
        self,
        learning_samples: List[str] = None,
        reference_materials: List[str] = None,
        style_feature: str = None,
        writing_theme: str = None,
    ):
        # This parameter is required.
        self.learning_samples = learning_samples
        # This parameter is required.
        self.reference_materials = reference_materials
        self.style_feature = style_feature
        # This parameter is required.
        self.writing_theme = writing_theme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.learning_samples is not None:
            result['learningSamples'] = self.learning_samples
        if self.reference_materials is not None:
            result['referenceMaterials'] = self.reference_materials
        if self.style_feature is not None:
            result['styleFeature'] = self.style_feature
        if self.writing_theme is not None:
            result['writingTheme'] = self.writing_theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('learningSamples') is not None:
            self.learning_samples = m.get('learningSamples')
        if m.get('referenceMaterials') is not None:
            self.reference_materials = m.get('referenceMaterials')
        if m.get('styleFeature') is not None:
            self.style_feature = m.get('styleFeature')
        if m.get('writingTheme') is not None:
            self.writing_theme = m.get('writingTheme')
        return self


class RunStyleWritingShrinkRequest(TeaModel):
    def __init__(
        self,
        learning_samples_shrink: str = None,
        reference_materials_shrink: str = None,
        style_feature: str = None,
        writing_theme: str = None,
    ):
        # This parameter is required.
        self.learning_samples_shrink = learning_samples_shrink
        # This parameter is required.
        self.reference_materials_shrink = reference_materials_shrink
        self.style_feature = style_feature
        # This parameter is required.
        self.writing_theme = writing_theme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.learning_samples_shrink is not None:
            result['learningSamples'] = self.learning_samples_shrink
        if self.reference_materials_shrink is not None:
            result['referenceMaterials'] = self.reference_materials_shrink
        if self.style_feature is not None:
            result['styleFeature'] = self.style_feature
        if self.writing_theme is not None:
            result['writingTheme'] = self.writing_theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('learningSamples') is not None:
            self.learning_samples_shrink = m.get('learningSamples')
        if m.get('referenceMaterials') is not None:
            self.reference_materials_shrink = m.get('referenceMaterials')
        if m.get('styleFeature') is not None:
            self.style_feature = m.get('styleFeature')
        if m.get('writingTheme') is not None:
            self.writing_theme = m.get('writingTheme')
        return self


class RunStyleWritingResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        request_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.request_id = request_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.event_info is not None:
            result['eventInfo'] = self.event_info
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunStyleWritingResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunStyleWritingResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunStyleWritingResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunStyleWritingResponseBodyPayloadOutput = None,
        usage: RunStyleWritingResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = RunStyleWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunStyleWritingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunStyleWritingResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunStyleWritingResponseBodyHeader = None,
        payload: RunStyleWritingResponseBodyPayload = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('header') is not None:
            temp_model = RunStyleWritingResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunStyleWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunStyleWritingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunStyleWritingResponseBody = None,
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
            temp_model = RunStyleWritingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunVideoAnalysisRequest(TeaModel):
    def __init__(
        self,
        generate_options: List[str] = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        original_session_id: str = None,
        task_id: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_url: str = None,
    ):
        self.generate_options = generate_options
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.task_id = task_id
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_options is not None:
            result['generateOptions'] = self.generate_options
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template
        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateOptions') is not None:
            self.generate_options = m.get('generateOptions')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')
        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class RunVideoAnalysisShrinkRequest(TeaModel):
    def __init__(
        self,
        generate_options_shrink: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        original_session_id: str = None,
        task_id: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_url: str = None,
    ):
        self.generate_options_shrink = generate_options_shrink
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.task_id = task_id
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_options_shrink is not None:
            result['generateOptions'] = self.generate_options_shrink
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template
        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateOptions') is not None:
            self.generate_options_shrink = m.get('generateOptions')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')
        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class RunVideoAnalysisResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.event_info is not None:
            result['eventInfo'] = self.event_info
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        text: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage = None,
        video_shot_analysis_results: List[RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults] = None,
    ):
        self.generate_finished = generate_finished
        self.text = text
        self.usage = usage
        self.video_shot_analysis_results = video_shot_analysis_results

    def validate(self):
        if self.usage:
            self.usage.validate()
        if self.video_shot_analysis_results:
            for k in self.video_shot_analysis_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        result['videoShotAnalysisResults'] = []
        if self.video_shot_analysis_results is not None:
            for k in self.video_shot_analysis_results:
                result['videoShotAnalysisResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        self.video_shot_analysis_results = []
        if m.get('videoShotAnalysisResults') is not None:
            for k in m.get('videoShotAnalysisResults'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults()
                self.video_shot_analysis_results.append(temp_model.from_map(k))
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResultVideoCaptions(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        end_time_format: str = None,
        start_time: int = None,
        start_time_format: str = None,
        text: str = None,
    ):
        self.end_time = end_time
        self.end_time_format = end_time_format
        self.start_time = start_time
        self.start_time_format = start_time_format
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.end_time_format is not None:
            result['endTimeFormat'] = self.end_time_format
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.start_time_format is not None:
            result['startTimeFormat'] = self.start_time_format
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('endTimeFormat') is not None:
            self.end_time_format = m.get('endTimeFormat')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('startTimeFormat') is not None:
            self.start_time_format = m.get('startTimeFormat')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        video_captions: List[RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResultVideoCaptions] = None,
    ):
        self.generate_finished = generate_finished
        self.video_captions = video_captions

    def validate(self):
        if self.video_captions:
            for k in self.video_captions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished
        result['videoCaptions'] = []
        if self.video_captions is not None:
            for k in self.video_captions:
                result['videoCaptions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        self.video_captions = []
        if m.get('videoCaptions') is not None:
            for k in m.get('videoCaptions'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResultVideoCaptions()
                self.video_captions.append(temp_model.from_map(k))
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.text = text
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes(TeaModel):
    def __init__(
        self,
        child_nodes: List[RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes] = None,
        name: str = None,
    ):
        self.child_nodes = child_nodes
        self.name = name

    def validate(self):
        if self.child_nodes:
            for k in self.child_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['childNodes'] = []
        if self.child_nodes is not None:
            for k in self.child_nodes:
                result['childNodes'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_nodes = []
        if m.get('childNodes') is not None:
            for k in m.get('childNodes'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes()
                self.child_nodes.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings(TeaModel):
    def __init__(
        self,
        child_nodes: List[RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes] = None,
        name: str = None,
    ):
        self.child_nodes = child_nodes
        self.name = name

    def validate(self):
        if self.child_nodes:
            for k in self.child_nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['childNodes'] = []
        if self.child_nodes is not None:
            for k in self.child_nodes:
                result['childNodes'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_nodes = []
        if m.get('childNodes') is not None:
            for k in m.get('childNodes'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes()
                self.child_nodes.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage = None,
        video_mind_mappings: List[RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings] = None,
    ):
        self.generate_finished = generate_finished
        self.text = text
        self.usage = usage
        self.video_mind_mappings = video_mind_mappings

    def validate(self):
        if self.usage:
            self.usage.validate()
        if self.video_mind_mappings:
            for k in self.video_mind_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        result['videoMindMappings'] = []
        if self.video_mind_mappings is not None:
            for k in self.video_mind_mappings:
                result['videoMindMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        self.video_mind_mappings = []
        if m.get('videoMindMappings') is not None:
            for k in m.get('videoMindMappings'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings()
                self.video_mind_mappings.append(temp_model.from_map(k))
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.text = text
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunVideoAnalysisResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        video_analysis_result: RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult = None,
        video_caption_result: RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult = None,
        video_generate_result: RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult = None,
        video_mind_mapping_generate_result: RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult = None,
        video_title_generate_result: RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult = None,
    ):
        self.video_analysis_result = video_analysis_result
        self.video_caption_result = video_caption_result
        self.video_generate_result = video_generate_result
        self.video_mind_mapping_generate_result = video_mind_mapping_generate_result
        self.video_title_generate_result = video_title_generate_result

    def validate(self):
        if self.video_analysis_result:
            self.video_analysis_result.validate()
        if self.video_caption_result:
            self.video_caption_result.validate()
        if self.video_generate_result:
            self.video_generate_result.validate()
        if self.video_mind_mapping_generate_result:
            self.video_mind_mapping_generate_result.validate()
        if self.video_title_generate_result:
            self.video_title_generate_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_analysis_result is not None:
            result['videoAnalysisResult'] = self.video_analysis_result.to_map()
        if self.video_caption_result is not None:
            result['videoCaptionResult'] = self.video_caption_result.to_map()
        if self.video_generate_result is not None:
            result['videoGenerateResult'] = self.video_generate_result.to_map()
        if self.video_mind_mapping_generate_result is not None:
            result['videoMindMappingGenerateResult'] = self.video_mind_mapping_generate_result.to_map()
        if self.video_title_generate_result is not None:
            result['videoTitleGenerateResult'] = self.video_title_generate_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoAnalysisResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult()
            self.video_analysis_result = temp_model.from_map(m['videoAnalysisResult'])
        if m.get('videoCaptionResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult()
            self.video_caption_result = temp_model.from_map(m['videoCaptionResult'])
        if m.get('videoGenerateResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult()
            self.video_generate_result = temp_model.from_map(m['videoGenerateResult'])
        if m.get('videoMindMappingGenerateResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult()
            self.video_mind_mapping_generate_result = temp_model.from_map(m['videoMindMappingGenerateResult'])
        if m.get('videoTitleGenerateResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult()
            self.video_title_generate_result = temp_model.from_map(m['videoTitleGenerateResult'])
        return self


class RunVideoAnalysisResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunVideoAnalysisResponseBodyPayloadOutput = None,
    ):
        self.output = output

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        return self


class RunVideoAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        header: RunVideoAnalysisResponseBodyHeader = None,
        payload: RunVideoAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = RunVideoAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RunVideoAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunVideoAnalysisResponseBody = None,
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
            temp_model = RunVideoAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


