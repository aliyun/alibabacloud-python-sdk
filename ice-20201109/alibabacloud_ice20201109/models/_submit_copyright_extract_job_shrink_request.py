# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCopyrightExtractJobShrinkRequest(DaraModel):
    def __init__(
        self,
        input_shrink: str = None,
        params: str = None,
        user_data: str = None,
    ):
        # The source video file from which to extract the watermark.
        # 
        # > The OSS object or media asset must reside in the same region as the IMS service region.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # Additional parameters for the watermark job, provided as a JSON string. Supported parameter:
        # 
        # *   algoType: The algorithm type. Defaults to v1. The extraction algorithm must match the one used for embedding.
        # 
        #     *   v1: Copyright watermark extraction algorithm for long videos.
        #     *   v2: Copyright watermark extraction algorithm for short videos.
        self.params = params
        # The custom data, which can be up to 1,024 bytes in size.
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

