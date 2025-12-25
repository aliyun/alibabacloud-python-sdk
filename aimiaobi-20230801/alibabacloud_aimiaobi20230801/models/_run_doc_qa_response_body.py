# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunDocQaResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunDocQaResponseBodyHeader = None,
        payload: main_models.RunDocQaResponseBodyPayload = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = main_models.RunDocQaResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('Payload') is not None:
            temp_model = main_models.RunDocQaResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunDocQaResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunDocQaResponseBodyPayloadOutput = None,
        usage: main_models.RunDocQaResponseBodyPayloadUsage = None,
    ):
        self.output = output
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
            temp_model = main_models.RunDocQaResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunDocQaResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunDocQaResponseBodyPayloadUsage(DaraModel):
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

class RunDocQaResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        content: str = None,
        intervene_content: str = None,
        is_reject: bool = None,
        media_url_list: List[main_models.RunDocQaResponseBodyPayloadOutputMediaUrlList] = None,
        recommends: List[main_models.RunDocQaResponseBodyPayloadOutputRecommends] = None,
        references: List[main_models.RunDocQaResponseBodyPayloadOutputReferences] = None,
    ):
        self.content = content
        self.intervene_content = intervene_content
        self.is_reject = is_reject
        self.media_url_list = media_url_list
        self.recommends = recommends
        self.references = references

    def validate(self):
        if self.media_url_list:
            for v1 in self.media_url_list:
                 if v1:
                    v1.validate()
        if self.recommends:
            for v1 in self.recommends:
                 if v1:
                    v1.validate()
        if self.references:
            for v1 in self.references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.intervene_content is not None:
            result['InterveneContent'] = self.intervene_content

        if self.is_reject is not None:
            result['IsReject'] = self.is_reject

        result['MediaUrlList'] = []
        if self.media_url_list is not None:
            for k1 in self.media_url_list:
                result['MediaUrlList'].append(k1.to_map() if k1 else None)

        result['Recommends'] = []
        if self.recommends is not None:
            for k1 in self.recommends:
                result['Recommends'].append(k1.to_map() if k1 else None)

        result['References'] = []
        if self.references is not None:
            for k1 in self.references:
                result['References'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('InterveneContent') is not None:
            self.intervene_content = m.get('InterveneContent')

        if m.get('IsReject') is not None:
            self.is_reject = m.get('IsReject')

        self.media_url_list = []
        if m.get('MediaUrlList') is not None:
            for k1 in m.get('MediaUrlList'):
                temp_model = main_models.RunDocQaResponseBodyPayloadOutputMediaUrlList()
                self.media_url_list.append(temp_model.from_map(k1))

        self.recommends = []
        if m.get('Recommends') is not None:
            for k1 in m.get('Recommends'):
                temp_model = main_models.RunDocQaResponseBodyPayloadOutputRecommends()
                self.recommends.append(temp_model.from_map(k1))

        self.references = []
        if m.get('References') is not None:
            for k1 in m.get('References'):
                temp_model = main_models.RunDocQaResponseBodyPayloadOutputReferences()
                self.references.append(temp_model.from_map(k1))

        return self

class RunDocQaResponseBodyPayloadOutputReferences(DaraModel):
    def __init__(
        self,
        pub_time: str = None,
        source: str = None,
        source_doc_id: str = None,
        title: str = None,
        url: str = None,
    ):
        self.pub_time = pub_time
        self.source = source
        self.source_doc_id = source_doc_id
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.source_doc_id is not None:
            result['SourceDocId'] = self.source_doc_id

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceDocId') is not None:
            self.source_doc_id = m.get('SourceDocId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunDocQaResponseBodyPayloadOutputRecommends(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunDocQaResponseBodyPayloadOutputMediaUrlList(DaraModel):
    def __init__(
        self,
        clip_infos: List[main_models.RunDocQaResponseBodyPayloadOutputMediaUrlListClipInfos] = None,
        file_url: str = None,
        media_type: str = None,
    ):
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_type = media_type

    def validate(self):
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunDocQaResponseBodyPayloadOutputMediaUrlListClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunDocQaResponseBodyPayloadOutputMediaUrlListClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        to: float = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class RunDocQaResponseBodyHeader(DaraModel):
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

        if self.event_info is not None:
            result['EventInfo'] = self.event_info

        if self.session_id is not None:
            result['SessionId'] = self.session_id

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

        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

