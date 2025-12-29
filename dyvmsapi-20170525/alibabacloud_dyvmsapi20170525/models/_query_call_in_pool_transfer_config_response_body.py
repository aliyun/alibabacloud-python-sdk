# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryCallInPoolTransferConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryCallInPoolTransferConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryCallInPoolTransferConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryCallInPoolTransferConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        called_route_mode: str = None,
        details: List[main_models.QueryCallInPoolTransferConfigResponseBodyDataDetails] = None,
        gmt_create: int = None,
        transfer_timeout: str = None,
    ):
        # The call mode. Valid values:
        # 
        # *   **roundRobin**
        # *   **random**
        self.called_route_mode = called_route_mode
        # The details of the response parameters.
        self.details = details
        # The time when the call transfer task was created.
        self.gmt_create = gmt_create
        # The timeout period for transferring the call.
        self.transfer_timeout = transfer_timeout

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_route_mode is not None:
            result['CalledRouteMode'] = self.called_route_mode

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.transfer_timeout is not None:
            result['TransferTimeout'] = self.transfer_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledRouteMode') is not None:
            self.called_route_mode = m.get('CalledRouteMode')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.QueryCallInPoolTransferConfigResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('TransferTimeout') is not None:
            self.transfer_timeout = m.get('TransferTimeout')

        return self

class QueryCallInPoolTransferConfigResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        called: str = None,
    ):
        # The number used to transfer the call.
        self.called = called

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called is not None:
            result['Called'] = self.called

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')

        return self

