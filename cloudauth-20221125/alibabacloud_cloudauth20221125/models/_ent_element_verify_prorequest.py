# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EntElementVerifyPRORequest(DaraModel):
    def __init__(
        self,
        ent_name: str = None,
        info_verify_type: str = None,
        legal_person_cert_no: str = None,
        legal_person_name: str = None,
        license_no: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        scene_code: str = None,
        user_authorization: str = None,
    ):
        self.ent_name = ent_name
        self.info_verify_type = info_verify_type
        self.legal_person_cert_no = legal_person_cert_no
        self.legal_person_name = legal_person_name
        self.license_no = license_no
        self.merchant_biz_id = merchant_biz_id
        self.merchant_user_id = merchant_user_id
        self.scene_code = scene_code
        self.user_authorization = user_authorization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ent_name is not None:
            result['EntName'] = self.ent_name

        if self.info_verify_type is not None:
            result['InfoVerifyType'] = self.info_verify_type

        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.license_no is not None:
            result['LicenseNo'] = self.license_no

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.user_authorization is not None:
            result['UserAuthorization'] = self.user_authorization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')

        if m.get('InfoVerifyType') is not None:
            self.info_verify_type = m.get('InfoVerifyType')

        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('UserAuthorization') is not None:
            self.user_authorization = m.get('UserAuthorization')

        return self

