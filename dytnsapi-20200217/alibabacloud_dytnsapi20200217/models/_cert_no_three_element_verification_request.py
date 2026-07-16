# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CertNoThreeElementVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_picture: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The authorization code. Sources:
        # - In the Cell Phone Number Service console, go to the [Tag Square](https://dytns.console.aliyun.com/analysis/square) page, select the **ID Card Three Elements** tag, and submit a usage application. After the application is approved, you will obtain the authorization code.
        # - On the [My Applications](https://dytns.console.aliyun.com/analysis/apply) page of the Cell Phone Number Service console, view the approved **ID Card Three Elements** authorization ID.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The name to be verified.
        # 
        # This parameter is required.
        self.cert_name = cert_name
        # The ID card number to be verified.
        # 
        # This parameter is required.
        self.cert_no = cert_no
        # The BASE64 encoding of the portrait photo to be verified. **Remove the encoded URI information (such as `data:image/png;base64,`) before submission**. The photo size and the BASE64-encoded size must not exceed 50 KB.
        # 
        # This parameter is required.
        self.cert_picture = cert_picture
        # Specifies whether to encrypt. Currently only unencrypted is supported.
        self.mask = mask
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.cert_picture is not None:
            result['CertPicture'] = self.cert_picture

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertPicture') is not None:
            self.cert_picture = m.get('CertPicture')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

