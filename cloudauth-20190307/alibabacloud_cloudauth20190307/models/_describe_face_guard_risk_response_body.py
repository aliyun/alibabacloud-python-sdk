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
        # Return code, **200** indicates successful response from the interface.
        self.code = code
        # Return message.
        self.message = message
        # ID of the request
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
            temp_model = main_models.DescribeFaceGuardRiskResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeFaceGuardRiskResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        risk_extends: str = None,
        risk_tags: str = None,
    ):
        # Unique real-person authentication identifier.
        self.certify_id = certify_id
        # Extended information, in JSON format. (Customized return based on tenant requirements)
        self.risk_extends = risk_extends
        # Device risk tags.
        # 
        # - Multiple device risk tags are separated by commas (,). For example, “ROOT,VPN,HOOK”,
        # 
        # - For more information about device risk tags and their meanings, please refer to the official documentation on Face Guard Tag Descriptions.
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

        if self.risk_extends is not None:
            result['RiskExtends'] = self.risk_extends

        if self.risk_tags is not None:
            result['RiskTags'] = self.risk_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('RiskExtends') is not None:
            self.risk_extends = m.get('RiskExtends')

        if m.get('RiskTags') is not None:
            self.risk_tags = m.get('RiskTags')

        return self

