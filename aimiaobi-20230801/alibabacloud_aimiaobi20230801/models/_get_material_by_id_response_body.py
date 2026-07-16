# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetMaterialByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMaterialByIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code
        self.code = code
        # Business data
        self.data = data
        # HTTP status code
        self.http_status_code = http_status_code
        # Error description
        self.message = message
        # Unique request identifier
        self.request_id = request_id
        # Indicates success: true for success, false for failure
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
            temp_model = main_models.GetMaterialByIdResponseBodyData()
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

class GetMaterialByIdResponseBodyData(DaraModel):
    def __init__(
        self,
        author: str = None,
        create_time: str = None,
        create_user: str = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
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
        url: str = None,
    ):
        # Author
        self.author = author
        # Creation time
        self.create_time = create_time
        # Creator user ID
        self.create_user = create_user
        # Document tags used for classification and other purposes. Separate multiple keywords with commas.
        self.doc_keywords = doc_keywords
        # Document type, such as pdf, word, url, or image
        self.doc_type = doc_type
        # URL uploaded by an external customer. Used only for record keeping.
        self.external_url = external_url
        # Web page content
        self.html_content = html_content
        # Primary key
        self.id = id
        # Publication time
        self.pub_time = pub_time
        # Temporary public URL
        self.public_url = public_url
        # Sharing attribute stored as bit flags. The first bit indicates sharing within the workspace, the second bit indicates sharing within the tenant, and the third bit indicates system-wide sharing.
        self.share_attr = share_attr
        # Document source, such as user_upload, search, or viewpoint
        self.src_from = src_from
        # Document summary
        self.summary = summary
        # Parsed text content. Empty for images.
        self.text_content = text_content
        # Base64-encoded thumbnail for image documents
        self.thumbnail_in_base_64 = thumbnail_in_base_64
        # Document title
        self.title = title
        # Modification time
        self.update_time = update_time
        # Modifier user ID
        self.update_user = update_user
        # Internal document storage URL
        self.url = url

    def validate(self):
        pass

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

        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url

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

        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')

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

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

