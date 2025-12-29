# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebOSSConfig(DaraModel):
    def __init__(
        self,
        mount_points: List[main_models.WebOSSMountPoint] = None,
    ):
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
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k1 in self.mount_points:
                result['MountPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k1 in m.get('MountPoints'):
                temp_model = main_models.WebOSSMountPoint()
                self.mount_points.append(temp_model.from_map(k1))

        return self

