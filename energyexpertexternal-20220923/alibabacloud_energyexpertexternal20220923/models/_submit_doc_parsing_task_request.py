# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDocParsingTaskRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        folder_id: str = None,
        need_analyze_img: bool = None,
    ):
        # The filename must include the file type extension.
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
        # > - Long Text RAG: Supports pdf, doc/docx, supports up to 1000 pages
        # > - Image Processing: Supports pdf, jpg, jpeg, png, bmp
        # > - Long Text Understanding: Supports pdf, doc/docx, xls/xlsx
        self.file_url = file_url
        # - Unique knowledge base folder ID, used when categorizing documents and controlling the scope of documents for online Q&A queries.
        # - The folder ID needs to be obtained from the Intelligent Document Console after logging in.
        self.folder_id = folder_id
        # Whether to parse image content within the document.
        self.need_analyze_img = need_analyze_img

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.need_analyze_img is not None:
            result['needAnalyzeImg'] = self.need_analyze_img

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('needAnalyzeImg') is not None:
            self.need_analyze_img = m.get('needAnalyzeImg')

        return self

