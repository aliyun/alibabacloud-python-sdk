# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWmInfoMappingRequest(DaraModel):
    def __init__(
        self,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_type: str = None,
    ):
        # The Base64-encoded string-format watermark information. Length: 1 to 300 characters.
        # 
        # This parameter is required.
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        # The capacity bit width of the watermark information. Default is 32. This parameter must be consistent with the capacity bit width used during actual embedding or transparent image generation. Valid range: 32 to 64.
        self.wm_info_size = wm_info_size
        # Watermark type. Valid values:
        # - **PureWebappInvisible**: Webpage watermark.
        # - **PureAppInvisible**: App watermark.
        # - **PureScreenInvisible**: Screen watermark.
        # - **PureDocument**: Document watermark.
        # - **PureImage**: Image watermark.
        # - **PureAudio**: Audio watermark.
        # - **PureVideo**: Video watermark.
        # - **AigcWebappInvisible**: AIGC webpage watermark.
        # - **AigcAppInvisible**: AIGC App watermark.
        # - **AigcScreenInvisible**: AIGC screen watermark.
        # - **AigcDocument**: AIGC document watermark.
        # - **AigcImage**: AIGC image watermark.
        # - **AigcAudio**: AIGC audio watermark.
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
        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64

        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')

        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        return self

