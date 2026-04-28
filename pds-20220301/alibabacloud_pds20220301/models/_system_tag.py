# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SystemTag(DaraModel):
    def __init__(
        self,
        centric_score: float = None,
        confidence: float = None,
        name: str = None,
        parent_name: str = None,
        tag_level: int = None,
    ):
        # The center value of the tag, which specifies whether the tag is the subject in the image. Valid values: 0 to 1. A value of 0 specifies the lowest proportion. A value of 1 specifies the highest proportion.
        self.centric_score = centric_score
        # The confidence level of the tag. Valid values: 0 to 1. A value of 0 specifies the lowest confidence level. A value of 1 specifies the highest confidence level.
        self.confidence = confidence
        # The name of the tag.
        self.name = name
        # The name of the parent tag of the tag.
        self.parent_name = parent_name
        # The level of the tag. The value must be greater than or equal to 1.
        self.tag_level = tag_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.centric_score is not None:
            result['centric_score'] = self.centric_score

        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.name is not None:
            result['name'] = self.name

        if self.parent_name is not None:
            result['parent_name'] = self.parent_name

        if self.tag_level is not None:
            result['tag_level'] = self.tag_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centric_score') is not None:
            self.centric_score = m.get('centric_score')

        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parent_name') is not None:
            self.parent_name = m.get('parent_name')

        if m.get('tag_level') is not None:
            self.tag_level = m.get('tag_level')

        return self

