# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class CredentialVerifyV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.CredentialVerifyV2ResponseBodyResultObject = None,
    ):
        # The return code. A value of 200 indicates success. Other values indicate failure.
        self.code = code
        # The return message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.CredentialVerifyV2ResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class CredentialVerifyV2ResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        material_info: str = None,
        ocr_info: str = None,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
        verify_detail: str = None,
        verify_result: str = None,
        vl_result: main_models.CredentialVerifyV2ResponseBodyResultObjectVlResult = None,
    ):
        # The additional information in JSON format.
        self.material_info = material_info
        # The OCR recognition result.
        # >Danger: Deprecated.
        self.ocr_info = ocr_info
        # The risk result. Valid values:
        # 
        # - 0: Low risk.
        # - 1: High risk.
        # - 2: Suspicious.
        self.result = result
        # The risk score map.
        self.risk_score = risk_score
        # The risk tags, separated by commas (,). Valid values:
        # 
        # - PS: image manipulation.
        # - SCREEN_PHOTO: screen recapture.
        # - SCREENSHOT: screenshot.
        # - WATERMARK: watermark.
        # - SAME_BACKGROUND: similar background.
        # - ORIGINAL_PHOTO: non-original image.
        self.risk_tag = risk_tag
        # The authoritative verification details.
        # >Danger: Deprecated.
        self.verify_detail = verify_detail
        # The authoritative verification result.
        # >Danger: Deprecated.
        self.verify_result = verify_result
        # This feature is offline. This parameter no longer takes effect.
        self.vl_result = vl_result

    def validate(self):
        if self.vl_result:
            self.vl_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info

        if self.ocr_info is not None:
            result['OcrInfo'] = self.ocr_info

        if self.result is not None:
            result['Result'] = self.result

        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score

        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag

        if self.verify_detail is not None:
            result['VerifyDetail'] = self.verify_detail

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        if self.vl_result is not None:
            result['VlResult'] = self.vl_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')

        if m.get('OcrInfo') is not None:
            self.ocr_info = m.get('OcrInfo')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')

        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')

        if m.get('VerifyDetail') is not None:
            self.verify_detail = m.get('VerifyDetail')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        if m.get('VlResult') is not None:
            temp_model = main_models.CredentialVerifyV2ResponseBodyResultObjectVlResult()
            self.vl_result = temp_model.from_map(m.get('VlResult'))

        return self

class CredentialVerifyV2ResponseBodyResultObjectVlResult(DaraModel):
    def __init__(
        self,
        success: bool = None,
        vl_content: str = None,
    ):
        # This feature is offline. This parameter no longer takes effect.
        self.success = success
        # This feature is offline. This parameter no longer takes effect.
        self.vl_content = vl_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success is not None:
            result['Success'] = self.success

        if self.vl_content is not None:
            result['VlContent'] = self.vl_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('VlContent') is not None:
            self.vl_content = m.get('VlContent')

        return self

