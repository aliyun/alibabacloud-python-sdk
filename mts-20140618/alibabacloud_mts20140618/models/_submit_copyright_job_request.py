# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCopyrightJobRequest(DaraModel):
    def __init__(
        self,
        call_back: str = None,
        description: str = None,
        input: str = None,
        level: int = None,
        message: str = None,
        output: str = None,
        params: str = None,
        start_time: int = None,
        total_time: int = None,
        url: str = None,
        user_data: str = None,
    ):
        self.call_back = call_back
        self.description = description
        self.input = input
        self.level = level
        # This parameter is required.
        self.message = message
        # This parameter is required.
        self.output = output
        self.params = params
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

        if self.description is not None:
            result['Description'] = self.description

        if self.input is not None:
            result['Input'] = self.input

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output

        if self.params is not None:
            result['Params'] = self.params

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

