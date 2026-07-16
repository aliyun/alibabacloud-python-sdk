# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTraceDiagnoseRequest(DaraModel):
    def __init__(
        self,
        source: str = None,
        url: str = None,
    ):
        # The source of the request.
        self.source = source
        # The URL to diagnose.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

