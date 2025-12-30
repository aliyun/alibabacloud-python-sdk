# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MediaConvertVolume(DaraModel):
    def __init__(
        self,
        integrated_loudness_target: int = None,
        level: int = None,
        loudness_range_target: int = None,
        method: str = None,
        true_peak: int = None,
    ):
        self.integrated_loudness_target = integrated_loudness_target
        self.level = level
        self.loudness_range_target = loudness_range_target
        self.method = method
        self.true_peak = true_peak

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.integrated_loudness_target is not None:
            result['IntegratedLoudnessTarget'] = self.integrated_loudness_target

        if self.level is not None:
            result['Level'] = self.level

        if self.loudness_range_target is not None:
            result['LoudnessRangeTarget'] = self.loudness_range_target

        if self.method is not None:
            result['Method'] = self.method

        if self.true_peak is not None:
            result['TruePeak'] = self.true_peak

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntegratedLoudnessTarget') is not None:
            self.integrated_loudness_target = m.get('IntegratedLoudnessTarget')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LoudnessRangeTarget') is not None:
            self.loudness_range_target = m.get('LoudnessRangeTarget')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('TruePeak') is not None:
            self.true_peak = m.get('TruePeak')

        return self

