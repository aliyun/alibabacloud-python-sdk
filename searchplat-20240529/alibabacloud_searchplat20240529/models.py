# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateDocumentAnalyzeTaskRequestDocument(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        file_type: str = None,
        url: str = None,
    ):
        self.content = content
        self.file_name = file_name
        self.file_type = file_type
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
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_type is not None:
            result['file_type'] = self.file_type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_type') is not None:
            self.file_type = m.get('file_type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateDocumentAnalyzeTaskRequestOutput(TeaModel):
    def __init__(
        self,
        image_storage: str = None,
    ):
        self.image_storage = image_storage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_storage is not None:
            result['image_storage'] = self.image_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_storage') is not None:
            self.image_storage = m.get('image_storage')
        return self


class CreateDocumentAnalyzeTaskRequestStrategy(TeaModel):
    def __init__(
        self,
        enable_semantic: bool = None,
    ):
        self.enable_semantic = enable_semantic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_semantic is not None:
            result['enable_semantic'] = self.enable_semantic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable_semantic') is not None:
            self.enable_semantic = m.get('enable_semantic')
        return self


class CreateDocumentAnalyzeTaskRequest(TeaModel):
    def __init__(
        self,
        document: CreateDocumentAnalyzeTaskRequestDocument = None,
        output: CreateDocumentAnalyzeTaskRequestOutput = None,
        strategy: CreateDocumentAnalyzeTaskRequestStrategy = None,
    ):
        self.document = document
        self.output = output
        self.strategy = strategy

    def validate(self):
        if self.document:
            self.document.validate()
        if self.output:
            self.output.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document.to_map()
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            temp_model = CreateDocumentAnalyzeTaskRequestDocument()
            self.document = temp_model.from_map(m['document'])
        if m.get('output') is not None:
            temp_model = CreateDocumentAnalyzeTaskRequestOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('strategy') is not None:
            temp_model = CreateDocumentAnalyzeTaskRequestStrategy()
            self.strategy = temp_model.from_map(m['strategy'])
        return self


class CreateDocumentAnalyzeTaskResponseBodyResult(TeaModel):
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
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class CreateDocumentAnalyzeTaskResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: CreateDocumentAnalyzeTaskResponseBodyResult = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = CreateDocumentAnalyzeTaskResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateDocumentAnalyzeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDocumentAnalyzeTaskResponseBody = None,
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
            temp_model = CreateDocumentAnalyzeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageAnalyzeTaskRequestDocument(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        file_type: str = None,
        url: str = None,
    ):
        self.content = content
        self.file_name = file_name
        self.file_type = file_type
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
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_type is not None:
            result['file_type'] = self.file_type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_type') is not None:
            self.file_type = m.get('file_type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateImageAnalyzeTaskRequest(TeaModel):
    def __init__(
        self,
        document: CreateImageAnalyzeTaskRequestDocument = None,
    ):
        self.document = document

    def validate(self):
        if self.document:
            self.document.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            temp_model = CreateImageAnalyzeTaskRequestDocument()
            self.document = temp_model.from_map(m['document'])
        return self


class CreateImageAnalyzeTaskResponseBodyResult(TeaModel):
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
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class CreateImageAnalyzeTaskResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: CreateImageAnalyzeTaskResponseBodyResult = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = CreateImageAnalyzeTaskResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class CreateImageAnalyzeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageAnalyzeTaskResponseBody = None,
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
            temp_model = CreateImageAnalyzeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentAnalyzeTaskStatusRequest(TeaModel):
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
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetDocumentAnalyzeTaskStatusResponseBodyResultData(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        page_num: int = None,
    ):
        self.content = content
        self.content_type = content_type
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.page_num is not None:
            result['page_num'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('page_num') is not None:
            self.page_num = m.get('page_num')
        return self


class GetDocumentAnalyzeTaskStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: GetDocumentAnalyzeTaskStatusResponseBodyResultData = None,
        error: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.data = data
        self.error = error
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error is not None:
            result['error'] = self.error
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDocumentAnalyzeTaskStatusResponseBodyResultData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error') is not None:
            self.error = m.get('error')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetDocumentAnalyzeTaskStatusResponseBodyUsage(TeaModel):
    def __init__(
        self,
        image_count: int = None,
        table_count: int = None,
        token_count: int = None,
    ):
        self.image_count = image_count
        self.table_count = table_count
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_count is not None:
            result['image_count'] = self.image_count
        if self.table_count is not None:
            result['table_count'] = self.table_count
        if self.token_count is not None:
            result['token_count'] = self.token_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')
        if m.get('table_count') is not None:
            self.table_count = m.get('table_count')
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')
        return self


class GetDocumentAnalyzeTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetDocumentAnalyzeTaskStatusResponseBodyResult = None,
        usage: GetDocumentAnalyzeTaskStatusResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetDocumentAnalyzeTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetDocumentAnalyzeTaskStatusResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetDocumentAnalyzeTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentAnalyzeTaskStatusResponseBody = None,
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
            temp_model = GetDocumentAnalyzeTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentRankRequest(TeaModel):
    def __init__(
        self,
        docs: List[str] = None,
        query: str = None,
    ):
        # This parameter is required.
        self.docs = docs
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs is not None:
            result['docs'] = self.docs
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docs') is not None:
            self.docs = m.get('docs')
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class GetDocumentRankResponseBodyResultScores(TeaModel):
    def __init__(
        self,
        index: int = None,
        score: float = None,
    ):
        self.index = index
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['index'] = self.index
        if self.score is not None:
            result['score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('score') is not None:
            self.score = m.get('score')
        return self


class GetDocumentRankResponseBodyResult(TeaModel):
    def __init__(
        self,
        scores: List[GetDocumentRankResponseBodyResultScores] = None,
    ):
        self.scores = scores

    def validate(self):
        if self.scores:
            for k in self.scores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['scores'] = []
        if self.scores is not None:
            for k in self.scores:
                result['scores'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scores = []
        if m.get('scores') is not None:
            for k in m.get('scores'):
                temp_model = GetDocumentRankResponseBodyResultScores()
                self.scores.append(temp_model.from_map(k))
        return self


class GetDocumentRankResponseBodyUsage(TeaModel):
    def __init__(
        self,
        doc_count: int = None,
    ):
        self.doc_count = doc_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_count is not None:
            result['doc_count'] = self.doc_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('doc_count') is not None:
            self.doc_count = m.get('doc_count')
        return self


class GetDocumentRankResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetDocumentRankResponseBodyResult = None,
        usage: GetDocumentRankResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetDocumentRankResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetDocumentRankResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetDocumentRankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentRankResponseBody = None,
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
            temp_model = GetDocumentRankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocumentSplitRequestDocument(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_encoding: str = None,
        content_type: str = None,
    ):
        self.content = content
        self.content_encoding = content_encoding
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_encoding is not None:
            result['content_encoding'] = self.content_encoding
        if self.content_type is not None:
            result['content_type'] = self.content_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('content_encoding') is not None:
            self.content_encoding = m.get('content_encoding')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        return self


class GetDocumentSplitRequestStrategy(TeaModel):
    def __init__(
        self,
        compute_type: str = None,
        max_chunk_size: int = None,
        need_sentence: bool = None,
    ):
        self.compute_type = compute_type
        self.max_chunk_size = max_chunk_size
        self.need_sentence = need_sentence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_type is not None:
            result['compute_type'] = self.compute_type
        if self.max_chunk_size is not None:
            result['max_chunk_size'] = self.max_chunk_size
        if self.need_sentence is not None:
            result['need_sentence'] = self.need_sentence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compute_type') is not None:
            self.compute_type = m.get('compute_type')
        if m.get('max_chunk_size') is not None:
            self.max_chunk_size = m.get('max_chunk_size')
        if m.get('need_sentence') is not None:
            self.need_sentence = m.get('need_sentence')
        return self


class GetDocumentSplitRequest(TeaModel):
    def __init__(
        self,
        document: GetDocumentSplitRequestDocument = None,
        strategy: GetDocumentSplitRequestStrategy = None,
    ):
        # This parameter is required.
        self.document = document
        self.strategy = strategy

    def validate(self):
        if self.document:
            self.document.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document is not None:
            result['document'] = self.document.to_map()
        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            temp_model = GetDocumentSplitRequestDocument()
            self.document = temp_model.from_map(m['document'])
        if m.get('strategy') is not None:
            temp_model = GetDocumentSplitRequestStrategy()
            self.strategy = temp_model.from_map(m['strategy'])
        return self


class GetDocumentSplitResponseBodyResultChunks(TeaModel):
    def __init__(
        self,
        content: str = None,
        meta: Dict[str, str] = None,
    ):
        self.content = content
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class GetDocumentSplitResponseBodyResultRichTexts(TeaModel):
    def __init__(
        self,
        content: str = None,
        meta: Dict[str, str] = None,
    ):
        self.content = content
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class GetDocumentSplitResponseBodyResultSentences(TeaModel):
    def __init__(
        self,
        content: str = None,
        meta: Dict[str, str] = None,
    ):
        self.content = content
        self.meta = meta

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.meta is not None:
            result['meta'] = self.meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        return self


class GetDocumentSplitResponseBodyResult(TeaModel):
    def __init__(
        self,
        chunks: List[GetDocumentSplitResponseBodyResultChunks] = None,
        nodes: List[Dict[str, str]] = None,
        rich_texts: List[GetDocumentSplitResponseBodyResultRichTexts] = None,
        sentences: List[GetDocumentSplitResponseBodyResultSentences] = None,
    ):
        self.chunks = chunks
        self.nodes = nodes
        self.rich_texts = rich_texts
        self.sentences = sentences

    def validate(self):
        if self.chunks:
            for k in self.chunks:
                if k:
                    k.validate()
        if self.rich_texts:
            for k in self.rich_texts:
                if k:
                    k.validate()
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['chunks'] = []
        if self.chunks is not None:
            for k in self.chunks:
                result['chunks'].append(k.to_map() if k else None)
        if self.nodes is not None:
            result['nodes'] = self.nodes
        result['rich_texts'] = []
        if self.rich_texts is not None:
            for k in self.rich_texts:
                result['rich_texts'].append(k.to_map() if k else None)
        result['sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['sentences'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k in m.get('chunks'):
                temp_model = GetDocumentSplitResponseBodyResultChunks()
                self.chunks.append(temp_model.from_map(k))
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        self.rich_texts = []
        if m.get('rich_texts') is not None:
            for k in m.get('rich_texts'):
                temp_model = GetDocumentSplitResponseBodyResultRichTexts()
                self.rich_texts.append(temp_model.from_map(k))
        self.sentences = []
        if m.get('sentences') is not None:
            for k in m.get('sentences'):
                temp_model = GetDocumentSplitResponseBodyResultSentences()
                self.sentences.append(temp_model.from_map(k))
        return self


class GetDocumentSplitResponseBodyUsage(TeaModel):
    def __init__(
        self,
        token_count: int = None,
    ):
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token_count is not None:
            result['token_count'] = self.token_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')
        return self


class GetDocumentSplitResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetDocumentSplitResponseBodyResult = None,
        usage: GetDocumentSplitResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetDocumentSplitResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetDocumentSplitResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetDocumentSplitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocumentSplitResponseBody = None,
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
            temp_model = GetDocumentSplitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmbeddingTuningRequest(TeaModel):
    def __init__(
        self,
        input: List[List[float]] = None,
        parameters: Dict[str, Any] = None,
    ):
        self.input = input
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class GetEmbeddingTuningResponseBodyResult(TeaModel):
    def __init__(
        self,
        output: List[List[float]] = None,
    ):
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        return self


class GetEmbeddingTuningResponseBodyUsage(TeaModel):
    def __init__(
        self,
        doc_count: int = None,
    ):
        self.doc_count = doc_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_count is not None:
            result['doc_count'] = self.doc_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('doc_count') is not None:
            self.doc_count = m.get('doc_count')
        return self


class GetEmbeddingTuningResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetEmbeddingTuningResponseBodyResult = None,
        usage: GetEmbeddingTuningResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetEmbeddingTuningResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetEmbeddingTuningResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetEmbeddingTuningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEmbeddingTuningResponseBody = None,
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
            temp_model = GetEmbeddingTuningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageAnalyzeTaskStatusRequest(TeaModel):
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
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetImageAnalyzeTaskStatusResponseBodyResultData(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        page_num: int = None,
    ):
        self.content = content
        self.content_type = content_type
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.page_num is not None:
            result['page_num'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('page_num') is not None:
            self.page_num = m.get('page_num')
        return self


class GetImageAnalyzeTaskStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: GetImageAnalyzeTaskStatusResponseBodyResultData = None,
        error: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.data = data
        self.error = error
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error is not None:
            result['error'] = self.error
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetImageAnalyzeTaskStatusResponseBodyResultData()
            self.data = temp_model.from_map(m['data'])
        if m.get('error') is not None:
            self.error = m.get('error')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetImageAnalyzeTaskStatusResponseBodyUsage(TeaModel):
    def __init__(
        self,
        pv_count: int = None,
        token_count: int = None,
    ):
        self.pv_count = pv_count
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pv_count is not None:
            result['pv_count'] = self.pv_count
        if self.token_count is not None:
            result['token_count'] = self.token_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pv_count') is not None:
            self.pv_count = m.get('pv_count')
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')
        return self


class GetImageAnalyzeTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetImageAnalyzeTaskStatusResponseBodyResult = None,
        usage: GetImageAnalyzeTaskStatusResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetImageAnalyzeTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetImageAnalyzeTaskStatusResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetImageAnalyzeTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetImageAnalyzeTaskStatusResponseBody = None,
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
            temp_model = GetImageAnalyzeTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiModalEmbeddingRequestInput(TeaModel):
    def __init__(
        self,
        image: str = None,
        text: str = None,
    ):
        self.image = image
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetMultiModalEmbeddingRequest(TeaModel):
    def __init__(
        self,
        input: List[GetMultiModalEmbeddingRequestInput] = None,
    ):
        self.input = input

    def validate(self):
        if self.input:
            for k in self.input:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['input'] = []
        if self.input is not None:
            for k in self.input:
                result['input'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input = []
        if m.get('input') is not None:
            for k in m.get('input'):
                temp_model = GetMultiModalEmbeddingRequestInput()
                self.input.append(temp_model.from_map(k))
        return self


class GetMultiModalEmbeddingResponseBodyResultEmbeddings(TeaModel):
    def __init__(
        self,
        embedding: List[float] = None,
        index: int = None,
    ):
        self.embedding = embedding
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embedding is not None:
            result['embedding'] = self.embedding
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('embedding') is not None:
            self.embedding = m.get('embedding')
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class GetMultiModalEmbeddingResponseBodyResult(TeaModel):
    def __init__(
        self,
        embeddings: List[GetMultiModalEmbeddingResponseBodyResultEmbeddings] = None,
    ):
        self.embeddings = embeddings

    def validate(self):
        if self.embeddings:
            for k in self.embeddings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['embeddings'] = []
        if self.embeddings is not None:
            for k in self.embeddings:
                result['embeddings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.embeddings = []
        if m.get('embeddings') is not None:
            for k in m.get('embeddings'):
                temp_model = GetMultiModalEmbeddingResponseBodyResultEmbeddings()
                self.embeddings.append(temp_model.from_map(k))
        return self


class GetMultiModalEmbeddingResponseBodyUsage(TeaModel):
    def __init__(
        self,
        image: int = None,
        token_count: int = None,
    ):
        self.image = image
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.token_count is not None:
            result['token_count'] = self.token_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')
        return self


class GetMultiModalEmbeddingResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetMultiModalEmbeddingResponseBodyResult = None,
        usage: GetMultiModalEmbeddingResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetMultiModalEmbeddingResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetMultiModalEmbeddingResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetMultiModalEmbeddingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiModalEmbeddingResponseBody = None,
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
            temp_model = GetMultiModalEmbeddingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPredictionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        token: str = None,
    ):
        self.common_headers = common_headers
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetPredictionRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetPredictionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetQueryAnalysisRequestFunctions(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.name = name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class GetQueryAnalysisRequestHistory(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
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
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class GetQueryAnalysisRequest(TeaModel):
    def __init__(
        self,
        functions: List[GetQueryAnalysisRequestFunctions] = None,
        history: List[GetQueryAnalysisRequestHistory] = None,
        query: str = None,
    ):
        self.functions = functions
        self.history = history
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        result['history'] = []
        if self.history is not None:
            for k in self.history:
                result['history'].append(k.to_map() if k else None)
        if self.query is not None:
            result['query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = GetQueryAnalysisRequestFunctions()
                self.functions.append(temp_model.from_map(k))
        self.history = []
        if m.get('history') is not None:
            for k in m.get('history'):
                temp_model = GetQueryAnalysisRequestHistory()
                self.history.append(temp_model.from_map(k))
        if m.get('query') is not None:
            self.query = m.get('query')
        return self


class GetQueryAnalysisResponseBodyResult(TeaModel):
    def __init__(
        self,
        intent: str = None,
        queries: List[str] = None,
        query: str = None,
        sql: Dict[str, Any] = None,
    ):
        self.intent = intent
        self.queries = queries
        self.query = query
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent is not None:
            result['intent'] = self.intent
        if self.queries is not None:
            result['queries'] = self.queries
        if self.query is not None:
            result['query'] = self.query
        if self.sql is not None:
            result['sql'] = self.sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intent') is not None:
            self.intent = m.get('intent')
        if m.get('queries') is not None:
            self.queries = m.get('queries')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        return self


class GetQueryAnalysisResponseBodyUsage(TeaModel):
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
            result['input_tokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')
        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')
        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')
        return self


class GetQueryAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetQueryAnalysisResponseBodyResult = None,
        usage: GetQueryAnalysisResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetQueryAnalysisResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetQueryAnalysisResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetQueryAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryAnalysisResponseBody = None,
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
            temp_model = GetQueryAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextEmbeddingRequest(TeaModel):
    def __init__(
        self,
        input: List[str] = None,
        input_type: str = None,
    ):
        # This parameter is required.
        self.input = input
        self.input_type = input_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.input_type is not None:
            result['input_type'] = self.input_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('input_type') is not None:
            self.input_type = m.get('input_type')
        return self


class GetTextEmbeddingResponseBodyResultEmbeddings(TeaModel):
    def __init__(
        self,
        embedding: List[float] = None,
        index: int = None,
    ):
        self.embedding = embedding
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embedding is not None:
            result['embedding'] = self.embedding
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('embedding') is not None:
            self.embedding = m.get('embedding')
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class GetTextEmbeddingResponseBodyResult(TeaModel):
    def __init__(
        self,
        embeddings: List[GetTextEmbeddingResponseBodyResultEmbeddings] = None,
    ):
        self.embeddings = embeddings

    def validate(self):
        if self.embeddings:
            for k in self.embeddings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['embeddings'] = []
        if self.embeddings is not None:
            for k in self.embeddings:
                result['embeddings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.embeddings = []
        if m.get('embeddings') is not None:
            for k in m.get('embeddings'):
                temp_model = GetTextEmbeddingResponseBodyResultEmbeddings()
                self.embeddings.append(temp_model.from_map(k))
        return self


class GetTextEmbeddingResponseBodyUsage(TeaModel):
    def __init__(
        self,
        token_count: int = None,
    ):
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token_count is not None:
            result['token_count'] = self.token_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')
        return self


class GetTextEmbeddingResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetTextEmbeddingResponseBodyResult = None,
        usage: GetTextEmbeddingResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetTextEmbeddingResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetTextEmbeddingResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetTextEmbeddingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTextEmbeddingResponseBody = None,
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
            temp_model = GetTextEmbeddingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextGenerationRequestMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
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
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class GetTextGenerationRequest(TeaModel):
    def __init__(
        self,
        csi_level: str = None,
        enable_search: bool = None,
        messages: List[GetTextGenerationRequestMessages] = None,
        parameters: Dict[str, Any] = None,
        stream: bool = None,
    ):
        self.csi_level = csi_level
        self.enable_search = enable_search
        # This parameter is required.
        self.messages = messages
        self.parameters = parameters
        self.stream = stream

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csi_level is not None:
            result['csi_level'] = self.csi_level
        if self.enable_search is not None:
            result['enable_search'] = self.enable_search
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('csi_level') is not None:
            self.csi_level = m.get('csi_level')
        if m.get('enable_search') is not None:
            self.enable_search = m.get('enable_search')
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = GetTextGenerationRequestMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class GetTextGenerationResponseBodyResultSearchResults(TeaModel):
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


class GetTextGenerationResponseBodyResult(TeaModel):
    def __init__(
        self,
        search_results: List[GetTextGenerationResponseBodyResultSearchResults] = None,
        text: str = None,
    ):
        self.search_results = search_results
        self.text = text

    def validate(self):
        if self.search_results:
            for k in self.search_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['search_results'] = []
        if self.search_results is not None:
            for k in self.search_results:
                result['search_results'].append(k.to_map() if k else None)
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_results = []
        if m.get('search_results') is not None:
            for k in m.get('search_results'):
                temp_model = GetTextGenerationResponseBodyResultSearchResults()
                self.search_results.append(temp_model.from_map(k))
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetTextGenerationResponseBodyUsage(TeaModel):
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
            result['input_tokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')
        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')
        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')
        return self


class GetTextGenerationResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetTextGenerationResponseBodyResult = None,
        usage: GetTextGenerationResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetTextGenerationResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetTextGenerationResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetTextGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTextGenerationResponseBody = None,
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
            temp_model = GetTextGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTextSparseEmbeddingRequest(TeaModel):
    def __init__(
        self,
        input: List[str] = None,
        input_type: str = None,
        return_token: bool = None,
    ):
        # This parameter is required.
        self.input = input
        self.input_type = input_type
        self.return_token = return_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['input'] = self.input
        if self.input_type is not None:
            result['input_type'] = self.input_type
        if self.return_token is not None:
            result['return_token'] = self.return_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('input_type') is not None:
            self.input_type = m.get('input_type')
        if m.get('return_token') is not None:
            self.return_token = m.get('return_token')
        return self


class GetTextSparseEmbeddingResponseBodyResultSparseEmbeddingsEmbedding(TeaModel):
    def __init__(
        self,
        token: str = None,
        token_id: int = None,
        weight: float = None,
    ):
        self.token = token
        self.token_id = token_id
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['token'] = self.token
        if self.token_id is not None:
            result['token_id'] = self.token_id
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('token_id') is not None:
            self.token_id = m.get('token_id')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetTextSparseEmbeddingResponseBodyResultSparseEmbeddings(TeaModel):
    def __init__(
        self,
        embedding: List[GetTextSparseEmbeddingResponseBodyResultSparseEmbeddingsEmbedding] = None,
        index: int = None,
    ):
        self.embedding = embedding
        self.index = index

    def validate(self):
        if self.embedding:
            for k in self.embedding:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['embedding'] = []
        if self.embedding is not None:
            for k in self.embedding:
                result['embedding'].append(k.to_map() if k else None)
        if self.index is not None:
            result['index'] = self.index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.embedding = []
        if m.get('embedding') is not None:
            for k in m.get('embedding'):
                temp_model = GetTextSparseEmbeddingResponseBodyResultSparseEmbeddingsEmbedding()
                self.embedding.append(temp_model.from_map(k))
        if m.get('index') is not None:
            self.index = m.get('index')
        return self


class GetTextSparseEmbeddingResponseBodyResult(TeaModel):
    def __init__(
        self,
        sparse_embeddings: List[GetTextSparseEmbeddingResponseBodyResultSparseEmbeddings] = None,
    ):
        self.sparse_embeddings = sparse_embeddings

    def validate(self):
        if self.sparse_embeddings:
            for k in self.sparse_embeddings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['sparse_embeddings'] = []
        if self.sparse_embeddings is not None:
            for k in self.sparse_embeddings:
                result['sparse_embeddings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sparse_embeddings = []
        if m.get('sparse_embeddings') is not None:
            for k in m.get('sparse_embeddings'):
                temp_model = GetTextSparseEmbeddingResponseBodyResultSparseEmbeddings()
                self.sparse_embeddings.append(temp_model.from_map(k))
        return self


class GetTextSparseEmbeddingResponseBodyUsage(TeaModel):
    def __init__(
        self,
        token_count: int = None,
    ):
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token_count is not None:
            result['token_count'] = self.token_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')
        return self


class GetTextSparseEmbeddingResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetTextSparseEmbeddingResponseBodyResult = None,
        usage: GetTextSparseEmbeddingResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetTextSparseEmbeddingResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetTextSparseEmbeddingResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetTextSparseEmbeddingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTextSparseEmbeddingResponseBody = None,
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
            temp_model = GetTextSparseEmbeddingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebSearchRequest(TeaModel):
    def __init__(
        self,
        query: str = None,
        top_k: int = None,
        way: str = None,
    ):
        # This parameter is required.
        self.query = query
        self.top_k = top_k
        self.way = way

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.top_k is not None:
            result['top_k'] = self.top_k
        if self.way is not None:
            result['way'] = self.way
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('top_k') is not None:
            self.top_k = m.get('top_k')
        if m.get('way') is not None:
            self.way = m.get('way')
        return self


class GetWebSearchResponseBodyResultSearchResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        link: str = None,
        position: int = None,
        snippet: str = None,
        tilte: str = None,
    ):
        self.content = content
        self.link = link
        self.position = position
        self.snippet = snippet
        self.tilte = tilte

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.link is not None:
            result['link'] = self.link
        if self.position is not None:
            result['position'] = self.position
        if self.snippet is not None:
            result['snippet'] = self.snippet
        if self.tilte is not None:
            result['tilte'] = self.tilte
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        if m.get('tilte') is not None:
            self.tilte = m.get('tilte')
        return self


class GetWebSearchResponseBodyResult(TeaModel):
    def __init__(
        self,
        search_result: List[GetWebSearchResponseBodyResultSearchResult] = None,
    ):
        self.search_result = search_result

    def validate(self):
        if self.search_result:
            for k in self.search_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['search_result'] = []
        if self.search_result is not None:
            for k in self.search_result:
                result['search_result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_result = []
        if m.get('search_result') is not None:
            for k in m.get('search_result'):
                temp_model = GetWebSearchResponseBodyResultSearchResult()
                self.search_result.append(temp_model.from_map(k))
        return self


class GetWebSearchResponseBodyUsageFilterModel(TeaModel):
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
            result['input_tokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')
        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')
        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')
        return self


class GetWebSearchResponseBodyUsageRewriteModel(TeaModel):
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
            result['input_tokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')
        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')
        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')
        return self


class GetWebSearchResponseBodyUsage(TeaModel):
    def __init__(
        self,
        filter_model: GetWebSearchResponseBodyUsageFilterModel = None,
        rewrite_model: GetWebSearchResponseBodyUsageRewriteModel = None,
        search_count: int = None,
    ):
        self.filter_model = filter_model
        self.rewrite_model = rewrite_model
        self.search_count = search_count

    def validate(self):
        if self.filter_model:
            self.filter_model.validate()
        if self.rewrite_model:
            self.rewrite_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_model is not None:
            result['filter_model'] = self.filter_model.to_map()
        if self.rewrite_model is not None:
            result['rewrite_model'] = self.rewrite_model.to_map()
        if self.search_count is not None:
            result['search_count'] = self.search_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter_model') is not None:
            temp_model = GetWebSearchResponseBodyUsageFilterModel()
            self.filter_model = temp_model.from_map(m['filter_model'])
        if m.get('rewrite_model') is not None:
            temp_model = GetWebSearchResponseBodyUsageRewriteModel()
            self.rewrite_model = temp_model.from_map(m['rewrite_model'])
        if m.get('search_count') is not None:
            self.search_count = m.get('search_count')
        return self


class GetWebSearchResponseBody(TeaModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: GetWebSearchResponseBodyResult = None,
        usage: GetWebSearchResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latency is not None:
            result['latency'] = self.latency
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.usage is not None:
            result['usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('result') is not None:
            temp_model = GetWebSearchResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('usage') is not None:
            temp_model = GetWebSearchResponseBodyUsage()
            self.usage = temp_model.from_map(m['usage'])
        return self


class GetWebSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebSearchResponseBody = None,
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
            temp_model = GetWebSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


