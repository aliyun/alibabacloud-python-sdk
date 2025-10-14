# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class BatchTranslateRequestExtConfig(TeaModel):
    def __init__(
        self,
        skip_csi_check: bool = None,
    ):
        self.skip_csi_check = skip_csi_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_csi_check is not None:
            result['skipCsiCheck'] = self.skip_csi_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipCsiCheck') is not None:
            self.skip_csi_check = m.get('skipCsiCheck')
        return self


class BatchTranslateRequestExtExamples(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class BatchTranslateRequestExtTerminologies(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class BatchTranslateRequestExtTextTransform(TeaModel):
    def __init__(
        self,
        to_lower: bool = None,
        to_title: bool = None,
        to_upper: bool = None,
    ):
        self.to_lower = to_lower
        self.to_title = to_title
        self.to_upper = to_upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to_lower is not None:
            result['toLower'] = self.to_lower
        if self.to_title is not None:
            result['toTitle'] = self.to_title
        if self.to_upper is not None:
            result['toUpper'] = self.to_upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toLower') is not None:
            self.to_lower = m.get('toLower')
        if m.get('toTitle') is not None:
            self.to_title = m.get('toTitle')
        if m.get('toUpper') is not None:
            self.to_upper = m.get('toUpper')
        return self


class BatchTranslateRequestExt(TeaModel):
    def __init__(
        self,
        config: BatchTranslateRequestExtConfig = None,
        domain_hint: str = None,
        examples: List[BatchTranslateRequestExtExamples] = None,
        sensitives: List[str] = None,
        terminologies: List[BatchTranslateRequestExtTerminologies] = None,
        text_transform: BatchTranslateRequestExtTextTransform = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.examples = examples
        self.sensitives = sensitives
        self.terminologies = terminologies
        self.text_transform = text_transform

    def validate(self):
        if self.config:
            self.config.validate()
        if self.examples:
            for k in self.examples:
                if k:
                    k.validate()
        if self.terminologies:
            for k in self.terminologies:
                if k:
                    k.validate()
        if self.text_transform:
            self.text_transform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint
        result['examples'] = []
        if self.examples is not None:
            for k in self.examples:
                result['examples'].append(k.to_map() if k else None)
        if self.sensitives is not None:
            result['sensitives'] = self.sensitives
        result['terminologies'] = []
        if self.terminologies is not None:
            for k in self.terminologies:
                result['terminologies'].append(k.to_map() if k else None)
        if self.text_transform is not None:
            result['textTransform'] = self.text_transform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = BatchTranslateRequestExtConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')
        self.examples = []
        if m.get('examples') is not None:
            for k in m.get('examples'):
                temp_model = BatchTranslateRequestExtExamples()
                self.examples.append(temp_model.from_map(k))
        if m.get('sensitives') is not None:
            self.sensitives = m.get('sensitives')
        self.terminologies = []
        if m.get('terminologies') is not None:
            for k in m.get('terminologies'):
                temp_model = BatchTranslateRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k))
        if m.get('textTransform') is not None:
            temp_model = BatchTranslateRequestExtTextTransform()
            self.text_transform = temp_model.from_map(m['textTransform'])
        return self


class BatchTranslateRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        ext: BatchTranslateRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        self.app_name = app_name
        self.ext = ext
        self.format = format
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('ext') is not None:
            temp_model = BatchTranslateRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class BatchTranslateShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text_shrink: str = None,
        workspace_id: str = None,
    ):
        self.app_name = app_name
        self.ext_shrink = ext_shrink
        self.format = format
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.text_shrink = text_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text_shrink is not None:
            result['text'] = self.text_shrink
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text_shrink = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class BatchTranslateResponseBodyDataTranslationListUsage(TeaModel):
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


