# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnalyzeVlRealtimeRequest(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        language: str = None,
        template_id: str = None,
    ):
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use in the form of a document URL, for a single document (supports up to 1000 pages and 100MB)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url = file_url
        # Language, parameters that can be passed
        # - zh-CN: Chinese (default)
        # - en-US: English
        self.language = language
        # A unique parsing template ID used to specify the key-value pairs to be extracted from the document. You need to log in to the template management page, configure the template, and then get the corresponding template ID.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.language is not None:
            result['language'] = self.language

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

