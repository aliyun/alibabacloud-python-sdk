# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTraceExtractJobShrinkRequest(DaraModel):
    def __init__(
        self,
        input_shrink: str = None,
        params: str = None,
        user_data: str = None,
    ):
        # The input video from which to extract the watermark.
        # 
        # > - The OSS object or media asset must be in the same region as your IMS service.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # Extraction job parameters, specified as a JSON string. The following parameters are supported:
        # 
        # - `m3u8Type`: The algorithm type. The default value is `v1`.
        # 
        #   - `v1`: Extracts an m3u8 playlist with absolute paths.
        # 
        #   - `v2`: Extracts an m3u8 playlist with relative paths.
        self.params = params
        # The user-defined data. Maximum length: 1,024 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.params is not None:
            result['Params'] = self.params

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

