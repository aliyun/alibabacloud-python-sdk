# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLProgressSlow(DaraModel):
    def __init__(
        self,
        details: List[main_models.RLProgressSlowDetail] = None,
        elapsed: float = None,
        time: int = None,
    ):
        # The slow inference details, up to 20 entries.
        self.details = details
        # The elapsed time of the slowest entry in seconds.
        self.elapsed = elapsed
        # The log timestamp of the slowest entry in UNIX seconds.
        self.time = time

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.elapsed is not None:
            result['Elapsed'] = self.elapsed

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.RLProgressSlowDetail()
                self.details.append(temp_model.from_map(k1))

        if m.get('Elapsed') is not None:
            self.elapsed = m.get('Elapsed')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

