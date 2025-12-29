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
        # Security Token, used for anti-replay and anti-tampering checks. If this parameter is passed, the CallbackToken field will be displayed in the callback address.
        self.callback_token = callback_token
        # - The callback notification address for the authentication result, which must start with https.
        # - The platform will call back this address after completing the authentication and automatically add the certifyId and passed fields, example: https://www.aliyun.com?certifyId=xxxx&passed=T
        # - Warning
        # The callback is triggered only when the authentication is completed. If the authentication is abandoned, interrupted abnormally, or not performed, no notification will be sent. It is recommended that when you receive the callback notification, if necessary, you can obtain detailed authentication information through the query interface.
        self.callback_url = callback_url
        # Number of card pages collected by the SDK
        # - You can input 1 or 2; input 1 to collect the front side, input 2 to collect both the front and back sides.
        # 
        # - If the verification type is ID period (VerifyMeta value is ID_PERIOD), you must input 2.
        # 
        # This parameter is required.
        self.card_page_number = card_page_number
        # Type of identification
        # - Resident Second Generation ID Card: IDENTITY_CARD
        # 
        # This parameter is required.
        self.card_type = card_type
        # Enumeration of photo-taking methods (manual/auto)
        # - Take a photo: shoot
        # - Scan: scan 
        # - Auto switch: auto
        self.doc_scan_mode = doc_scan_mode
        # A unique business identifier you define, used for subsequent troubleshooting.
        # Supports a combination of 32 alphanumeric characters, please ensure uniqueness.
        # 
        # This parameter is required.
        self.merchant_biz_id = merchant_biz_id
        # MetaInfo environment parameter, which needs to be obtained through the client SDK.
        # 
        # This parameter is required.
        self.meta_info = meta_info
        # Verification method, value:
        # - OCR_VERIFY: OCR recognition and verification mode.
        # 
        # This parameter is required.
        self.model = model
        # Whether to temporarily store the images collected by the app.
        # - Y: Yes
        # - N: No
        # - If \\"Yes\\" is selected here, the query interface will support returning the card image information.
        # 
        # This parameter is required.
        self.picture_save = picture_save
        # Verification type, value:
        # - Identity two elements (name + ID number): ID_2_META
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

