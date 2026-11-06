# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListNumberBindingsOfInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListNumberBindingsOfInstanceResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The list of number binding information.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned by the API operation.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListNumberBindingsOfInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListNumberBindingsOfInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        bound: bool = None,
        number: str = None,
        sip_trunk_id: str = None,
        sip_trunk_name: str = None,
    ):
        # Indicates whether the number is bound to the instance specified in the request.
        self.bound = bound
        # The bound number.
        self.number = number
        # The SIP trunk ID.
        self.sip_trunk_id = sip_trunk_id
        # The SIP trunk name.
        self.sip_trunk_name = sip_trunk_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound is not None:
            result['Bound'] = self.bound

        if self.number is not None:
            result['Number'] = self.number

        if self.sip_trunk_id is not None:
            result['SipTrunkId'] = self.sip_trunk_id

        if self.sip_trunk_name is not None:
            result['SipTrunkName'] = self.sip_trunk_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('SipTrunkId') is not None:
            self.sip_trunk_id = m.get('SipTrunkId')

        if m.get('SipTrunkName') is not None:
            self.sip_trunk_name = m.get('SipTrunkName')

        return self

