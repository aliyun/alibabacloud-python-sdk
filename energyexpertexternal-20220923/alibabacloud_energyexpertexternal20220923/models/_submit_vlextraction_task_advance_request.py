# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class SubmitVLExtractionTaskAdvanceRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        folder_id: str = None,
        template_id: str = None,
    ):
        # The filename must include the file type suffix.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Choose one of fileUrl or fileUrlObject:
        # 
        # - fileUrl: Use by providing the document URL, for a single document (supports up to 1000 pages and 100MB in size)
        # 
        # - fileUrlObject: Use when calling the interface with local file upload, for a single document (supports up to 1000 pages and 100 MB in size)
        # 
        # > The relationship between file parsing methods and supported document types
        # > - Long Text RAG: Supports pdf, doc/docx, up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url_object = file_url_object
        # - Unique knowledge base folder ID, used when you need to categorize documents and control the scope of online Q&A queries.
        # - The folder ID needs to be obtained from the intelligent document console after logging in.
        self.folder_id = folder_id
        # Unique parsing template ID, used to specify the key-value pairs to be extracted from the document. You need to configure the template on the template management page and then obtain the corresponding template ID.
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

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url_object = m.get('fileUrl')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

