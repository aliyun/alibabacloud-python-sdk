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
        # The height of the watermark image, in pixels. Valid values: 100 to 5000.
        # 
        # This parameter is required.
        self.height = height
        # The image watermark control parameters.
        self.image_control_shrink = image_control_shrink
        # The opacity of the watermark image. Valid values: 1 to 255. A larger value indicates lower transparency.
        # 
        # This parameter is required.
        self.opacity = opacity
        # The scaling ratio of the watermark image.
        # 
        # This parameter is required.
        self.scale = scale
        # The width of the watermark image, in pixels. Valid values: 100 to 5000.
        # 
        # This parameter is required.
        self.width = width
        # The watermark information in Base64-encoded string format. The length is 1 to 300 characters. If this parameter is set, the WmInfoUint parameter cannot be set.
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        # The bit width of the watermark information capacity. Default value: 32. This parameter must be consistent between embedding and extraction. For example, if the SDK used for embedding is 40-bit, set this parameter to 40 during extraction as well.
        self.wm_info_size = wm_info_size
        # The watermark information in decimal number format. If this parameter is set, WmInfoBytesB64 cannot be set.
        # 
        # The valid range depends on the WmInfoSize parameter:
        # 
        # - If WmInfoSize is **32**, the valid range is 1 to 4294967295.
        # 
        # - If WmInfoSize is **40**, the valid range is 1 to 1099511627775.
        # 
        # - If WmInfoSize is **64**, the valid range is 1 to 18446744073709551615.
        self.wm_info_uint = wm_info_uint
        # The watermark type. Valid values:
        # - **PureWebappInvisible**: web watermark.
        # - **PureAppInvisible**: App watermark.
        # - **PureScreenInvisible**: screen watermark.
        # - **AigcWebappInvisible**: AIGC web watermark.
        # - **AigcAppInvisible**: AIGC App watermark.
        # - **AigcScreenInvisible**: AIGC screen watermark.
        # 
        # This parameter is required.
        self.wm_type = wm_type
        # The remarks.
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

