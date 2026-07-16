# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComfyUserDataUploadUrlRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        file_md_5: str = None,
        file_name: str = None,
        file_size_bytes: int = None,
    ):
        # The content type of the file.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The MD5 hash of the file to be uploaded. This value must be the file\\"s actual MD5 hash. The file size is also verified during the upload.
        # 
        # This parameter is required.
        self.file_md_5 = file_md_5
        # The name of the file to upload. The filename can be a single file, such as \\`1.jpg\\`, or include a path, such as \\`directory1/1.jpg\\`.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The actual size of the file in bytes. This value must be the exact size of the file. The file size is verified when you use the upload URL.
        # 
        # This parameter is required.
        self.file_size_bytes = file_size_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size_bytes is not None:
            result['FileSizeBytes'] = self.file_size_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSizeBytes') is not None:
            self.file_size_bytes = m.get('FileSizeBytes')

        return self

