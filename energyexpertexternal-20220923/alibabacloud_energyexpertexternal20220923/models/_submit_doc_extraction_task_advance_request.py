# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SubmitDocExtractionTaskAdvanceRequest(DaraModel):
    def __init__(
        self,
        extract_type: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # Document extraction type:
        # Supports rag and long text understanding types, default is rag.
        self.extract_type = extract_type
        # The filename must include the file type extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages, 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages, 100 MB in size)
        # 
        # > The relationship between file extraction methods and supported document types
        # > - Long text RAG: Supports pdf, doc/docx, xlsx, csv, txt, up to 1000 pages
        # > - Image processing: Supports pdf, jpg, jpeg, png, bmp, jpe, tif, tiff, webp, heic
        # > - Long text understanding: Supports doc/docx, xlsx, pdf, csv, txt
        self.file_url_object = file_url_object
        # - A unique knowledge base folder ID, used when you need to categorize documents and control the scope of documents for online Q&A queries.
        # - The folder ID needs to be obtained by logging into the intelligent document console.
        self.folder_id = folder_id
        # A unique extraction template ID used to specify the content to be extracted from the document. You need to log in to the template management page to configure the template and obtain the corresponding template ID.
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
        if self.extract_type is not None:
            result['extractType'] = self.extract_type

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
        if m.get('extractType') is not None:
            self.extract_type = m.get('extractType')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

