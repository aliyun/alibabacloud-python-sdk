# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class AlertRuleLabelFilter(DaraModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        opt: str = None,
    ):
        self.labels = labels
        self.opt = opt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['labels'] = self.labels

        if self.opt is not None:
            result['opt'] = self.opt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('opt') is not None:
            self.opt = m.get('opt')

        return self

