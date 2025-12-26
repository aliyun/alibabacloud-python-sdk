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
        # Specifies whether to enable verification with an authoritative data source to enhance document anti-spoofing capabilities.
        # 
        # - **T**: Enable
        # 
        # - **F**: Disable (default)
        # 
        # > 
        # > - **Applicable document types**: Chinese resident ID cards (CHN01001) and Chinese mainland driver\\"s licenses (CHN02001).
        # > - **Data transfer declaration**: If you enable this parameter, you agree to transfer the user\\"s name and certificate number to an authoritative data source in the Chinese mainland for consistency verification.
        # > - **Performance impact:** After you enable this feature, the response time of the API operation increases by 1 to 2 seconds. Adjust the timeout setting.
        self.authorize = authorize
        # Page expected to be recognized
        # 
        # - 01 (default): ID portrait.
        # 
        # - 02: Back of the certificate
        self.doc_page = doc_page
        # Document type.
        # Format: Country (region) code + document type abbreviation + page (optional)
        # Note: If provided, it will automatically check if it matches the model recognition result; if empty, the document type will be returned after model recognition.
        self.doc_type = doc_type
        # Document image, base64 encoded binary stream
        self.id_ocr_picture_base_64 = id_ocr_picture_base_64
        # Document image URL
        self.id_ocr_picture_url = id_ocr_picture_url
        # Whether to turn on the certificate anti-counterfeiting function:
        # 
        # - T: open
        # 
        # - F (default): not turned on.
        self.id_spoof = id_spoof
        # Custom OCR quality detection threshold mode:
        # 
        # - 0: System default
        # - 1: Strict mode
        # - 2: Lenient mode
        # - 3 (default): Disable quality detection
        self.id_threshold = id_threshold
        # A unique business identifier defined by the merchant, used for subsequent problem localization and troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure its uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # Your custom user ID or other identifiers that can uniquely identify a specific user, such as a phone number or email address. It is strongly recommended to pre-desensitize the value of this field, for example, by hashing it.
        self.merchant_user_id = merchant_user_id
        # OCR recognition mode.
        # 0: General document mode.
        # 1: Custom mode.
        self.ocr_model = ocr_model
        # Specifies whether to return additional OCR fields in a standardized format:
        # 
        # - **0**: No (default)
        # 
        # - **1**: Yes
        self.ocr_value_standard = ocr_value_standard
        # The product solution to be integrated.
        # 
        # Value: ID_OCR_MAX
        self.product_code = product_code
        # Prompt (for custom mode)
        self.prompt = prompt
        # Custom scene code, used to distinguish business scenarios, a 10-digit number.
        self.scene_code = scene_code
        # Whether to enable document anti-counterfeiting function, default is not enabled.
        # 
        # - T: Enable document anti-counterfeiting function.
        # - F: Do not enable.
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

