# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class CreateAddressInfo(DaraModel):
    def __init__(
        self,
        address_detail: main_models.AddressDetail = None,
        name: str = None,
        tags: str = None,
    ):
        # The details of the data address.
        # 
        # This parameter is required.
        self.address_detail = address_detail
        # The name of the data address.\\
        # The name can contain lowercase letters, digits, hyphens (-), and underscores (_). The name must be 3 to 63 characters in length. The name is case-sensitive and encoded in UTF-8. The name cannot start with a hyphen (-) or an underscore (_). You must specify a name.
        # 
        # This parameter is required.
        self.name = name
        # The tags in the key:value format.\\
        # The value can contain letters, digits, hyphens (-), underscores (_), and commas (,). The value can be up to 1,024 characters in length.
        self.tags = tags

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            temp_model = main_models.AddressDetail()
            self.address_detail = temp_model.from_map(m.get('AddressDetail'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

