# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUnknownThreatDetectStrategyRequest(DaraModel):
    def __init__(
        self,
        asset_selection_type: str = None,
        duration_days_after_init: int = None,
        duration_days_after_stop: int = None,
        name: str = None,
        study_mode: str = None,
    ):
        # The asset selection type.
        self.asset_selection_type = asset_selection_type
        # The duration of the initial learning period, in days.
        self.duration_days_after_init = duration_days_after_init
        # The number of consecutive days without detecting new processes before the learning process stops.
        self.duration_days_after_stop = duration_days_after_stop
        # The strategy name.
        self.name = name
        # The whitelist mode. Valid values:
        # 
        # - **hash**: The process hash.
        # 
        # - **path**: The process path.
        self.study_mode = study_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_selection_type is not None:
            result['AssetSelectionType'] = self.asset_selection_type

        if self.duration_days_after_init is not None:
            result['DurationDaysAfterInit'] = self.duration_days_after_init

        if self.duration_days_after_stop is not None:
            result['DurationDaysAfterStop'] = self.duration_days_after_stop

        if self.name is not None:
            result['Name'] = self.name

        if self.study_mode is not None:
            result['StudyMode'] = self.study_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSelectionType') is not None:
            self.asset_selection_type = m.get('AssetSelectionType')

        if m.get('DurationDaysAfterInit') is not None:
            self.duration_days_after_init = m.get('DurationDaysAfterInit')

        if m.get('DurationDaysAfterStop') is not None:
            self.duration_days_after_stop = m.get('DurationDaysAfterStop')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StudyMode') is not None:
            self.study_mode = m.get('StudyMode')

        return self

