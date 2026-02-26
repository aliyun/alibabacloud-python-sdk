# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchUpdateFileMetaShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        files_shrink: str = None,
        project_name: str = None,
    ):
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The files whose metadata you want to update.
        # 
        # This parameter is required.
        self.files_shrink = files_shrink
        # The name of the project.[](~~478153~~)
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

        if self.files_shrink is not None:
            result['Files'] = self.files_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

