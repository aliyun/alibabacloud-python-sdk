# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Label(DaraModel):
    def __init__(
        self,
        centric_score: float = None,
        clips: List[main_models.Clip] = None,
        label_alias: str = None,
        label_confidence: float = None,
        label_level: int = None,
        label_name: str = None,
        language: str = None,
        parent_label_name: str = None,
    ):
        # The centric score of the tag. This indicates whether the tag is the main subject in the image. The value ranges from 0 to 1. A higher value indicates higher confidence that the tag is the main subject of the image.
        self.centric_score = centric_score
        # Event clips.
        self.clips = clips
        # The tag alias.
        self.label_alias = label_alias
        # The tag confidence level. The value ranges from 0 (lowest confidence) to 1 (highest confidence).
        self.label_confidence = label_confidence
        # The tag level. Valid values are 1, 2, and 3, representing first-level, second-level, and third-level tags, respectively.
        self.label_level = label_level
        # The tag name.
        self.label_name = label_name
        # The tag language, in BCP 47 format.
        self.language = language
        # The parent tag name.
        self.parent_label_name = parent_label_name

    def validate(self):
        if self.clips:
            for v1 in self.clips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.centric_score is not None:
            result['CentricScore'] = self.centric_score

        result['Clips'] = []
        if self.clips is not None:
            for k1 in self.clips:
                result['Clips'].append(k1.to_map() if k1 else None)

        if self.label_alias is not None:
            result['LabelAlias'] = self.label_alias

        if self.label_confidence is not None:
            result['LabelConfidence'] = self.label_confidence

        if self.label_level is not None:
            result['LabelLevel'] = self.label_level

        if self.label_name is not None:
            result['LabelName'] = self.label_name

        if self.language is not None:
            result['Language'] = self.language

        if self.parent_label_name is not None:
            result['ParentLabelName'] = self.parent_label_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CentricScore') is not None:
            self.centric_score = m.get('CentricScore')

        self.clips = []
        if m.get('Clips') is not None:
            for k1 in m.get('Clips'):
                temp_model = main_models.Clip()
                self.clips.append(temp_model.from_map(k1))

        if m.get('LabelAlias') is not None:
            self.label_alias = m.get('LabelAlias')

        if m.get('LabelConfidence') is not None:
            self.label_confidence = m.get('LabelConfidence')

        if m.get('LabelLevel') is not None:
            self.label_level = m.get('LabelLevel')

        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ParentLabelName') is not None:
            self.parent_label_name = m.get('ParentLabelName')

        return self

