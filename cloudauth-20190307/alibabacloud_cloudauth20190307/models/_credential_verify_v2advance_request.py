# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO, List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class CredentialVerifyV2AdvanceRequest(DaraModel):
    def __init__(
        self,
        cert_num: str = None,
        cred_name: str = None,
        cred_type: str = None,
        identify_num: str = None,
        image_context: str = None,
        image_file_object: BinaryIO = None,
        image_url: str = None,
        is_check: str = None,
        is_ocr: str = None,
        merchant_detail: List[main_models.CredentialVerifyV2AdvanceRequestMerchantDetail] = None,
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
        # - 01: personal card or certificate
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
        # - 01: personal card or certificate
        # - 02: business scenario
        # - 03: enterprise qualification.
        self.cred_type = cred_type
        # The ID card number.
        self.identify_num = identify_num
        # The Base64-encoded image. Specify one of imageUrl, imageFile, or imageContext.
        self.image_context = image_context
        # The input stream of the image. Specify one of imageUrl, imageFile, or imageContext.
        self.image_file_object = image_file_object
        # The URL of the image. Specify one of imageUrl, imageFile, or imageContext.
        self.image_url = image_url
        # Specifies whether to enable authoritative verification. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        # >Danger: Deprecated.
        self.is_check = is_check
        # Specifies whether to enable OCR.
        # >Danger: Deprecated.
        self.is_ocr = is_ocr
        # This feature is offline. This parameter no longer takes effect.
        self.merchant_detail = merchant_detail
        # The merchant ID. This parameter is required when CredName is set to 02.
        self.merchant_id = merchant_id
        # The call mode. Valid values:
        # 
        # - ANTI_FAKE_CHECK (default): image anti-forgery detection.
        self.product_code = product_code
        # This feature is offline. This parameter no longer takes effect.
        self.prompt = prompt
        # This feature is offline. This parameter no longer takes effect.
        self.prompt_model = prompt_model
        # The name.
        self.user_name = user_name

    def validate(self):
        if self.merchant_detail:
            for v1 in self.merchant_detail:
                 if v1:
                    v1.validate()

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

        if self.image_file_object is not None:
            result['ImageFile'] = self.image_file_object

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.is_check is not None:
            result['IsCheck'] = self.is_check

        if self.is_ocr is not None:
            result['IsOcr'] = self.is_ocr

        result['MerchantDetail'] = []
        if self.merchant_detail is not None:
            for k1 in self.merchant_detail:
                result['MerchantDetail'].append(k1.to_map() if k1 else None)

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

        if m.get('ImageFile') is not None:
            self.image_file_object = m.get('ImageFile')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('IsCheck') is not None:
            self.is_check = m.get('IsCheck')

        if m.get('IsOcr') is not None:
            self.is_ocr = m.get('IsOcr')

        self.merchant_detail = []
        if m.get('MerchantDetail') is not None:
            for k1 in m.get('MerchantDetail'):
                temp_model = main_models.CredentialVerifyV2AdvanceRequestMerchantDetail()
                self.merchant_detail.append(temp_model.from_map(k1))

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

class CredentialVerifyV2AdvanceRequestMerchantDetail(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This feature is offline. This parameter no longer takes effect.
        self.key = key
        # This feature is offline. This parameter no longer takes effect.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

