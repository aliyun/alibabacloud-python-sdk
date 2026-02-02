# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class ListAddressResponseBody(DaraModel):
    def __init__(
        self,
        import_address_list: main_models.ListAddressResp = None,
    ):
        # The details of migration addresses.
        self.import_address_list = import_address_list

    def validate(self):
        if self.import_address_list:
            self.import_address_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_address_list is not None:
            result['ImportAddressList'] = self.import_address_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAddressList') is not None:
            temp_model = main_models.ListAddressResp()
            self.import_address_list = temp_model.from_map(m.get('ImportAddressList'))

        return self

