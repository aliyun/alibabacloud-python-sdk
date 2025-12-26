# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class FaceGuardRiskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.FaceGuardRiskResponseBodyResult = None,
    ):
        # The return code. A value of Success indicates that the API operation responded successfully. For more information about how to determine the authentication result, expand the **Return codes** section below.
        self.code = code
        # A detailed description of the return code.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Result object
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.FaceGuardRiskResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class FaceGuardRiskResponseBodyResult(DaraModel):
    def __init__(
        self,
        guard_risk_score: float = None,
        risk_extends: str = None,
        risk_tags: str = None,
        transaction_id: str = None,
    ):
        # The device risk probability predicted by the Device Guard algorithm. A higher score indicates a higher device risk.
        # 
        # Valid values: 0 to 100.
        self.guard_risk_score = guard_risk_score
        # Extended information. This is empty by default.
        self.risk_extends = risk_extends
        # The device risk tags. Multiple risk tags are separated by commas (**,**). For more information about the risk tags and their meanings, expand the **Risk tags (RiskTags)** section below.
        self.risk_tags = risk_tags
        # The transaction ID.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guard_risk_score is not None:
            result['GuardRiskScore'] = self.guard_risk_score

        if self.risk_extends is not None:
            result['RiskExtends'] = self.risk_extends

        if self.risk_tags is not None:
            result['RiskTags'] = self.risk_tags

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuardRiskScore') is not None:
            self.guard_risk_score = m.get('GuardRiskScore')

        if m.get('RiskExtends') is not None:
            self.risk_extends = m.get('RiskExtends')

        if m.get('RiskTags') is not None:
            self.risk_tags = m.get('RiskTags')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

