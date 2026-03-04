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
        # The output volume.
        # 
        # *   This parameter takes effect only if Method is set to dynamic.
        # *   Unit: dB.
        # *   Valid values: [-70,-5].
        # *   Default value: -6.
        self.integrated_loudness_target = integrated_loudness_target
        # The amount of gain to apply, relative to the input audio.
        # 
        # *   This parameter takes effect only if Method is set to linear.
        # *   Unit: dB.
        # *   Valid values: less than or equal to 20.
        # *   Default value: -20.
        self.level = level
        # The target loudness range.
        # 
        # *   This parameter takes effect only if Method is set to dynamic.
        # *   Unit: dB.
        # *   Valid values: [1,20].
        # *   Default value: 8.
        self.loudness_range_target = loudness_range_target
        # The volume adjustment method. Valid values:
        # 
        # *   auto
        # *   dynamic
        # *   linear
        # *   Default value: dynamic.
        # 
        # <!---->
        # 
        # *
        # *
        # *
        # *
        self.method = method
        # The maximum volume.
        # 
        # *   This parameter takes effect only if Method is set to dynamic.
        # *   Unit: dB.
        # *   Valid values: [-9,0].
        # *   Default value: -1.
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

