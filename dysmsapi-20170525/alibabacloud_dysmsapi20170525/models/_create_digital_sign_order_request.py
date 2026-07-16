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
        # Reserved for future use.
        self.extend_message = extend_message
        # The qualification information. This object is required when you create a signature, or when you update a signature\\"s qualification information.
        # 
        # - qualificationCompanyName: Company name. The name can be up to 150 characters long. It cannot consist of only digits or contain symbols other than the middle dot (·), Chinese brackets (【】), Chinese parentheses (（）), English parentheses (()), and spaces.
        # 
        # - `qualificationOrganizationCode`: The 18-character Unified Social Credit Identifier (USCI). It must be an 18-digit code or a code that consists of 18 uppercase or lowercase letters and digits.
        # 
        # - `qualificationAdminName`: The name of the agent or legal representative. The name must be in Chinese.
        # 
        # - `qualificationAdminIDCard`: The 18-digit ID card number of the agent. Only PRC ID cards are supported.
        # 
        # - `qualificationLegalPersonName`: The name of the legal representative or agent.
        # 
        # - `qualificationLegalPersonIDCard`: The 18-digit ID card number of the legal representative. Only PRC ID cards are supported.
        self.order_context = order_context
        # The operation to perform on the signature. Valid values:
        # 
        # - `UPDATE_DIGITALSMS_SIGN`: Update a signature.
        # 
        # - `DELETE_DIGITALSMS_SIGN`: Delete a signature.
        # 
        # - `CREATE_DIGITALSMS_SIGN`: Create a signature.
        self.order_type = order_type
        self.owner_id = owner_id
        # The ID of the qualification.
        self.qualification_id = qualification_id
        # The version of the qualification.
        self.qualification_version = qualification_version
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the signature.
        self.sign_id = sign_id
        # The industry type. This parameter is required when you create or update a signature. It is optional when you delete a signature. Valid values:
        # 
        # - `0`: General (GENERAL)
        # 
        # - `1`: E-commerce and retail (ECOMMERCE)
        self.sign_industry = sign_industry
        # The signature name. This parameter is required for creating, updating, and deleting signatures.
        # 
        # 1. The name must be 2 to 16 characters in length.
        # 
        # 2. The name can contain Chinese characters, letters, and digits.
        # 
        # - Special characters are not allowed, including $, &, %, #, @, !, ^, \\*, (, ), _, +, -, =, {, }, [, ], |, ;, :, \\", ", <, >, ,, ., /, ?, \\~, and .
        # 
        # - The name cannot be only letters.
        # 
        # - The name cannot be only digits. Spaces are not allowed.
        # 
        # - Emojis are not allowed.
        self.sign_name = sign_name
        # The signature source. This parameter is required when you create or update a signature. It is optional when you delete a signature. Valid values:
        # 
        # - `0`: Enterprises and public institutions
        # 
        # - `2`: App
        self.sign_source = sign_source
        # The ID of the user who submits the order.
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

