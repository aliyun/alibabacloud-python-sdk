# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DsgDesensPlanUpdateStatusRequest(DaraModel):
    def __init__(
        self,
        ids: List[int] = None,
        scene_code: str = None,
        status: int = None,
    ):
        # A collection of IDs of the data masking rules of which the status you want to modify.
        # 
        # This parameter is required.
        self.ids = ids
        # The code of the level-1 data masking scenario to which the rule belongs. Valid values:
        # 
        # *   dataworks_display_desense_code: masking of displayed data in DataStudio and Data Map
        # *   maxcompute_desense_code: data masking at the MaxCompute compute engine layer
        # *   maxcompute_new_desense_code: data masking at the MaxCompute compute engine layer (new)
        # *   hologres_display_desense_code: data masking at the Hologres compute engine layer
        # *   dataworks_data_integration_desense_code: static data masking in Data Integration
        # *   dataworks_analysis_desense_code: masking of displayed data in DataAnalysis
        # 
        # This parameter is required.
        self.scene_code = scene_code
        # The status of the data masking rule. Valid values:
        # 
        # *   0: expired
        # *   1: effective
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

