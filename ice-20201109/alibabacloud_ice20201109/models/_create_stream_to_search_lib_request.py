# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStreamToSearchLibRequest(DaraModel):
    def __init__(
        self,
        input: str = None,
        namespace: str = None,
        search_lib_name: str = None,
    ):
        # The URL of the live stream to be ingested and analyzed.
        self.input = input
        # The namespace.
        self.namespace = namespace
        # The search library.
        self.search_lib_name = search_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

