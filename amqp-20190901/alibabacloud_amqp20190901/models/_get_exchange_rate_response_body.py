# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetExchangeRateResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetExchangeRateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetExchangeRateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetExchangeRateResponseBodyData(DaraModel):
    def __init__(
        self,
        exchange_quota_vo: List[main_models.GetExchangeRateResponseBodyDataExchangeQuotaVO] = None,
    ):
        self.exchange_quota_vo = exchange_quota_vo

    def validate(self):
        if self.exchange_quota_vo:
            for v1 in self.exchange_quota_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExchangeQuotaVO'] = []
        if self.exchange_quota_vo is not None:
            for k1 in self.exchange_quota_vo:
                result['ExchangeQuotaVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchange_quota_vo = []
        if m.get('ExchangeQuotaVO') is not None:
            for k1 in m.get('ExchangeQuotaVO'):
                temp_model = main_models.GetExchangeRateResponseBodyDataExchangeQuotaVO()
                self.exchange_quota_vo.append(temp_model.from_map(k1))

        return self

class GetExchangeRateResponseBodyDataExchangeQuotaVO(DaraModel):
    def __init__(
        self,
        exchange_name: str = None,
        in_qps: int = None,
        instance_id: str = None,
        out_qps: int = None,
        vhost_name: str = None,
    ):
        self.exchange_name = exchange_name
        self.in_qps = in_qps
        self.instance_id = instance_id
        self.out_qps = out_qps
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name

        if self.in_qps is not None:
            result['InQps'] = self.in_qps

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.out_qps is not None:
            result['OutQps'] = self.out_qps

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')

        if m.get('InQps') is not None:
            self.in_qps = m.get('InQps')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutQps') is not None:
            self.out_qps = m.get('OutQps')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

