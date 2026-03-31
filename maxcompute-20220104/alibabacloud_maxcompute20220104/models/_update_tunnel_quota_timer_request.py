# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class UpdateTunnelQuotaTimerRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.UpdateTunnelQuotaTimerRequestBody] = None,
        timezone: str = None,
    ):
        # The request body.
        self.body = body
        self.timezone = timezone

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.timezone is not None:
            result['timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.UpdateTunnelQuotaTimerRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        return self

class UpdateTunnelQuotaTimerRequestBody(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        tunnel_quota_parameter: main_models.UpdateTunnelQuotaTimerRequestBodyTunnelQuotaParameter = None,
    ):
        # The start time of the time-specific configuration.
        self.begin_time = begin_time
        # The end time of the time-specific configuration.
        self.end_time = end_time
        # The parameters for the time-specific configuration.
        self.tunnel_quota_parameter = tunnel_quota_parameter

    def validate(self):
        if self.tunnel_quota_parameter:
            self.tunnel_quota_parameter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.tunnel_quota_parameter is not None:
            result['tunnelQuotaParameter'] = self.tunnel_quota_parameter.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('tunnelQuotaParameter') is not None:
            temp_model = main_models.UpdateTunnelQuotaTimerRequestBodyTunnelQuotaParameter()
            self.tunnel_quota_parameter = temp_model.from_map(m.get('tunnelQuotaParameter'))

        return self

class UpdateTunnelQuotaTimerRequestBodyTunnelQuotaParameter(DaraModel):
    def __init__(
        self,
        elastic_reserved_slot_num: int = None,
        slot_num: int = None,
    ):
        # The number of elastically reserved slots.
        self.elastic_reserved_slot_num = elastic_reserved_slot_num
        # The number of reserved slots.
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_reserved_slot_num is not None:
            result['elasticReservedSlotNum'] = self.elastic_reserved_slot_num

        if self.slot_num is not None:
            result['slotNum'] = self.slot_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedSlotNum') is not None:
            self.elastic_reserved_slot_num = m.get('elasticReservedSlotNum')

        if m.get('slotNum') is not None:
            self.slot_num = m.get('slotNum')

        return self

