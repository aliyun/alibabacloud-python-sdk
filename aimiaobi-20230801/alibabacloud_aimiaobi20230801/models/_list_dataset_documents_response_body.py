# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListDatasetDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListDatasetDocumentsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDatasetDocumentsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDatasetDocumentsResponseBodyData(DaraModel):
    def __init__(
        self,
        category_uuid: str = None,
        content: str = None,
        create_time: str = None,
        disable_handle_multimodal_media: bool = None,
        doc_id: str = None,
        doc_type: str = None,
        doc_uuid: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        multimodal_medias: List[main_models.ListDatasetDocumentsResponseBodyDataMultimodalMedias] = None,
        pub_time: str = None,
        source_from: str = None,
        status: int = None,
        summary: str = None,
        title: str = None,
        update_time: str = None,
        url: str = None,
    ):
        self.category_uuid = category_uuid
        self.content = content
        self.create_time = create_time
        self.disable_handle_multimodal_media = disable_handle_multimodal_media
        self.doc_id = doc_id
        self.doc_type = doc_type
        self.doc_uuid = doc_uuid
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.multimodal_medias = multimodal_medias
        self.pub_time = pub_time
        self.source_from = source_from
        self.status = status
        self.summary = summary
        self.title = title
        self.update_time = update_time
        # url
        self.url = url

    def validate(self):
        if self.multimodal_medias:
            for v1 in self.multimodal_medias:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuid is not None:
            result['CategoryUuid'] = self.category_uuid

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        result['MultimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k1 in self.multimodal_medias:
                result['MultimodalMedias'].append(k1.to_map() if k1 else None)

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

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuid') is not None:
            self.category_uuid = m.get('CategoryUuid')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        self.multimodal_medias = []
        if m.get('MultimodalMedias') is not None:
            for k1 in m.get('MultimodalMedias'):
                temp_model = main_models.ListDatasetDocumentsResponseBodyDataMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k1))

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

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListDatasetDocumentsResponseBodyDataMultimodalMedias(DaraModel):
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

