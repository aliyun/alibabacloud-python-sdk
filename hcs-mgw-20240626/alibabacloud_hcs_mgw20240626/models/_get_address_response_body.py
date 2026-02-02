# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetAddressResponseBody(DaraModel):
    def __init__(
        self,
        import_address: main_models.GetAddressResp = None,
    ):
        # The details for obtaining the data address.
        # 
        # Valid values:
        # 
        # *   1:1
        self.import_address = import_address

    def validate(self):
        if self.import_address:
            self.import_address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_address is not None:
            result['ImportAddress'] = self.import_address.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAddress') is not None:
            temp_model = main_models.GetAddressResp()
            self.import_address = temp_model.from_map(m.get('ImportAddress'))

        return self

