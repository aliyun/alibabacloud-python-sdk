# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class AddDatasetDocumentRequest(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        document: main_models.AddDatasetDocumentRequestDocument = None,
        workspace_id: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        # This parameter is required.
        self.document = document
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.document:
            self.document.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.document is not None:
            result['Document'] = self.document.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Document') is not None:
            temp_model = main_models.AddDatasetDocumentRequestDocument()
            self.document = temp_model.from_map(m.get('Document'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AddDatasetDocumentRequestDocument(DaraModel):
    def __init__(
        self,
        content: str = None,
        disable_handle_multimodal_media: bool = None,
        doc_id: str = None,
        doc_type: str = None,
        doc_uuid: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        metadata: main_models.AddDatasetDocumentRequestDocumentMetadata = None,
        multimodal_index_name: str = None,
        multimodal_medias: List[main_models.AddDatasetDocumentRequestDocumentMultimodalMedias] = None,
        pub_time: str = None,
        source_from: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.disable_handle_multimodal_media = disable_handle_multimodal_media
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.doc_uuid = doc_uuid
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.metadata = metadata
        self.multimodal_index_name = multimodal_index_name
        self.multimodal_medias = multimodal_medias
        self.pub_time = pub_time
        self.source_from = source_from
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.multimodal_medias:
            for v1 in self.multimodal_medias:
                 if v1:
                    v1.validate()

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

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        if self.multimodal_index_name is not None:
            result['MultimodalIndexName'] = self.multimodal_index_name

        result['MultimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k1 in self.multimodal_medias:
                result['MultimodalMedias'].append(k1.to_map() if k1 else None)

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source_from is not None:
            result['SourceFrom'] = self.source_from

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

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('Metadata') is not None:
            temp_model = main_models.AddDatasetDocumentRequestDocumentMetadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        if m.get('MultimodalIndexName') is not None:
            self.multimodal_index_name = m.get('MultimodalIndexName')

        self.multimodal_medias = []
        if m.get('MultimodalMedias') is not None:
            for k1 in m.get('MultimodalMedias'):
                temp_model = main_models.AddDatasetDocumentRequestDocumentMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k1))

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SourceFrom') is not None:
            self.source_from = m.get('SourceFrom')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class AddDatasetDocumentRequestDocumentMultimodalMedias(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class AddDatasetDocumentRequestDocumentMetadata(DaraModel):
    def __init__(
        self,
        asr_sentences: List[main_models.AddDatasetDocumentRequestDocumentMetadataAsrSentences] = None,
        text: str = None,
        video_shots: List[main_models.AddDatasetDocumentRequestDocumentMetadataVideoShots] = None,
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
                temp_model = main_models.AddDatasetDocumentRequestDocumentMetadataAsrSentences()
                self.asr_sentences.append(temp_model.from_map(k1))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        self.video_shots = []
        if m.get('VideoShots') is not None:
            for k1 in m.get('VideoShots'):
                temp_model = main_models.AddDatasetDocumentRequestDocumentMetadataVideoShots()
                self.video_shots.append(temp_model.from_map(k1))

        return self

class AddDatasetDocumentRequestDocumentMetadataVideoShots(DaraModel):
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

class AddDatasetDocumentRequestDocumentMetadataAsrSentences(DaraModel):
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

