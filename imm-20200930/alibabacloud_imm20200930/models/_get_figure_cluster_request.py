# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFigureClusterRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
    ):
        # The dataset name.[](~~CreateDataset~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The ID of the face clustering task. You can obtain the ID from the face clustering information returned after you call the [QueryFigureClusters](~~QueryFigureClusters~~) operation.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The project name.[](~~CreateProject~~)
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

