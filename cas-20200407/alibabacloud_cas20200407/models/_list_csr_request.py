# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCsrRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        current_page: int = None,
        key_word: str = None,
        show_size: int = None,
    ):
        # The algorithm. Valid values: RSA, ECC, and SM2.
        self.algorithm = algorithm
        # The page number.
        self.current_page = current_page
        # The keyword.
        self.key_word = key_word
        # The number of entries per page. Default value: 50.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

