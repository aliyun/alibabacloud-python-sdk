# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFileInfoRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_id: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_id is not None:
            result['FileId'] = self.file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        return self

