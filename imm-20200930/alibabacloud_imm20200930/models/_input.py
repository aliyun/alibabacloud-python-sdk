# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Input(DaraModel):
    def __init__(
        self,
        oss: main_models.InputOSS = None,
    ):
        # The input data source from Object Storage Service (OSS).
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss is not None:
            result['OSS'] = self.oss.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSS') is not None:
            temp_model = main_models.InputOSS()
            self.oss = temp_model.from_map(m.get('OSS'))

        return self

