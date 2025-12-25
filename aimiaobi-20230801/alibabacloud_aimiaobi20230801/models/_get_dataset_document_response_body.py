# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetDatasetDocumentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDatasetDocumentResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetDatasetDocumentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDatasetDocumentResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        disable_handle_multimodal_media: bool = None,
        doc_id: str = None,
        doc_type: str = None,
        doc_uuid: str = None,
        metadata: main_models.GetDatasetDocumentResponseBodyDataMetadata = None,
        pub_time: str = None,
        source_from: str = None,
        status: int = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.disable_handle_multimodal_media = disable_handle_multimodal_media
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.doc_uuid = doc_uuid
        self.metadata = metadata
        self.pub_time = pub_time
        self.source_from = source_from
        self.status = status
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.disable_handle_multimodal_media is not None:
            result['DisableHandleMultimodalMedia'] = self.disable_handle_multimodal_media

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source_from is not None:
            result['SourceFrom'] = self.source_from

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DisableHandleMultimodalMedia') is not None:
            self.disable_handle_multimodal_media = m.get('DisableHandleMultimodalMedia')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('Metadata') is not None:
            temp_model = main_models.GetDatasetDocumentResponseBodyDataMetadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SourceFrom') is not None:
            self.source_from = m.get('SourceFrom')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetDatasetDocumentResponseBodyDataMetadata(DaraModel):
    def __init__(
        self,
        asr_sentences: List[main_models.GetDatasetDocumentResponseBodyDataMetadataAsrSentences] = None,
        text: str = None,
        video_shots: List[main_models.GetDatasetDocumentResponseBodyDataMetadataVideoShots] = None,
    ):
        self.asr_sentences = asr_sentences
        self.text = text
        self.video_shots = video_shots

    def validate(self):
        if self.asr_sentences:
            for v1 in self.asr_sentences:
                 if v1:
                    v1.validate()
        if self.video_shots:
            for v1 in self.video_shots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsrSentences'] = []
        if self.asr_sentences is not None:
            for k1 in self.asr_sentences:
                result['AsrSentences'].append(k1.to_map() if k1 else None)

        if self.text is not None:
            result['Text'] = self.text

        result['VideoShots'] = []
        if self.video_shots is not None:
            for k1 in self.video_shots:
                result['VideoShots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_sentences = []
        if m.get('AsrSentences') is not None:
            for k1 in m.get('AsrSentences'):
                temp_model = main_models.GetDatasetDocumentResponseBodyDataMetadataAsrSentences()
                self.asr_sentences.append(temp_model.from_map(k1))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        self.video_shots = []
        if m.get('VideoShots') is not None:
            for k1 in m.get('VideoShots'):
                temp_model = main_models.GetDatasetDocumentResponseBodyDataMetadataVideoShots()
                self.video_shots.append(temp_model.from_map(k1))

        return self

class GetDatasetDocumentResponseBodyDataMetadataVideoShots(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class GetDatasetDocumentResponseBodyDataMetadataAsrSentences(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

