# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ClusterForReq(DaraModel):
    def __init__(
        self,
        cover: main_models.ClusterForReqCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        name: str = None,
        object_id: str = None,
    ):
        # The cover.
        self.cover = cover
        # The custom ID.
        self.custom_id = custom_id
        # The custom labels.
        self.custom_labels = custom_labels
        # The name of the cluster.
        self.name = name
        # The ID of the cluster.
        self.object_id = object_id

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.name is not None:
            result['Name'] = self.name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = main_models.ClusterForReqCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        return self

class ClusterForReqCover(DaraModel):
    def __init__(
        self,
        figures: List[main_models.ClusterForReqCoverFigures] = None,
    ):
        # The persons.
        self.figures = figures

    def validate(self):
        if self.figures:
            for v1 in self.figures:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Figures'] = []
        if self.figures is not None:
            for k1 in self.figures:
                result['Figures'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.figures = []
        if m.get('Figures') is not None:
            for k1 in m.get('Figures'):
                temp_model = main_models.ClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k1))

        return self



class ClusterForReqCoverFigures(DaraModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # The person ID.
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')

        return self

