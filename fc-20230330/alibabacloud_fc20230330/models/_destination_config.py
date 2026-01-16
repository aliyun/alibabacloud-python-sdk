# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class DestinationConfig(DaraModel):
    def __init__(
        self,
        on_failure: main_models.Destination = None,
        on_success: main_models.Destination = None,
    ):
        self.on_failure = on_failure
        self.on_success = on_success

    def validate(self):
        if self.on_failure:
            self.on_failure.validate()
        if self.on_success:
            self.on_success.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.on_failure is not None:
            result['onFailure'] = self.on_failure.to_map()

        if self.on_success is not None:
            result['onSuccess'] = self.on_success.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onFailure') is not None:
            temp_model = main_models.Destination()
            self.on_failure = temp_model.from_map(m.get('onFailure'))

        if m.get('onSuccess') is not None:
            temp_model = main_models.Destination()
            self.on_success = temp_model.from_map(m.get('onSuccess'))

        return self

