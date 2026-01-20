# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListFeatureViewOnlineFeaturesRequest(DaraModel):
    def __init__(
        self,
        join_ids: List[str] = None,
    ):
        # This parameter is required.
        self.join_ids = join_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join_ids is not None:
            result['JoinIds'] = self.join_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinIds') is not None:
            self.join_ids = m.get('JoinIds')

        return self

