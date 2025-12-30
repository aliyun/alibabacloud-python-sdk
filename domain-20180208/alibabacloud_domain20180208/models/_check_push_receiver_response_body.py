# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class CheckPushReceiverResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.CheckPushReceiverResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.CheckPushReceiverResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckPushReceiverResponseBodyModule(DaraModel):
    def __init__(
        self,
        can_receive_push: bool = None,
        masked_mobile: str = None,
        reason_code: str = None,
    ):
        self.can_receive_push = can_receive_push
        self.masked_mobile = masked_mobile
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_receive_push is not None:
            result['CanReceivePush'] = self.can_receive_push

        if self.masked_mobile is not None:
            result['MaskedMobile'] = self.masked_mobile

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanReceivePush') is not None:
            self.can_receive_push = m.get('CanReceivePush')

        if m.get('MaskedMobile') is not None:
            self.masked_mobile = m.get('MaskedMobile')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        return self

