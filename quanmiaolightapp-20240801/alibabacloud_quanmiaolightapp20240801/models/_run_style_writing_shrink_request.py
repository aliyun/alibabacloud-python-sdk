# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunStyleWritingShrinkRequest(DaraModel):
    def __init__(
        self,
        learning_samples_shrink: str = None,
        process_stage: str = None,
        reference_materials_shrink: str = None,
        style_feature: str = None,
        use_search: bool = None,
        writing_theme: str = None,
    ):
        self.learning_samples_shrink = learning_samples_shrink
        self.process_stage = process_stage
        self.reference_materials_shrink = reference_materials_shrink
        self.style_feature = style_feature
        self.use_search = use_search
        self.writing_theme = writing_theme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.learning_samples_shrink is not None:
            result['learningSamples'] = self.learning_samples_shrink

        if self.process_stage is not None:
            result['processStage'] = self.process_stage

        if self.reference_materials_shrink is not None:
            result['referenceMaterials'] = self.reference_materials_shrink

        if self.style_feature is not None:
            result['styleFeature'] = self.style_feature

        if self.use_search is not None:
            result['useSearch'] = self.use_search

        if self.writing_theme is not None:
            result['writingTheme'] = self.writing_theme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('learningSamples') is not None:
            self.learning_samples_shrink = m.get('learningSamples')

        if m.get('processStage') is not None:
            self.process_stage = m.get('processStage')

        if m.get('referenceMaterials') is not None:
            self.reference_materials_shrink = m.get('referenceMaterials')

        if m.get('styleFeature') is not None:
            self.style_feature = m.get('styleFeature')

        if m.get('useSearch') is not None:
            self.use_search = m.get('useSearch')

        if m.get('writingTheme') is not None:
            self.writing_theme = m.get('writingTheme')

        return self

