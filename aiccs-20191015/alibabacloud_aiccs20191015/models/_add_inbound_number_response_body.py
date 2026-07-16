# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class AddInboundNumberResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.AddInboundNumberResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details about why access was denied.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the API call succeeded.
        # 
        # - **true**: The call succeeded.
        # 
        # - **false**: The call failed.
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.AddInboundNumberResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AddInboundNumberResponseBodyData(DaraModel):
    def __init__(
        self,
        inbound_number: str = None,
        message: str = None,
        result: bool = None,
    ):
        # The inbound number.
        self.inbound_number = inbound_number
        # The error description.
        self.message = message
        # Indicates whether the number was added successfully. `true` indicates success, and `false` indicates failure.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inbound_number is not None:
            result['InboundNumber'] = self.inbound_number

        if self.message is not None:
            result['Message'] = self.message

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InboundNumber') is not None:
            self.inbound_number = m.get('InboundNumber')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

