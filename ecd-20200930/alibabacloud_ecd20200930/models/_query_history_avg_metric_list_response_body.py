# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryAvgMetricListResponseBody(DaraModel):
    def __init__(
        self,
        avg_metric_list: List[main_models.QueryHistoryAvgMetricListResponseBodyAvgMetricList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.avg_metric_list = avg_metric_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.avg_metric_list:
            for v1 in self.avg_metric_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvgMetricList'] = []
        if self.avg_metric_list is not None:
            for k1 in self.avg_metric_list:
                result['AvgMetricList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avg_metric_list = []
        if m.get('AvgMetricList') is not None:
            for k1 in m.get('AvgMetricList'):
                temp_model = main_models.QueryHistoryAvgMetricListResponseBodyAvgMetricList()
                self.avg_metric_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryHistoryAvgMetricListResponseBodyAvgMetricList(DaraModel):
    def __init__(
        self,
        avg_value: float = None,
        charge_type: str = None,
        cpu: int = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_type: str = None,
        end_user_ids: List[str] = None,
        gpu_spec: str = None,
        management_flag: str = None,
        memory: int = None,
        multi_resource: bool = None,
        platform: str = None,
        region_id: str = None,
        sessions: List[main_models.QueryHistoryAvgMetricListResponseBodyAvgMetricListSessions] = None,
        sub_pay_type: str = None,
    ):
        self.avg_value = avg_value
        self.charge_type = charge_type
        self.cpu = cpu
        self.desktop_group_id = desktop_group_id
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.desktop_type = desktop_type
        self.end_user_ids = end_user_ids
        self.gpu_spec = gpu_spec
        self.management_flag = management_flag
        self.memory = memory
        self.multi_resource = multi_resource
        self.platform = platform
        self.region_id = region_id
        self.sessions = sessions
        self.sub_pay_type = sub_pay_type

    def validate(self):
        if self.sessions:
            for v1 in self.sessions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_value is not None:
            result['AvgValue'] = self.avg_value

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.multi_resource is not None:
            result['MultiResource'] = self.multi_resource

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Sessions'] = []
        if self.sessions is not None:
            for k1 in self.sessions:
                result['Sessions'].append(k1.to_map() if k1 else None)

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgValue') is not None:
            self.avg_value = m.get('AvgValue')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MultiResource') is not None:
            self.multi_resource = m.get('MultiResource')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.sessions = []
        if m.get('Sessions') is not None:
            for k1 in m.get('Sessions'):
                temp_model = main_models.QueryHistoryAvgMetricListResponseBodyAvgMetricListSessions()
                self.sessions.append(temp_model.from_map(k1))

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        return self

class QueryHistoryAvgMetricListResponseBodyAvgMetricListSessions(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
        external_user_name: str = None,
        nick_name: str = None,
    ):
        self.end_user_id = end_user_id
        self.establishment_time = establishment_time
        self.external_user_name = external_user_name
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time

        if self.external_user_name is not None:
            result['ExternalUserName'] = self.external_user_name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')

        if m.get('ExternalUserName') is not None:
            self.external_user_name = m.get('ExternalUserName')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        return self

