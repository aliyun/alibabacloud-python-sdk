# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class InstanceLifecycleConfig(DaraModel):
    def __init__(
        self,
        initializer: main_models.LifecycleHook = None,
        pre_stop: main_models.LifecycleHook = None,
    ):
        self.initializer = initializer
        self.pre_stop = pre_stop

    def validate(self):
        if self.initializer:
            self.initializer.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.initializer is not None:
            result['initializer'] = self.initializer.to_map()

        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('initializer') is not None:
            temp_model = main_models.LifecycleHook()
            self.initializer = temp_model.from_map(m.get('initializer'))

        if m.get('preStop') is not None:
            temp_model = main_models.LifecycleHook()
            self.pre_stop = temp_model.from_map(m.get('preStop'))

        return self

