# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketplaceintl20221230 import models as main_models
from darabonba.model import DaraModel

class PushMeteringDataRequest(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        metering: str = None,
        metering_data: List[main_models.PushMeteringDataRequestMeteringData] = None,
    ):
        self.gmt_create = gmt_create
        self.metering = metering
        self.metering_data = metering_data

    def validate(self):
        if self.metering_data:
            for v1 in self.metering_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.metering is not None:
            result['Metering'] = self.metering

        result['MeteringData'] = []
        if self.metering_data is not None:
            for k1 in self.metering_data:
                result['MeteringData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Metering') is not None:
            self.metering = m.get('Metering')

        self.metering_data = []
        if m.get('MeteringData') is not None:
            for k1 in m.get('MeteringData'):
                temp_model = main_models.PushMeteringDataRequestMeteringData()
                self.metering_data.append(temp_model.from_map(k1))

        return self

class PushMeteringDataRequestMeteringData(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        metering_assist: str = None,
        metering_entity: str = None,
        push_order_biz_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.metering_assist = metering_assist
        self.metering_entity = metering_entity
        self.push_order_biz_id = push_order_biz_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.metering_assist is not None:
            result['MeteringAssist'] = self.metering_assist

        if self.metering_entity is not None:
            result['MeteringEntity'] = self.metering_entity

        if self.push_order_biz_id is not None:
            result['PushOrderBizId'] = self.push_order_biz_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MeteringAssist') is not None:
            self.metering_assist = m.get('MeteringAssist')

        if m.get('MeteringEntity') is not None:
            self.metering_entity = m.get('MeteringEntity')

        if m.get('PushOrderBizId') is not None:
            self.push_order_biz_id = m.get('PushOrderBizId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

