# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Image(DaraModel):
    def __init__(
        self,
        cropping_suggestions: List[main_models.CroppingSuggestion] = None,
        exif: str = None,
        image_height: int = None,
        image_score: main_models.ImageScore = None,
        image_width: int = None,
        ocrcontents: List[main_models.OCRContents] = None,
    ):
        # The image cropping suggestions. This parameter is reserved and not available.
        self.cropping_suggestions = cropping_suggestions
        # The original EXIF information about the image. The EXIF information is stored in the serialized JSON format. For more information, see [Query image information](https://help.aliyun.com/document_detail/44975.html).
        self.exif = exif
        # The height of the image. Unit: pixels.
        self.image_height = image_height
        # The image scoring information.
        self.image_score = image_score
        # The width of the image. Unit: pixels.
        self.image_width = image_width
        # The results of optical character recognition (OCR). This parameter is reserved and not available.
        self.ocrcontents = ocrcontents

    def validate(self):
        if self.cropping_suggestions:
            for v1 in self.cropping_suggestions:
                 if v1:
                    v1.validate()
        if self.image_score:
            self.image_score.validate()
        if self.ocrcontents:
            for v1 in self.ocrcontents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k1 in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k1.to_map() if k1 else None)

        if self.exif is not None:
            result['EXIF'] = self.exif

        if self.image_height is not None:
            result['ImageHeight'] = self.image_height

        if self.image_score is not None:
            result['ImageScore'] = self.image_score.to_map()

        if self.image_width is not None:
            result['ImageWidth'] = self.image_width

        result['OCRContents'] = []
        if self.ocrcontents is not None:
            for k1 in self.ocrcontents:
                result['OCRContents'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k1 in m.get('CroppingSuggestions'):
                temp_model = main_models.CroppingSuggestion()
                self.cropping_suggestions.append(temp_model.from_map(k1))

        if m.get('EXIF') is not None:
            self.exif = m.get('EXIF')

        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')

        if m.get('ImageScore') is not None:
            temp_model = main_models.ImageScore()
            self.image_score = temp_model.from_map(m.get('ImageScore'))

        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')

        self.ocrcontents = []
        if m.get('OCRContents') is not None:
            for k1 in m.get('OCRContents'):
                temp_model = main_models.OCRContents()
                self.ocrcontents.append(temp_model.from_map(k1))

        return self

