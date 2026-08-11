# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class UpdateModelPermissionsRequest(DaraModel):
    def __init__(
        self,
        access_all_entities: str = None,
        models: List[main_models.UpdateModelPermissionsRequestModels] = None,
        workspace_id: str = None,
    ):
        self.access_all_entities = access_all_entities
        self.models = models
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_all_entities is not None:
            result['accessAllEntities'] = self.access_all_entities

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessAllEntities') is not None:
            self.access_all_entities = m.get('accessAllEntities')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.UpdateModelPermissionsRequestModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateModelPermissionsRequestModels(DaraModel):
    def __init__(
        self,
        deploy: bool = None,
        fine_tune: bool = None,
        inference: bool = None,
        model: str = None,
    ):
        self.deploy = deploy
        self.fine_tune = fine_tune
        self.inference = inference
        # This parameter is required.
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy is not None:
            result['deploy'] = self.deploy

        if self.fine_tune is not None:
            result['fineTune'] = self.fine_tune

        if self.inference is not None:
            result['inference'] = self.inference

        if self.model is not None:
            result['model'] = self.model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploy') is not None:
            self.deploy = m.get('deploy')

        if m.get('fineTune') is not None:
            self.fine_tune = m.get('fineTune')

        if m.get('inference') is not None:
            self.inference = m.get('inference')

        if m.get('model') is not None:
            self.model = m.get('model')

        return self

