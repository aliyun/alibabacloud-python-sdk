# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobRequest(DaraModel):
    def __init__(
        self,
        by_version: str = None,
    ):
        # Specifies whether to obtain the details of the migration task by using the task ID.
        self.by_version = by_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.by_version is not None:
            result['byVersion'] = self.by_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('byVersion') is not None:
            self.by_version = m.get('byVersion')

        return self

