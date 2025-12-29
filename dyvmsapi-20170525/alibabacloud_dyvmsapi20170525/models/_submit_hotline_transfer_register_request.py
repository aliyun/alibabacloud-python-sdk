# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SubmitHotlineTransferRegisterRequest(DaraModel):
    def __init__(
        self,
        agreement: str = None,
        hotline_number: str = None,
        operator_identity_card: str = None,
        operator_mail: str = None,
        operator_mail_verify_code: str = None,
        operator_mobile: str = None,
        operator_mobile_verify_code: str = None,
        operator_name: str = None,
        owner_id: int = None,
        qualification_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        transfer_phone_number_infos: List[main_models.SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos] = None,
    ):
        # The authenticity of the commitment. Valid values:
        # 
        # *   **true**: The commitment is authentic.
        # *   **false**: The commitment is not authentic.
        # 
        # This parameter is required.
        self.agreement = agreement
        # The China 400 number.
        # 
        # This parameter is required.
        self.hotline_number = hotline_number
        # The ID card number of the handler.
        # 
        # This parameter is required.
        self.operator_identity_card = operator_identity_card
        # The email address of the handler.
        # 
        # This parameter is required.
        self.operator_mail = operator_mail
        # The verification code that is received by the mailbox of the handler.
        self.operator_mail_verify_code = operator_mail_verify_code
        # The mobile phone number of the handler.
        # 
        # This parameter is required.
        self.operator_mobile = operator_mobile
        # The verification code that is received by the mobile phone of the handler.
        # 
        # This parameter is required.
        self.operator_mobile_verify_code = operator_mobile_verify_code
        # The name of the handler.
        # 
        # This parameter is required.
        self.operator_name = operator_name
        self.owner_id = owner_id
        # The qualification ID. You can call the [GetHotlineQualificationByOrder](https://help.aliyun.com/document_detail/393548.html) operation to obtain the qualification ID.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The registration information about the China 400 number.
        # 
        # This parameter is required.
        self.transfer_phone_number_infos = transfer_phone_number_infos

    def validate(self):
        if self.transfer_phone_number_infos:
            for v1 in self.transfer_phone_number_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agreement is not None:
            result['Agreement'] = self.agreement

        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number

        if self.operator_identity_card is not None:
            result['OperatorIdentityCard'] = self.operator_identity_card

        if self.operator_mail is not None:
            result['OperatorMail'] = self.operator_mail

        if self.operator_mail_verify_code is not None:
            result['OperatorMailVerifyCode'] = self.operator_mail_verify_code

        if self.operator_mobile is not None:
            result['OperatorMobile'] = self.operator_mobile

        if self.operator_mobile_verify_code is not None:
            result['OperatorMobileVerifyCode'] = self.operator_mobile_verify_code

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['TransferPhoneNumberInfos'] = []
        if self.transfer_phone_number_infos is not None:
            for k1 in self.transfer_phone_number_infos:
                result['TransferPhoneNumberInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agreement') is not None:
            self.agreement = m.get('Agreement')

        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')

        if m.get('OperatorIdentityCard') is not None:
            self.operator_identity_card = m.get('OperatorIdentityCard')

        if m.get('OperatorMail') is not None:
            self.operator_mail = m.get('OperatorMail')

        if m.get('OperatorMailVerifyCode') is not None:
            self.operator_mail_verify_code = m.get('OperatorMailVerifyCode')

        if m.get('OperatorMobile') is not None:
            self.operator_mobile = m.get('OperatorMobile')

        if m.get('OperatorMobileVerifyCode') is not None:
            self.operator_mobile_verify_code = m.get('OperatorMobileVerifyCode')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.transfer_phone_number_infos = []
        if m.get('TransferPhoneNumberInfos') is not None:
            for k1 in m.get('TransferPhoneNumberInfos'):
                temp_model = main_models.SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos()
                self.transfer_phone_number_infos.append(temp_model.from_map(k1))

        return self

class SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos(DaraModel):
    def __init__(
        self,
        identity_card: str = None,
        phone_number: str = None,
        phone_number_owner_name: str = None,
    ):
        # The ID card number of the number owner.
        # 
        # This parameter is required.
        self.identity_card = identity_card
        # The China 400 number that you want to submit for registration.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The real name or company name of the number owner.
        # 
        # This parameter is required.
        self.phone_number_owner_name = phone_number_owner_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_card is not None:
            result['IdentityCard'] = self.identity_card

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_number_owner_name is not None:
            result['PhoneNumberOwnerName'] = self.phone_number_owner_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityCard') is not None:
            self.identity_card = m.get('IdentityCard')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneNumberOwnerName') is not None:
            self.phone_number_owner_name = m.get('PhoneNumberOwnerName')

        return self

