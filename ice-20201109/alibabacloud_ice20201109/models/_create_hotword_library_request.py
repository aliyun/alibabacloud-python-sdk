# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateHotwordLibraryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        hotwords: List[main_models.Hotword] = None,
        name: str = None,
        usage_scenario: str = None,
    ):
        # The description of the hotword library. It can be up to 200 characters in length.
        self.description = description
        # The hotword list. You can add up to 300 hotword entries to a single library.
        # 
        # This parameter is required.
        self.hotwords = hotwords
        # The name of the hotword library. It can be up to 100 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The usage scenario of the hotword library. Valid values:
        # 
        # · ASR: Automatic Speech Recognition
        # 
        # · StructuredMediaAssets: structured media analysis
        # 
        # · VideoTranslation: Video translation.
        # 
        # This field cannot be modified after the hotword library is created.
        # 
        # This parameter is required.
        self.usage_scenario = usage_scenario

    def validate(self):
        if self.hotwords:
            for v1 in self.hotwords:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Hotwords'] = []
        if self.hotwords is not None:
            for k1 in self.hotwords:
                result['Hotwords'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.hotwords = []
        if m.get('Hotwords') is not None:
            for k1 in m.get('Hotwords'):
                temp_model = main_models.Hotword()
                self.hotwords.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')

        return self