class BatchTranslateResponseBodyDataTranslationList(TeaModel):
    def __init__(
        self,
        code: int = None,
        index: str = None,
        message: str = None,
        translation: str = None,
        usage: BatchTranslateResponseBodyDataTranslationListUsage = None,
    ):
        self.code = code
        self.index = index
        self.message = message
        self.translation = translation
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.index is not None:
            result['index'] = self.index
        if self.message is not None:
            result['message'] = self.message
        if self.translation is not None:
            result['translation'] = self.translation
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('translation') is not None:
            self.translation = m.get('translation')
        if m.get('usage') is not None:
            temp_model = BatchTranslateResponseBodyDataTranslationListUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class BatchTranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        translation_list: List[BatchTranslateResponseBodyDataTranslationList] = None,
    ):
        self.translation_list = translation_list

    def validate(self):
        if self.translation_list:
            for k in self.translation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['translationList'] = []
        if self.translation_list is not None:
            for k in self.translation_list:
                result['translationList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.translation_list = []
        if m.get('translationList') is not None:
            for k in m.get('translationList'):
                temp_model = BatchTranslateResponseBodyDataTranslationList()
                self.translation_list.append(temp_model.from_map(k))
        return self


class BatchTranslateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchTranslateResponseBodyData = None,
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
            temp_model = BatchTranslateResponseBodyData()
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


class BatchTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchTranslateResponseBody = None,
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
            temp_model = BatchTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocTranslateTaskRequest(TeaModel):
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


class GetDocTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        characters_count: int = None,
        page_count: int = None,
        status: str = None,
        task_id: str = None,
        translate_file_url: str = None,
    ):
        self.characters_count = characters_count
        self.page_count = page_count
        self.status = status
        self.task_id = task_id
        self.translate_file_url = translate_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.characters_count is not None:
            result['charactersCount'] = self.characters_count
        if self.page_count is not None:
            result['pageCount'] = self.page_count
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.translate_file_url is not None:
            result['translateFileUrl'] = self.translate_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('charactersCount') is not None:
            self.characters_count = m.get('charactersCount')
        if m.get('pageCount') is not None:
            self.page_count = m.get('pageCount')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('translateFileUrl') is not None:
            self.translate_file_url = m.get('translateFileUrl')
        return self


class GetDocTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDocTranslateTaskResponseBodyData = None,
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
            temp_model = GetDocTranslateTaskResponseBodyData()
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


class GetDocTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocTranslateTaskResponseBody = None,
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
            temp_model = GetDocTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHtmlTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        workspace_id: str = None,
    ):
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


class GetHtmlTranslateTaskResponseBodyDataUsage(TeaModel):
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


class GetHtmlTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        translation: str = None,
        usage: GetHtmlTranslateTaskResponseBodyDataUsage = None,
    ):
        self.translation = translation
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translation is not None:
            result['translation'] = self.translation
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('translation') is not None:
            self.translation = m.get('translation')
        if m.get('usage') is not None:
            temp_model = GetHtmlTranslateTaskResponseBodyDataUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetHtmlTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHtmlTranslateTaskResponseBodyData = None,
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
            temp_model = GetHtmlTranslateTaskResponseBodyData()
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


class GetHtmlTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHtmlTranslateTaskResponseBody = None,
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
            temp_model = GetHtmlTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageTranslateTaskRequest(TeaModel):
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


