# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUnknownThreatDetectStrategyRequest(DaraModel):
    def __init__(
        self,
        duration_days_after_init: int = None,
        duration_days_after_stop: int = None,
        id: str = None,
        name: str = None,
        study_mode: str = None,
    ):
        self.duration_days_after_init = duration_days_after_init
        self.duration_days_after_stop = duration_days_after_stop
        # This parameter is required.
        self.id = id
        self.name = name
        self.study_mode = study_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_days_after_init is not None:
            result['DurationDaysAfterInit'] = self.duration_days_after_init

        if self.duration_days_after_stop is not None:
            result['DurationDaysAfterStop'] = self.duration_days_after_stop

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.study_mode is not None:
            result['StudyMode'] = self.study_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationDaysAfterInit') is not None:
            self.duration_days_after_init = m.get('DurationDaysAfterInit')

        if m.get('DurationDaysAfterStop') is not None:
            self.duration_days_after_stop = m.get('DurationDaysAfterStop')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StudyMode') is not None:
            self.study_mode = m.get('StudyMode')

        return self

