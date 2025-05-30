# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, Dict, List


class PodcastTaskResultQueryRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class PodcastTaskResultQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        extra_result: Any = None,
        result_url: Any = None,
        script: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.extra_result = extra_result
        self.result_url = result_url
        self.script = script
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_result is not None:
            result['extraResult'] = self.extra_result
        if self.result_url is not None:
            result['resultUrl'] = self.result_url
        if self.script is not None:
            result['script'] = self.script
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extraResult') is not None:
            self.extra_result = m.get('extraResult')
        if m.get('resultUrl') is not None:
            self.result_url = m.get('resultUrl')
        if m.get('script') is not None:
            self.script = m.get('script')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        return self


class PodcastTaskResultQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PodcastTaskResultQueryResponseBodyData = None,
        http_status_code: str = None,
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
            temp_model = PodcastTaskResultQueryResponseBodyData()
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


class PodcastTaskResultQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PodcastTaskResultQueryResponseBody = None,
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
            temp_model = PodcastTaskResultQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PodcastTaskSubmitRequest(TeaModel):
    def __init__(
        self,
        counts: int = None,
        file_urls: List[str] = None,
        source_lang: str = None,
        text: str = None,
        topic: str = None,
        voices: List[str] = None,
        workspace_id: str = None,
    ):
        self.counts = counts
        self.file_urls = file_urls
        self.source_lang = source_lang
        self.text = text
        self.topic = topic
        self.voices = voices
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.counts is not None:
            result['counts'] = self.counts
        if self.file_urls is not None:
            result['fileUrls'] = self.file_urls
        if self.source_lang is not None:
            result['sourceLang'] = self.source_lang
        if self.text is not None:
            result['text'] = self.text
        if self.topic is not None:
            result['topic'] = self.topic
        if self.voices is not None:
            result['voices'] = self.voices
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('counts') is not None:
            self.counts = m.get('counts')
        if m.get('fileUrls') is not None:
            self.file_urls = m.get('fileUrls')
        if m.get('sourceLang') is not None:
            self.source_lang = m.get('sourceLang')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('voices') is not None:
            self.voices = m.get('voices')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class PodcastTaskSubmitShrinkRequest(TeaModel):
    def __init__(
        self,
        counts: int = None,
        file_urls_shrink: str = None,
        source_lang: str = None,
        text: str = None,
        topic: str = None,
        voices_shrink: str = None,
        workspace_id: str = None,
    ):
        self.counts = counts
        self.file_urls_shrink = file_urls_shrink
        self.source_lang = source_lang
        self.text = text
        self.topic = topic
        self.voices_shrink = voices_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.counts is not None:
            result['counts'] = self.counts
        if self.file_urls_shrink is not None:
            result['fileUrls'] = self.file_urls_shrink
        if self.source_lang is not None:
            result['sourceLang'] = self.source_lang
        if self.text is not None:
            result['text'] = self.text
        if self.topic is not None:
            result['topic'] = self.topic
        if self.voices_shrink is not None:
            result['voices'] = self.voices_shrink
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('counts') is not None:
            self.counts = m.get('counts')
        if m.get('fileUrls') is not None:
            self.file_urls_shrink = m.get('fileUrls')
        if m.get('sourceLang') is not None:
            self.source_lang = m.get('sourceLang')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        if m.get('voices') is not None:
            self.voices_shrink = m.get('voices')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class PodcastTaskSubmitResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_status: str = None,
    ):
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        return self


class PodcastTaskSubmitResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PodcastTaskSubmitResponseBodyData = None,
        http_status_code: str = None,
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
            temp_model = PodcastTaskSubmitResponseBodyData()
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


class PodcastTaskSubmitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PodcastTaskSubmitResponseBody = None,
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
            temp_model = PodcastTaskSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


