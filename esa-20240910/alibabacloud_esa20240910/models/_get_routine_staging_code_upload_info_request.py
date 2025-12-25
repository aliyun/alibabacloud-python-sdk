# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoutineStagingCodeUploadInfoRequest(DaraModel):
    def __init__(
        self,
        code_description: str = None,
        name: str = None,
    ):
        # The code description.
        self.code_description = code_description
        # The routine name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

