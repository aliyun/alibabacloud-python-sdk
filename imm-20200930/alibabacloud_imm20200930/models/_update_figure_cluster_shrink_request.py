# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFigureClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        figure_cluster_shrink: str = None,
        project_name: str = None,
    ):
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The information about the cluster.
        # 
        # This parameter is required.
        self.figure_cluster_shrink = figure_cluster_shrink
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

        if self.figure_cluster_shrink is not None:
            result['FigureCluster'] = self.figure_cluster_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('FigureCluster') is not None:
            self.figure_cluster_shrink = m.get('FigureCluster')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

