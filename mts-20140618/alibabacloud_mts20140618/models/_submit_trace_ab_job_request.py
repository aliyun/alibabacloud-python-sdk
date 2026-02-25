# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTraceAbJobRequest(DaraModel):
    def __init__(
        self,
        call_back: str = None,
        cipher_base_64ed: str = None,
        input: str = None,
        level: int = None,
        output: str = None,
        start_time: int = None,
        total_time: int = None,
        url: str = None,
        user_data: str = None,
    ):
        self.call_back = call_back
        self.cipher_base_64ed = cipher_base_64ed
        self.input = input
        self.level = level
        # This parameter is required.
        self.output = output
        self.start_time = start_time
        self.total_time = total_time
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

        if self.cipher_base_64ed is not None:
            result['CipherBase64ed'] = self.cipher_base_64ed

        if self.input is not None:
            result['Input'] = self.input

        if self.level is not None:
            result['Level'] = self.level

        if self.output is not None:
            result['Output'] = self.output

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.url is not None:
            result['Url'] = self.url

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')

        if m.get('CipherBase64ed') is not None:
            self.cipher_base_64ed = m.get('CipherBase64ed')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

