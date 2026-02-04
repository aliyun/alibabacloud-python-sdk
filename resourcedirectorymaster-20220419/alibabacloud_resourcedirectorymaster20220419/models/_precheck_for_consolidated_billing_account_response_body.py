# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class PrecheckForConsolidatedBillingAccountResponseBody(DaraModel):
    def __init__(
        self,
        reasons: List[main_models.PrecheckForConsolidatedBillingAccountResponseBodyReasons] = None,
        request_id: str = None,
        result: bool = None,
    ):
        # The cause of the check failure.
        self.reasons = reasons
        # The request ID.
        self.request_id = request_id
        # Indicates whether the check was successful. Valid values:
        # 
        # *   true
        # *   false
        self.result = result

    def validate(self):
        if self.reasons:
            for v1 in self.reasons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Reasons'] = []
        if self.reasons is not None:
            for k1 in self.reasons:
                result['Reasons'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reasons = []
        if m.get('Reasons') is not None:
            for k1 in m.get('Reasons'):
                temp_model = main_models.PrecheckForConsolidatedBillingAccountResponseBodyReasons()
                self.reasons.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class PrecheckForConsolidatedBillingAccountResponseBodyReasons(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

