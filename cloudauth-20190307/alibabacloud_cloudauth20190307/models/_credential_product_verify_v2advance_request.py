# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CredentialProductVerifyV2AdvanceRequest(DaraModel):
    def __init__(
        self,
        cred_name: str = None,
        cred_type: str = None,
        image_file_object: BinaryIO = None,
        image_url: str = None,
        merchant_id: str = None,
        product_code: str = None,
    ):
        # Credential name: Only supports value 0501 (product image).
        # 
        # This parameter is required.
        self.cred_name = cred_name
        # Credential type: Only supports value 05 (product image).
        # 
        # This parameter is required.
        self.cred_type = cred_type
        # InputStream object of the image.
        self.image_file_object = image_file_object
        # URL of the image.
        self.image_url = image_url
        # Merchant ID.
        self.merchant_id = merchant_id
        # Invocation mode:
        # Only supports value ANTI_FAKE_CHECK.
        # 
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cred_name is not None:
            result['CredName'] = self.cred_name

        if self.cred_type is not None:
            result['CredType'] = self.cred_type

        if self.image_file_object is not None:
            result['ImageFile'] = self.image_file_object

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')

        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')

        if m.get('ImageFile') is not None:
            self.image_file_object = m.get('ImageFile')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

