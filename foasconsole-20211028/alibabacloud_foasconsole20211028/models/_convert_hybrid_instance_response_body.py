# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class ConvertHybridInstanceResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        order_info: main_models.ConvertHybridInstanceResponseBodyOrderInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_code = err_code
        self.order_info = order_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.order_info:
            self.order_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.order_info is not None:
            result['OrderInfo'] = self.order_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('OrderInfo') is not None:
            temp_model = main_models.ConvertHybridInstanceResponseBodyOrderInfo()
            self.order_info = temp_model.from_map(m.get('OrderInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ConvertHybridInstanceResponseBodyOrderInfo(DaraModel):
    def __init__(
        self,
        elastic_instance_id: str = None,
        instance_id: str = None,
        order_id: int = None,
    ):
        self.elastic_instance_id = elastic_instance_id
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_instance_id is not None:
            result['ElasticInstanceId'] = self.elastic_instance_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticInstanceId') is not None:
            self.elastic_instance_id = m.get('ElasticInstanceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        return self

