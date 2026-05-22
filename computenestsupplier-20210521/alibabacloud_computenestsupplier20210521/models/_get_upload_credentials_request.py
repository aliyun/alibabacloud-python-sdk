# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUploadCredentialsRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        visibility: str = None,
    ):
        # The file name to upload.
        # 
        # This parameter is required.
        self.file_name = file_name
        # Specifies whether the file is publicly accessible. Valid values: **public** or **private**. The default value is **private**.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

