# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTraceM3u8JobRequest(DaraModel):
    def __init__(
        self,
        key_uri: str = None,
        media_id: str = None,
        output: str = None,
        params: str = None,
        trace: str = None,
    ):
        self.key_uri = key_uri
        self.media_id = media_id
        self.output = output
        self.params = params
        self.trace = trace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_uri is not None:
            result['KeyUri'] = self.key_uri

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output is not None:
            result['Output'] = self.output

        if self.params is not None:
            result['Params'] = self.params

        if self.trace is not None:
            result['Trace'] = self.trace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyUri') is not None:
            self.key_uri = m.get('KeyUri')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Trace') is not None:
            self.trace = m.get('Trace')

        return self

