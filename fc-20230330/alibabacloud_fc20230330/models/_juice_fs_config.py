# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class JuiceFsConfig(DaraModel):
    def __init__(
        self,
        envs: Dict[str, str] = None,
        mount_points: List[main_models.JuiceFsMountConfig] = None,
    ):
        self.envs = envs
        self.mount_points = mount_points

    def validate(self):
        if self.mount_points:
            for v1 in self.mount_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.envs is not None:
            result['envs'] = self.envs

        result['mountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['mountPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('envs') is not None:
            self.envs = m.get('envs')

        self.mount_points = []
        if m.get('mountPoints') is not None:
            for k1 in m.get('mountPoints'):
                temp_model = main_models.JuiceFsMountConfig()
                self.mount_points.append(temp_model.from_map(k1))

        return self

