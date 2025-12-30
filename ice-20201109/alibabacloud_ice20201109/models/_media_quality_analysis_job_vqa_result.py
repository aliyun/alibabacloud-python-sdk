# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaQualityAnalysisJobVqaResult(DaraModel):
    def __init__(
        self,
        block: main_models.MediaQualityAnalysisJobVqaScoreDetail = None,
        color: main_models.MediaQualityAnalysisJobVqaScoreDetail = None,
        detail: main_models.MediaQualityAnalysisJobVqaScoreDetail = None,
        noise: main_models.MediaQualityAnalysisJobVqaScoreDetail = None,
        score_result: main_models.MediaQualityAnalysisJobVqaResultScoreResult = None,
        sharp: main_models.MediaQualityAnalysisJobVqaScoreDetail = None,
        state: str = None,
    ):
        self.block = block
        self.color = color
        self.detail = detail
        self.noise = noise
        self.score_result = score_result
        self.sharp = sharp
        self.state = state

    def validate(self):
        if self.block:
            self.block.validate()
        if self.color:
            self.color.validate()
        if self.detail:
            self.detail.validate()
        if self.noise:
            self.noise.validate()
        if self.score_result:
            self.score_result.validate()
        if self.sharp:
            self.sharp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block is not None:
            result['Block'] = self.block.to_map()

        if self.color is not None:
            result['Color'] = self.color.to_map()

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.noise is not None:
            result['Noise'] = self.noise.to_map()

        if self.score_result is not None:
            result['ScoreResult'] = self.score_result.to_map()

        if self.sharp is not None:
            result['Sharp'] = self.sharp.to_map()

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaScoreDetail()
            self.block = temp_model.from_map(m.get('Block'))

        if m.get('Color') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaScoreDetail()
            self.color = temp_model.from_map(m.get('Color'))

        if m.get('Detail') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaScoreDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Noise') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaScoreDetail()
            self.noise = temp_model.from_map(m.get('Noise'))

        if m.get('ScoreResult') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResultScoreResult()
            self.score_result = temp_model.from_map(m.get('ScoreResult'))

        if m.get('Sharp') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaScoreDetail()
            self.sharp = temp_model.from_map(m.get('Sharp'))

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class MediaQualityAnalysisJobVqaResultScoreResult(DaraModel):
    def __init__(
        self,
        block: main_models.MediaQualityAnalysisJobVqaResultScoreResultBlock = None,
        color: main_models.MediaQualityAnalysisJobVqaResultScoreResultColor = None,
        detail: main_models.MediaQualityAnalysisJobVqaResultScoreResultDetail = None,
        noise: main_models.MediaQualityAnalysisJobVqaResultScoreResultNoise = None,
        sharp: main_models.MediaQualityAnalysisJobVqaResultScoreResultSharp = None,
    ):
        self.block = block
        self.color = color
        self.detail = detail
        self.noise = noise
        self.sharp = sharp

    def validate(self):
        if self.block:
            self.block.validate()
        if self.color:
            self.color.validate()
        if self.detail:
            self.detail.validate()
        if self.noise:
            self.noise.validate()
        if self.sharp:
            self.sharp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block is not None:
            result['Block'] = self.block.to_map()

        if self.color is not None:
            result['Color'] = self.color.to_map()

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.noise is not None:
            result['Noise'] = self.noise.to_map()

        if self.sharp is not None:
            result['Sharp'] = self.sharp.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResultScoreResultBlock()
            self.block = temp_model.from_map(m.get('Block'))

        if m.get('Color') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResultScoreResultColor()
            self.color = temp_model.from_map(m.get('Color'))

        if m.get('Detail') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResultScoreResultDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Noise') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResultScoreResultNoise()
            self.noise = temp_model.from_map(m.get('Noise'))

        if m.get('Sharp') is not None:
            temp_model = main_models.MediaQualityAnalysisJobVqaResultScoreResultSharp()
            self.sharp = temp_model.from_map(m.get('Sharp'))

        return self

class MediaQualityAnalysisJobVqaResultScoreResultSharp(DaraModel):
    def __init__(
        self,
        intensity_value: float = None,
        perceptual_score: float = None,
    ):
        self.intensity_value = intensity_value
        self.perceptual_score = perceptual_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intensity_value is not None:
            result['IntensityValue'] = self.intensity_value

        if self.perceptual_score is not None:
            result['PerceptualScore'] = self.perceptual_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntensityValue') is not None:
            self.intensity_value = m.get('IntensityValue')

        if m.get('PerceptualScore') is not None:
            self.perceptual_score = m.get('PerceptualScore')

        return self

class MediaQualityAnalysisJobVqaResultScoreResultNoise(DaraModel):
    def __init__(
        self,
        intensity_value: float = None,
        perceptual_score: float = None,
    ):
        self.intensity_value = intensity_value
        self.perceptual_score = perceptual_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intensity_value is not None:
            result['IntensityValue'] = self.intensity_value

        if self.perceptual_score is not None:
            result['PerceptualScore'] = self.perceptual_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntensityValue') is not None:
            self.intensity_value = m.get('IntensityValue')

        if m.get('PerceptualScore') is not None:
            self.perceptual_score = m.get('PerceptualScore')

        return self

class MediaQualityAnalysisJobVqaResultScoreResultDetail(DaraModel):
    def __init__(
        self,
        intensity_value: float = None,
        perceptual_score: float = None,
    ):
        self.intensity_value = intensity_value
        self.perceptual_score = perceptual_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intensity_value is not None:
            result['IntensityValue'] = self.intensity_value

        if self.perceptual_score is not None:
            result['PerceptualScore'] = self.perceptual_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntensityValue') is not None:
            self.intensity_value = m.get('IntensityValue')

        if m.get('PerceptualScore') is not None:
            self.perceptual_score = m.get('PerceptualScore')

        return self

class MediaQualityAnalysisJobVqaResultScoreResultColor(DaraModel):
    def __init__(
        self,
        intensity_value: float = None,
        perceptual_score: float = None,
    ):
        self.intensity_value = intensity_value
        self.perceptual_score = perceptual_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intensity_value is not None:
            result['IntensityValue'] = self.intensity_value

        if self.perceptual_score is not None:
            result['PerceptualScore'] = self.perceptual_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntensityValue') is not None:
            self.intensity_value = m.get('IntensityValue')

        if m.get('PerceptualScore') is not None:
            self.perceptual_score = m.get('PerceptualScore')

        return self

class MediaQualityAnalysisJobVqaResultScoreResultBlock(DaraModel):
    def __init__(
        self,
        intensity_value: float = None,
        perceptual_score: float = None,
    ):
        self.intensity_value = intensity_value
        self.perceptual_score = perceptual_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.intensity_value is not None:
            result['IntensityValue'] = self.intensity_value

        if self.perceptual_score is not None:
            result['PerceptualScore'] = self.perceptual_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntensityValue') is not None:
            self.intensity_value = m.get('IntensityValue')

        if m.get('PerceptualScore') is not None:
            self.perceptual_score = m.get('PerceptualScore')

        return self

