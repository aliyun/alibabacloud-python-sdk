# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWmBaseImageShrinkRequest(DaraModel):
    def __init__(
        self,
        height: int = None,
        image_control_shrink: str = None,
        opacity: int = None,
        scale: int = None,
        width: int = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
        comment: str = None,
    ):
        # This parameter is required.
        self.height = height
        self.image_control_shrink = image_control_shrink
        # This parameter is required.
        self.opacity = opacity
        # This parameter is required.
        self.scale = scale
        # This parameter is required.
        self.width = width
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        self.wm_info_uint = wm_info_uint
        # This parameter is required.
        self.wm_type = wm_type
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.image_control_shrink is not None:
            result['ImageControl'] = self.image_control_shrink

        if self.opacity is not None:
            result['Opacity'] = self.opacity

        if self.scale is not None:
            result['Scale'] = self.scale

        if self.width is not None:
            result['Width'] = self.width

        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64

        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        if self.comment is not None:
            result['comment'] = self.comment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ImageControl') is not None:
            self.image_control_shrink = m.get('ImageControl')

        if m.get('Opacity') is not None:
            self.opacity = m.get('Opacity')

        if m.get('Scale') is not None:
            self.scale = m.get('Scale')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')

        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        return self

