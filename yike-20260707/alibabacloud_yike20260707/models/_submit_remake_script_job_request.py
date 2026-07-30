# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitRemakeScriptJobRequest(DaraModel):
    def __init__(
        self,
        remake_params: str = None,
        remake_type: str = None,
        user_data: str = None,
    ):
        self.remake_params = remake_params
        self.remake_type = remake_type
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remake_params is not None:
            result['RemakeParams'] = self.remake_params

        if self.remake_type is not None:
            result['RemakeType'] = self.remake_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemakeParams') is not None:
            self.remake_params = m.get('RemakeParams')

        if m.get('RemakeType') is not None:
            self.remake_type = m.get('RemakeType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

