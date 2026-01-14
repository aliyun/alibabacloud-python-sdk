# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyFileUploadLeaseRequest(DaraModel):
    def __init__(
        self,
        category_type: str = None,
        file_name: str = None,
        md_5: str = None,
        size_in_bytes: str = None,
        use_internal_endpoint: bool = None,
    ):
        self.category_type = category_type
        # The name of the uploaded document, including the extension. Supported formats: pdf, doc, docx, md, txt, ppt, and pptx. The document name must be 4 to 128 characters in length.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The MD5 value of the uploaded document. This parameter is verified by the server (not in the current version).
        # 
        # This parameter is required.
        self.md_5 = md_5
        # The size of the uploaded document, in bytes. This parameter is verified by the server (not in the current version). Valid values: 1 to 100000000.
        # 
        # This parameter is required.
        self.size_in_bytes = size_in_bytes
        self.use_internal_endpoint = use_internal_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes

        if self.use_internal_endpoint is not None:
            result['UseInternalEndpoint'] = self.use_internal_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')

        if m.get('UseInternalEndpoint') is not None:
            self.use_internal_endpoint = m.get('UseInternalEndpoint')

        return self

