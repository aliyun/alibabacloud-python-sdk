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
        # The video file for watermark extraction.
        # 
        # > - The region of the Object Storage Service (OSS) file or media asset must match the region of the current Intelligent Media Service (IMS) instance.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The watermark job parameters, specified as a JSON string.
        # 
        # - algoType: The algorithm type. Default value: v1. The extraction algorithm type must match the algorithm type used for embedding the watermark.
        # 
        #   - v1: The copyright extraction algorithm for long-form videos.
        # 
        #   - v2: The copyright extraction algorithm for short-form videos.
        self.params = params
        # The user-defined data. The maximum length is 1,024 bytes.
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

