# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetFigureClusterResponseBody(DaraModel):
    def __init__(
        self,
        figure_cluster: main_models.FigureCluster = None,
        request_id: str = None,
    ):
        # The information about the face cluster.
        self.figure_cluster = figure_cluster
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.figure_cluster:
            self.figure_cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.figure_cluster is not None:
            result['FigureCluster'] = self.figure_cluster.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureCluster') is not None:
            temp_model = main_models.FigureCluster()
            self.figure_cluster = temp_model.from_map(m.get('FigureCluster'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

