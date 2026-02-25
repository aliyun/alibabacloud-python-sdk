# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitImageCopyrightRequest(DaraModel):
    def __init__(
        self,
        message: str = None,
        output: str = None,
        params: str = None,
    ):
        # This parameter is required.
        self.message = message
        self.output = output
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

