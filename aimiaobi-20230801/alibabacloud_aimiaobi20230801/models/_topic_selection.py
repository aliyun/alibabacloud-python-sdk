# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class TopicSelection(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.TopicSelectionOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.TopicSelectionOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class TopicSelectionOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

