# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GenerateBroadcastNewsRequest(TeaModel):
    def __init__(
        self,
        prompt: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt is not None:
            result['prompt'] = self.prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        return self


class GenerateBroadcastNewsResponseBodyDataHotTopicSummariesImages(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GenerateBroadcastNewsResponseBodyDataHotTopicSummaries(TeaModel):
    def __init__(
        self,
        category: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        id: str = None,
        images: List[GenerateBroadcastNewsResponseBodyDataHotTopicSummariesImages] = None,
        text_summary: str = None,
    ):
        self.category = category
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.id = id
        self.images = images
        self.text_summary = text_summary

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.hot_topic is not None:
            result['hotTopic'] = self.hot_topic
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.hot_value is not None:
            result['hotValue'] = self.hot_value
        if self.id is not None:
            result['id'] = self.id
        result['images'] = []
        if self.images is not None:
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        if self.text_summary is not None:
            result['textSummary'] = self.text_summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('hotValue') is not None:
            self.hot_value = m.get('hotValue')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = GenerateBroadcastNewsResponseBodyDataHotTopicSummariesImages()
                self.images.append(temp_model.from_map(k))
        if m.get('textSummary') is not None:
            self.text_summary = m.get('textSummary')
        return self


class GenerateBroadcastNewsResponseBodyDataUsage(TeaModel):
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


class GenerateBroadcastNewsResponseBodyData(TeaModel):
    def __init__(
        self,
        hot_topic_summaries: List[GenerateBroadcastNewsResponseBodyDataHotTopicSummaries] = None,
        session_id: str = None,
        task_id: str = None,
        text: str = None,
        usage: GenerateBroadcastNewsResponseBodyDataUsage = None,
    ):
        self.hot_topic_summaries = hot_topic_summaries
        self.session_id = session_id
        self.task_id = task_id
        self.text = text
        self.usage = usage

    def validate(self):
        if self.hot_topic_summaries:
            for k in self.hot_topic_summaries:
                if k:
                    k.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['hotTopicSummaries'] = []
        if self.hot_topic_summaries is not None:
            for k in self.hot_topic_summaries:
                result['hotTopicSummaries'].append(k.to_map() if k else None)
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_topic_summaries = []
        if m.get('hotTopicSummaries') is not None:
            for k in m.get('hotTopicSummaries'):
                temp_model = GenerateBroadcastNewsResponseBodyDataHotTopicSummaries()
                self.hot_topic_summaries.append(temp_model.from_map(k))
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = GenerateBroadcastNewsResponseBodyDataUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GenerateBroadcastNewsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateBroadcastNewsResponseBodyData = None,
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GenerateBroadcastNewsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GenerateBroadcastNewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateBroadcastNewsResponseBody = None,
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
            temp_model = GenerateBroadcastNewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateOutputFormatRequestTags(TeaModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_define_prompt is not None:
            result['tagDefinePrompt'] = self.tag_define_prompt
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('tagDefinePrompt')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        return self


class GenerateOutputFormatRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        tags: List[GenerateOutputFormatRequestTags] = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        self.content = content
        self.extra_info = extra_info
        # This parameter is required.
        self.tags = tags
        self.task_description = task_description

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.content is not None:
            result['content'] = self.content
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GenerateOutputFormatRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        return self


class GenerateOutputFormatShrinkRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        tags_shrink: str = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        self.content = content
        self.extra_info = extra_info
        # This parameter is required.
        self.tags_shrink = tags_shrink
        self.task_description = task_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.content is not None:
            result['content'] = self.content
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        return self


class GenerateOutputFormatResponseBodyData(TeaModel):
    def __init__(
        self,
        output_format: str = None,
    ):
        self.output_format = output_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        return self


class GenerateOutputFormatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateOutputFormatResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GenerateOutputFormatResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GenerateOutputFormatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateOutputFormatResponseBody = None,
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
            temp_model = GenerateOutputFormatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagMiningAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTagMiningAnalysisTaskResponseBodyDataResultsHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        request_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadOutput(TeaModel):
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


class GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadUsage(TeaModel):
    def __init__(
        self,
        input_token: int = None,
        output_token: int = None,
        total_token: int = None,
    ):
        self.input_token = input_token
        self.output_token = output_token
        self.total_token = total_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_token is not None:
            result['inputToken'] = self.input_token
        if self.output_token is not None:
            result['outputToken'] = self.output_token
        if self.total_token is not None:
            result['totalToken'] = self.total_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputToken') is not None:
            self.input_token = m.get('inputToken')
        if m.get('outputToken') is not None:
            self.output_token = m.get('outputToken')
        if m.get('totalToken') is not None:
            self.total_token = m.get('totalToken')
        return self


class GetTagMiningAnalysisTaskResponseBodyDataResultsPayload(TeaModel):
    def __init__(
        self,
        output: GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadOutput = None,
        usage: GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadUsage = None,
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
            temp_model = GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetTagMiningAnalysisTaskResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        custom_id: str = None,
        header: GetTagMiningAnalysisTaskResponseBodyDataResultsHeader = None,
        payload: GetTagMiningAnalysisTaskResponseBodyDataResultsPayload = None,
    ):
        self.custom_id = custom_id
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
        if self.custom_id is not None:
            result['customId'] = self.custom_id
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customId') is not None:
            self.custom_id = m.get('customId')
        if m.get('header') is not None:
            temp_model = GetTagMiningAnalysisTaskResponseBodyDataResultsHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = GetTagMiningAnalysisTaskResponseBodyDataResultsPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class GetTagMiningAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        results: List[GetTagMiningAnalysisTaskResponseBodyDataResults] = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.results = results
        self.status = status

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['results'] = []
        if self.results is not None:
            for k in self.results:
                result['results'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.results = []
        if m.get('results') is not None:
            for k in m.get('results'):
                temp_model = GetTagMiningAnalysisTaskResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetTagMiningAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTagMiningAnalysisTaskResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # requestId
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTagMiningAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTagMiningAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTagMiningAnalysisTaskResponseBody = None,
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
            temp_model = GetTagMiningAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoAnalysisConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        async_concurrency: int = None,
    ):
        self.async_concurrency = async_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_concurrency is not None:
            result['asyncConcurrency'] = self.async_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncConcurrency') is not None:
            self.async_concurrency = m.get('asyncConcurrency')
        return self


class GetVideoAnalysisConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVideoAnalysisConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetVideoAnalysisConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetVideoAnalysisConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoAnalysisConfigResponseBody = None,
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
            temp_model = GetVideoAnalysisConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetVideoAnalysisTaskResponseBodyDataHeader(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResultUsage(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResultVideoShotAnalysisResults(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResultUsage = None,
        video_shot_analysis_results: List[GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResultVideoShotAnalysisResults] = None,
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
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        self.video_shot_analysis_results = []
        if m.get('videoShotAnalysisResults') is not None:
            for k in m.get('videoShotAnalysisResults'):
                temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResultVideoShotAnalysisResults()
                self.video_shot_analysis_results.append(temp_model.from_map(k))
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoCaptionResultVideoCaptions(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoCaptionResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        video_captions: List[GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoCaptionResultVideoCaptions] = None,
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
                temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoCaptionResultVideoCaptions()
                self.video_captions.append(temp_model.from_map(k))
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResultUsage(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        index: int = None,
        model_id: str = None,
        model_reduce: bool = None,
        reason_text: str = None,
        text: str = None,
        usage: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.index = index
        self.model_id = model_id
        self.model_reduce = model_reduce
        self.reason_text = reason_text
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
        if self.index is not None:
            result['index'] = self.index
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce
        if self.reason_text is not None:
            result['reasonText'] = self.reason_text
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')
        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResultsUsage(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResults(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        index: int = None,
        model_id: str = None,
        reason_text: str = None,
        text: str = None,
        usage: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResultsUsage = None,
    ):
        self.generate_finished = generate_finished
        self.index = index
        self.model_id = model_id
        self.reason_text = reason_text
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
        if self.index is not None:
            result['index'] = self.index
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.reason_text is not None:
            result['reasonText'] = self.reason_text
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResultsUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultUsage(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes(TeaModel):
    def __init__(
        self,
        child_nodes: List[GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes] = None,
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
                temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes()
                self.child_nodes.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappings(TeaModel):
    def __init__(
        self,
        child_nodes: List[GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes] = None,
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
                temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes()
                self.child_nodes.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultUsage = None,
        video_mind_mappings: List[GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappings] = None,
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
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        self.video_mind_mappings = []
        if m.get('videoMindMappings') is not None:
            for k in m.get('videoMindMappings'):
                temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResultVideoMindMappings()
                self.video_mind_mappings.append(temp_model.from_map(k))
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoTitleGenerateResultUsage(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoTitleGenerateResult(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        text: str = None,
        usage: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoTitleGenerateResultUsage = None,
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
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoTitleGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadOutput(TeaModel):
    def __init__(
        self,
        result_json_file_url: str = None,
        video_analysis_result: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResult = None,
        video_caption_result: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoCaptionResult = None,
        video_generate_result: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResult = None,
        video_generate_results: List[GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResults] = None,
        video_mind_mapping_generate_result: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResult = None,
        video_title_generate_result: GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoTitleGenerateResult = None,
    ):
        self.result_json_file_url = result_json_file_url
        self.video_analysis_result = video_analysis_result
        self.video_caption_result = video_caption_result
        self.video_generate_result = video_generate_result
        self.video_generate_results = video_generate_results
        self.video_mind_mapping_generate_result = video_mind_mapping_generate_result
        self.video_title_generate_result = video_title_generate_result

    def validate(self):
        if self.video_analysis_result:
            self.video_analysis_result.validate()
        if self.video_caption_result:
            self.video_caption_result.validate()
        if self.video_generate_result:
            self.video_generate_result.validate()
        if self.video_generate_results:
            for k in self.video_generate_results:
                if k:
                    k.validate()
        if self.video_mind_mapping_generate_result:
            self.video_mind_mapping_generate_result.validate()
        if self.video_title_generate_result:
            self.video_title_generate_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_json_file_url is not None:
            result['resultJsonFileUrl'] = self.result_json_file_url
        if self.video_analysis_result is not None:
            result['videoAnalysisResult'] = self.video_analysis_result.to_map()
        if self.video_caption_result is not None:
            result['videoCaptionResult'] = self.video_caption_result.to_map()
        if self.video_generate_result is not None:
            result['videoGenerateResult'] = self.video_generate_result.to_map()
        result['videoGenerateResults'] = []
        if self.video_generate_results is not None:
            for k in self.video_generate_results:
                result['videoGenerateResults'].append(k.to_map() if k else None)
        if self.video_mind_mapping_generate_result is not None:
            result['videoMindMappingGenerateResult'] = self.video_mind_mapping_generate_result.to_map()
        if self.video_title_generate_result is not None:
            result['videoTitleGenerateResult'] = self.video_title_generate_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resultJsonFileUrl') is not None:
            self.result_json_file_url = m.get('resultJsonFileUrl')
        if m.get('videoAnalysisResult') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoAnalysisResult()
            self.video_analysis_result = temp_model.from_map(m['videoAnalysisResult'])
        if m.get('videoCaptionResult') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoCaptionResult()
            self.video_caption_result = temp_model.from_map(m['videoCaptionResult'])
        if m.get('videoGenerateResult') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResult()
            self.video_generate_result = temp_model.from_map(m['videoGenerateResult'])
        self.video_generate_results = []
        if m.get('videoGenerateResults') is not None:
            for k in m.get('videoGenerateResults'):
                temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoGenerateResults()
                self.video_generate_results.append(temp_model.from_map(k))
        if m.get('videoMindMappingGenerateResult') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoMindMappingGenerateResult()
            self.video_mind_mapping_generate_result = temp_model.from_map(m['videoMindMappingGenerateResult'])
        if m.get('videoTitleGenerateResult') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutputVideoTitleGenerateResult()
            self.video_title_generate_result = temp_model.from_map(m['videoTitleGenerateResult'])
        return self


class GetVideoAnalysisTaskResponseBodyDataPayloadUsage(TeaModel):
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


class GetVideoAnalysisTaskResponseBodyDataPayload(TeaModel):
    def __init__(
        self,
        output: GetVideoAnalysisTaskResponseBodyDataPayloadOutput = None,
        usage: GetVideoAnalysisTaskResponseBodyDataPayloadUsage = None,
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
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetVideoAnalysisTaskResponseBodyDataTaskRunInfo(TeaModel):
    def __init__(
        self,
        concurrent_charge_enable: bool = None,
        response_time: int = None,
    ):
        self.concurrent_charge_enable = concurrent_charge_enable
        self.response_time = response_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrent_charge_enable is not None:
            result['concurrentChargeEnable'] = self.concurrent_charge_enable
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrentChargeEnable') is not None:
            self.concurrent_charge_enable = m.get('concurrentChargeEnable')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        return self


class GetVideoAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        header: GetVideoAnalysisTaskResponseBodyDataHeader = None,
        payload: GetVideoAnalysisTaskResponseBodyDataPayload = None,
        task_id: str = None,
        task_run_info: GetVideoAnalysisTaskResponseBodyDataTaskRunInfo = None,
        task_status: str = None,
    ):
        self.error_message = error_message
        self.header = header
        self.payload = payload
        self.task_id = task_id
        self.task_run_info = task_run_info
        self.task_status = task_status

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()
        if self.task_run_info:
            self.task_run_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_run_info is not None:
            result['taskRunInfo'] = self.task_run_info.to_map()
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('header') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskRunInfo') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyDataTaskRunInfo()
            self.task_run_info = temp_model.from_map(m['taskRunInfo'])
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        return self


class GetVideoAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetVideoAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetVideoAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetVideoAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoAnalysisTaskResponseBody = None,
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
            temp_model = GetVideoAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotTopicSummariesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.category = category
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.hot_topic is not None:
            result['hotTopic'] = self.hot_topic
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListHotTopicSummariesResponseBodyDataNewsComments(TeaModel):
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


class ListHotTopicSummariesResponseBodyDataNews(TeaModel):
    def __init__(
        self,
        comments: List[ListHotTopicSummariesResponseBodyDataNewsComments] = None,
        content: str = None,
        pub_time: str = None,
        title: str = None,
        url: str = None,
    ):
        self.comments = comments
        self.content = content
        self.pub_time = pub_time
        self.title = title
        # url
        self.url = url

    def validate(self):
        if self.comments:
            for k in self.comments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['comments'] = []
        if self.comments is not None:
            for k in self.comments:
                result['comments'].append(k.to_map() if k else None)
        if self.content is not None:
            result['content'] = self.content
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comments = []
        if m.get('comments') is not None:
            for k in m.get('comments'):
                temp_model = ListHotTopicSummariesResponseBodyDataNewsComments()
                self.comments.append(temp_model.from_map(k))
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListHotTopicSummariesResponseBodyDataSummarySummaries(TeaModel):
    def __init__(
        self,
        summary: str = None,
        title: str = None,
    ):
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary is not None:
            result['summary'] = self.summary
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListHotTopicSummariesResponseBodyDataSummary(TeaModel):
    def __init__(
        self,
        summaries: List[ListHotTopicSummariesResponseBodyDataSummarySummaries] = None,
    ):
        self.summaries = summaries

    def validate(self):
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['summaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summaries = []
        if m.get('summaries') is not None:
            for k in m.get('summaries'):
                temp_model = ListHotTopicSummariesResponseBodyDataSummarySummaries()
                self.summaries.append(temp_model.from_map(k))
        return self


class ListHotTopicSummariesResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        id: str = None,
        news: List[ListHotTopicSummariesResponseBodyDataNews] = None,
        summary: ListHotTopicSummariesResponseBodyDataSummary = None,
        text_summary: str = None,
    ):
        self.category = category
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.id = id
        self.news = news
        self.summary = summary
        self.text_summary = text_summary

    def validate(self):
        if self.news:
            for k in self.news:
                if k:
                    k.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.hot_topic is not None:
            result['hotTopic'] = self.hot_topic
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.hot_value is not None:
            result['hotValue'] = self.hot_value
        if self.id is not None:
            result['id'] = self.id
        result['news'] = []
        if self.news is not None:
            for k in self.news:
                result['news'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['summary'] = self.summary.to_map()
        if self.text_summary is not None:
            result['textSummary'] = self.text_summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('hotValue') is not None:
            self.hot_value = m.get('hotValue')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.news = []
        if m.get('news') is not None:
            for k in m.get('news'):
                temp_model = ListHotTopicSummariesResponseBodyDataNews()
                self.news.append(temp_model.from_map(k))
        if m.get('summary') is not None:
            temp_model = ListHotTopicSummariesResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['summary'])
        if m.get('textSummary') is not None:
            self.text_summary = m.get('textSummary')
        return self


class ListHotTopicSummariesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListHotTopicSummariesResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
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
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.message is not None:
            result['message'] = self.message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListHotTopicSummariesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListHotTopicSummariesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotTopicSummariesResponseBody = None,
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
            temp_model = ListHotTopicSummariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunHotTopicChatRequestMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        role: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class RunHotTopicChatRequestStepForBroadcastContentConfigCustomHotValueWeights(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        weight: int = None,
    ):
        self.dimension = dimension
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class RunHotTopicChatRequestStepForBroadcastContentConfig(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        custom_hot_value_weights: List[RunHotTopicChatRequestStepForBroadcastContentConfigCustomHotValueWeights] = None,
        topic_count: int = None,
    ):
        self.categories = categories
        self.custom_hot_value_weights = custom_hot_value_weights
        self.topic_count = topic_count

    def validate(self):
        if self.custom_hot_value_weights:
            for k in self.custom_hot_value_weights:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['categories'] = self.categories
        result['customHotValueWeights'] = []
        if self.custom_hot_value_weights is not None:
            for k in self.custom_hot_value_weights:
                result['customHotValueWeights'].append(k.to_map() if k else None)
        if self.topic_count is not None:
            result['topicCount'] = self.topic_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')
        self.custom_hot_value_weights = []
        if m.get('customHotValueWeights') is not None:
            for k in m.get('customHotValueWeights'):
                temp_model = RunHotTopicChatRequestStepForBroadcastContentConfigCustomHotValueWeights()
                self.custom_hot_value_weights.append(temp_model.from_map(k))
        if m.get('topicCount') is not None:
            self.topic_count = m.get('topicCount')
        return self


class RunHotTopicChatRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        generate_options: List[str] = None,
        hot_topic_version: str = None,
        hot_topics: List[str] = None,
        image_count: int = None,
        messages: List[RunHotTopicChatRequestMessages] = None,
        model_custom_prompt_template: str = None,
        model_id: str = None,
        original_session_id: str = None,
        prompt: str = None,
        step_for_broadcast_content_config: RunHotTopicChatRequestStepForBroadcastContentConfig = None,
        task_id: str = None,
    ):
        self.category = category
        self.generate_options = generate_options
        self.hot_topic_version = hot_topic_version
        self.hot_topics = hot_topics
        self.image_count = image_count
        self.messages = messages
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.prompt = prompt
        self.step_for_broadcast_content_config = step_for_broadcast_content_config
        self.task_id = task_id

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()
        if self.step_for_broadcast_content_config:
            self.step_for_broadcast_content_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.generate_options is not None:
            result['generateOptions'] = self.generate_options
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.hot_topics is not None:
            result['hotTopics'] = self.hot_topics
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.step_for_broadcast_content_config is not None:
            result['stepForBroadcastContentConfig'] = self.step_for_broadcast_content_config.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('generateOptions') is not None:
            self.generate_options = m.get('generateOptions')
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('hotTopics') is not None:
            self.hot_topics = m.get('hotTopics')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = RunHotTopicChatRequestMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('stepForBroadcastContentConfig') is not None:
            temp_model = RunHotTopicChatRequestStepForBroadcastContentConfig()
            self.step_for_broadcast_content_config = temp_model.from_map(m['stepForBroadcastContentConfig'])
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class RunHotTopicChatShrinkRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        generate_options_shrink: str = None,
        hot_topic_version: str = None,
        hot_topics_shrink: str = None,
        image_count: int = None,
        messages_shrink: str = None,
        model_custom_prompt_template: str = None,
        model_id: str = None,
        original_session_id: str = None,
        prompt: str = None,
        step_for_broadcast_content_config_shrink: str = None,
        task_id: str = None,
    ):
        self.category = category
        self.generate_options_shrink = generate_options_shrink
        self.hot_topic_version = hot_topic_version
        self.hot_topics_shrink = hot_topics_shrink
        self.image_count = image_count
        self.messages_shrink = messages_shrink
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.prompt = prompt
        self.step_for_broadcast_content_config_shrink = step_for_broadcast_content_config_shrink
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.generate_options_shrink is not None:
            result['generateOptions'] = self.generate_options_shrink
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.hot_topics_shrink is not None:
            result['hotTopics'] = self.hot_topics_shrink
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.messages_shrink is not None:
            result['messages'] = self.messages_shrink
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.step_for_broadcast_content_config_shrink is not None:
            result['stepForBroadcastContentConfig'] = self.step_for_broadcast_content_config_shrink
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('generateOptions') is not None:
            self.generate_options_shrink = m.get('generateOptions')
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('hotTopics') is not None:
            self.hot_topics_shrink = m.get('hotTopics')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('messages') is not None:
            self.messages_shrink = m.get('messages')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('stepForBroadcastContentConfig') is not None:
            self.step_for_broadcast_content_config_shrink = m.get('stepForBroadcastContentConfig')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class RunHotTopicChatResponseBodyHeader(TeaModel):
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


class RunHotTopicChatResponseBodyPayloadOutputArticles(TeaModel):
    def __init__(
        self,
        content: str = None,
        pub_time: str = None,
        score: float = None,
        search_source_name: str = None,
        select: bool = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.pub_time = pub_time
        self.score = score
        self.search_source_name = search_source_name
        self.select = select
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.pub_time is not None:
            result['pubTime'] = self.pub_time
        if self.score is not None:
            result['score'] = self.score
        if self.search_source_name is not None:
            result['searchSourceName'] = self.search_source_name
        if self.select is not None:
            result['select'] = self.select
        if self.summary is not None:
            result['summary'] = self.summary
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('searchSourceName') is not None:
            self.search_source_name = m.get('searchSourceName')
        if m.get('select') is not None:
            self.select = m.get('select')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesImages(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesNews(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RunHotTopicChatResponseBodyPayloadOutputHotTopicSummaries(TeaModel):
    def __init__(
        self,
        custom_hot_value: float = None,
        custom_text_summary: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        images: List[RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesImages] = None,
        news: List[RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesNews] = None,
        text_summary: str = None,
    ):
        self.custom_hot_value = custom_hot_value
        self.custom_text_summary = custom_text_summary
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.images = images
        self.news = news
        self.text_summary = text_summary

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.news:
            for k in self.news:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_hot_value is not None:
            result['customHotValue'] = self.custom_hot_value
        if self.custom_text_summary is not None:
            result['customTextSummary'] = self.custom_text_summary
        if self.hot_topic is not None:
            result['hotTopic'] = self.hot_topic
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.hot_value is not None:
            result['hotValue'] = self.hot_value
        result['images'] = []
        if self.images is not None:
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        result['news'] = []
        if self.news is not None:
            for k in self.news:
                result['news'].append(k.to_map() if k else None)
        if self.text_summary is not None:
            result['textSummary'] = self.text_summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customHotValue') is not None:
            self.custom_hot_value = m.get('customHotValue')
        if m.get('customTextSummary') is not None:
            self.custom_text_summary = m.get('customTextSummary')
        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('hotValue') is not None:
            self.hot_value = m.get('hotValue')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesImages()
                self.images.append(temp_model.from_map(k))
        self.news = []
        if m.get('news') is not None:
            for k in m.get('news'):
                temp_model = RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesNews()
                self.news.append(temp_model.from_map(k))
        if m.get('textSummary') is not None:
            self.text_summary = m.get('textSummary')
        return self


class RunHotTopicChatResponseBodyPayloadOutputMultimodalMedias(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        media_type: str = None,
        sort_score: float = None,
    ):
        self.file_url = file_url
        self.media_type = media_type
        self.sort_score = sort_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.sort_score is not None:
            result['sortScore'] = self.sort_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('sortScore') is not None:
            self.sort_score = m.get('sortScore')
        return self


class RunHotTopicChatResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        articles: List[RunHotTopicChatResponseBodyPayloadOutputArticles] = None,
        hot_topic_summaries: List[RunHotTopicChatResponseBodyPayloadOutputHotTopicSummaries] = None,
        multimodal_medias: List[RunHotTopicChatResponseBodyPayloadOutputMultimodalMedias] = None,
        recommend_queries: List[str] = None,
        search_query: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.hot_topic_summaries = hot_topic_summaries
        self.multimodal_medias = multimodal_medias
        self.recommend_queries = recommend_queries
        self.search_query = search_query
        self.text = text

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()
        if self.hot_topic_summaries:
            for k in self.hot_topic_summaries:
                if k:
                    k.validate()
        if self.multimodal_medias:
            for k in self.multimodal_medias:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['articles'].append(k.to_map() if k else None)
        result['hotTopicSummaries'] = []
        if self.hot_topic_summaries is not None:
            for k in self.hot_topic_summaries:
                result['hotTopicSummaries'].append(k.to_map() if k else None)
        result['multimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k in self.multimodal_medias:
                result['multimodalMedias'].append(k.to_map() if k else None)
        if self.recommend_queries is not None:
            result['recommendQueries'] = self.recommend_queries
        if self.search_query is not None:
            result['searchQuery'] = self.search_query
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('articles') is not None:
            for k in m.get('articles'):
                temp_model = RunHotTopicChatResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k))
        self.hot_topic_summaries = []
        if m.get('hotTopicSummaries') is not None:
            for k in m.get('hotTopicSummaries'):
                temp_model = RunHotTopicChatResponseBodyPayloadOutputHotTopicSummaries()
                self.hot_topic_summaries.append(temp_model.from_map(k))
        self.multimodal_medias = []
        if m.get('multimodalMedias') is not None:
            for k in m.get('multimodalMedias'):
                temp_model = RunHotTopicChatResponseBodyPayloadOutputMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k))
        if m.get('recommendQueries') is not None:
            self.recommend_queries = m.get('recommendQueries')
        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunHotTopicChatResponseBodyPayloadUsage(TeaModel):
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


class RunHotTopicChatResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunHotTopicChatResponseBodyPayloadOutput = None,
        usage: RunHotTopicChatResponseBodyPayloadUsage = None,
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
            temp_model = RunHotTopicChatResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunHotTopicChatResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunHotTopicChatResponseBody(TeaModel):
    def __init__(
        self,
        header: RunHotTopicChatResponseBodyHeader = None,
        payload: RunHotTopicChatResponseBodyPayload = None,
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
            temp_model = RunHotTopicChatResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunHotTopicChatResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RunHotTopicChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunHotTopicChatResponseBody = None,
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
            temp_model = RunHotTopicChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunHotTopicSummaryRequestStepForCustomSummaryStyleConfig(TeaModel):
    def __init__(
        self,
        summary_image_count: int = None,
        summary_model: str = None,
        summary_prompt: str = None,
    ):
        self.summary_image_count = summary_image_count
        self.summary_model = summary_model
        self.summary_prompt = summary_prompt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_image_count is not None:
            result['summaryImageCount'] = self.summary_image_count
        if self.summary_model is not None:
            result['summaryModel'] = self.summary_model
        if self.summary_prompt is not None:
            result['summaryPrompt'] = self.summary_prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summaryImageCount') is not None:
            self.summary_image_count = m.get('summaryImageCount')
        if m.get('summaryModel') is not None:
            self.summary_model = m.get('summaryModel')
        if m.get('summaryPrompt') is not None:
            self.summary_prompt = m.get('summaryPrompt')
        return self


class RunHotTopicSummaryRequest(TeaModel):
    def __init__(
        self,
        hot_topic_version: str = None,
        step_for_custom_summary_style_config: RunHotTopicSummaryRequestStepForCustomSummaryStyleConfig = None,
        topic_ids: List[str] = None,
    ):
        # This parameter is required.
        self.hot_topic_version = hot_topic_version
        # This parameter is required.
        self.step_for_custom_summary_style_config = step_for_custom_summary_style_config
        # This parameter is required.
        self.topic_ids = topic_ids

    def validate(self):
        if self.step_for_custom_summary_style_config:
            self.step_for_custom_summary_style_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.step_for_custom_summary_style_config is not None:
            result['stepForCustomSummaryStyleConfig'] = self.step_for_custom_summary_style_config.to_map()
        if self.topic_ids is not None:
            result['topicIds'] = self.topic_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('stepForCustomSummaryStyleConfig') is not None:
            temp_model = RunHotTopicSummaryRequestStepForCustomSummaryStyleConfig()
            self.step_for_custom_summary_style_config = temp_model.from_map(m['stepForCustomSummaryStyleConfig'])
        if m.get('topicIds') is not None:
            self.topic_ids = m.get('topicIds')
        return self


class RunHotTopicSummaryShrinkRequest(TeaModel):
    def __init__(
        self,
        hot_topic_version: str = None,
        step_for_custom_summary_style_config_shrink: str = None,
        topic_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.hot_topic_version = hot_topic_version
        # This parameter is required.
        self.step_for_custom_summary_style_config_shrink = step_for_custom_summary_style_config_shrink
        # This parameter is required.
        self.topic_ids_shrink = topic_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version
        if self.step_for_custom_summary_style_config_shrink is not None:
            result['stepForCustomSummaryStyleConfig'] = self.step_for_custom_summary_style_config_shrink
        if self.topic_ids_shrink is not None:
            result['topicIds'] = self.topic_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')
        if m.get('stepForCustomSummaryStyleConfig') is not None:
            self.step_for_custom_summary_style_config_shrink = m.get('stepForCustomSummaryStyleConfig')
        if m.get('topicIds') is not None:
            self.topic_ids_shrink = m.get('topicIds')
        return self


class RunHotTopicSummaryResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
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
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunHotTopicSummaryResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
        topic_id: str = None,
    ):
        self.text = text
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.topic_id is not None:
            result['topicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('topicId') is not None:
            self.topic_id = m.get('topicId')
        return self


class RunHotTopicSummaryResponseBodyPayloadUsage(TeaModel):
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


class RunHotTopicSummaryResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunHotTopicSummaryResponseBodyPayloadOutput = None,
        usage: RunHotTopicSummaryResponseBodyPayloadUsage = None,
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
            temp_model = RunHotTopicSummaryResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunHotTopicSummaryResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunHotTopicSummaryResponseBody(TeaModel):
    def __init__(
        self,
        header: RunHotTopicSummaryResponseBodyHeader = None,
        payload: RunHotTopicSummaryResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        # Id of the request
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
            temp_model = RunHotTopicSummaryResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunHotTopicSummaryResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RunHotTopicSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunHotTopicSummaryResponseBody = None,
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
            temp_model = RunHotTopicSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        custom_limitation: str = None,
        custom_prompt: str = None,
        input_example: str = None,
        model_id: str = None,
        output_example: str = None,
        source_material: str = None,
        writing_type: str = None,
    ):
        self.custom_limitation = custom_limitation
        self.custom_prompt = custom_prompt
        self.input_example = input_example
        self.model_id = model_id
        self.output_example = output_example
        self.source_material = source_material
        self.writing_type = writing_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_limitation is not None:
            result['customLimitation'] = self.custom_limitation
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt
        if self.input_example is not None:
            result['inputExample'] = self.input_example
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_example is not None:
            result['outputExample'] = self.output_example
        if self.source_material is not None:
            result['sourceMaterial'] = self.source_material
        if self.writing_type is not None:
            result['writingType'] = self.writing_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customLimitation') is not None:
            self.custom_limitation = m.get('customLimitation')
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')
        if m.get('inputExample') is not None:
            self.input_example = m.get('inputExample')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputExample') is not None:
            self.output_example = m.get('outputExample')
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


class RunNetworkContentAuditRequestTags(TeaModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_define_prompt is not None:
            result['tagDefinePrompt'] = self.tag_define_prompt
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('tagDefinePrompt')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        return self


class RunNetworkContentAuditRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags: List[RunNetworkContentAuditRequestTags] = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        # This parameter is required.
        self.content = content
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags = tags
        self.task_description = task_description

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.content is not None:
            result['content'] = self.content
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RunNetworkContentAuditRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        return self


class RunNetworkContentAuditShrinkRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags_shrink: str = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        # This parameter is required.
        self.content = content
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags_shrink = tags_shrink
        self.task_description = task_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.content is not None:
            result['content'] = self.content
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        return self


class RunNetworkContentAuditResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
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
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunNetworkContentAuditResponseBodyPayloadOutput(TeaModel):
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


class RunNetworkContentAuditResponseBodyPayloadUsage(TeaModel):
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


class RunNetworkContentAuditResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunNetworkContentAuditResponseBodyPayloadOutput = None,
        usage: RunNetworkContentAuditResponseBodyPayloadUsage = None,
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
            temp_model = RunNetworkContentAuditResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunNetworkContentAuditResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunNetworkContentAuditResponseBody(TeaModel):
    def __init__(
        self,
        header: RunNetworkContentAuditResponseBodyHeader = None,
        payload: RunNetworkContentAuditResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        # Id of the request
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
            temp_model = RunNetworkContentAuditResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunNetworkContentAuditResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RunNetworkContentAuditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunNetworkContentAuditResponseBody = None,
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
            temp_model = RunNetworkContentAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunScriptChatRequest(TeaModel):
    def __init__(
        self,
        prompt: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class RunScriptChatResponseBodyHeader(TeaModel):
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


class RunScriptChatResponseBodyPayloadOutput(TeaModel):
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


class RunScriptChatResponseBodyPayloadUsage(TeaModel):
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


class RunScriptChatResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunScriptChatResponseBodyPayloadOutput = None,
        usage: RunScriptChatResponseBodyPayloadUsage = None,
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
            temp_model = RunScriptChatResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunScriptChatResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunScriptChatResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunScriptChatResponseBodyHeader = None,
        payload: RunScriptChatResponseBodyPayload = None,
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
            temp_model = RunScriptChatResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunScriptChatResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunScriptChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunScriptChatResponseBody = None,
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
            temp_model = RunScriptChatResponseBody()
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


class RunScriptRefineRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class RunScriptRefineResponseBodyHeader(TeaModel):
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


class RunScriptRefineResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        content: List[Dict[str, str]] = None,
        outline: str = None,
        role: str = None,
        scene: str = None,
        summary: str = None,
        text: str = None,
    ):
        self.content = content
        self.outline = outline
        self.role = role
        self.scene = scene
        self.summary = summary
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.outline is not None:
            result['outline'] = self.outline
        if self.role is not None:
            result['role'] = self.role
        if self.scene is not None:
            result['scene'] = self.scene
        if self.summary is not None:
            result['summary'] = self.summary
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('outline') is not None:
            self.outline = m.get('outline')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunScriptRefineResponseBodyPayloadUsage(TeaModel):
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


class RunScriptRefineResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunScriptRefineResponseBodyPayloadOutput = None,
        usage: RunScriptRefineResponseBodyPayloadUsage = None,
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
            temp_model = RunScriptRefineResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunScriptRefineResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunScriptRefineResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunScriptRefineResponseBodyHeader = None,
        payload: RunScriptRefineResponseBodyPayload = None,
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
            temp_model = RunScriptRefineResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunScriptRefineResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        return self


class RunScriptRefineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunScriptRefineResponseBody = None,
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
            temp_model = RunScriptRefineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunStyleWritingRequest(TeaModel):
    def __init__(
        self,
        learning_samples: List[str] = None,
        process_stage: str = None,
        reference_materials: List[str] = None,
        style_feature: str = None,
        use_search: bool = None,
        writing_theme: str = None,
    ):
        self.learning_samples = learning_samples
        self.process_stage = process_stage
        self.reference_materials = reference_materials
        self.style_feature = style_feature
        self.use_search = use_search
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
        if self.process_stage is not None:
            result['processStage'] = self.process_stage
        if self.reference_materials is not None:
            result['referenceMaterials'] = self.reference_materials
        if self.style_feature is not None:
            result['styleFeature'] = self.style_feature
        if self.use_search is not None:
            result['useSearch'] = self.use_search
        if self.writing_theme is not None:
            result['writingTheme'] = self.writing_theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('learningSamples') is not None:
            self.learning_samples = m.get('learningSamples')
        if m.get('processStage') is not None:
            self.process_stage = m.get('processStage')
        if m.get('referenceMaterials') is not None:
            self.reference_materials = m.get('referenceMaterials')
        if m.get('styleFeature') is not None:
            self.style_feature = m.get('styleFeature')
        if m.get('useSearch') is not None:
            self.use_search = m.get('useSearch')
        if m.get('writingTheme') is not None:
            self.writing_theme = m.get('writingTheme')
        return self


class RunStyleWritingShrinkRequest(TeaModel):
    def __init__(
        self,
        learning_samples_shrink: str = None,
        process_stage: str = None,
        reference_materials_shrink: str = None,
        style_feature: str = None,
        use_search: bool = None,
        writing_theme: str = None,
    ):
        self.learning_samples_shrink = learning_samples_shrink
        self.process_stage = process_stage
        self.reference_materials_shrink = reference_materials_shrink
        self.style_feature = style_feature
        self.use_search = use_search
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
        if self.process_stage is not None:
            result['processStage'] = self.process_stage
        if self.reference_materials_shrink is not None:
            result['referenceMaterials'] = self.reference_materials_shrink
        if self.style_feature is not None:
            result['styleFeature'] = self.style_feature
        if self.use_search is not None:
            result['useSearch'] = self.use_search
        if self.writing_theme is not None:
            result['writingTheme'] = self.writing_theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('learningSamples') is not None:
            self.learning_samples_shrink = m.get('learningSamples')
        if m.get('processStage') is not None:
            self.process_stage = m.get('processStage')
        if m.get('referenceMaterials') is not None:
            self.reference_materials_shrink = m.get('referenceMaterials')
        if m.get('styleFeature') is not None:
            self.style_feature = m.get('styleFeature')
        if m.get('useSearch') is not None:
            self.use_search = m.get('useSearch')
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


class RunTagMiningAnalysisRequestTags(TeaModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_define_prompt is not None:
            result['tagDefinePrompt'] = self.tag_define_prompt
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('tagDefinePrompt')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        return self


class RunTagMiningAnalysisRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags: List[RunTagMiningAnalysisRequestTags] = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        # This parameter is required.
        self.content = content
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags = tags
        self.task_description = task_description

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.content is not None:
            result['content'] = self.content
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = RunTagMiningAnalysisRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        return self


class RunTagMiningAnalysisShrinkRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        content: str = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags_shrink: str = None,
        task_description: str = None,
    ):
        self.business_type = business_type
        # This parameter is required.
        self.content = content
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags_shrink = tags_shrink
        self.task_description = task_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.content is not None:
            result['content'] = self.content
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        return self


class RunTagMiningAnalysisResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
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
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class RunTagMiningAnalysisResponseBodyPayloadOutput(TeaModel):
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


class RunTagMiningAnalysisResponseBodyPayloadUsage(TeaModel):
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


class RunTagMiningAnalysisResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunTagMiningAnalysisResponseBodyPayloadOutput = None,
        usage: RunTagMiningAnalysisResponseBodyPayloadUsage = None,
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
            temp_model = RunTagMiningAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunTagMiningAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunTagMiningAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        header: RunTagMiningAnalysisResponseBodyHeader = None,
        payload: RunTagMiningAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        # Id of the request
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
            temp_model = RunTagMiningAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            temp_model = RunTagMiningAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m['payload'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RunTagMiningAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunTagMiningAnalysisResponseBody = None,
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
            temp_model = RunTagMiningAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunVideoAnalysisRequestFrameSampleMethod(TeaModel):
    def __init__(
        self,
        interval: float = None,
        method_name: str = None,
        pixel: int = None,
    ):
        self.interval = interval
        self.method_name = method_name
        self.pixel = pixel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.interval is not None:
            result['interval'] = self.interval
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.pixel is not None:
            result['pixel'] = self.pixel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('pixel') is not None:
            self.pixel = m.get('pixel')
        return self


class RunVideoAnalysisRequestTextProcessTasks(TeaModel):
    def __init__(
        self,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
    ):
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        return self


class RunVideoAnalysisRequestVideoRoles(TeaModel):
    def __init__(
        self,
        role_info: str = None,
        role_name: str = None,
        urls: List[str] = None,
    ):
        self.role_info = role_info
        self.role_name = role_name
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_info is not None:
            result['roleInfo'] = self.role_info
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.urls is not None:
            result['urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleInfo') is not None:
            self.role_info = m.get('roleInfo')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        return self


class RunVideoAnalysisRequest(TeaModel):
    def __init__(
        self,
        face_identity_similarity_min_score: float = None,
        frame_sample_method: RunVideoAnalysisRequestFrameSampleMethod = None,
        generate_options: List[str] = None,
        language: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        original_session_id: str = None,
        snapshot_interval: float = None,
        split_interval: int = None,
        task_id: str = None,
        text_process_tasks: List[RunVideoAnalysisRequestTextProcessTasks] = None,
        video_extra_info: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_roles: List[RunVideoAnalysisRequestVideoRoles] = None,
        video_shot_face_identity_count: int = None,
        video_url: str = None,
    ):
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.frame_sample_method = frame_sample_method
        self.generate_options = generate_options
        self.language = language
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.snapshot_interval = snapshot_interval
        self.split_interval = split_interval
        self.task_id = task_id
        self.text_process_tasks = text_process_tasks
        self.video_extra_info = video_extra_info
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_roles = video_roles
        self.video_shot_face_identity_count = video_shot_face_identity_count
        self.video_url = video_url

    def validate(self):
        if self.frame_sample_method:
            self.frame_sample_method.validate()
        if self.text_process_tasks:
            for k in self.text_process_tasks:
                if k:
                    k.validate()
        if self.video_roles:
            for k in self.video_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_identity_similarity_min_score is not None:
            result['faceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score
        if self.frame_sample_method is not None:
            result['frameSampleMethod'] = self.frame_sample_method.to_map()
        if self.generate_options is not None:
            result['generateOptions'] = self.generate_options
        if self.language is not None:
            result['language'] = self.language
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id
        if self.snapshot_interval is not None:
            result['snapshotInterval'] = self.snapshot_interval
        if self.split_interval is not None:
            result['splitInterval'] = self.split_interval
        if self.task_id is not None:
            result['taskId'] = self.task_id
        result['textProcessTasks'] = []
        if self.text_process_tasks is not None:
            for k in self.text_process_tasks:
                result['textProcessTasks'].append(k.to_map() if k else None)
        if self.video_extra_info is not None:
            result['videoExtraInfo'] = self.video_extra_info
        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template
        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id
        result['videoRoles'] = []
        if self.video_roles is not None:
            for k in self.video_roles:
                result['videoRoles'].append(k.to_map() if k else None)
        if self.video_shot_face_identity_count is not None:
            result['videoShotFaceIdentityCount'] = self.video_shot_face_identity_count
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('faceIdentitySimilarityMinScore')
        if m.get('frameSampleMethod') is not None:
            temp_model = RunVideoAnalysisRequestFrameSampleMethod()
            self.frame_sample_method = temp_model.from_map(m['frameSampleMethod'])
        if m.get('generateOptions') is not None:
            self.generate_options = m.get('generateOptions')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')
        if m.get('snapshotInterval') is not None:
            self.snapshot_interval = m.get('snapshotInterval')
        if m.get('splitInterval') is not None:
            self.split_interval = m.get('splitInterval')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        self.text_process_tasks = []
        if m.get('textProcessTasks') is not None:
            for k in m.get('textProcessTasks'):
                temp_model = RunVideoAnalysisRequestTextProcessTasks()
                self.text_process_tasks.append(temp_model.from_map(k))
        if m.get('videoExtraInfo') is not None:
            self.video_extra_info = m.get('videoExtraInfo')
        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')
        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')
        self.video_roles = []
        if m.get('videoRoles') is not None:
            for k in m.get('videoRoles'):
                temp_model = RunVideoAnalysisRequestVideoRoles()
                self.video_roles.append(temp_model.from_map(k))
        if m.get('videoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('videoShotFaceIdentityCount')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class RunVideoAnalysisShrinkRequest(TeaModel):
    def __init__(
        self,
        face_identity_similarity_min_score: float = None,
        frame_sample_method_shrink: str = None,
        generate_options_shrink: str = None,
        language: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        original_session_id: str = None,
        snapshot_interval: float = None,
        split_interval: int = None,
        task_id: str = None,
        text_process_tasks_shrink: str = None,
        video_extra_info: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_roles_shrink: str = None,
        video_shot_face_identity_count: int = None,
        video_url: str = None,
    ):
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.frame_sample_method_shrink = frame_sample_method_shrink
        self.generate_options_shrink = generate_options_shrink
        self.language = language
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.snapshot_interval = snapshot_interval
        self.split_interval = split_interval
        self.task_id = task_id
        self.text_process_tasks_shrink = text_process_tasks_shrink
        self.video_extra_info = video_extra_info
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_roles_shrink = video_roles_shrink
        self.video_shot_face_identity_count = video_shot_face_identity_count
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_identity_similarity_min_score is not None:
            result['faceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score
        if self.frame_sample_method_shrink is not None:
            result['frameSampleMethod'] = self.frame_sample_method_shrink
        if self.generate_options_shrink is not None:
            result['generateOptions'] = self.generate_options_shrink
        if self.language is not None:
            result['language'] = self.language
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id
        if self.snapshot_interval is not None:
            result['snapshotInterval'] = self.snapshot_interval
        if self.split_interval is not None:
            result['splitInterval'] = self.split_interval
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.text_process_tasks_shrink is not None:
            result['textProcessTasks'] = self.text_process_tasks_shrink
        if self.video_extra_info is not None:
            result['videoExtraInfo'] = self.video_extra_info
        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template
        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id
        if self.video_roles_shrink is not None:
            result['videoRoles'] = self.video_roles_shrink
        if self.video_shot_face_identity_count is not None:
            result['videoShotFaceIdentityCount'] = self.video_shot_face_identity_count
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('faceIdentitySimilarityMinScore')
        if m.get('frameSampleMethod') is not None:
            self.frame_sample_method_shrink = m.get('frameSampleMethod')
        if m.get('generateOptions') is not None:
            self.generate_options_shrink = m.get('generateOptions')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')
        if m.get('snapshotInterval') is not None:
            self.snapshot_interval = m.get('snapshotInterval')
        if m.get('splitInterval') is not None:
            self.split_interval = m.get('splitInterval')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('textProcessTasks') is not None:
            self.text_process_tasks_shrink = m.get('textProcessTasks')
        if m.get('videoExtraInfo') is not None:
            self.video_extra_info = m.get('videoExtraInfo')
        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')
        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')
        if m.get('videoRoles') is not None:
            self.video_roles_shrink = m.get('videoRoles')
        if m.get('videoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('videoShotFaceIdentityCount')
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
        model_id: str = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage = None,
        video_shot_analysis_results: List[RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults] = None,
    ):
        self.generate_finished = generate_finished
        self.model_id = model_id
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
        if self.model_id is not None:
            result['modelId'] = self.model_id
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
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
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
        index: int = None,
        model_id: str = None,
        model_reduce: bool = None,
        reason_text: str = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.index = index
        self.model_id = model_id
        self.model_reduce = model_reduce
        self.reason_text = reason_text
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
        if self.index is not None:
            result['index'] = self.index
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce
        if self.reason_text is not None:
            result['reasonText'] = self.reason_text
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')
        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultsUsage(TeaModel):
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


class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResults(TeaModel):
    def __init__(
        self,
        generate_finished: bool = None,
        index: int = None,
        model_id: str = None,
        reason_text: str = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultsUsage = None,
    ):
        self.generate_finished = generate_finished
        self.index = index
        self.model_id = model_id
        self.reason_text = reason_text
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
        if self.index is not None:
            result['index'] = self.index
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.reason_text is not None:
            result['reasonText'] = self.reason_text
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultsUsage()
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
        model_id: str = None,
        model_reduce: bool = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage = None,
        video_mind_mappings: List[RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings] = None,
    ):
        self.generate_finished = generate_finished
        self.model_id = model_id
        self.model_reduce = model_reduce
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
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce
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
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')
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


class RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShotsVideoSnapshots(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShots(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        end_time_format: str = None,
        start_time: int = None,
        start_time_format: str = None,
        video_snapshots: List[RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShotsVideoSnapshots] = None,
    ):
        self.end_time = end_time
        self.end_time_format = end_time_format
        self.start_time = start_time
        self.start_time_format = start_time_format
        self.video_snapshots = video_snapshots

    def validate(self):
        if self.video_snapshots:
            for k in self.video_snapshots:
                if k:
                    k.validate()

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
        result['videoSnapshots'] = []
        if self.video_snapshots is not None:
            for k in self.video_snapshots:
                result['videoSnapshots'].append(k.to_map() if k else None)
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
        self.video_snapshots = []
        if m.get('videoSnapshots') is not None:
            for k in m.get('videoSnapshots'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShotsVideoSnapshots()
                self.video_snapshots.append(temp_model.from_map(k))
        return self


class RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResult(TeaModel):
    def __init__(
        self,
        video_shots: List[RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShots] = None,
    ):
        self.video_shots = video_shots

    def validate(self):
        if self.video_shots:
            for k in self.video_shots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['videoShots'] = []
        if self.video_shots is not None:
            for k in self.video_shots:
                result['videoShots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_shots = []
        if m.get('videoShots') is not None:
            for k in m.get('videoShots'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShots()
                self.video_shots.append(temp_model.from_map(k))
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
        model_id: str = None,
        model_reduce: bool = None,
        text: str = None,
        usage: RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.model_id = model_id
        self.model_reduce = model_reduce
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
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce
        if self.text is not None:
            result['text'] = self.text
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class RunVideoAnalysisResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        result_json_file_url: str = None,
        video_analysis_result: RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult = None,
        video_caption_result: RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult = None,
        video_generate_result: RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult = None,
        video_generate_results: List[RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResults] = None,
        video_mind_mapping_generate_result: RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult = None,
        video_shot_snapshot_result: RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResult = None,
        video_title_generate_result: RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult = None,
    ):
        self.result_json_file_url = result_json_file_url
        self.video_analysis_result = video_analysis_result
        self.video_caption_result = video_caption_result
        self.video_generate_result = video_generate_result
        self.video_generate_results = video_generate_results
        self.video_mind_mapping_generate_result = video_mind_mapping_generate_result
        self.video_shot_snapshot_result = video_shot_snapshot_result
        self.video_title_generate_result = video_title_generate_result

    def validate(self):
        if self.video_analysis_result:
            self.video_analysis_result.validate()
        if self.video_caption_result:
            self.video_caption_result.validate()
        if self.video_generate_result:
            self.video_generate_result.validate()
        if self.video_generate_results:
            for k in self.video_generate_results:
                if k:
                    k.validate()
        if self.video_mind_mapping_generate_result:
            self.video_mind_mapping_generate_result.validate()
        if self.video_shot_snapshot_result:
            self.video_shot_snapshot_result.validate()
        if self.video_title_generate_result:
            self.video_title_generate_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_json_file_url is not None:
            result['resultJsonFileUrl'] = self.result_json_file_url
        if self.video_analysis_result is not None:
            result['videoAnalysisResult'] = self.video_analysis_result.to_map()
        if self.video_caption_result is not None:
            result['videoCaptionResult'] = self.video_caption_result.to_map()
        if self.video_generate_result is not None:
            result['videoGenerateResult'] = self.video_generate_result.to_map()
        result['videoGenerateResults'] = []
        if self.video_generate_results is not None:
            for k in self.video_generate_results:
                result['videoGenerateResults'].append(k.to_map() if k else None)
        if self.video_mind_mapping_generate_result is not None:
            result['videoMindMappingGenerateResult'] = self.video_mind_mapping_generate_result.to_map()
        if self.video_shot_snapshot_result is not None:
            result['videoShotSnapshotResult'] = self.video_shot_snapshot_result.to_map()
        if self.video_title_generate_result is not None:
            result['videoTitleGenerateResult'] = self.video_title_generate_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resultJsonFileUrl') is not None:
            self.result_json_file_url = m.get('resultJsonFileUrl')
        if m.get('videoAnalysisResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult()
            self.video_analysis_result = temp_model.from_map(m['videoAnalysisResult'])
        if m.get('videoCaptionResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult()
            self.video_caption_result = temp_model.from_map(m['videoCaptionResult'])
        if m.get('videoGenerateResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult()
            self.video_generate_result = temp_model.from_map(m['videoGenerateResult'])
        self.video_generate_results = []
        if m.get('videoGenerateResults') is not None:
            for k in m.get('videoGenerateResults'):
                temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResults()
                self.video_generate_results.append(temp_model.from_map(k))
        if m.get('videoMindMappingGenerateResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult()
            self.video_mind_mapping_generate_result = temp_model.from_map(m['videoMindMappingGenerateResult'])
        if m.get('videoShotSnapshotResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResult()
            self.video_shot_snapshot_result = temp_model.from_map(m['videoShotSnapshotResult'])
        if m.get('videoTitleGenerateResult') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult()
            self.video_title_generate_result = temp_model.from_map(m['videoTitleGenerateResult'])
        return self


class RunVideoAnalysisResponseBodyPayloadUsage(TeaModel):
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


class RunVideoAnalysisResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunVideoAnalysisResponseBodyPayloadOutput = None,
        usage: RunVideoAnalysisResponseBodyPayloadUsage = None,
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
            temp_model = RunVideoAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('usage') is not None:
            temp_model = RunVideoAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['usage'])
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


class SubmitTagMiningAnalysisTaskRequestTags(TeaModel):
    def __init__(
        self,
        tag_define_prompt: str = None,
        tag_name: str = None,
    ):
        self.tag_define_prompt = tag_define_prompt
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_define_prompt is not None:
            result['tagDefinePrompt'] = self.tag_define_prompt
        if self.tag_name is not None:
            result['tagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDefinePrompt') is not None:
            self.tag_define_prompt = m.get('tagDefinePrompt')
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')
        return self


class SubmitTagMiningAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        contents: List[str] = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags: List[SubmitTagMiningAnalysisTaskRequestTags] = None,
        task_description: str = None,
        url: str = None,
    ):
        self.business_type = business_type
        self.contents = contents
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags = tags
        self.task_description = task_description
        self.url = url

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.contents is not None:
            result['contents'] = self.contents
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('contents') is not None:
            self.contents = m.get('contents')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = SubmitTagMiningAnalysisTaskRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class SubmitTagMiningAnalysisTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        business_type: str = None,
        contents_shrink: str = None,
        extra_info: str = None,
        model_id: str = None,
        output_format: str = None,
        tags_shrink: str = None,
        task_description: str = None,
        url: str = None,
    ):
        self.business_type = business_type
        self.contents_shrink = contents_shrink
        self.extra_info = extra_info
        self.model_id = model_id
        self.output_format = output_format
        self.tags_shrink = tags_shrink
        self.task_description = task_description
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.contents_shrink is not None:
            result['contents'] = self.contents_shrink
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.task_description is not None:
            result['taskDescription'] = self.task_description
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('contents') is not None:
            self.contents_shrink = m.get('contents')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class SubmitTagMiningAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitTagMiningAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTagMiningAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = SubmitTagMiningAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SubmitTagMiningAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTagMiningAnalysisTaskResponseBody = None,
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
            temp_model = SubmitTagMiningAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitVideoAnalysisTaskRequestFrameSampleMethod(TeaModel):
    def __init__(
        self,
        interval: float = None,
        method_name: str = None,
        pixel: int = None,
    ):
        self.interval = interval
        self.method_name = method_name
        self.pixel = pixel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.interval is not None:
            result['interval'] = self.interval
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.pixel is not None:
            result['pixel'] = self.pixel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('pixel') is not None:
            self.pixel = m.get('pixel')
        return self


class SubmitVideoAnalysisTaskRequestTextProcessTasks(TeaModel):
    def __init__(
        self,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
    ):
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        return self


class SubmitVideoAnalysisTaskRequestVideoRoles(TeaModel):
    def __init__(
        self,
        role_info: str = None,
        role_name: str = None,
        urls: List[str] = None,
    ):
        self.role_info = role_info
        self.role_name = role_name
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_info is not None:
            result['roleInfo'] = self.role_info
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.urls is not None:
            result['urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleInfo') is not None:
            self.role_info = m.get('roleInfo')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('urls') is not None:
            self.urls = m.get('urls')
        return self


class SubmitVideoAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        face_identity_similarity_min_score: float = None,
        frame_sample_method: SubmitVideoAnalysisTaskRequestFrameSampleMethod = None,
        generate_options: List[str] = None,
        language: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        snapshot_interval: float = None,
        split_interval: int = None,
        text_process_tasks: List[SubmitVideoAnalysisTaskRequestTextProcessTasks] = None,
        video_extra_info: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_roles: List[SubmitVideoAnalysisTaskRequestVideoRoles] = None,
        video_shot_face_identity_count: int = None,
        video_url: str = None,
    ):
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.frame_sample_method = frame_sample_method
        self.generate_options = generate_options
        self.language = language
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.snapshot_interval = snapshot_interval
        self.split_interval = split_interval
        self.text_process_tasks = text_process_tasks
        self.video_extra_info = video_extra_info
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_roles = video_roles
        self.video_shot_face_identity_count = video_shot_face_identity_count
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        if self.frame_sample_method:
            self.frame_sample_method.validate()
        if self.text_process_tasks:
            for k in self.text_process_tasks:
                if k:
                    k.validate()
        if self.video_roles:
            for k in self.video_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_identity_similarity_min_score is not None:
            result['faceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score
        if self.frame_sample_method is not None:
            result['frameSampleMethod'] = self.frame_sample_method.to_map()
        if self.generate_options is not None:
            result['generateOptions'] = self.generate_options
        if self.language is not None:
            result['language'] = self.language
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.snapshot_interval is not None:
            result['snapshotInterval'] = self.snapshot_interval
        if self.split_interval is not None:
            result['splitInterval'] = self.split_interval
        result['textProcessTasks'] = []
        if self.text_process_tasks is not None:
            for k in self.text_process_tasks:
                result['textProcessTasks'].append(k.to_map() if k else None)
        if self.video_extra_info is not None:
            result['videoExtraInfo'] = self.video_extra_info
        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template
        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id
        result['videoRoles'] = []
        if self.video_roles is not None:
            for k in self.video_roles:
                result['videoRoles'].append(k.to_map() if k else None)
        if self.video_shot_face_identity_count is not None:
            result['videoShotFaceIdentityCount'] = self.video_shot_face_identity_count
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('faceIdentitySimilarityMinScore')
        if m.get('frameSampleMethod') is not None:
            temp_model = SubmitVideoAnalysisTaskRequestFrameSampleMethod()
            self.frame_sample_method = temp_model.from_map(m['frameSampleMethod'])
        if m.get('generateOptions') is not None:
            self.generate_options = m.get('generateOptions')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('snapshotInterval') is not None:
            self.snapshot_interval = m.get('snapshotInterval')
        if m.get('splitInterval') is not None:
            self.split_interval = m.get('splitInterval')
        self.text_process_tasks = []
        if m.get('textProcessTasks') is not None:
            for k in m.get('textProcessTasks'):
                temp_model = SubmitVideoAnalysisTaskRequestTextProcessTasks()
                self.text_process_tasks.append(temp_model.from_map(k))
        if m.get('videoExtraInfo') is not None:
            self.video_extra_info = m.get('videoExtraInfo')
        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')
        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')
        self.video_roles = []
        if m.get('videoRoles') is not None:
            for k in m.get('videoRoles'):
                temp_model = SubmitVideoAnalysisTaskRequestVideoRoles()
                self.video_roles.append(temp_model.from_map(k))
        if m.get('videoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('videoShotFaceIdentityCount')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class SubmitVideoAnalysisTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        face_identity_similarity_min_score: float = None,
        frame_sample_method_shrink: str = None,
        generate_options_shrink: str = None,
        language: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        snapshot_interval: float = None,
        split_interval: int = None,
        text_process_tasks_shrink: str = None,
        video_extra_info: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_roles_shrink: str = None,
        video_shot_face_identity_count: int = None,
        video_url: str = None,
    ):
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.frame_sample_method_shrink = frame_sample_method_shrink
        self.generate_options_shrink = generate_options_shrink
        self.language = language
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.snapshot_interval = snapshot_interval
        self.split_interval = split_interval
        self.text_process_tasks_shrink = text_process_tasks_shrink
        self.video_extra_info = video_extra_info
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_roles_shrink = video_roles_shrink
        self.video_shot_face_identity_count = video_shot_face_identity_count
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_identity_similarity_min_score is not None:
            result['faceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score
        if self.frame_sample_method_shrink is not None:
            result['frameSampleMethod'] = self.frame_sample_method_shrink
        if self.generate_options_shrink is not None:
            result['generateOptions'] = self.generate_options_shrink
        if self.language is not None:
            result['language'] = self.language
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template
        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id
        if self.model_id is not None:
            result['modelId'] = self.model_id
        if self.snapshot_interval is not None:
            result['snapshotInterval'] = self.snapshot_interval
        if self.split_interval is not None:
            result['splitInterval'] = self.split_interval
        if self.text_process_tasks_shrink is not None:
            result['textProcessTasks'] = self.text_process_tasks_shrink
        if self.video_extra_info is not None:
            result['videoExtraInfo'] = self.video_extra_info
        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template
        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id
        if self.video_roles_shrink is not None:
            result['videoRoles'] = self.video_roles_shrink
        if self.video_shot_face_identity_count is not None:
            result['videoShotFaceIdentityCount'] = self.video_shot_face_identity_count
        if self.video_url is not None:
            result['videoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('faceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('faceIdentitySimilarityMinScore')
        if m.get('frameSampleMethod') is not None:
            self.frame_sample_method_shrink = m.get('frameSampleMethod')
        if m.get('generateOptions') is not None:
            self.generate_options_shrink = m.get('generateOptions')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')
        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('snapshotInterval') is not None:
            self.snapshot_interval = m.get('snapshotInterval')
        if m.get('splitInterval') is not None:
            self.split_interval = m.get('splitInterval')
        if m.get('textProcessTasks') is not None:
            self.text_process_tasks_shrink = m.get('textProcessTasks')
        if m.get('videoExtraInfo') is not None:
            self.video_extra_info = m.get('videoExtraInfo')
        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')
        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')
        if m.get('videoRoles') is not None:
            self.video_roles_shrink = m.get('videoRoles')
        if m.get('videoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('videoShotFaceIdentityCount')
        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')
        return self


class SubmitVideoAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitVideoAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitVideoAnalysisTaskResponseBodyData = None,
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = SubmitVideoAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SubmitVideoAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitVideoAnalysisTaskResponseBody = None,
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
            temp_model = SubmitVideoAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVideoAnalysisConfigRequest(TeaModel):
    def __init__(
        self,
        async_concurrency: int = None,
    ):
        # This parameter is required.
        self.async_concurrency = async_concurrency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_concurrency is not None:
            result['asyncConcurrency'] = self.async_concurrency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncConcurrency') is not None:
            self.async_concurrency = m.get('asyncConcurrency')
        return self


class UpdateVideoAnalysisConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateVideoAnalysisConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVideoAnalysisConfigResponseBody = None,
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
            temp_model = UpdateVideoAnalysisConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


