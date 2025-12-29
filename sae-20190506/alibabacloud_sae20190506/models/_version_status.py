# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VersionStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

