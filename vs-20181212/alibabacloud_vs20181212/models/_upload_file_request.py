# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadFileRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_name: str = None,
        md_5: str = None,
        origin_url: str = None,
        target_path: str = None,
    ):
        # The description of the file.
        self.description = description
        # A custom file name. The name must be unique and serves as a unique identifier for the file. The name must meet the following requirements:
        # 
        # 1. It must be 8 to 255 characters in length.
        # 
        # 2. It can contain lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 
        # 3. The first and last characters must be a letter or a digit.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The MD5 hash of the file. This is used to verify the integrity of the file.
        # 
        # This parameter is required.
        self.md_5 = md_5
        # The download URL of the file.
        # 
        # This parameter is required.
        self.origin_url = origin_url
        # The destination path on the service instance. This must be an absolute path to a file. You cannot specify only a folder. The parent folder of the destination path is restricted to the following locations:
        # 
        # 1. /data/local
        # 
        # 2. /data/user
        # 
        # 3. /data/data
        # 
        # 4. /data/cache
        # 
        # 5. /data/tmp
        # 
        # 6. /data/storage
        # 
        # 7. /data/media/0
        # 
        # This parameter is required.
        self.target_path = target_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.origin_url is not None:
            result['OriginUrl'] = self.origin_url

        if self.target_path is not None:
            result['TargetPath'] = self.target_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('OriginUrl') is not None:
            self.origin_url = m.get('OriginUrl')

        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')

        return self

