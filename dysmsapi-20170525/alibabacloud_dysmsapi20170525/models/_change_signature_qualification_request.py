# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeSignatureQualificationRequest(DaraModel):
    def __init__(
        self,
        authorization_letter_id: int = None,
        owner_id: int = None,
        qualification_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        signature_name: str = None,
    ):
        # 授权委托书id
        self.authorization_letter_id = authorization_letter_id
        self.owner_id = owner_id
        # 资质id
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        # 
        # This parameter is required.
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        return self

