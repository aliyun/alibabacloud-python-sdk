# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class UpdateTemplateInput(DaraModel):
    def __init__(
        self,
        log_configuration: main_models.LogConfiguration = None,
    ):
        self.log_configuration = log_configuration

    def validate(self):
        if self.log_configuration:
            self.log_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        return self

