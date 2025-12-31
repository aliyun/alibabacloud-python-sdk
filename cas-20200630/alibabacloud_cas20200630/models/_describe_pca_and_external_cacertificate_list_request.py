# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePcaAndExternalCACertificateListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        show_size: int = None,
    ):
        self.current_page = current_page
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

