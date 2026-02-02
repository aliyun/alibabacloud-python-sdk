# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class VerifyAddressResponseBody(DaraModel):
    def __init__(
        self,
        verify_address_response: main_models.VerifyAddressResp = None,
    ):
        # The details for verifying the data address.
        self.verify_address_response = verify_address_response

    def validate(self):
        if self.verify_address_response:
            self.verify_address_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.verify_address_response is not None:
            result['VerifyAddressResponse'] = self.verify_address_response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyAddressResponse') is not None:
            temp_model = main_models.VerifyAddressResp()
            self.verify_address_response = temp_model.from_map(m.get('VerifyAddressResponse'))

        return self

