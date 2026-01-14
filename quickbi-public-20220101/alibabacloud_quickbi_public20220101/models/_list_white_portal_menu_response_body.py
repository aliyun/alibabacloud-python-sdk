# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListWhitePortalMenuResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListWhitePortalMenuResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListWhitePortalMenuResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWhitePortalMenuResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_points_value: int = None,
        receiver_id: str = None,
        receiver_type: int = None,
    ):
        self.auth_points_value = auth_points_value
        self.receiver_id = receiver_id
        self.receiver_type = receiver_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_points_value is not None:
            result['AuthPointsValue'] = self.auth_points_value

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPointsValue') is not None:
            self.auth_points_value = m.get('AuthPointsValue')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        return self

