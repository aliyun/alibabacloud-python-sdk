# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConfigResponseBody(DaraModel):
    def __init__(
        self,
        deleted: int = None,
        message: str = None,
    ):
        # The number of configurations deleted.
        self.deleted = deleted
        # A message indicating the operation result.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted is not None:
            result['deleted'] = self.deleted

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

