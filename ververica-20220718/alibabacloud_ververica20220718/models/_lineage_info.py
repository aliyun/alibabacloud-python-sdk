# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class LineageInfo(DaraModel):
    def __init__(
        self,
        edges: main_models.Edge = None,
        job_infos: List[main_models.JobInfo] = None,
        nodes: List[main_models.Node] = None,
    ):
        # The edge information.
        self.edges = edges
        # The deployments.
        self.job_infos = job_infos
        # The nodes.
        self.nodes = nodes

    def validate(self):
        if self.edges:
            self.edges.validate()
        if self.job_infos:
            for v1 in self.job_infos:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edges is not None:
            result['edges'] = self.edges.to_map()

        result['jobInfos'] = []
        if self.job_infos is not None:
            for k1 in self.job_infos:
                result['jobInfos'].append(k1.to_map() if k1 else None)

        result['nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edges') is not None:
            temp_model = main_models.Edge()
            self.edges = temp_model.from_map(m.get('edges'))

        self.job_infos = []
        if m.get('jobInfos') is not None:
            for k1 in m.get('jobInfos'):
                temp_model = main_models.JobInfo()
                self.job_infos.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('nodes') is not None:
            for k1 in m.get('nodes'):
                temp_model = main_models.Node()
                self.nodes.append(temp_model.from_map(k1))

        return self

