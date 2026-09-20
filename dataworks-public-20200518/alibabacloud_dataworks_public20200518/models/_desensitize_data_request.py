# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DesensitizeDataRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        scene_code: str = None,
    ):
        # The input data to be masked.
        # 
        # This parameter is required.
        self.data = data
        # The masking scene code. You can view this on the Data Masking Management page of DataWorks Data Protection Umbrella in the DataWorks console.
        # 
        # You can obtain this value from Data[].SceneCode in the response of DsgSceneQuerySceneListByName.
        # 
        # This parameter is required.
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

