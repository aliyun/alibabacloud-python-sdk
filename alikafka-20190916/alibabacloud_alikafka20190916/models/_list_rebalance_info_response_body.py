# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class ListRebalanceInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListRebalanceInfoResponseBodyData = None,
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
            temp_model = main_models.ListRebalanceInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRebalanceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        rebalance_info_list: List[main_models.ListRebalanceInfoResponseBodyDataRebalanceInfoList] = None,
    ):
        self.rebalance_info_list = rebalance_info_list

    def validate(self):
        if self.rebalance_info_list:
            for v1 in self.rebalance_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RebalanceInfoList'] = []
        if self.rebalance_info_list is not None:
            for k1 in self.rebalance_info_list:
                result['RebalanceInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rebalance_info_list = []
        if m.get('RebalanceInfoList') is not None:
            for k1 in m.get('RebalanceInfoList'):
                temp_model = main_models.ListRebalanceInfoResponseBodyDataRebalanceInfoList()
                self.rebalance_info_list.append(temp_model.from_map(k1))

        return self

class ListRebalanceInfoResponseBodyDataRebalanceInfoList(DaraModel):
    def __init__(
        self,
        generation: int = None,
        group_id: str = None,
        last_rebalance_timestamp: int = None,
        reason: str = None,
        rebalance_success: bool = None,
        rebalance_time_consuming: int = None,
    ):
        self.generation = generation
        self.group_id = group_id
        self.last_rebalance_timestamp = last_rebalance_timestamp
        self.reason = reason
        self.rebalance_success = rebalance_success
        self.rebalance_time_consuming = rebalance_time_consuming

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generation is not None:
            result['Generation'] = self.generation

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.last_rebalance_timestamp is not None:
            result['LastRebalanceTimestamp'] = self.last_rebalance_timestamp

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.rebalance_success is not None:
            result['RebalanceSuccess'] = self.rebalance_success

        if self.rebalance_time_consuming is not None:
            result['RebalanceTimeConsuming'] = self.rebalance_time_consuming

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LastRebalanceTimestamp') is not None:
            self.last_rebalance_timestamp = m.get('LastRebalanceTimestamp')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RebalanceSuccess') is not None:
            self.rebalance_success = m.get('RebalanceSuccess')

        if m.get('RebalanceTimeConsuming') is not None:
            self.rebalance_time_consuming = m.get('RebalanceTimeConsuming')

        return self

