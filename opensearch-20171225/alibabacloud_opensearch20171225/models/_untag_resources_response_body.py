# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesResponseBody(DaraModel):
    def __init__(
        self,
        tequest_id: str = None,
    ):
        # The ID of the request.
        self.tequest_id = tequest_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tequest_id is not None:
            result['tequestId'] = self.tequest_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tequestId') is not None:
            self.tequest_id = m.get('tequestId')

        return self

