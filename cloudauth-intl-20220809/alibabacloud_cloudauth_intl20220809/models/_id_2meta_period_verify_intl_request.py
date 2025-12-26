# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id2MetaPeriodVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        doc_name: str = None,
        doc_no: str = None,
        doc_type: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        product_code: str = None,
        scene_code: str = None,
        validity_end_date: str = None,
        validity_start_date: str = None,
    ):
        # The user\\"s name.
        # 
        # This parameter is required.
        self.doc_name = doc_name
        # The user\\"s certificate number.
        # 
        # This parameter is required.
        self.doc_no = doc_no
        # The certificate type, which is uniquely identified by an 8-digit number.
        # 
        # Currently, only second-generation resident ID cards from the Chinese mainland are supported. Set the value to the static field: **00000001**.
        # 
        # For more information, see [Certificate types](https://www.alibabacloud.com/help/en/ekyc/latest/im1u641gyesiqmbg?spm=a2c63.p38356.0.i13#Hu5TG).
        # 
        # This parameter is required.
        self.doc_type = doc_type
        # A unique business identifier that you can customize. Use this identifier to locate and troubleshoot issues. The identifier can be up to 32 characters in length and can contain letters and digits. Make sure that the identifier is unique.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # A custom user ID or another identifier for a specific user, such as a mobile number or email address. Desensitize the value of this field in advance, for example, by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The product solution to integrate. Set the value to **eKYC_Date_MIN**.
        # 
        # This parameter is required.
        self.product_code = product_code
        # A custom authentication scenario ID. You can use this ID to query related records in the console. The ID can be up to 10 characters in length and can contain letters, digits, and underscores (_).
        self.scene_code = scene_code
        # The expiration date of the ID card\\"s validity period. The format is YYYYMMDD.
        # 
        # > If the ID card is valid for a long term, enter **long-term** for this parameter.
        # 
        # This parameter is required.
        self.validity_end_date = validity_end_date
        # The start date of the validity period. The format is YYYYMMDD.
        # 
        # This parameter is required.
        self.validity_start_date = validity_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.doc_no is not None:
            result['DocNo'] = self.doc_no

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.validity_end_date is not None:
            result['ValidityEndDate'] = self.validity_end_date

        if self.validity_start_date is not None:
            result['ValidityStartDate'] = self.validity_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('ValidityEndDate') is not None:
            self.validity_end_date = m.get('ValidityEndDate')

        if m.get('ValidityStartDate') is not None:
            self.validity_start_date = m.get('ValidityStartDate')

        return self

