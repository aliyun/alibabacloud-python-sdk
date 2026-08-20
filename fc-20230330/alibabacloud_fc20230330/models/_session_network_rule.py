# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class SessionNetworkRule(DaraModel):
    def __init__(
        self,
        transform: main_models.SessionNetworkRuleTransform = None,
    ):
        self.transform = transform

    def validate(self):
        if self.transform:
            self.transform.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transform is not None:
            result['transform'] = self.transform.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('transform') is not None:
            temp_model = main_models.SessionNetworkRuleTransform()
            self.transform = temp_model.from_map(m.get('transform'))

        return self

