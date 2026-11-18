# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_marketplaceintl20221230 import models as main_models
from darabonba.model import DaraModel

class DescribePushMeteringDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dynamic_message: str = None,
        force_fatal: bool = None,
        message: str = None,
        request_id: str = None,
        result: main_models.DescribePushMeteringDataResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_message = dynamic_message
        self.force_fatal = force_fatal
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.force_fatal is not None:
            result['ForceFatal'] = self.force_fatal

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ForceFatal') is not None:
            self.force_fatal = m.get('ForceFatal')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribePushMeteringDataResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class DescribePushMeteringDataResponseBodyResult(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        is_push_billing: bool = None,
        metering_assist: str = None,
        metering_entity: str = None,
        push_order_biz_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.is_push_billing = is_push_billing
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

        if self.is_push_billing is not None:
            result['IsPushBilling'] = self.is_push_billing

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

        if m.get('IsPushBilling') is not None:
            self.is_push_billing = m.get('IsPushBilling')

        if m.get('MeteringAssist') is not None:
            self.metering_assist = m.get('MeteringAssist')

        if m.get('MeteringEntity') is not None:
            self.metering_entity = m.get('MeteringEntity')

        if m.get('PushOrderBizId') is not None:
            self.push_order_biz_id = m.get('PushOrderBizId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

