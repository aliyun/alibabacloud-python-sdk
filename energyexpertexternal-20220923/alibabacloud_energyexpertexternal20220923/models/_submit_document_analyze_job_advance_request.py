# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SubmitDocumentAnalyzeJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        analysis_type: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # The default extraction method is "doc", with the following optional values:
        # 
        # - vl: Image processing
        # - doc: Long text RAG (Retrieval-Augmented Generation)
        # - docUnderstanding: Long text comprehension
        # - recommender: Recommendation type
        self.analysis_type = analysis_type
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one between fileUrl and fileUrlObject:
        # 
        # - fileUrl: Use the document URL method for a single document (supports documents with up to 1000 pages and within 100MB).
        # 
        # - fileUrlObject: Use when calling the API via local file upload, for a single document (supports documents with up to 1000 pages and 
        # within 100MB).
        # 
        # > Relationship between file parsing methods and supported document types. 
        # >- Long Text RAG: Supports pdf, doc/docx, and up to 1000 pages
        # >- Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # >- Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url_object = file_url_object
        # Unique knowledge base folder ID, used for categorizing documents and controlling the scope of online Q&A queries. If empty, the document will be uploaded to the tenant\\"s root directory.
        self.folder_id = folder_id
        # The unique extraction template ID is used to specify the key-value pairs to be extracted from the document. You need to log in to the template management page to configure the template and obtain the corresponding template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_type is not None:
            result['analysisType'] = self.analysis_type

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_url_object is not None:
            result['fileUrl'] = self.file_url_object

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisType') is not None:
            self.analysis_type = m.get('analysisType')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

