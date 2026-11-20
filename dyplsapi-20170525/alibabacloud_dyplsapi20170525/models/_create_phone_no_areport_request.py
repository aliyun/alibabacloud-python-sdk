# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePhoneNoAReportRequest(DaraModel):
    def __init__(
        self,
        ano_white_group_id: int = None,
        cust_name: str = None,
        document_number: str = None,
        document_type: int = None,
        id_card_alive_photo: str = None,
        id_card_back_photo: str = None,
        id_card_front_photo: str = None,
        owner_id: int = None,
        phone_no_a: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # ID of the A-number group. On the [Qualification Management](https://dyplsnext.console.aliyun.com/qualification) page, click View Details in the A-number whitelist section of the relevant qualification.
        # 
        # This parameter is required.
        self.ano_white_group_id = ano_white_group_id
        # Name.
        # 
        # This parameter is required.
        self.cust_name = cust_name
        # Certificate number.
        # 
        # This parameter is required.
        self.document_number = document_number
        # Certificate type. Enter 1 for an ID card.
        # 
        # This parameter is required.
        self.document_type = document_type
        # OSS path of the front-facing portrait photo.
        # 
        # This parameter is required.
        self.id_card_alive_photo = id_card_alive_photo
        # OSS path of the photo of the back side (portrait side) of the ID card.
        self.id_card_back_photo = id_card_back_photo
        # OSS path of the photo of the front side (national emblem side) of the ID card.
        self.id_card_front_photo = id_card_front_photo
        self.owner_id = owner_id
        # Phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Remark (business remark added by the user).
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ano_white_group_id is not None:
            result['ANoWhiteGroupId'] = self.ano_white_group_id

        if self.cust_name is not None:
            result['CustName'] = self.cust_name

        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number

        if self.document_type is not None:
            result['DocumentType'] = self.document_type

        if self.id_card_alive_photo is not None:
            result['IdCardAlivePhoto'] = self.id_card_alive_photo

        if self.id_card_back_photo is not None:
            result['IdCardBackPhoto'] = self.id_card_back_photo

        if self.id_card_front_photo is not None:
            result['IdCardFrontPhoto'] = self.id_card_front_photo

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ANoWhiteGroupId') is not None:
            self.ano_white_group_id = m.get('ANoWhiteGroupId')

        if m.get('CustName') is not None:
            self.cust_name = m.get('CustName')

        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')

        if m.get('DocumentType') is not None:
            self.document_type = m.get('DocumentType')

        if m.get('IdCardAlivePhoto') is not None:
            self.id_card_alive_photo = m.get('IdCardAlivePhoto')

        if m.get('IdCardBackPhoto') is not None:
            self.id_card_back_photo = m.get('IdCardBackPhoto')

        if m.get('IdCardFrontPhoto') is not None:
            self.id_card_front_photo = m.get('IdCardFrontPhoto')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

