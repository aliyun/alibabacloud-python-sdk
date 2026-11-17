# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocOcrMaxRequest(DaraModel):
    def __init__(
        self,
        authorize: str = None,
        doc_page: str = None,
        doc_type: str = None,
        id_ocr_picture_base_64: str = None,
        id_ocr_picture_url: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        ocr_model: str = None,
        ocr_value_standard: str = None,
        product_code: str = None,
        prompt: str = None,
        scene_code: str = None,
        spoof: str = None,
    ):
        # Specifies whether to enable authoritative data source verification to enhance the anti-spoofing capability of identity documents. Valid values:
        # - **T**: Enabled.
        # - **F**: Not enabled (default).
        # > 
        # > - **Applicable identity document types**: Chinese resident identity card (CHN01001) and Chinese mainland driver\\"s license (CHN02001).
        # > - **Data transmission statement**: Enabling this parameter indicates that you agree to transmit the user\\"s name and identity document number to an authoritative data source in the Chinese mainland for consistency verification.
        # > - **Performance impact**: After this parameter is enabled, the API response time increases by about 1 to 2 seconds. Adjust the timeout settings accordingly.
        self.authorize = authorize
        # The page to be recognized. Valid values:
        # - 01: portrait side of the identity document (default)
        # - 02: back side of the identity document
        self.doc_page = doc_page
        # The type of the identity document.
        # - Format: country code + identity document type abbreviation + page (optional).
        # 
        # Note
        # - OcrModel = 0: DocType is required and specifies the identity document type. The existing logic remains unchanged.
        # - OcrModel = 1 or 2: DocType must be left empty.
        self.doc_type = doc_type
        # The Base64-encoded image of the identity document. If you choose to pass the identity document image by using the IdOcrPictureBase64 (Base64-encoded image) method, check the image size and do not pass an excessively large image.
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # The URL of the identity document image. The URL must be an HTTP or HTTPS link that is accessible over the Internet.
        self.id_ocr_picture_url = id_ocr_picture_url
        # Specifies whether to enable the identity document anti-spoofing feature. Valid values:
        # - T: Enabled.
        # - F: Not enabled (default).
        self.id_spoof = id_spoof
        # The custom OCR quality check threshold mode. Valid values:
        # - 0: system default
        # - 1: strict mode
        # - 2: loose mode
        # - 3: disable quality check (default)
        self.id_threshold = id_threshold
        # The custom unique business identifier, which is used to locate and troubleshoot issues later. The value can be up to 32 characters in length and can contain letters and digits. Make sure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The custom user ID or other identifiers that can identify a specific user, such as a mobile phone number or an email address. Desensitize the value of this field in advance, such as by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The OCR recognition mode. Valid values:
        # - 0: general identity document recognition mode (default)
        # - 1: automatic identity document classification mode
        # - 2: automatic identity document classification and general recognition mode
        self.ocr_model = ocr_model
        # Specifies whether to enable the standardization of key fields in OCR recognition. Valid values:
        # - 0: no (default) 
        # - 1: yes
        self.ocr_value_standard = ocr_value_standard
        # The product solution to be integrated. Valid value: ID_OCR_MAX.
        self.product_code = product_code
        # **[Deprecated]**
        self.prompt = prompt
        # The custom authentication scene ID, which is used to query related records by entering this scene ID in the console later. The value can be up to 10 characters in length and can contain letters, digits, and underscores.
        self.scene_code = scene_code
        # **[Deprecated]**
        self.spoof = spoof

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorize is not None:
            result['Authorize'] = self.authorize

        if self.doc_page is not None:
            result['DocPage'] = self.doc_page

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.id_ocr_picture_base_64 is not None:
            result['IdOcrPictureBase64'] = self.id_ocr_picture_base_64

        if self.id_ocr_picture_url is not None:
            result['IdOcrPictureUrl'] = self.id_ocr_picture_url

        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof

        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.ocr_model is not None:
            result['OcrModel'] = self.ocr_model

        if self.ocr_value_standard is not None:
            result['OcrValueStandard'] = self.ocr_value_standard

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.spoof is not None:
            result['Spoof'] = self.spoof

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')

        if m.get('DocPage') is not None:
            self.doc_page = m.get('DocPage')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('IdOcrPictureBase64') is not None:
            self.id_ocr_picture_base_64 = m.get('IdOcrPictureBase64')

        if m.get('IdOcrPictureUrl') is not None:
            self.id_ocr_picture_url = m.get('IdOcrPictureUrl')

        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')

        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('OcrModel') is not None:
            self.ocr_model = m.get('OcrModel')

        if m.get('OcrValueStandard') is not None:
            self.ocr_value_standard = m.get('OcrValueStandard')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('Spoof') is not None:
            self.spoof = m.get('Spoof')

        return self

