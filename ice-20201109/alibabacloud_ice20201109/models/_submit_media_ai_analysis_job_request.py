# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaAiAnalysisJobRequest(DaraModel):
    def __init__(
        self,
        analysis_params: str = None,
        input: str = None,
        user_data: str = None,
    ):
        # The analysis parameters.
        self.analysis_params = analysis_params
        # The media asset that you want to analyze. You can specify an Object Storage Service (OSS) URL, a media asset ID, or an external URL.
        self.input = input
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_params is not None:
            result['AnalysisParams'] = self.analysis_params

        if self.input is not None:
            result['Input'] = self.input

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisParams') is not None:
            self.analysis_params = m.get('AnalysisParams')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

