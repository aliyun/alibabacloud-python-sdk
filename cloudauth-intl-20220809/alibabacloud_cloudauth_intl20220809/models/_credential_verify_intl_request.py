# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        cred_name: str = None,
        cred_type: str = None,
        image_file: str = None,
        image_url: str = None,
        product_code: str = None,
    ):
        # The credential name (specified as a numeric code). Valid values:
        # 
        # - Codes starting with 03: enterprise qualification
        #   - 0301: business license issued in the Chinese mainland
        # - Codes starting with 04: transaction voucher
        #   - 0401: bank statement
        #   - 0402: payslip
        #   - 0403: utility bill
        #   - 0405: credit card statement
        #   - 0499: other.
        # 
        # This parameter is required.
        self.cred_name = cred_name
        # The credential type. Valid values:
        # 
        # - 03: enterprise qualification
        # - 04: transaction voucher.
        # 
        # This parameter is required.
        self.cred_type = cred_type
        # The image input stream.
        # > Specify either ImageUrl or ImageFile.
        self.image_file = image_file
        # The URL of the image.
        # > Specify either ImageUrl or ImageFile.
        self.image_url = image_url
        # The call mode. Valid values:
        # - ANTI_FAKE_CHECK: image quality and tampering detection.
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

        if self.image_file is not None:
            result['ImageFile'] = self.image_file

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

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
            self.image_file = m.get('ImageFile')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

