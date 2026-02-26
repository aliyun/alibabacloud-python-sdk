# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class UpdateFigureClusterRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        figure_cluster: main_models.FigureClusterForReq = None,
        project_name: str = None,
    ):
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The information about the cluster.
        # 
        # This parameter is required.
        self.figure_cluster = figure_cluster
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('FigureCluster') is not None:
            temp_model = main_models.FigureClusterForReq()
            self.figure_cluster = temp_model.from_map(m.get('FigureCluster'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

