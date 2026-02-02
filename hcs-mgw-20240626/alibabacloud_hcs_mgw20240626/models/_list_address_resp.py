# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListAddressResp(DaraModel):
    def __init__(
        self,
        import_address: List[main_models.GetAddressResp] = None,
        next_marker: str = None,
        truncated: bool = None,
    ):
        self.import_address = import_address
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.import_address:
            for v1 in self.import_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImportAddress'] = []
        if self.import_address is not None:
            for k1 in self.import_address:
                result['ImportAddress'].append(k1.to_map() if k1 else None)

        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker

        if self.truncated is not None:
            result['Truncated'] = self.truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_address = []
        if m.get('ImportAddress') is not None:
            for k1 in m.get('ImportAddress'):
                temp_model = main_models.GetAddressResp()
                self.import_address.append(temp_model.from_map(k1))

        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')

        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')

        return self

