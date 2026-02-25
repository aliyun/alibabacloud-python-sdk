# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCopyrightExtractJobRequest(DaraModel):
    def __init__(
        self,
        call_back: str = None,
        input: str = None,
        params: str = None,
        url: str = None,
        user_data: str = None,
    ):
        self.call_back = call_back
        self.input = input
        self.params = params
        self.url = url
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_back is not None:
            result['CallBack'] = self.call_back

        if self.input is not None:
            result['Input'] = self.input

        if self.params is not None:
            result['Params'] = self.params

        if self.url is not None:
            result['Url'] = self.url

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

