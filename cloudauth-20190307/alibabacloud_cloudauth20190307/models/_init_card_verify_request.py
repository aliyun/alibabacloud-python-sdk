# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitCardVerifyRequest(DaraModel):
    def __init__(
        self,
        callback_token: str = None,
        callback_url: str = None,
        card_page_number: str = None,
        card_type: str = None,
        doc_scan_mode: str = None,
        merchant_biz_id: str = None,
        meta_info: str = None,
        model: str = None,
        picture_save: str = None,
        verify_meta: str = None,
    ):
        # The security token used for anti-replay and anti-tampering verification. If you specify this parameter, the CallbackToken field is displayed in the callback URL.
        self.callback_token = callback_token
        # The callback URL for authentication results. The URL must start with https. After the authentication is completed, the platform calls back this URL and automatically adds the certifyId and passed fields. Example: https://www.aliyun.com?certifyId=xxxx&passed=T.
        # Warning: The callback is triggered only when the authentication is completed. If the authentication is abandoned, abnormally interrupted, or not performed, no notification is sent. When you receive the callback notification, call the query API to obtain the authentication details if needed.
        self.callback_url = callback_url
        # The number of pages of the ID document collected by the SDK. Valid values:
        # - 1: collects the front side.
        # - 2: collects the front and back sides.
        # If the verification type is the validity period of the ID document (VerifyMeta is set to ID_PERIOD), you must set this parameter to 2.
        # 
        # This parameter is required.
        self.card_page_number = card_page_number
        # The type of the ID document. Valid values:
        # - IDENTITY_CARD: second-generation resident ID card.
        # 
        # This parameter is required.
        self.card_type = card_type
        # The photo capture mode. Valid values:
        # - shoot: photo capture.
        # - scan: scanning.
        # - auto: automatic switchover.
        self.doc_scan_mode = doc_scan_mode
        # The custom unique business identifier used for subsequent troubleshooting. The value must be a unique combination of up to 32 letters and digits.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The MetaInfo environment parameter, which must be obtained by using the client SDK.
        # 
        # This parameter is required.
        self.meta_info = meta_info
        # The verification method. Valid values:
        # - OCR_VERIFY: OCR recognition and authentication mode.
        # 
        # This parameter is required.
        self.model = model
        # Specifies whether to temporarily store the image information collected by the app. Valid values:
        # - Y: yes. If you select this value, the query API can return the image information of the ID document.
        # - N: no.
        # 
        # This parameter is required.
        self.picture_save = picture_save
        # The verification type. Valid values:
        # - ID_2_META: two identity elements (name and ID number).
        # 
        # This parameter is required.
        self.verify_meta = verify_meta

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.card_page_number is not None:
            result['CardPageNumber'] = self.card_page_number

        if self.card_type is not None:
            result['CardType'] = self.card_type

        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.model is not None:
            result['Model'] = self.model

        if self.picture_save is not None:
            result['PictureSave'] = self.picture_save

        if self.verify_meta is not None:
            result['VerifyMeta'] = self.verify_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CardPageNumber') is not None:
            self.card_page_number = m.get('CardPageNumber')

        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')

        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('PictureSave') is not None:
            self.picture_save = m.get('PictureSave')

        if m.get('VerifyMeta') is not None:
            self.verify_meta = m.get('VerifyMeta')

        return self

