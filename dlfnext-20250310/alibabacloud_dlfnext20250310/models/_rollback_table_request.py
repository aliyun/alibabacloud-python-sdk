# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class RollbackTableRequest(DaraModel):
    def __init__(
        self,
        instant: main_models.FullInstant = None,
    ):
        self.instant = instant

    def validate(self):
        if self.instant:
            self.instant.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instant is not None:
            result['instant'] = self.instant.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instant') is not None:
            temp_model = main_models.FullInstant()
            self.instant = temp_model.from_map(m.get('instant'))

        return self

