# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHotwordLibraryShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        hotwords_shrink: str = None,
        name: str = None,
        usage_scenario: str = None,
    ):
        # The description of the hotword library. It can be up to 200 characters in length.
        self.description = description
        # The hotword list. You can add up to 300 hotword entries to a single library.
        # 
        # This parameter is required.
        self.hotwords_shrink = hotwords_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.hotwords_shrink is not None:
            result['Hotwords'] = self.hotwords_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Hotwords') is not None:
            self.hotwords_shrink = m.get('Hotwords')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')

        return self

