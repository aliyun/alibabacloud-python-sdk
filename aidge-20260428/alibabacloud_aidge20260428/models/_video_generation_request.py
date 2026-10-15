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
        # The video duration varies by Intent.goal: auto_video supports 5 to 15 seconds, scripted_video supports 5 to 30 seconds, and camera_motion generates a fixed 10-second video and returns two 5-second videos.
        # 
        # This parameter is required.
        self.duration = duration
        # The output resolution.
        # 
        # This parameter is required.
        self.quality = quality
        # The aspect ratio varies by Intent.goal: auto_video and scripted_video only support 9:16, and camera_motion only supports 3:4.
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
        # The delivery channel.
        self.channel = channel
        # Specifies the business goal. Valid values:
        # 
        # - camera_motion: Camera movement mode. Generates videos based on a fixed 360-degree camera movement logic.
        # 
        # - scripted_video: Scripted mode. Provides a script or prompt, and the system generates the video according to the script.
        # 
        # - auto_video: Unscripted mode. Does not provide a script, and the system automatically plans the script and generates the video.
        self.goal = goal
        # The script or prompt.
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
        # The asset binding list.
        self.asset_bindings = asset_bindings
        # The extended information.
        self.extra = extra
        # The list of product image URLs (1 to 8 images), which must be accessible over the Internet.
        # 
        # This parameter is required.
        self.images = images
        # The product title. Only the first 60 characters are used.
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
        # The asset index, such as 0, 1, 2, or 3, which must be consistent with the number of the image URL.
        self.asset_index = asset_index
        # The description of the image. Examples:   
        # 1. Description for look_reference: Front full-body outfit reference image of the person.   
        # 2. Description for scene_reference: Specified clothing display scene.   
        # 3. Description for garment_reference:   
        # ● Front of the top;   
        # ● Back of the bottom;   
        # ● Side of the shoes.
        self.description = description
        # Specifies the asset usage. Valid values:   
        # - look_reference: Corresponds to the full outfit effect image of the person wearing the clothes (overall visual).   
        # - scene_reference: Corresponds to the scene reference image (usually the cover main image).   
        # - garment_reference: Corresponds to all product detail images (including front, back, and side of clothes, shoes, skirts, and other partial close-ups).
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

