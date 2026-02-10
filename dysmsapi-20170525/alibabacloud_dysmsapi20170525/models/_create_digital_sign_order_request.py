# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateDigitalSignOrderRequest(DaraModel):
    def __init__(
        self,
        extend_message: str = None,
        order_context: Dict[str, Any] = None,
        order_type: str = None,
        owner_id: int = None,
        qualification_id: int = None,
        qualification_version: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_id: int = None,
        sign_industry: int = None,
        sign_name: str = None,
        sign_source: int = None,
        submitter: str = None,
    ):
        self.extend_message = extend_message
        self.order_context = order_context
        self.order_type = order_type
        self.owner_id = owner_id
        self.qualification_id = qualification_id
        self.qualification_version = qualification_version
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_id = sign_id
        self.sign_industry = sign_industry
        self.sign_name = sign_name
        self.sign_source = sign_source
        self.submitter = submitter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_message is not None:
            result['ExtendMessage'] = self.extend_message

        if self.order_context is not None:
            result['OrderContext'] = self.order_context

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.qualification_version is not None:
            result['QualificationVersion'] = self.qualification_version

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_id is not None:
            result['SignId'] = self.sign_id

        if self.sign_industry is not None:
            result['SignIndustry'] = self.sign_industry

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sign_source is not None:
            result['SignSource'] = self.sign_source

        if self.submitter is not None:
            result['Submitter'] = self.submitter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendMessage') is not None:
            self.extend_message = m.get('ExtendMessage')

        if m.get('OrderContext') is not None:
            self.order_context = m.get('OrderContext')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('QualificationVersion') is not None:
            self.qualification_version = m.get('QualificationVersion')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')

        if m.get('SignIndustry') is not None:
            self.sign_industry = m.get('SignIndustry')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')

        if m.get('Submitter') is not None:
            self.submitter = m.get('Submitter')

        return self

