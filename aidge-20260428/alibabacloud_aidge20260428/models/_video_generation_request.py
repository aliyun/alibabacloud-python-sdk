# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class VideoGenerationRequest(DaraModel):
    def __init__(
        self,
        input: main_models.VideoGenerationRequestInput = None,
        intent: main_models.VideoGenerationRequestIntent = None,
        output: main_models.VideoGenerationRequestOutput = None,
    ):
        # The product input.
        # 
        # This parameter is required.
        self.input = input
        # The intent parameters. Currently unavailable.
        self.intent = intent
        # The output parameters.
        # 
        # This parameter is required.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()
        if self.intent:
            self.intent.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.intent is not None:
            result['Intent'] = self.intent.to_map()

        if self.output is not None:
            result['Output'] = self.output.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.VideoGenerationRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Intent') is not None:
            temp_model = main_models.VideoGenerationRequestIntent()
            self.intent = temp_model.from_map(m.get('Intent'))

        if m.get('Output') is not None:
            temp_model = main_models.VideoGenerationRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        return self

class VideoGenerationRequestOutput(DaraModel):
    def __init__(
        self,
        duration: int = None,
        quality: str = None,
        ratio: str = None,
    ):
        # The video duration in seconds. Currently supports integers between 5 and 15. More options will be available in the future.
        # 
        # This parameter is required.
        self.duration = duration
        # The output resolution.
        # 
        # This parameter is required.
        self.quality = quality
        # The video aspect ratio.
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

class VideoGenerationRequestIntent(DaraModel):
    def __init__(
        self,
        channel: str = None,
        goal: str = None,
        script: str = None,
    ):
        # The distribution channel.
        self.channel = channel
        # The business goal.
        self.goal = goal
        # Required when goal is set to scripted_video.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.goal is not None:
            result['Goal'] = self.goal

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Goal') is not None:
            self.goal = m.get('Goal')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

class VideoGenerationRequestInput(DaraModel):
    def __init__(
        self,
        asset_bindings: List[main_models.VideoGenerationRequestInputAssetBindings] = None,
        extra: Dict[str, Any] = None,
        images: List[str] = None,
        title: str = None,
    ):
        # Specifies the purpose and description of images by asset index.
        self.asset_bindings = asset_bindings
        # The extended information.
        self.extra = extra
        # The list of product image URLs (1 to 6 images). The URLs must be publicly accessible.
        # 
        # This parameter is required.
        self.images = images
        # The product title. A maximum of the first 60 characters are used.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.asset_bindings:
            for v1 in self.asset_bindings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssetBindings'] = []
        if self.asset_bindings is not None:
            for k1 in self.asset_bindings:
                result['AssetBindings'].append(k1.to_map() if k1 else None)

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.images is not None:
            result['Images'] = self.images

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asset_bindings = []
        if m.get('AssetBindings') is not None:
            for k1 in m.get('AssetBindings'):
                temp_model = main_models.VideoGenerationRequestInputAssetBindings()
                self.asset_bindings.append(temp_model.from_map(k1))

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class VideoGenerationRequestInputAssetBindings(DaraModel):
    def __init__(
        self,
        asset_index: int = None,
        description: str = None,
        slot: str = None,
    ):
        # The asset index.
        self.asset_index = asset_index
        # The natural language description of the asset.
        self.description = description
        # Valid values:
        # - look_reference: appearance reference.
        # - scene_reference: scene reference.
        self.slot = slot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_index is not None:
            result['AssetIndex'] = self.asset_index

        if self.description is not None:
            result['Description'] = self.description

        if self.slot is not None:
            result['Slot'] = self.slot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetIndex') is not None:
            self.asset_index = m.get('AssetIndex')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Slot') is not None:
            self.slot = m.get('Slot')

        return self

