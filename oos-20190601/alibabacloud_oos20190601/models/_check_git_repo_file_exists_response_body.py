# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckGitRepoFileExistsResponseBody(DaraModel):
    def __init__(
        self,
        file_exists: bool = None,
        request_id: str = None,
    ):
        self.file_exists = file_exists
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_exists is not None:
            result['FileExists'] = self.file_exists

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileExists') is not None:
            self.file_exists = m.get('FileExists')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

