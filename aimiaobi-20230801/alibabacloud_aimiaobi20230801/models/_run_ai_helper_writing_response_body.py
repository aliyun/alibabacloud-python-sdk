# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunAiHelperWritingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        header: main_models.RunAiHelperWritingResponseBodyHeader = None,
        http_status_code: str = None,
        message: str = None,
        payload: main_models.RunAiHelperWritingResponseBodyPayload = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 业务处理结果状态码
        self.code = code
        # 流式响应的头部信息，包含事件类型、状态码等元数据
        self.header = header
        # HTTP响应状态码
        self.http_status_code = http_status_code
        # 业务处理结果描述信息
        self.message = message
        # 包含写作输出内容和Token使用量统计
        self.payload = payload
        # 本次API请求的唯一标识
        self.request_id = request_id
        # 请求是否处理成功
        self.success = success

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Header') is not None:
            temp_model = main_models.RunAiHelperWritingResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Payload') is not None:
            temp_model = main_models.RunAiHelperWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RunAiHelperWritingResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunAiHelperWritingResponseBodyPayloadOutput = None,
        usage: main_models.RunAiHelperWritingResponseBodyPayloadUsage = None,
    ):
        # AI生成的写作内容
        self.output = output
        # 本次请求的Token消耗统计
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = main_models.RunAiHelperWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunAiHelperWritingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunAiHelperWritingResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        # 输入内容消耗的Token数量
        self.input_tokens = input_tokens
        # 生成内容消耗的Token数量
        self.output_tokens = output_tokens
        # 输入和输出Token的总和
        self.total_tokens = total_tokens

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunAiHelperWritingResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        text: str = None,
        writing_params: Dict[str, str] = None,
    ):
        # AI生成的文章内容，流式返回时为增量文本
        self.text = text
        # 返回的写作参数键值对
        self.writing_params = writing_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.writing_params is not None:
            result['WritingParams'] = self.writing_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('WritingParams') is not None:
            self.writing_params = m.get('WritingParams')

        return self

class RunAiHelperWritingResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        status_code: int = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        # 请求错误时的错误码
        self.error_code = error_code
        # 请求错误时的详细错误信息
        self.error_message = error_message
        # SSE事件类型，如：result-generated(生成结果)、task-finished(任务完成)
        self.event = event
        # 当前写作会话的唯一标识
        self.session_id = session_id
        # HTTP状态码
        self.status_code = status_code
        # 写作任务的唯一标识
        self.task_id = task_id
        # 用于问题排查的链路追踪标识
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event is not None:
            result['Event'] = self.event

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

