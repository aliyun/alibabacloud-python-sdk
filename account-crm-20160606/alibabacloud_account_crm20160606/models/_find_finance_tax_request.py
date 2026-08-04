# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindFinanceTaxRequest(DaraModel):
    def __init__(
        self,
        hid: int = None,
        tax_version: str = None,
    ):
        # This parameter is required.
        self.hid = hid
        self.tax_version = tax_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hid is not None:
            result['HId'] = self.hid

        if self.tax_version is not None:
            result['TaxVersion'] = self.tax_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HId') is not None:
            self.hid = m.get('HId')

        if m.get('TaxVersion') is not None:
            self.tax_version = m.get('TaxVersion')

        return self

