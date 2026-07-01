# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsTrademarkRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        trademark_applicant_name: str = None,
        trademark_eff_exp_date: str = None,
        trademark_name: str = None,
        trademark_pic: str = None,
        trademark_registration_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the applicant. The value can be up to 50 characters in length.
        # 
        # This parameter is required.
        self.trademark_applicant_name = trademark_applicant_name
        # The effective and expiration dates of the exclusive right.
        # 
        # This parameter is required.
        self.trademark_eff_exp_date = trademark_eff_exp_date
        # The trademark name. The value can be up to 15 characters in length.
        # 
        # This parameter is required.
        self.trademark_name = trademark_name
        # The fileKey of the trademark details screenshot.
        # 
        # 1. How to query a trademark:
        # - Log on to the China Trademark Network, click **Trademark Online Query**, and take a screenshot of the trademark details.
        # - Accept the terms of use and enter the **Application/Registration Number** to query.
        # - Click the **Application/Registration Number** to view the details.
        # 
        # 2. Information about the trademark file uploaded to OSS. File upload requirements:
        # - The name of the file to be uploaded cannot contain Chinese characters or special characters.
        # - Only images in JPG, PNG, GIF, and JPEG formats are supported, and the image size cannot exceed 5 MB.
        # - The screenshot must contain the complete URL.
        # - The trademark image must be clear and identical to the **signature name**.
        # - The **applicant name** must be identical to the name of the enterprise or institution associated with the signature.
        # - The trademark status must be registered trademark.
        # 
        # 3. To obtain the fileKey, see [Upload files to OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # This parameter is required.
        self.trademark_pic = trademark_pic
        # The trademark registration number. The value can be up to 15 characters in length.
        # 
        # This parameter is required.
        self.trademark_registration_number = trademark_registration_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.trademark_applicant_name is not None:
            result['TrademarkApplicantName'] = self.trademark_applicant_name

        if self.trademark_eff_exp_date is not None:
            result['TrademarkEffExpDate'] = self.trademark_eff_exp_date

        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name

        if self.trademark_pic is not None:
            result['TrademarkPic'] = self.trademark_pic

        if self.trademark_registration_number is not None:
            result['TrademarkRegistrationNumber'] = self.trademark_registration_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrademarkApplicantName') is not None:
            self.trademark_applicant_name = m.get('TrademarkApplicantName')

        if m.get('TrademarkEffExpDate') is not None:
            self.trademark_eff_exp_date = m.get('TrademarkEffExpDate')

        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')

        if m.get('TrademarkPic') is not None:
            self.trademark_pic = m.get('TrademarkPic')

        if m.get('TrademarkRegistrationNumber') is not None:
            self.trademark_registration_number = m.get('TrademarkRegistrationNumber')

        return self

