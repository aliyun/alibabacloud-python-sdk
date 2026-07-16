# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class RunStrategies(DaraModel):
    def __init__(
        self,
        backfill: main_models.BackfillStrategy = None,
        continuous: main_models.ContinuousStrategy = None,
    ):
        self.backfill = backfill
        self.continuous = continuous

    def validate(self):
        if self.backfill:
            self.backfill.validate()
        if self.continuous:
            self.continuous.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backfill is not None:
            result['backfill'] = self.backfill.to_map()

        if self.continuous is not None:
            result['continuous'] = self.continuous.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('backfill') is not None:
            temp_model = main_models.BackfillStrategy()
            self.backfill = temp_model.from_map(m.get('backfill'))

        if m.get('continuous') is not None:
            temp_model = main_models.ContinuousStrategy()
            self.continuous = temp_model.from_map(m.get('continuous'))

        return self

