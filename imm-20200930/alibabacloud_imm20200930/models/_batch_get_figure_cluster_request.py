# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchGetFigureClusterRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        object_ids: List[str] = None,
        project_name: str = None,
    ):
        # The name of the dataset.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The cluster IDs.
        # 
        # This parameter is required.
        self.object_ids = object_ids
        # The name of the project.
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

        if self.object_ids is not None:
            result['ObjectIds'] = self.object_ids

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ObjectIds') is not None:
            self.object_ids = m.get('ObjectIds')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

