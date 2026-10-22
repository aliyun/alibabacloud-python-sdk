# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class SubmitPenetrationTestResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SubmitPenetrationTestResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The response data.
        self.data = data
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The call status. Valid values:
        # 
        # - **true**: Successful.
        # - **false**: Failed.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.SubmitPenetrationTestResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SubmitPenetrationTestResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.SubmitPenetrationTestResponseBodyDataList] = None,
    ):
        # The response data.
        self.list = list

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.SubmitPenetrationTestResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class SubmitPenetrationTestResponseBodyDataList(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        ip: str = None,
    ):
        # The type of the asset. Valid values:
        # 
        # - **EIP**: The public IP address of a virtual private cloud (VPC).
        # - **SLB**: load balancing.
        # - **ECS**: The public IP address of an Elastic Compute Service (ECS) instance in the classic network.
        self.asset_type = asset_type
        # The IP address of the asset.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

