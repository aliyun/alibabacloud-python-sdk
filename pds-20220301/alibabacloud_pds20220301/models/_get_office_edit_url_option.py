# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOfficeEditUrlOption(DaraModel):
    def __init__(
        self,
        copy: bool = None,
        print: bool = None,
        readonly: bool = None,
    ):
        self.copy = copy
        self.print = print
        self.readonly = readonly

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

        if self.readonly is not None:
            result['readonly'] = self.readonly

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copy') is not None:
            self.copy = m.get('copy')

        if m.get('print') is not None:
            self.print = m.get('print')

        if m.get('readonly') is not None:
            self.readonly = m.get('readonly')

        return self

