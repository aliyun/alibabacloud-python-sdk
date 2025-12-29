# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class InstanceLifecycleConfig(DaraModel):
    def __init__(
        self,
        pre_freeze: main_models.LifecycleHook = None,
        pre_stop: main_models.LifecycleHook = None,
    ):
        self.pre_freeze = pre_freeze
        self.pre_stop = pre_stop

    def validate(self):
        if self.pre_freeze:
            self.pre_freeze.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pre_freeze is not None:
            result['preFreeze'] = self.pre_freeze.to_map()

        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('preFreeze') is not None:
            temp_model = main_models.LifecycleHook()
            self.pre_freeze = temp_model.from_map(m.get('preFreeze'))

        if m.get('preStop') is not None:
            temp_model = main_models.LifecycleHook()
            self.pre_stop = temp_model.from_map(m.get('preStop'))

        return self

