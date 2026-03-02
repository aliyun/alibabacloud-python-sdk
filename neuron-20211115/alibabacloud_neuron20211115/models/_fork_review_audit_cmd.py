# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForkReviewAuditCmd(DaraModel):
    def __init__(
        self,
        approve: bool = None,
    ):
        self.approve = approve

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve is not None:
            result['approve'] = self.approve

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approve') is not None:
            self.approve = m.get('approve')

        return self

