# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class TargetImage(DaraModel):
    def __init__(
        self,
        animations: List[main_models.TargetImageAnimations] = None,
        snapshots: List[main_models.TargetImageSnapshots] = None,
        sprites: List[main_models.TargetImageSprites] = None,
    ):
        # Animations
        self.animations = animations
        # Snapshots
        self.snapshots = snapshots
        # Sprites
        self.sprites = sprites

    def validate(self):
        if self.animations:
            for v1 in self.animations:
                 if v1:
                    v1.validate()
        if self.snapshots:
            for v1 in self.snapshots:
                 if v1:
                    v1.validate()
        if self.sprites:
            for v1 in self.sprites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Animations'] = []
        if self.animations is not None:
            for k1 in self.animations:
                result['Animations'].append(k1.to_map() if k1 else None)

        result['Snapshots'] = []
        if self.snapshots is not None:
            for k1 in self.snapshots:
                result['Snapshots'].append(k1.to_map() if k1 else None)

        result['Sprites'] = []
        if self.sprites is not None:
            for k1 in self.sprites:
                result['Sprites'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.animations = []
        if m.get('Animations') is not None:
            for k1 in m.get('Animations'):
                temp_model = main_models.TargetImageAnimations()
                self.animations.append(temp_model.from_map(k1))

        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k1 in m.get('Snapshots'):
                temp_model = main_models.TargetImageSnapshots()
                self.snapshots.append(temp_model.from_map(k1))

        self.sprites = []
        if m.get('Sprites') is not None:
            for k1 in m.get('Sprites'):
                temp_model = main_models.TargetImageSprites()
                self.sprites.append(temp_model.from_map(k1))

        return self

class TargetImageSprites(DaraModel):
    def __init__(
        self,
        format: str = None,
        interval: float = None,
        margin: int = None,
        mode: str = None,
        number: int = None,
        pad: int = None,
        scale_height: float = None,
        scale_type: str = None,
        scale_width: float = None,
        start_time: float = None,
        threshold: int = None,
        tile_height: int = None,
        tile_width: int = None,
        uri: str = None,
    ):
        # Image format
        # 
        # This parameter is required.
        self.format = format
        # Time interval between sprites, in seconds
        self.interval = interval
        # Margin around the sprite grid, in pixels
        self.margin = margin
        self.mode = mode
        # Total number of sprites to generate
        self.number = number
        # Padding between sprite tiles, in pixels
        self.pad = pad
        # Output height after scaling, in pixels
        self.scale_height = scale_height
        # Scaling method
        self.scale_type = scale_type
        # Output width after scaling, in pixels
        self.scale_width = scale_width
        # StartTime
        self.start_time = start_time
        self.threshold = threshold
        # Height of each sprite tile, in pixels
        self.tile_height = tile_height
        # Width of each sprite tile, in pixels
        self.tile_width = tile_width
        # URI
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.margin is not None:
            result['Margin'] = self.margin

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.number is not None:
            result['Number'] = self.number

        if self.pad is not None:
            result['Pad'] = self.pad

        if self.scale_height is not None:
            result['ScaleHeight'] = self.scale_height

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.scale_width is not None:
            result['ScaleWidth'] = self.scale_width

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.tile_height is not None:
            result['TileHeight'] = self.tile_height

        if self.tile_width is not None:
            result['TileWidth'] = self.tile_width

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Margin') is not None:
            self.margin = m.get('Margin')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Pad') is not None:
            self.pad = m.get('Pad')

        if m.get('ScaleHeight') is not None:
            self.scale_height = m.get('ScaleHeight')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('ScaleWidth') is not None:
            self.scale_width = m.get('ScaleWidth')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('TileHeight') is not None:
            self.tile_height = m.get('TileHeight')

        if m.get('TileWidth') is not None:
            self.tile_width = m.get('TileWidth')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class TargetImageSnapshots(DaraModel):
    def __init__(
        self,
        format: str = None,
        height: float = None,
        interval: float = None,
        mode: str = None,
        number: int = None,
        scale_type: str = None,
        start_time: float = None,
        threshold: int = None,
        uri: str = None,
        width: float = None,
    ):
        # Image format
        # 
        # This parameter is required.
        self.format = format
        # Output height, in pixels
        self.height = height
        # Time interval between snapshots, in seconds
        self.interval = interval
        self.mode = mode
        # The sequence number of the snapshot.
        self.number = number
        # Scaling method
        self.scale_type = scale_type
        # The start time of the snapshot.
        self.start_time = start_time
        self.threshold = threshold
        # OSS URI where snapshots are stored
        # 
        # This parameter is required.
        self.uri = uri
        # The width of the snapshot.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.height is not None:
            result['Height'] = self.height

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.number is not None:
            result['Number'] = self.number

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.uri is not None:
            result['URI'] = self.uri

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class TargetImageAnimations(DaraModel):
    def __init__(
        self,
        format: str = None,
        frame_rate: float = None,
        height: float = None,
        interval: float = None,
        number: int = None,
        scale_type: str = None,
        start_time: float = None,
        uri: str = None,
        width: float = None,
    ):
        # Format
        # 
        # This parameter is required.
        self.format = format
        # Animation frame rate, in frames per second
        self.frame_rate = frame_rate
        # Height
        self.height = height
        # Time interval between animation frames, in seconds
        self.interval = interval
        # Total number of animation frames to generate
        self.number = number
        # Scaling method
        self.scale_type = scale_type
        # StartTime
        self.start_time = start_time
        # The URI of the animation.
        # 
        # This parameter is required.
        self.uri = uri
        # Output width, in pixels
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.height is not None:
            result['Height'] = self.height

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.number is not None:
            result['Number'] = self.number

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.uri is not None:
            result['URI'] = self.uri

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

