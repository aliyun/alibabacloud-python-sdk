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
        self.description = description
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.md_5 = md_5
        # This parameter is required.
        self.origin_url = origin_url
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

