# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssUploadTokenRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_type: str = None,
        upload_type: int = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.upload_type is not None:
            result['uploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('uploadType') is not None:
            self.upload_type = m.get('uploadType')

        return self

