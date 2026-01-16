# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class OSSTriggerConfig(DaraModel):
    def __init__(
        self,
        events: List[str] = None,
        filter: main_models.Filter = None,
    ):
        self.events = events
        self.filter = filter

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.events is not None:
            result['events'] = self.events

        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('events') is not None:
            self.events = m.get('events')

        if m.get('filter') is not None:
            temp_model = main_models.Filter()
            self.filter = temp_model.from_map(m.get('filter'))

        return self

