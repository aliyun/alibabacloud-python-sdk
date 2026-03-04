# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class Hotword(DaraModel):
    def __init__(
        self,
        language: str = None,
        text: str = None,
        transposition_result_list: List[main_models.TranspositionResult] = None,
        weight: int = None,
    ):
        # The language of the hotword text. Valid values:
        # 
        # *   For structured media analysis and ASR: zh: Chinese en: English
        # *   For video translation: Supports 53 languages.
        # *
        self.language = language
        # The text of the hotword.
        # 
        # *   For structured media analysis and ASR:
        # *   *   Chinese: Up to 15 characters.
        # *   *   English: Up to 10 words, separated by spaces.
        # *   *   Mixed: Each letter is counted as one character (following the Chinese limit).
        # *   For video translation: Up to 100 characters.
        # *
        self.text = text
        # *   Predefined translation results for the hotword.
        # *   This field is only used in translation-related scenarios.
        self.transposition_result_list = transposition_result_list
        # The weight of the hotword.
        # 
        # 1.  Valid values: [-6,5].
        # 2.  A positive value increases the likelihood of the word being recognized, while a negative value decreases the likelihood.
        # 3.  A value of -6 specifies that recognition of this word should be minimized.
        # 4.  Recommended value: 2.
        # 5.  If the desired effect is not achieved, you can increase the weight. However, excessively high weights may negatively impact the recognition accuracy of other words.
        self.weight = weight

    def validate(self):
        if self.transposition_result_list:
            for v1 in self.transposition_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.text is not None:
            result['Text'] = self.text

        result['TranspositionResultList'] = []
        if self.transposition_result_list is not None:
            for k1 in self.transposition_result_list:
                result['TranspositionResultList'].append(k1.to_map() if k1 else None)

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        self.transposition_result_list = []
        if m.get('TranspositionResultList') is not None:
            for k1 in m.get('TranspositionResultList'):
                temp_model = main_models.TranspositionResult()
                self.transposition_result_list.append(temp_model.from_map(k1))

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

