# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogicalModelRequest(DaraModel):
    def __init__(
        self,
        expected_revision: int = None,
    ):
        # The expected object version number.
        # 
        # This parameter is required.
        self.expected_revision = expected_revision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expected_revision is not None:
            result['expectedRevision'] = self.expected_revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expectedRevision') is not None:
            self.expected_revision = m.get('expectedRevision')

        return self