class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownLeft(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownRight(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpLeft(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpRight(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxes(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        direction: int = None,
        down_left: GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownLeft = None,
        down_right: GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownRight = None,
        table_cell_id: int = None,
        table_id: int = None,
        text: str = None,
        translation: Dict[str, Any] = None,
        up_left: GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpLeft = None,
        up_right: GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpRight = None,
    ):
        self.confidence = confidence
        self.direction = direction
        self.down_left = down_left
        self.down_right = down_right
        self.table_cell_id = table_cell_id
        self.table_id = table_id
        self.text = text
        self.translation = translation
        self.up_left = up_left
        self.up_right = up_right

    def validate(self):
        if self.down_left:
            self.down_left.validate()
        if self.down_right:
            self.down_right.validate()
        if self.up_left:
            self.up_left.validate()
        if self.up_right:
            self.up_right.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence
        if self.direction is not None:
            result['direction'] = self.direction
        if self.down_left is not None:
            result['downLeft'] = self.down_left.to_map()
        if self.down_right is not None:
            result['downRight'] = self.down_right.to_map()
        if self.table_cell_id is not None:
            result['tableCellId'] = self.table_cell_id
        if self.table_id is not None:
            result['tableId'] = self.table_id
        if self.text is not None:
            result['text'] = self.text
        if self.translation is not None:
            result['translation'] = self.translation
        if self.up_left is not None:
            result['upLeft'] = self.up_left.to_map()
        if self.up_right is not None:
            result['upRight'] = self.up_right.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('downLeft') is not None:
            temp_model = GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownLeft()
            self.down_left = temp_model.from_map(m['downLeft'])
        if m.get('downRight') is not None:
            temp_model = GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownRight()
            self.down_right = temp_model.from_map(m['downRight'])
        if m.get('tableCellId') is not None:
            self.table_cell_id = m.get('tableCellId')
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('translation') is not None:
            self.translation = m.get('translation')
        if m.get('upLeft') is not None:
            temp_model = GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpLeft()
            self.up_left = temp_model.from_map(m['upLeft'])
        if m.get('upRight') is not None:
            temp_model = GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpRight()
            self.up_right = temp_model.from_map(m['upRight'])
        return self


class GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfosPos(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['x'] = self.x
        if self.y is not None:
            result['y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')
        if m.get('y') is not None:
            self.y = m.get('y')
        return self


class GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfos(TeaModel):
    def __init__(
        self,
        pos: List[GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfosPos] = None,
        table_cell_id: int = None,
        text: str = None,
        xec: int = None,
        xsc: int = None,
        yec: int = None,
        ysc: int = None,
    ):
        self.pos = pos
        self.table_cell_id = table_cell_id
        self.text = text
        self.xec = xec
        self.xsc = xsc
        self.yec = yec
        self.ysc = ysc

    def validate(self):
        if self.pos:
            for k in self.pos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['pos'] = []
        if self.pos is not None:
            for k in self.pos:
                result['pos'].append(k.to_map() if k else None)
        if self.table_cell_id is not None:
            result['tableCellId'] = self.table_cell_id
        if self.text is not None:
            result['text'] = self.text
        if self.xec is not None:
            result['xec'] = self.xec
        if self.xsc is not None:
            result['xsc'] = self.xsc
        if self.yec is not None:
            result['yec'] = self.yec
        if self.ysc is not None:
            result['ysc'] = self.ysc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pos = []
        if m.get('pos') is not None:
            for k in m.get('pos'):
                temp_model = GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfosPos()
                self.pos.append(temp_model.from_map(k))
        if m.get('tableCellId') is not None:
            self.table_cell_id = m.get('tableCellId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('xec') is not None:
            self.xec = m.get('xec')
        if m.get('xsc') is not None:
            self.xsc = m.get('xsc')
        if m.get('yec') is not None:
            self.yec = m.get('yec')
        if m.get('ysc') is not None:
            self.ysc = m.get('ysc')
        return self


class GetImageTranslateTaskResponseBodyDataTranslationTableInfos(TeaModel):
    def __init__(
        self,
        cell_infos: List[GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfos] = None,
        table_id: int = None,
        x_cell_size: int = None,
        y_cell_size: int = None,
    ):
        self.cell_infos = cell_infos
        self.table_id = table_id
        self.x_cell_size = x_cell_size
        self.y_cell_size = y_cell_size

    def validate(self):
        if self.cell_infos:
            for k in self.cell_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cellInfos'] = []
        if self.cell_infos is not None:
            for k in self.cell_infos:
                result['cellInfos'].append(k.to_map() if k else None)
        if self.table_id is not None:
            result['tableId'] = self.table_id
        if self.x_cell_size is not None:
            result['xCellSize'] = self.x_cell_size
        if self.y_cell_size is not None:
            result['yCellSize'] = self.y_cell_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cell_infos = []
        if m.get('cellInfos') is not None:
            for k in m.get('cellInfos'):
                temp_model = GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfos()
                self.cell_infos.append(temp_model.from_map(k))
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        if m.get('xCellSize') is not None:
            self.x_cell_size = m.get('xCellSize')
        if m.get('yCellSize') is not None:
            self.y_cell_size = m.get('yCellSize')
        return self


class GetImageTranslateTaskResponseBodyDataTranslation(TeaModel):
    def __init__(
        self,
        angle: int = None,
        bounding_boxes: List[GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxes] = None,
        boxes_count: int = None,
        height: int = None,
        org_height: int = None,
        org_width: int = None,
        table_infos: List[GetImageTranslateTaskResponseBodyDataTranslationTableInfos] = None,
        width: int = None,
    ):
        self.angle = angle
        self.bounding_boxes = bounding_boxes
        self.boxes_count = boxes_count
        self.height = height
        self.org_height = org_height
        self.org_width = org_width
        self.table_infos = table_infos
        self.width = width

    def validate(self):
        if self.bounding_boxes:
            for k in self.bounding_boxes:
                if k:
                    k.validate()
        if self.table_infos:
            for k in self.table_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['angle'] = self.angle
        result['boundingBoxes'] = []
        if self.bounding_boxes is not None:
            for k in self.bounding_boxes:
                result['boundingBoxes'].append(k.to_map() if k else None)
        if self.boxes_count is not None:
            result['boxesCount'] = self.boxes_count
        if self.height is not None:
            result['height'] = self.height
        if self.org_height is not None:
            result['orgHeight'] = self.org_height
        if self.org_width is not None:
            result['orgWidth'] = self.org_width
        result['tableInfos'] = []
        if self.table_infos is not None:
            for k in self.table_infos:
                result['tableInfos'].append(k.to_map() if k else None)
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('angle') is not None:
            self.angle = m.get('angle')
        self.bounding_boxes = []
        if m.get('boundingBoxes') is not None:
            for k in m.get('boundingBoxes'):
                temp_model = GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxes()
                self.bounding_boxes.append(temp_model.from_map(k))
        if m.get('boxesCount') is not None:
            self.boxes_count = m.get('boxesCount')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('orgHeight') is not None:
            self.org_height = m.get('orgHeight')
        if m.get('orgWidth') is not None:
            self.org_width = m.get('orgWidth')
        self.table_infos = []
        if m.get('tableInfos') is not None:
            for k in m.get('tableInfos'):
                temp_model = GetImageTranslateTaskResponseBodyDataTranslationTableInfos()
                self.table_infos.append(temp_model.from_map(k))
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class GetImageTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        trace_id: str = None,
        translation: GetImageTranslateTaskResponseBodyDataTranslation = None,
    ):
        self.trace_id = trace_id
        self.translation = translation

    def validate(self):
        if self.translation:
            self.translation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        if self.translation is not None:
            result['translation'] = self.translation.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        if m.get('translation') is not None:
            temp_model = GetImageTranslateTaskResponseBodyDataTranslation()
            self.translation = temp_model.from_map(m['translation'])
        return self


class GetImageTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetImageTranslateTaskResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.synchro is not None:
            result['synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetImageTranslateTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('synchro') is not None:
            self.synchro = m.get('synchro')
        return self


class GetImageTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageTranslateTaskResponseBody = None,
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
            temp_model = GetImageTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLongTextTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        workspace_id: str = None,
    ):
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


class GetLongTextTranslateTaskResponseBodyDataUsage(TeaModel):
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


class GetLongTextTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        translation: str = None,
        usage: GetLongTextTranslateTaskResponseBodyDataUsage = None,
    ):
        self.translation = translation
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translation is not None:
            result['translation'] = self.translation
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('translation') is not None:
            self.translation = m.get('translation')
        if m.get('usage') is not None:
            temp_model = GetLongTextTranslateTaskResponseBodyDataUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetLongTextTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetLongTextTranslateTaskResponseBodyData = None,
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
            temp_model = GetLongTextTranslateTaskResponseBodyData()
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


class GetLongTextTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLongTextTranslateTaskResponseBody = None,
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
            temp_model = GetLongTextTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocTranslateTaskRequestExtConfig(TeaModel):
    def __init__(
        self,
        skip_img_trans: bool = None,
    ):
        self.skip_img_trans = skip_img_trans

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_img_trans is not None:
            result['skipImgTrans'] = self.skip_img_trans
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipImgTrans') is not None:
            self.skip_img_trans = m.get('skipImgTrans')
        return self


class SubmitDocTranslateTaskRequestExtTerminologies(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitDocTranslateTaskRequestExt(TeaModel):
    def __init__(
        self,
        config: SubmitDocTranslateTaskRequestExtConfig = None,
        domain_hint: str = None,
        terminologies: List[SubmitDocTranslateTaskRequestExtTerminologies] = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.terminologies = terminologies

    def validate(self):
        if self.config:
            self.config.validate()
        if self.terminologies:
            for k in self.terminologies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint
        result['terminologies'] = []
        if self.terminologies is not None:
            for k in self.terminologies:
                result['terminologies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = SubmitDocTranslateTaskRequestExtConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')
        self.terminologies = []
        if m.get('terminologies') is not None:
            for k in m.get('terminologies'):
                temp_model = SubmitDocTranslateTaskRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k))
        return self


class SubmitDocTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        ext: SubmitDocTranslateTaskRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        self.format = format
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        self.target_language = target_language
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            temp_model = SubmitDocTranslateTaskRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitDocTranslateTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext_shrink = ext_shrink
        self.format = format
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        self.target_language = target_language
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitDocTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitDocTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitDocTranslateTaskResponseBodyData = None,
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
            temp_model = SubmitDocTranslateTaskResponseBodyData()
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


class SubmitDocTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocTranslateTaskResponseBody = None,
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
            temp_model = SubmitDocTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitHtmlTranslateTaskRequestExtConfig(TeaModel):
    def __init__(
        self,
        skip_csi_check: bool = None,
    ):
        self.skip_csi_check = skip_csi_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_csi_check is not None:
            result['skipCsiCheck'] = self.skip_csi_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipCsiCheck') is not None:
            self.skip_csi_check = m.get('skipCsiCheck')
        return self


class SubmitHtmlTranslateTaskRequestExtExamples(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitHtmlTranslateTaskRequestExtTerminologies(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitHtmlTranslateTaskRequestExtTextTransform(TeaModel):
    def __init__(
        self,
        to_lower: bool = None,
        to_title: bool = None,
        to_upper: bool = None,
    ):
        self.to_lower = to_lower
        self.to_title = to_title
        self.to_upper = to_upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to_lower is not None:
            result['toLower'] = self.to_lower
        if self.to_title is not None:
            result['toTitle'] = self.to_title
        if self.to_upper is not None:
            result['toUpper'] = self.to_upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toLower') is not None:
            self.to_lower = m.get('toLower')
        if m.get('toTitle') is not None:
            self.to_title = m.get('toTitle')
        if m.get('toUpper') is not None:
            self.to_upper = m.get('toUpper')
        return self


class SubmitHtmlTranslateTaskRequestExt(TeaModel):
    def __init__(
        self,
        config: SubmitHtmlTranslateTaskRequestExtConfig = None,
        domain_hint: str = None,
        examples: List[SubmitHtmlTranslateTaskRequestExtExamples] = None,
        sensitives: List[str] = None,
        terminologies: List[SubmitHtmlTranslateTaskRequestExtTerminologies] = None,
        text_transform: SubmitHtmlTranslateTaskRequestExtTextTransform = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.examples = examples
        self.sensitives = sensitives
        self.terminologies = terminologies
        self.text_transform = text_transform

    def validate(self):
        if self.config:
            self.config.validate()
        if self.examples:
            for k in self.examples:
                if k:
                    k.validate()
        if self.terminologies:
            for k in self.terminologies:
                if k:
                    k.validate()
        if self.text_transform:
            self.text_transform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint
        result['examples'] = []
        if self.examples is not None:
            for k in self.examples:
                result['examples'].append(k.to_map() if k else None)
        if self.sensitives is not None:
            result['sensitives'] = self.sensitives
        result['terminologies'] = []
        if self.terminologies is not None:
            for k in self.terminologies:
                result['terminologies'].append(k.to_map() if k else None)
        if self.text_transform is not None:
            result['textTransform'] = self.text_transform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = SubmitHtmlTranslateTaskRequestExtConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')
        self.examples = []
        if m.get('examples') is not None:
            for k in m.get('examples'):
                temp_model = SubmitHtmlTranslateTaskRequestExtExamples()
                self.examples.append(temp_model.from_map(k))
        if m.get('sensitives') is not None:
            self.sensitives = m.get('sensitives')
        self.terminologies = []
        if m.get('terminologies') is not None:
            for k in m.get('terminologies'):
                temp_model = SubmitHtmlTranslateTaskRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k))
        if m.get('textTransform') is not None:
            temp_model = SubmitHtmlTranslateTaskRequestExtTextTransform()
            self.text_transform = temp_model.from_map(m['textTransform'])
        return self


class SubmitHtmlTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        ext: SubmitHtmlTranslateTaskRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        self.format = format
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            temp_model = SubmitHtmlTranslateTaskRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitHtmlTranslateTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext_shrink = ext_shrink
        self.format = format
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitHtmlTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitHtmlTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitHtmlTranslateTaskResponseBodyData = None,
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
            temp_model = SubmitHtmlTranslateTaskResponseBodyData()
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


class SubmitHtmlTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitHtmlTranslateTaskResponseBody = None,
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
            temp_model = SubmitHtmlTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImageTranslateTaskRequestExtExamples(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitImageTranslateTaskRequestExtTerminologies(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitImageTranslateTaskRequestExtTextTransform(TeaModel):
    def __init__(
        self,
        to_lower: bool = None,
        to_title: bool = None,
        to_upper: bool = None,
    ):
        self.to_lower = to_lower
        self.to_title = to_title
        self.to_upper = to_upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to_lower is not None:
            result['toLower'] = self.to_lower
        if self.to_title is not None:
            result['toTitle'] = self.to_title
        if self.to_upper is not None:
            result['toUpper'] = self.to_upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toLower') is not None:
            self.to_lower = m.get('toLower')
        if m.get('toTitle') is not None:
            self.to_title = m.get('toTitle')
        if m.get('toUpper') is not None:
            self.to_upper = m.get('toUpper')
        return self


class SubmitImageTranslateTaskRequestExt(TeaModel):
    def __init__(
        self,
        domain_hint: str = None,
        examples: List[SubmitImageTranslateTaskRequestExtExamples] = None,
        sensitives: List[str] = None,
        terminologies: List[SubmitImageTranslateTaskRequestExtTerminologies] = None,
        text_transform: SubmitImageTranslateTaskRequestExtTextTransform = None,
    ):
        self.domain_hint = domain_hint
        self.examples = examples
        self.sensitives = sensitives
        self.terminologies = terminologies
        self.text_transform = text_transform

    def validate(self):
        if self.examples:
            for k in self.examples:
                if k:
                    k.validate()
        if self.terminologies:
            for k in self.terminologies:
                if k:
                    k.validate()
        if self.text_transform:
            self.text_transform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint
        result['examples'] = []
        if self.examples is not None:
            for k in self.examples:
                result['examples'].append(k.to_map() if k else None)
        if self.sensitives is not None:
            result['sensitives'] = self.sensitives
        result['terminologies'] = []
        if self.terminologies is not None:
            for k in self.terminologies:
                result['terminologies'].append(k.to_map() if k else None)
        if self.text_transform is not None:
            result['textTransform'] = self.text_transform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')
        self.examples = []
        if m.get('examples') is not None:
            for k in m.get('examples'):
                temp_model = SubmitImageTranslateTaskRequestExtExamples()
                self.examples.append(temp_model.from_map(k))
        if m.get('sensitives') is not None:
            self.sensitives = m.get('sensitives')
        self.terminologies = []
        if m.get('terminologies') is not None:
            for k in m.get('terminologies'):
                temp_model = SubmitImageTranslateTaskRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k))
        if m.get('textTransform') is not None:
            temp_model = SubmitImageTranslateTaskRequestExtTextTransform()
            self.text_transform = temp_model.from_map(m['textTransform'])
        return self


class SubmitImageTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        ext: SubmitImageTranslateTaskRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: List[str] = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        self.format = format
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            temp_model = SubmitImageTranslateTaskRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitImageTranslateTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language_shrink: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext_shrink = ext_shrink
        self.format = format
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language_shrink = target_language_shrink
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language_shrink is not None:
            result['targetLanguage'] = self.target_language_shrink
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language_shrink = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitImageTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitImageTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitImageTranslateTaskResponseBodyData = None,
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
            temp_model = SubmitImageTranslateTaskResponseBodyData()
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


class SubmitImageTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitImageTranslateTaskResponseBody = None,
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
            temp_model = SubmitImageTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitLongTextTranslateTaskRequestExtConfig(TeaModel):
    def __init__(
        self,
        skip_csi_check: bool = None,
    ):
        self.skip_csi_check = skip_csi_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_csi_check is not None:
            result['skipCsiCheck'] = self.skip_csi_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipCsiCheck') is not None:
            self.skip_csi_check = m.get('skipCsiCheck')
        return self


class SubmitLongTextTranslateTaskRequestExtExamples(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitLongTextTranslateTaskRequestExtTerminologies(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class SubmitLongTextTranslateTaskRequestExtTextTransform(TeaModel):
    def __init__(
        self,
        to_lower: bool = None,
        to_title: bool = None,
        to_upper: bool = None,
    ):
        self.to_lower = to_lower
        self.to_title = to_title
        self.to_upper = to_upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to_lower is not None:
            result['toLower'] = self.to_lower
        if self.to_title is not None:
            result['toTitle'] = self.to_title
        if self.to_upper is not None:
            result['toUpper'] = self.to_upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toLower') is not None:
            self.to_lower = m.get('toLower')
        if m.get('toTitle') is not None:
            self.to_title = m.get('toTitle')
        if m.get('toUpper') is not None:
            self.to_upper = m.get('toUpper')
        return self


class SubmitLongTextTranslateTaskRequestExt(TeaModel):
    def __init__(
        self,
        config: SubmitLongTextTranslateTaskRequestExtConfig = None,
        domain_hint: str = None,
        examples: List[SubmitLongTextTranslateTaskRequestExtExamples] = None,
        sensitives: List[str] = None,
        terminologies: List[SubmitLongTextTranslateTaskRequestExtTerminologies] = None,
        text_transform: SubmitLongTextTranslateTaskRequestExtTextTransform = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.examples = examples
        self.sensitives = sensitives
        self.terminologies = terminologies
        self.text_transform = text_transform

    def validate(self):
        if self.config:
            self.config.validate()
        if self.examples:
            for k in self.examples:
                if k:
                    k.validate()
        if self.terminologies:
            for k in self.terminologies:
                if k:
                    k.validate()
        if self.text_transform:
            self.text_transform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint
        result['examples'] = []
        if self.examples is not None:
            for k in self.examples:
                result['examples'].append(k.to_map() if k else None)
        if self.sensitives is not None:
            result['sensitives'] = self.sensitives
        result['terminologies'] = []
        if self.terminologies is not None:
            for k in self.terminologies:
                result['terminologies'].append(k.to_map() if k else None)
        if self.text_transform is not None:
            result['textTransform'] = self.text_transform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = SubmitLongTextTranslateTaskRequestExtConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')
        self.examples = []
        if m.get('examples') is not None:
            for k in m.get('examples'):
                temp_model = SubmitLongTextTranslateTaskRequestExtExamples()
                self.examples.append(temp_model.from_map(k))
        if m.get('sensitives') is not None:
            self.sensitives = m.get('sensitives')
        self.terminologies = []
        if m.get('terminologies') is not None:
            for k in m.get('terminologies'):
                temp_model = SubmitLongTextTranslateTaskRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k))
        if m.get('textTransform') is not None:
            temp_model = SubmitLongTextTranslateTaskRequestExtTextTransform()
            self.text_transform = temp_model.from_map(m['textTransform'])
        return self


class SubmitLongTextTranslateTaskRequest(TeaModel):
    def __init__(
        self,
        ext: SubmitLongTextTranslateTaskRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        self.format = format
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            temp_model = SubmitLongTextTranslateTaskRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitLongTextTranslateTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext_shrink = ext_shrink
        self.format = format
        self.scene = scene
        self.source_language = source_language
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SubmitLongTextTranslateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class SubmitLongTextTranslateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitLongTextTranslateTaskResponseBodyData = None,
        http_status_code: str = None,
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
            temp_model = SubmitLongTextTranslateTaskResponseBodyData()
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


class SubmitLongTextTranslateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitLongTextTranslateTaskResponseBody = None,
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
            temp_model = SubmitLongTextTranslateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TermEditRequestExtTerms(TeaModel):
    def __init__(
        self,
        src: str = None,
        term_id: str = None,
        tgt: str = None,
    ):
        # This parameter is required.
        self.src = src
        self.term_id = term_id
        # This parameter is required.
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.term_id is not None:
            result['termId'] = self.term_id
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('termId') is not None:
            self.term_id = m.get('termId')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class TermEditRequestExt(TeaModel):
    def __init__(
        self,
        terms: List[TermEditRequestExtTerms] = None,
    ):
        # This parameter is required.
        self.terms = terms

    def validate(self):
        if self.terms:
            for k in self.terms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['terms'] = []
        if self.terms is not None:
            for k in self.terms:
                result['terms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terms = []
        if m.get('terms') is not None:
            for k in m.get('terms'):
                temp_model = TermEditRequestExtTerms()
                self.terms.append(temp_model.from_map(k))
        return self


class TermEditRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        ext: TermEditRequestExt = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.ext = ext
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('ext') is not None:
            temp_model = TermEditRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class TermEditShrinkRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        ext_shrink: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.ext_shrink = ext_shrink
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class TermEditResponseBodyDataTerms(TeaModel):
    def __init__(
        self,
        src: str = None,
        term_id: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.term_id = term_id
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.term_id is not None:
            result['termId'] = self.term_id
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('termId') is not None:
            self.term_id = m.get('termId')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class TermEditResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_count: int = None,
        terms: List[TermEditResponseBodyDataTerms] = None,
    ):
        self.fail_count = fail_count
        self.terms = terms

    def validate(self):
        if self.terms:
            for k in self.terms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_count is not None:
            result['failCount'] = self.fail_count
        result['terms'] = []
        if self.terms is not None:
            for k in self.terms:
                result['terms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')
        self.terms = []
        if m.get('terms') is not None:
            for k in m.get('terms'):
                temp_model = TermEditResponseBodyDataTerms()
                self.terms.append(temp_model.from_map(k))
        return self


class TermEditResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TermEditResponseBodyData = None,
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
            temp_model = TermEditResponseBodyData()
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


class TermEditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TermEditResponseBody = None,
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
            temp_model = TermEditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TermQueryRequest(TeaModel):
    def __init__(
        self,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class TermQueryResponseBodyDataTerms(TeaModel):
    def __init__(
        self,
        src: str = None,
        term_id: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.term_id = term_id
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.term_id is not None:
            result['termId'] = self.term_id
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('termId') is not None:
            self.term_id = m.get('termId')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class TermQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_count: int = None,
        terms: List[TermQueryResponseBodyDataTerms] = None,
    ):
        self.fail_count = fail_count
        self.terms = terms

    def validate(self):
        if self.terms:
            for k in self.terms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_count is not None:
            result['failCount'] = self.fail_count
        result['terms'] = []
        if self.terms is not None:
            for k in self.terms:
                result['terms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')
        self.terms = []
        if m.get('terms') is not None:
            for k in m.get('terms'):
                temp_model = TermQueryResponseBodyDataTerms()
                self.terms.append(temp_model.from_map(k))
        return self


class TermQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TermQueryResponseBodyData = None,
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
            temp_model = TermQueryResponseBodyData()
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


class TermQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TermQueryResponseBody = None,
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
            temp_model = TermQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TextTranslateRequestExtConfig(TeaModel):
    def __init__(
        self,
        skip_csi_check: bool = None,
    ):
        self.skip_csi_check = skip_csi_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip_csi_check is not None:
            result['skipCsiCheck'] = self.skip_csi_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('skipCsiCheck') is not None:
            self.skip_csi_check = m.get('skipCsiCheck')
        return self


class TextTranslateRequestExtExamples(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class TextTranslateRequestExtTerminologies(TeaModel):
    def __init__(
        self,
        src: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src is not None:
            result['src'] = self.src
        if self.tgt is not None:
            result['tgt'] = self.tgt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')
        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')
        return self


class TextTranslateRequestExtTextTransform(TeaModel):
    def __init__(
        self,
        to_lower: bool = None,
        to_title: bool = None,
        to_upper: bool = None,
    ):
        self.to_lower = to_lower
        self.to_title = to_title
        self.to_upper = to_upper

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to_lower is not None:
            result['toLower'] = self.to_lower
        if self.to_title is not None:
            result['toTitle'] = self.to_title
        if self.to_upper is not None:
            result['toUpper'] = self.to_upper
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('toLower') is not None:
            self.to_lower = m.get('toLower')
        if m.get('toTitle') is not None:
            self.to_title = m.get('toTitle')
        if m.get('toUpper') is not None:
            self.to_upper = m.get('toUpper')
        return self


class TextTranslateRequestExt(TeaModel):
    def __init__(
        self,
        config: TextTranslateRequestExtConfig = None,
        domain_hint: str = None,
        examples: List[TextTranslateRequestExtExamples] = None,
        sensitives: List[str] = None,
        terminologies: List[TextTranslateRequestExtTerminologies] = None,
        text_transform: TextTranslateRequestExtTextTransform = None,
    ):
        self.config = config
        self.domain_hint = domain_hint
        self.examples = examples
        self.sensitives = sensitives
        self.terminologies = terminologies
        self.text_transform = text_transform

    def validate(self):
        if self.config:
            self.config.validate()
        if self.examples:
            for k in self.examples:
                if k:
                    k.validate()
        if self.terminologies:
            for k in self.terminologies:
                if k:
                    k.validate()
        if self.text_transform:
            self.text_transform.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.domain_hint is not None:
            result['domainHint'] = self.domain_hint
        result['examples'] = []
        if self.examples is not None:
            for k in self.examples:
                result['examples'].append(k.to_map() if k else None)
        if self.sensitives is not None:
            result['sensitives'] = self.sensitives
        result['terminologies'] = []
        if self.terminologies is not None:
            for k in self.terminologies:
                result['terminologies'].append(k.to_map() if k else None)
        if self.text_transform is not None:
            result['textTransform'] = self.text_transform.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = TextTranslateRequestExtConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('domainHint') is not None:
            self.domain_hint = m.get('domainHint')
        self.examples = []
        if m.get('examples') is not None:
            for k in m.get('examples'):
                temp_model = TextTranslateRequestExtExamples()
                self.examples.append(temp_model.from_map(k))
        if m.get('sensitives') is not None:
            self.sensitives = m.get('sensitives')
        self.terminologies = []
        if m.get('terminologies') is not None:
            for k in m.get('terminologies'):
                temp_model = TextTranslateRequestExtTerminologies()
                self.terminologies.append(temp_model.from_map(k))
        if m.get('textTransform') is not None:
            temp_model = TextTranslateRequestExtTextTransform()
            self.text_transform = temp_model.from_map(m['textTransform'])
        return self


class TextTranslateRequest(TeaModel):
    def __init__(
        self,
        ext: TextTranslateRequestExt = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext = ext
        self.format = format
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.ext:
            self.ext.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext is not None:
            result['ext'] = self.ext.to_map()
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            temp_model = TextTranslateRequestExt()
            self.ext = temp_model.from_map(m['ext'])
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class TextTranslateShrinkRequest(TeaModel):
    def __init__(
        self,
        ext_shrink: str = None,
        format: str = None,
        scene: str = None,
        source_language: str = None,
        target_language: str = None,
        text: str = None,
        workspace_id: str = None,
    ):
        self.ext_shrink = ext_shrink
        self.format = format
        self.scene = scene
        # This parameter is required.
        self.source_language = source_language
        # This parameter is required.
        self.target_language = target_language
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_shrink is not None:
            result['ext'] = self.ext_shrink
        if self.format is not None:
            result['format'] = self.format
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source_language is not None:
            result['sourceLanguage'] = self.source_language
        if self.target_language is not None:
            result['targetLanguage'] = self.target_language
        if self.text is not None:
            result['text'] = self.text
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext') is not None:
            self.ext_shrink = m.get('ext')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sourceLanguage') is not None:
            self.source_language = m.get('sourceLanguage')
        if m.get('targetLanguage') is not None:
            self.target_language = m.get('targetLanguage')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class TextTranslateResponseBodyDataUsage(TeaModel):
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


class TextTranslateResponseBodyData(TeaModel):
    def __init__(
        self,
        translation: str = None,
        usage: TextTranslateResponseBodyDataUsage = None,
    ):
        self.translation = translation
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.translation is not None:
            result['translation'] = self.translation
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('translation') is not None:
            self.translation = m.get('translation')
        if m.get('usage') is not None:
            temp_model = TextTranslateResponseBodyDataUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class TextTranslateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TextTranslateResponseBodyData = None,
        http_status_code: str = None,
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
            temp_model = TextTranslateResponseBodyData()
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


class TextTranslateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextTranslateResponseBody = None,
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
            temp_model = TextTranslateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


