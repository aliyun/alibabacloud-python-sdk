# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddKnowledgeFileResponseBody(DaraModel):
    def __init__(
        self,
        id: int = None,
        location: str = None,
        request_id: str = None,
    ):
        # The ID of the imported file.
        self.id = id
        # The location of the imported file.
        self.location = location
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.location is not None:
            result['Location'] = self.location

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

