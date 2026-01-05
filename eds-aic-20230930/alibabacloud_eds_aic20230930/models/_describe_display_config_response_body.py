# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeDisplayConfigResponseBody(DaraModel):
    def __init__(
        self,
        display_config_model: List[main_models.DescribeDisplayConfigResponseBodyDisplayConfigModel] = None,
        request_id: str = None,
    ):
        self.display_config_model = display_config_model
        self.request_id = request_id

    def validate(self):
        if self.display_config_model:
            for v1 in self.display_config_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DisplayConfigModel'] = []
        if self.display_config_model is not None:
            for k1 in self.display_config_model:
                result['DisplayConfigModel'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.display_config_model = []
        if m.get('DisplayConfigModel') is not None:
            for k1 in m.get('DisplayConfigModel'):
                temp_model = main_models.DescribeDisplayConfigResponseBodyDisplayConfigModel()
                self.display_config_model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDisplayConfigResponseBodyDisplayConfigModel(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        dpi: int = None,
        fps: int = None,
        lock_resolution: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
    ):
        self.android_instance_id = android_instance_id
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
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

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
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

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

