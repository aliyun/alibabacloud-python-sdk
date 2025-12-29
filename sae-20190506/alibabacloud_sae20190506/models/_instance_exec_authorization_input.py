# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class InstanceExecAuthorizationInput(DaraModel):
    def __init__(
        self,
        options: main_models.InstanceExecAuthorizationInputOptions = None,
    ):
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.options is not None:
            result['options'] = self.options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            temp_model = main_models.InstanceExecAuthorizationInputOptions()
            self.options = temp_model.from_map(m.get('options'))

        return self

