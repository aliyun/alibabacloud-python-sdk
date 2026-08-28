# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentSpecImportFileUrlRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
    ):
        # The Content-Type of the file to upload. The client must use the same value from the response when performing the PUT request.
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        return self

