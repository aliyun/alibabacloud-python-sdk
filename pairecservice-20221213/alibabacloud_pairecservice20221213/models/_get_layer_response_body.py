# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLayerResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create_time: str = None,
        laboratory_id: str = None,
        name: str = None,
        request_id: str = None,
        residual_flow: int = None,
        scene_id: str = None,
    ):
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.laboratory_id = laboratory_id
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.residual_flow = residual_flow
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

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResidualFlow') is not None:
            self.residual_flow = m.get('ResidualFlow')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

