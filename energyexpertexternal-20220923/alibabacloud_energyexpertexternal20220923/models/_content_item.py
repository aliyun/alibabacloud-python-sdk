# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ContentItem(DaraModel):
    def __init__(
        self,
        ext_info: List[main_models.ContentItemExtInfo] = None,
        score: float = None,
        text: str = None,
        type: str = None,
    ):
        self.ext_info = ext_info
        self.score = score
        self.text = text
        self.type = type

    def validate(self):
        if self.ext_info:
            for v1 in self.ext_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extInfo'] = []
        if self.ext_info is not None:
            for k1 in self.ext_info:
                result['extInfo'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['score'] = self.score

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ext_info = []
        if m.get('extInfo') is not None:
            for k1 in m.get('extInfo'):
                temp_model = main_models.ContentItemExtInfo()
                self.ext_info.append(temp_model.from_map(k1))

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ContentItemExtInfo(DaraModel):
    def __init__(
        self,
        alignment: str = None,
        index: int = None,
        level: int = None,
        page_num: List[int] = None,
        pos: List[main_models.ContentItemExtInfoPos] = None,
        sub_type: str = None,
        text: str = None,
        type: str = None,
        unique_id: str = None,
    ):
        self.alignment = alignment
        self.index = index
        self.level = level
        self.page_num = page_num
        self.pos = pos
        self.sub_type = sub_type
        self.text = text
        self.type = type
        self.unique_id = unique_id

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alignment is not None:
            result['alignment'] = self.alignment

        if self.index is not None:
            result['index'] = self.index

        if self.level is not None:
            result['level'] = self.level

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                result['pos'].append(k1.to_map() if k1 else None)

        if self.sub_type is not None:
            result['subType'] = self.sub_type

        if self.text is not None:
            result['text'] = self.text

        if self.type is not None:
            result['type'] = self.type

        if self.unique_id is not None:
            result['uniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignment') is not None:
            self.alignment = m.get('alignment')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                temp_model = main_models.ContentItemExtInfoPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('uniqueId') is not None:
            self.unique_id = m.get('uniqueId')

        return self

class ContentItemExtInfoPos(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

