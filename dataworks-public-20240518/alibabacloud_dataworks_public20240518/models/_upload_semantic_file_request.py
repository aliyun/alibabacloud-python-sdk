# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadSemanticFileRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        file_name: str = None,
        size_bytes: int = None,
    ):
        # The MIME type of the object to upload. Maximum length: 128 characters. This value is included in the UploadUrl signature. Use the same Content-Type when performing the PUT request.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The original file name of the reference file to upload. Maximum length: 255 characters. When singleTableFile uses a FileId, only CSV or XLSX files are supported.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The size of the file to upload, in bytes. This value is recorded as attachment metadata. Specify the actual file size.
        # 
        # This parameter is required.
        self.size_bytes = size_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')

        return self

