# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LookupWmInfoMappingRequest(DaraModel):
    def __init__(
        self,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        # Bit width of the watermark information. Default value: 32. This parameter must match the bit width used when embedding or generating a transparent image. Valid values: 32 to 64. Use the same value as when you created the mapping. Otherwise, the mapping cannot be found.
        self.wm_info_size = wm_info_size
        # Numeric-formatted watermark information. Value source:
        # 
        # - [CreateWmInfoMapping](~~CreateWmInfoMapping~~): The **WmInfoUint** return value from the CreateWmInfoMapping API.
        # 
        # This parameter is required.
        self.wm_info_uint = wm_info_uint
        # Watermark type. Valid values:
        # 
        # - **PureWebappInvisible**: Webpage watermark.
        # 
        # - **PureAppInvisible**: App watermark.
        # 
        # - **PureScreenInvisible**: Screen watermark.
        # 
        # - **PureDocument**: Document watermark.
        # 
        # - **PureImage**: Image watermark.
        # 
        # - **PureAudio**: Audio watermark.
        # 
        # - **PureVideo**: Video watermark.
        # 
        # - **AigcWebappInvisible**: AIGC webpage watermark.
        # 
        # - **AigcAppInvisible**: AIGC app watermark.
        # 
        # - **AigcScreenInvisible**: AIGC screen watermark.
        # 
        # - **AigcDocument**: AIGC document watermark.
        # 
        # - **AigcImage**: AIGC image watermark.
        # 
        # - **AigcAudio**: AIGC audio watermark.
        # 
        # - **AigcVideo**: AIGC video watermark.
        # 
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        return self

