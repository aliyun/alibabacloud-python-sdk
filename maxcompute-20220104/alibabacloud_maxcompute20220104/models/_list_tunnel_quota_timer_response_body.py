# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListTunnelQuotaTimerResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListTunnelQuotaTimerResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListTunnelQuotaTimerResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListTunnelQuotaTimerResponseBodyData(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        timezone: str = None,
        tunnel_quota_parameter: main_models.ListTunnelQuotaTimerResponseBodyDataTunnelQuotaParameter = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.timezone = timezone
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

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.tunnel_quota_parameter is not None:
            result['tunnelQuotaParameter'] = self.tunnel_quota_parameter.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('tunnelQuotaParameter') is not None:
            temp_model = main_models.ListTunnelQuotaTimerResponseBodyDataTunnelQuotaParameter()
            self.tunnel_quota_parameter = temp_model.from_map(m.get('tunnelQuotaParameter'))

        return self

class ListTunnelQuotaTimerResponseBodyDataTunnelQuotaParameter(DaraModel):
    def __init__(
        self,
        elastic_reserved_slot_num: int = None,
        slot_num: int = None,
    ):
        self.elastic_reserved_slot_num = elastic_reserved_slot_num
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

