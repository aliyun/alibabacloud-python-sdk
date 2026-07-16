# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialVerifyShrinkRequest(DaraModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail_shrink: str = None,
        merchant_id: str = None,
        product_code: str = None,
        prompt: str = None,
        prompt_model: str = None,
        user_name: str = None,
    ):
        # The certificate number.
        self.cert_num = cert_num
        # The credential name. Valid values:
        # 
        # - 01: personal card and certificate
        #   - 0101: ID card
        #   - 0102: bank card
        #   - 0104: teacher qualification certificate
        #   - 0107: student ID card
        # - 02: business scenario
        #   - 0201: storefront photo
        #   - 0202: counter photo
        #   - 0203: scene photo
        # - 03: enterprise qualification
        #   - 0301: business license.
        self.cred_name = cred_name
        # The credential type. Valid values:
        # 
        # - 01: personal card and certificate
        # - 02: business scenario
        # - 03: enterprise qualification.
        self.cred_type = cred_type
        # The ID card number.
        self.identify_num = identify_num
        # The Base64-encoded image. Specify either imageUrl or imageContext.
        self.image_context = image_context
        # The image URL. Specify either imageUrl or imageContext.
        self.image_url = image_url
        # Specifies whether to enable authoritative verification. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.is_check = is_check
        # Specifies whether to enable optical character recognition (OCR). Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        # 
        # You can set **isOCR** to **1** only when **CredType** is set to **01**.
        self.is_ocr = is_ocr
        # This parameter is required when PromptModel is set to DEFAULT.
        self.merchant_detail_shrink = merchant_detail_shrink
        # The merchant ID. This parameter is required when **CredName** is set to **02**.
        self.merchant_id = merchant_id
        # The call mode. Valid values:
        # 
        # * ANTI_FAKE_CHECK: image anti-forgery detection.
        # 
        # * ANTI_FAKE_VL: image anti-forgery detection and semantic understanding.
        # 
        # * IMAGE_VL_COG: image semantic understanding.
        # 
        # Default value: ANTI_FAKE_CHECK.
        # 
        # ProductCode can be set to ANTI_FAKE_VL or IMAGE_VL_COG only when CredType is set to 02.
        self.product_code = product_code
        # The custom prompt content for image semantic understanding.
        # 
        # This parameter is required when PromptModel is set to CUSTOM.
        self.prompt = prompt
        # The method to obtain the prompt for image semantic understanding. Valid values:
        # 
        # * DEFAULT: system default.
        # 
        # * CUSTOM: custom.
        # 
        # Note: This parameter is required when ProductCode is set to ANTI_FAKE_VL or IMAGE_VL_COG.
        self.prompt_model = prompt_model
        # The name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_num is not None:
            result['CertNum'] = self.cert_num

        if self.cred_name is not None:
            result['CredName'] = self.cred_name

        if self.cred_type is not None:
            result['CredType'] = self.cred_type

        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.image_context is not None:
            result['ImageContext'] = self.image_context

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.is_check is not None:
            result['IsCheck'] = self.is_check

        if self.is_ocr is not None:
            result['IsOCR'] = self.is_ocr

        if self.merchant_detail_shrink is not None:
            result['MerchantDetail'] = self.merchant_detail_shrink

        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_model is not None:
            result['PromptModel'] = self.prompt_model

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertNum') is not None:
            self.cert_num = m.get('CertNum')

        if m.get('CredName') is not None:
            self.cred_name = m.get('CredName')

        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')

        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('ImageContext') is not None:
            self.image_context = m.get('ImageContext')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')

        if m.get('IsOCR') is not None:
            self.is_ocr = m.get('IsOCR')

        if m.get('MerchantDetail') is not None:
            self.merchant_detail_shrink = m.get('MerchantDetail')

        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptModel') is not None:
            self.prompt_model = m.get('PromptModel')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

