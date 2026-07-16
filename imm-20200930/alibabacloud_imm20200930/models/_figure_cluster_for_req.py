# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class FigureClusterForReq(DaraModel):
    def __init__(
        self,
        cover: main_models.FigureClusterForReqCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        meta_lock_version: int = None,
        name: str = None,
        object_id: str = None,
    ):
        # The cover of the cluster.
        self.cover = cover
        # The custom ID.
        self.custom_id = custom_id
        # A key-value map of custom labels that can be used to search for the figure cluster.
        self.custom_labels = custom_labels
        # The metadata lock version. This parameter enables optimistic locking to prevent conflicting updates during high concurrency. To ensure data consistency, pass the current MetaLockVersion value when updating a figure cluster. You can retrieve this value from a Get or List operation. The service proceeds with the update only if the provided version matches the system\\"s current version. The initial value is 0 and is incremented by 1 after each successful update.
        self.meta_lock_version = meta_lock_version
        # The cluster name.
        self.name = name
        # The object ID of the cluster.
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

        if self.meta_lock_version is not None:
            result['MetaLockVersion'] = self.meta_lock_version

        if self.name is not None:
            result['Name'] = self.name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            temp_model = main_models.FigureClusterForReqCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('MetaLockVersion') is not None:
            self.meta_lock_version = m.get('MetaLockVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        return self

class FigureClusterForReqCover(DaraModel):
    def __init__(
        self,
        figures: List[main_models.FigureClusterForReqCoverFigures] = None,
    ):
        # The figure list.
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
                temp_model = main_models.FigureClusterForReqCoverFigures()
                self.figures.append(temp_model.from_map(k1))

        return self

class FigureClusterForReqCoverFigures(DaraModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # The figure ID.
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

