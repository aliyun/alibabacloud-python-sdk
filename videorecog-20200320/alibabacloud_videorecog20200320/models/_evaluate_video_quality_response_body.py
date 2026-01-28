# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class EvaluateVideoQualityResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.EvaluateVideoQualityResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.EvaluateVideoQualityResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class EvaluateVideoQualityResponseBodyData(DaraModel):
    def __init__(
        self,
        json_url: str = None,
        pdf_url: str = None,
        video_quality_info: main_models.EvaluateVideoQualityResponseBodyDataVideoQualityInfo = None,
    ):
        self.json_url = json_url
        self.pdf_url = pdf_url
        self.video_quality_info = video_quality_info

    def validate(self):
        if self.video_quality_info:
            self.video_quality_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json_url is not None:
            result['JsonUrl'] = self.json_url

        if self.pdf_url is not None:
            result['PdfUrl'] = self.pdf_url

        if self.video_quality_info is not None:
            result['VideoQualityInfo'] = self.video_quality_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonUrl') is not None:
            self.json_url = m.get('JsonUrl')

        if m.get('PdfUrl') is not None:
            self.pdf_url = m.get('PdfUrl')

        if m.get('VideoQualityInfo') is not None:
            temp_model = main_models.EvaluateVideoQualityResponseBodyDataVideoQualityInfo()
            self.video_quality_info = temp_model.from_map(m.get('VideoQualityInfo'))

        return self

class EvaluateVideoQualityResponseBodyDataVideoQualityInfo(DaraModel):
    def __init__(
        self,
        blurriness: float = None,
        color_contrast: float = None,
        color_saturation: float = None,
        colorfulness: float = None,
        compressive_strength: float = None,
        luminance: float = None,
        mos_score: float = None,
        noise_intensity: float = None,
    ):
        self.blurriness = blurriness
        self.color_contrast = color_contrast
        self.color_saturation = color_saturation
        self.colorfulness = colorfulness
        self.compressive_strength = compressive_strength
        self.luminance = luminance
        self.mos_score = mos_score
        self.noise_intensity = noise_intensity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blurriness is not None:
            result['Blurriness'] = self.blurriness

        if self.color_contrast is not None:
            result['ColorContrast'] = self.color_contrast

        if self.color_saturation is not None:
            result['ColorSaturation'] = self.color_saturation

        if self.colorfulness is not None:
            result['Colorfulness'] = self.colorfulness

        if self.compressive_strength is not None:
            result['CompressiveStrength'] = self.compressive_strength

        if self.luminance is not None:
            result['Luminance'] = self.luminance

        if self.mos_score is not None:
            result['MosScore'] = self.mos_score

        if self.noise_intensity is not None:
            result['NoiseIntensity'] = self.noise_intensity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blurriness') is not None:
            self.blurriness = m.get('Blurriness')

        if m.get('ColorContrast') is not None:
            self.color_contrast = m.get('ColorContrast')

        if m.get('ColorSaturation') is not None:
            self.color_saturation = m.get('ColorSaturation')

        if m.get('Colorfulness') is not None:
            self.colorfulness = m.get('Colorfulness')

        if m.get('CompressiveStrength') is not None:
            self.compressive_strength = m.get('CompressiveStrength')

        if m.get('Luminance') is not None:
            self.luminance = m.get('Luminance')

        if m.get('MosScore') is not None:
            self.mos_score = m.get('MosScore')

        if m.get('NoiseIntensity') is not None:
            self.noise_intensity = m.get('NoiseIntensity')

        return self

