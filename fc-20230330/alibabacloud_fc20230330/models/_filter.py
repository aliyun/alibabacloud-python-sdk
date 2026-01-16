# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class Filter(DaraModel):
    def __init__(
        self,
        key: main_models.Key = None,
    ):
        self.key = key

    def validate(self):
        if self.key:
            self.key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            temp_model = main_models.Key()
            self.key = temp_model.from_map(m.get('key'))

        return self

