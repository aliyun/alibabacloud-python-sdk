# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoRenderJobRequest(DaraModel):
    def __init__(
        self,
        script: str = None,
        settings: str = None,
        user_data: str = None,
    ):
        self.script = script
        self.settings = settings
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script is not None:
            result['Script'] = self.script

        if self.settings is not None:
            result['Settings'] = self.settings

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('Settings') is not None:
            self.settings = m.get('Settings')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

