# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryVmsRealNumberCallConnectionRateInfoResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: main_models.QueryVmsRealNumberCallConnectionRateInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.QueryVmsRealNumberCallConnectionRateInfoResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryVmsRealNumberCallConnectionRateInfoResponseBodyModel(DaraModel):
    def __init__(
        self,
        call_connection_rate: float = None,
        complete_count: int = None,
        region_id: str = None,
        request_count: int = None,
        resource_id: str = None,
        resource_type: str = None,
        ringing_count: int = None,
        ringing_rate: float = None,
    ):
        # 接通率
        self.call_connection_rate = call_connection_rate
        # 接通数
        self.complete_count = complete_count
        self.region_id = region_id
        # 请求通话数
        self.request_count = request_count
        self.resource_id = resource_id
        # EcsInstance, EcsDisk, EcsImage, EcsSnapshot, EcsSecurityGroup, EcsEip, EcsVpc, EcsVRouter, EcsVSwitch, EcsVRouteTable, EcsAuthImage, EcsAll, SlbLoadbalancer, SlbVm, RdsInstance, RdsAllInstance, KvsInstance, OcsInstance, OdpsInstance
        self.resource_type = resource_type
        # 响铃数
        self.ringing_count = ringing_count
        # 响铃率
        self.ringing_rate = ringing_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_connection_rate is not None:
            result['CallConnectionRate'] = self.call_connection_rate

        if self.complete_count is not None:
            result['CompleteCount'] = self.complete_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.ringing_count is not None:
            result['RingingCount'] = self.ringing_count

        if self.ringing_rate is not None:
            result['RingingRate'] = self.ringing_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallConnectionRate') is not None:
            self.call_connection_rate = m.get('CallConnectionRate')

        if m.get('CompleteCount') is not None:
            self.complete_count = m.get('CompleteCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RingingCount') is not None:
            self.ringing_count = m.get('RingingCount')

        if m.get('RingingRate') is not None:
            self.ringing_rate = m.get('RingingRate')

        return self

