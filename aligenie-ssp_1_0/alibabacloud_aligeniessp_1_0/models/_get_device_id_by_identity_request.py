# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeviceIdByIdentityRequest(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_id: str = None,
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
        # Authentication identifier. Enter the MAC address or the SN value.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # Device authentication type. Enter **MAC**, **SN**, or **CTEI**.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The unique product identifier ProductKey, which is a globally unique identity issued by the platform when the product is created in the Tmall Genie AI platform. This parameter is optional when IdentityType is **CTEI**.
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

        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id

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

        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

