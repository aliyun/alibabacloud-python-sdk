# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyDisplayConfigRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        display_config: main_models.ModifyDisplayConfigRequestDisplayConfig = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.display_config = display_config

    def validate(self):
        if self.display_config:
            self.display_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('DisplayConfig') is not None:
            temp_model = main_models.ModifyDisplayConfigRequestDisplayConfig()
            self.display_config = temp_model.from_map(m.get('DisplayConfig'))

        return self

class ModifyDisplayConfigRequestDisplayConfig(DaraModel):
    def __init__(
        self,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.dpi = dpi
        self.fps = fps
        self.lock_resolution = lock_resolution
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi is not None:
            result['Dpi'] = self.dpi

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dpi') is not None:
            self.dpi = m.get('Dpi')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        return self

