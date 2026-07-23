# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListLayersResponseBody(DaraModel):
    def __init__(
        self,
        layers: List[main_models.ListLayersResponseBodyLayers] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array of layers.
        self.layers = layers
        # The request ID.
        self.request_id = request_id
        # The total count of layers.
        self.total_count = total_count

    def validate(self):
        if self.layers:
            for v1 in self.layers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Layers'] = []
        if self.layers is not None:
            for k1 in self.layers:
                result['Layers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layers = []
        if m.get('Layers') is not None:
            for k1 in m.get('Layers'):
                temp_model = main_models.ListLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLayersResponseBodyLayers(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create_time: str = None,
        laboratory_id: str = None,
        layer_id: str = None,
        name: str = None,
        residual_flow: int = None,
        scene_id: str = None,
    ):
        # The layer description.
        self.description = description
        # The time when the layer was created.
        self.gmt_create_time = gmt_create_time
        # The laboratory ID.
        self.laboratory_id = laboratory_id
        # The layer ID.
        self.layer_id = layer_id
        # The layer name.
        self.name = name
        # The remaining traffic for the layer.
        self.residual_flow = residual_flow
        # The scene ID.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.laboratory_id is not None:
            result['LaboratoryId'] = self.laboratory_id

        if self.layer_id is not None:
            result['LayerId'] = self.layer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.residual_flow is not None:
            result['ResidualFlow'] = self.residual_flow

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('LaboratoryId') is not None:
            self.laboratory_id = m.get('LaboratoryId')

        if m.get('LayerId') is not None:
            self.layer_id = m.get('LayerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResidualFlow') is not None:
            self.residual_flow = m.get('ResidualFlow')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

