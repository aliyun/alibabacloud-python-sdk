# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOfficePreviewUrlOption(DaraModel):
    def __init__(
        self,
        copy: bool = None,
        print: bool = None,
    ):
        self.copy = copy
        self.print = print

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy is not None:
            result['copy'] = self.copy

        if self.print is not None:
            result['print'] = self.print

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copy') is not None:
            self.copy = m.get('copy')

        if m.get('print') is not None:
            self.print = m.get('print')

        return self

