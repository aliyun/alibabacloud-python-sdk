# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHistoryAdvicesRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        language: str = None,
        page_num: int = None,
        page_size: int = None,
        product: str = None,
        reverse: bool = None,
        severity: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.language = language
        self.page_num = page_num
        self.page_size = page_size
        self.product = product
        self.reverse = reverse
        self.severity = severity
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.language is not None:
            result['Language'] = self.language

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product is not None:
            result['Product'] = self.product

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

