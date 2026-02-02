# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EntVerifyRequest(DaraModel):
    def __init__(
        self,
        account_no: str = None,
        ent_name: str = None,
        info_verify_type: str = None,
        legal_person_cert_no: str = None,
        legal_person_mobile: str = None,
        legal_person_name: str = None,
        license_no: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        risk_model_version: str = None,
        risk_verify_type: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        # Receiving account, to assist in improving the risk assessment effect.
        self.account_no = account_no
        # Enterprise name.
        self.ent_name = ent_name
        # Enterprise element verification type, currently not supported.
        self.info_verify_type = info_verify_type
        # Legal person\\"s ID number.
        self.legal_person_cert_no = legal_person_cert_no
        # Legal person\\"s mobile phone number.
        self.legal_person_mobile = legal_person_mobile
        # Legal person\\"s name.
        self.legal_person_name = legal_person_name
        # Business license number.
        self.license_no = license_no
        # A unique business identifier defined by the merchant, used for subsequent problem localization and troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure its uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # Merchant-side user ID. It supports a combination of letters and numbers, with a maximum length of 32 characters.
        self.merchant_user_id = merchant_user_id
        # Enterprise risk verification model version, required when RiskVerifyType is not empty. Currently supported:
        # 
        # - BASIC: Basic version
        self.risk_model_version = risk_model_version
        # Enterprise risk verification type, at least one of InfoVerifyType or this must be selected. Currently supported:
        # 
        # - BUSINESS_ANTIFRAUD
        self.risk_verify_type = risk_verify_type
        # Scene code.
        self.scene_code = scene_code
        # Whether the user authorization is obtained.
        # 
        # - 1: Authorized
        # 
        # - 0: Not authorized
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.ent_name is not None:
            result['EntName'] = self.ent_name

        if self.info_verify_type is not None:
            result['InfoVerifyType'] = self.info_verify_type

        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no

        if self.legal_person_mobile is not None:
            result['LegalPersonMobile'] = self.legal_person_mobile

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.license_no is not None:
            result['LicenseNo'] = self.license_no

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.risk_model_version is not None:
            result['RiskModelVersion'] = self.risk_model_version

        if self.risk_verify_type is not None:
            result['RiskVerifyType'] = self.risk_verify_type

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')

        if m.get('InfoVerifyType') is not None:
            self.info_verify_type = m.get('InfoVerifyType')

        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')

        if m.get('LegalPersonMobile') is not None:
            self.legal_person_mobile = m.get('LegalPersonMobile')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('RiskModelVersion') is not None:
            self.risk_model_version = m.get('RiskModelVersion')

        if m.get('RiskVerifyType') is not None:
            self.risk_verify_type = m.get('RiskVerifyType')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')

        return self

