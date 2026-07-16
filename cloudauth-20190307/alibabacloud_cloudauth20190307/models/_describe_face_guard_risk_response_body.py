# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeFaceGuardRiskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DescribeFaceGuardRiskResponseBodyResultObject = None,
    ):
        # The response code. **200** indicates that the request was successful.
        self.code = code
        # The response message.
        self.message = message
        # Id of the request
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
            temp_model = main_models.DescribeFaceGuardRiskResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeFaceGuardRiskResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        guard_risk_score: float = None,
        risk_extends: str = None,
        risk_tags: str = None,
    ):
        # The unique identifier for ID Verification.
        self.certify_id = certify_id
        # The device risk probability predicted by the device assistant algorithm. A higher score indicates a higher device risk.
        # 
        # Value range: 0 to 100.
        self.guard_risk_score = guard_risk_score
        # The extended information in JSON format. The returned content is customized based on tenant requirements.
        self.risk_extends = risk_extends
        # The device risk labels.
        # 
        # - Multiple device risk labels are separated by commas (,), such as "ROOT,VPN,HOOK".
        # 
        # - For more information about device risk labels and their descriptions, see the Face Guard label description in the official documentation.
        self.risk_tags = risk_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.guard_risk_score is not None:
            result['GuardRiskScore'] = self.guard_risk_score

        if self.risk_extends is not None:
            result['RiskExtends'] = self.risk_extends

        if self.risk_tags is not None:
            result['RiskTags'] = self.risk_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('GuardRiskScore') is not None:
            self.guard_risk_score = m.get('GuardRiskScore')

        if m.get('RiskExtends') is not None:
            self.risk_extends = m.get('RiskExtends')

        if m.get('RiskTags') is not None:
            self.risk_tags = m.get('RiskTags')

        return self

