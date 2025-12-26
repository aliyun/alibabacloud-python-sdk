# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class Rules(DaraModel):
    def __init__(
        self,
        scheduling: main_models.SchedulingRule = None,
    ):
        self.scheduling = scheduling

    def validate(self):
        if self.scheduling:
            self.scheduling.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheduling is not None:
            result['Scheduling'] = self.scheduling.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scheduling') is not None:
            temp_model = main_models.SchedulingRule()
            self.scheduling = temp_model.from_map(m.get('Scheduling'))

        return self

