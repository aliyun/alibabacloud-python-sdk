# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLicenseRequest(DaraModel):
    def __init__(
        self,
        license_code: str = None,
    ):
        # This parameter is required.
        self.license_code = license_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        return self

