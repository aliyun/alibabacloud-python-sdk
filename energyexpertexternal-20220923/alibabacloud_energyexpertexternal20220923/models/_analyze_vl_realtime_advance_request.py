# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class AnalyzeVlRealtimeAdvanceRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        language: str = None,
        template_id: str = None,
    ):
        # 文件名需带文件类型后缀
        self.file_name = file_name
        # Valid values: fileUrl and fileUrlObject.
        # 
        # *   fileUrl: used as a document URL. A single document with not more than 1,000 pages and whose size does not exceed 100 MB is supported.
        # *   fileUrlObject: used when the operation is called in local file upload mode. A single document with not more than 1,000 pages and whose size does not exceed 100 MB is supported.
        # 
        # > The relationship between file extraction methods and supported document types
        # > - Long text RAG: Supports pdf, doc/docx, xlsx, csv, txt, up to 1000 pages
        # > - Image processing: Supports pdf, jpg, jpeg, png, bmp, jpe, tif, tiff, webp, heic
        # > - Long text understanding: Supports doc/docx, xlsx, pdf, csv, txt
        self.file_url_object = file_url_object
        # The language, which can be transferred. Valid values:
        # 
        # *   zh-CN (default)
        # *   en-US
        self.language = language
        # The unique ID of an extraction template, which is used to specify the content to be extracted from a document. You must log on to the Template Management page to configure the template and then obtain the corresponding template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object

        if self.language is not None:
            result['language'] = self.language

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

