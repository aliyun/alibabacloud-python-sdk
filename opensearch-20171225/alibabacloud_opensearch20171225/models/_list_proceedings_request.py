# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProceedingsRequest(DaraModel):
    def __init__(
        self,
        filter_finished: bool = None,
    ):
        # Specifies whether the filtering is complete.
        self.filter_finished = filter_finished

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_finished is not None:
            result['filterFinished'] = self.filter_finished

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterFinished') is not None:
            self.filter_finished = m.get('filterFinished')

        return self

