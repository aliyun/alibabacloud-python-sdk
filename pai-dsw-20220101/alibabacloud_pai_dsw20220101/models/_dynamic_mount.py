# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class DynamicMount(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        mount_points: List[main_models.DynamicMountPoint] = None,
    ):
        self.enable = enable
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
        if self.enable is not None:
            result['Enable'] = self.enable

        result['MountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['MountPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k1 in m.get('MountPoints'):
                temp_model = main_models.DynamicMountPoint()
                self.mount_points.append(temp_model.from_map(k1))

        return self

