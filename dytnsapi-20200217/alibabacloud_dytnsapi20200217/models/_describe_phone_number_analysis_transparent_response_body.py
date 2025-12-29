# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneNumberAnalysisTransparentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.DescribePhoneNumberAnalysisTransparentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribePhoneNumberAnalysisTransparentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneNumberAnalysisTransparentResponseBodyData(DaraModel):
    def __init__(
        self,
        device_risk: str = None,
        ip_risk: str = None,
        score_1: str = None,
        score_2: str = None,
        score_3: str = None,
    ):
        self.device_risk = device_risk
        self.ip_risk = ip_risk
        self.score_1 = score_1
        self.score_2 = score_2
        self.score_3 = score_3

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_risk is not None:
            result['Device_risk'] = self.device_risk

        if self.ip_risk is not None:
            result['Ip_risk'] = self.ip_risk

        if self.score_1 is not None:
            result['Score1'] = self.score_1

        if self.score_2 is not None:
            result['Score2'] = self.score_2

        if self.score_3 is not None:
            result['Score3'] = self.score_3

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device_risk') is not None:
            self.device_risk = m.get('Device_risk')

        if m.get('Ip_risk') is not None:
            self.ip_risk = m.get('Ip_risk')

        if m.get('Score1') is not None:
            self.score_1 = m.get('Score1')

        if m.get('Score2') is not None:
            self.score_2 = m.get('Score2')

        if m.get('Score3') is not None:
            self.score_3 = m.get('Score3')

        return self

