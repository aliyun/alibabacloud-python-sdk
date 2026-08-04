# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDeviceIdByIdentitiesRequest(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_ids: List[str] = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # The value corresponding to the encoding type. Enter the Project ID of the project to which this product belongs. You can view it in the Tmall Genie AI platform console.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter **PROJECT_ID** here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # List of device authentication identifiers.
        self.identity_ids = identity_ids
        # Device authentication type. Enter **MAC** or **SN**.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The unique product identifier ProductKey, which is a globally unique identity issued by the platform when creating a product in the Tmall Genie AI platform.
        # 
        # This parameter is required.
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.identity_ids is not None:
            result['IdentityIds'] = self.identity_ids

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('IdentityIds') is not None:
            self.identity_ids = m.get('IdentityIds')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

