# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMaterialFileRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        directory_id: str = None,
        file_url: str = None,
        name: str = None,
        oss_key: str = None,
    ):
        # The business ID of the application instance.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        # The ID of the parent folder.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The file path.
        self.file_url = file_url
        # The file name.
        self.name = name
        # The OSS object key.
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        return self

