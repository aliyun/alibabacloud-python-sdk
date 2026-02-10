# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReceiveFunctionTrialRewardByAliUidRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        lang: str = None,
    ):
        # The name of the feature for which you want to apply for a free trial. Valid values:
        # 
        # *   **trail_honeypot_reward**: cloud honeypot
        # *   **trail_file_detect_api_reward**: SDK for malicious file detection
        self.function_name = function_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

