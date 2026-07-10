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
        # The security token used for anti-replay and anti-tampering verification. If you specify this parameter, the CallbackToken field is included in the callback URL.
        self.callback_token = callback_token
        # The callback URL for authentication results. The URL must start with https. After the authentication is complete, the system sends a callback to this URL with the certifyId and passed fields automatically appended. Example: https://www.aliyun.com?certifyId=xxxx&passed=T
        # 
        # > **Warning** The callback is triggered only when the authentication is complete. No notification is sent if the authentication is abandoned, interrupted, or not performed. After you receive the callback notification, call the query operation to obtain the authentication details if needed.
        self.callback_url = callback_url
        # The number of card pages to be collected by the SDK. Valid values:
        # - 1: collects the front side only.
        # - 2: collects both the front and back sides.
        # 
        # - If the verification type is ID card validity period (VerifyMeta is set to ID_PERIOD), set this parameter to 2.
        # 
        # This parameter is required.
        self.card_page_number = card_page_number
        # The document type. Valid values:
        # - IDENTITY_CARD: resident identity card.
        # 
        # This parameter is required.
        self.card_type = card_type
        # The photo capture mode (manual or automatic). Valid values:
        # - shoot: manual capture
        # - scan: scan mode 
        # - auto: automatic switchover.
        self.doc_scan_mode = doc_scan_mode
        # A custom business unique identifier that you define for subsequent troubleshooting. The value is a combination of letters and digits up to 32 characters in length. Make sure the value is unique.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # The MetaInfo environment parameter. Obtain this value by using the client SDK.
        # 
        # This parameter is required.
        self.meta_info = meta_info
        # The verification mode. Valid values:
        # - OCR_VERIFY: OCR recognition and authentication mode.
        # 
        # This parameter is required.
        self.model = model
        # Specifies whether to temporarily store images collected by the app. Valid values:
        # - Y: Yes.
        # - N: No.
        # - If you set this parameter to Y, the query operation returns card image information.
        # 
        # This parameter is required.
        self.picture_save = picture_save
        # The verification type. Valid values:
        # - ID_2_META: two-factor identity verification (name + ID card number).
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

