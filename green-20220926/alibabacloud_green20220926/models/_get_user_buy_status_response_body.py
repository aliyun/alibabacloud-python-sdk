# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetUserBuyStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetUserBuyStatusResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request. It can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
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

        if self.msg is not None:
            result['Msg'] = self.msg

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
            temp_model = main_models.GetUserBuyStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUserBuyStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        bid: int = None,
        buy: bool = None,
        indebt: bool = None,
        instance_id: str = None,
        tag: str = None,
    ):
        # Bid.
        self.bid = bid
        # Indicates whether the product has been activated on Alibaba Cloud.
        self.buy = buy
        # Indicates whether there is an outstanding payment.
        self.indebt = indebt
        self.instance_id = instance_id
        # Tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.buy is not None:
            result['Buy'] = self.buy

        if self.indebt is not None:
            result['Indebt'] = self.indebt

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Buy') is not None:
            self.buy = m.get('Buy')

        if m.get('Indebt') is not None:
            self.indebt = m.get('Indebt')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

