# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class DeepfakeDetectIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DeepfakeDetectIntlResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates a successful request, any other value indicates failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
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
            temp_model = main_models.DeepfakeDetectIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DeepfakeDetectIntlResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        result: str = None,
        risk_score: Dict[str, str] = None,
        risk_tag: str = None,
    ):
        # Risk result:
        # 
        # - **0**: Low risk
        # - **1**: High risk
        # - **2**: Suspicious
        self.result = result
        # Risk score map.
        self.risk_score = risk_score
        # Risk tags. Multiple tags are separated by commas (,). Includes:
        # 
        # - **SuspectDeepForgery** Suspected deep forgery  
        # - **SuspectPSFace** Suspected synthetic attack  
        # - **SuspectWarterMark** Suspected watermark presence  
        # - **SuspectTemple** Suspected template attack  
        # - **SuspectAIGCFace**  Suspected generated face  
        # - **SuspectRemake**  Suspected rephotographed face
        self.risk_tag = risk_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result

        if self.risk_score is not None:
            result['RiskScore'] = self.risk_score

        if self.risk_tag is not None:
            result['RiskTag'] = self.risk_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('RiskScore') is not None:
            self.risk_score = m.get('RiskScore')

        if m.get('RiskTag') is not None:
            self.risk_tag = m.get('RiskTag')

        return self

