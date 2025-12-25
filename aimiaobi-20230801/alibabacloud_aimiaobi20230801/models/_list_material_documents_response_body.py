# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListMaterialDocumentsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[main_models.ListMaterialDocumentsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

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

        if self.current is not None:
            result['Current'] = self.current

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMaterialDocumentsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListMaterialDocumentsResponseBodyData(DaraModel):
    def __init__(
        self,
        author: str = None,
        create_time: str = None,
        create_user: str = None,
        create_user_name: str = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
        file_attr: main_models.ListMaterialDocumentsResponseBodyDataFileAttr = None,
        file_key: str = None,
        html_content: str = None,
        id: int = None,
        pub_time: str = None,
        public_url: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        thumbnail_in_base_64: str = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
        update_user_name: str = None,
        url: str = None,
    ):
        self.author = author
        self.create_time = create_time
        self.create_user = create_user
        self.create_user_name = create_user_name
        self.doc_keywords = doc_keywords
        self.doc_type = doc_type
        self.external_url = external_url
        self.file_attr = file_attr
        self.file_key = file_key
        self.html_content = html_content
        self.id = id
        self.pub_time = pub_time
        self.public_url = public_url
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.thumbnail_in_base_64 = thumbnail_in_base_64
        self.title = title
        self.update_time = update_time
        self.update_user = update_user
        self.update_user_name = update_user_name
        self.url = url

    def validate(self):
        if self.file_attr:
            self.file_attr.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['Author'] = self.author

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url

        if self.file_attr is not None:
            result['FileAttr'] = self.file_attr.to_map()

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.html_content is not None:
            result['HtmlContent'] = self.html_content

        if self.id is not None:
            result['Id'] = self.id

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.public_url is not None:
            result['PublicUrl'] = self.public_url

        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr

        if self.src_from is not None:
            result['SrcFrom'] = self.src_from

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.text_content is not None:
            result['TextContent'] = self.text_content

        if self.thumbnail_in_base_64 is not None:
            result['ThumbnailInBase64'] = self.thumbnail_in_base_64

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')

        if m.get('FileAttr') is not None:
            temp_model = main_models.ListMaterialDocumentsResponseBodyDataFileAttr()
            self.file_attr = temp_model.from_map(m.get('FileAttr'))

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')

        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')

        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')

        if m.get('ThumbnailInBase64') is not None:
            self.thumbnail_in_base_64 = m.get('ThumbnailInBase64')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListMaterialDocumentsResponseBodyDataFileAttr(DaraModel):
    def __init__(
        self,
        duration: float = None,
        file_length: int = None,
        file_name: str = None,
        height: int = None,
        mime_type: str = None,
        width: int = None,
    ):
        self.duration = duration
        self.file_length = file_length
        self.file_name = file_name
        self.height = height
        self.mime_type = mime_type
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_length is not None:
            result['FileLength'] = self.file_length

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.height is not None:
            result['Height'] = self.height

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileLength') is not None:
            self.file_length = m.get('FileLength')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

