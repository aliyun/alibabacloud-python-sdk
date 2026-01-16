# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FunctionRestriction(DaraModel):
    def __init__(
        self,
        disable: bool = None,
        last_modified_time: str = None,
        reason: str = None,
    ):
        self.disable = disable
        self.last_modified_time = last_modified_time
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable is not None:
            result['disable'] = self.disable

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

