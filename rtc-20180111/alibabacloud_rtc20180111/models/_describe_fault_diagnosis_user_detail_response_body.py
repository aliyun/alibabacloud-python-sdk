# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeFaultDiagnosisUserDetailResponseBody(DaraModel):
    def __init__(
        self,
        call_info: main_models.DescribeFaultDiagnosisUserDetailResponseBodyCallInfo = None,
        factor_list: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorList] = None,
        fault_metric_data: main_models.DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData = None,
        network_operators: List[str] = None,
        request_id: str = None,
        user_detail: main_models.DescribeFaultDiagnosisUserDetailResponseBodyUserDetail = None,
    ):
        self.call_info = call_info
        self.factor_list = factor_list
        self.fault_metric_data = fault_metric_data
        self.network_operators = network_operators
        self.request_id = request_id
        self.user_detail = user_detail

    def validate(self):
        if self.call_info:
            self.call_info.validate()
        if self.factor_list:
            for v1 in self.factor_list:
                 if v1:
                    v1.validate()
        if self.fault_metric_data:
            self.fault_metric_data.validate()
        if self.user_detail:
            self.user_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_info is not None:
            result['CallInfo'] = self.call_info.to_map()

        result['FactorList'] = []
        if self.factor_list is not None:
            for k1 in self.factor_list:
                result['FactorList'].append(k1.to_map() if k1 else None)

        if self.fault_metric_data is not None:
            result['FaultMetricData'] = self.fault_metric_data.to_map()

        if self.network_operators is not None:
            result['NetworkOperators'] = self.network_operators

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_detail is not None:
            result['UserDetail'] = self.user_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallInfo') is not None:
            temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyCallInfo()
            self.call_info = temp_model.from_map(m.get('CallInfo'))

        self.factor_list = []
        if m.get('FactorList') is not None:
            for k1 in m.get('FactorList'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorList()
                self.factor_list.append(temp_model.from_map(k1))

        if m.get('FaultMetricData') is not None:
            temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData()
            self.fault_metric_data = temp_model.from_map(m.get('FaultMetricData'))

        if m.get('NetworkOperators') is not None:
            self.network_operators = m.get('NetworkOperators')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDetail') is not None:
            temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyUserDetail()
            self.user_detail = temp_model.from_map(m.get('UserDetail'))

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyUserDetail(DaraModel):
    def __init__(
        self,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        network: str = None,
        online_duration: int = None,
        online_periods: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods] = None,
        os: str = None,
        sdk_version: str = None,
        user_id: str = None,
    ):
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.location = location
        self.network = network
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.os = os
        self.sdk_version = sdk_version
        self.user_id = user_id

    def validate(self):
        if self.online_periods:
            for v1 in self.online_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.location is not None:
            result['Location'] = self.location

        if self.network is not None:
            result['Network'] = self.network

        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration

        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k1 in self.online_periods:
                result['OnlinePeriods'].append(k1.to_map() if k1 else None)

        if self.os is not None:
            result['Os'] = self.os

        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')

        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k1 in m.get('OnlinePeriods'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k1))

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyUserDetailOnlinePeriods(DaraModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts

        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')

        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes] = None,
    ):
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFaultMetricDataNodes(DaraModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFactorList(DaraModel):
    def __init__(
        self,
        factor_id: str = None,
        fault_source: str = None,
        related_event_datas: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas] = None,
        related_metric_datas: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas] = None,
    ):
        self.factor_id = factor_id
        self.fault_source = fault_source
        self.related_event_datas = related_event_datas
        self.related_metric_datas = related_metric_datas

    def validate(self):
        if self.related_event_datas:
            for v1 in self.related_event_datas:
                 if v1:
                    v1.validate()
        if self.related_metric_datas:
            for v1 in self.related_metric_datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id

        if self.fault_source is not None:
            result['FaultSource'] = self.fault_source

        result['RelatedEventDatas'] = []
        if self.related_event_datas is not None:
            for k1 in self.related_event_datas:
                result['RelatedEventDatas'].append(k1.to_map() if k1 else None)

        result['RelatedMetricDatas'] = []
        if self.related_metric_datas is not None:
            for k1 in self.related_metric_datas:
                result['RelatedMetricDatas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')

        if m.get('FaultSource') is not None:
            self.fault_source = m.get('FaultSource')

        self.related_event_datas = []
        if m.get('RelatedEventDatas') is not None:
            for k1 in m.get('RelatedEventDatas'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas()
                self.related_event_datas.append(temp_model.from_map(k1))

        self.related_metric_datas = []
        if m.get('RelatedMetricDatas') is not None:
            for k1 in m.get('RelatedMetricDatas'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas()
                self.related_metric_datas.append(temp_model.from_map(k1))

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatas(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes] = None,
        role: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.role = role
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedMetricDatasNodes(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatas(DaraModel):
    def __init__(
        self,
        event_data_items: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems] = None,
        role: str = None,
        user_id: str = None,
    ):
        self.event_data_items = event_data_items
        self.role = role
        self.user_id = user_id

    def validate(self):
        if self.event_data_items:
            for v1 in self.event_data_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k1 in self.event_data_items:
                result['EventDataItems'].append(k1.to_map() if k1 else None)

        if self.role is not None:
            result['Role'] = self.role

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k1 in m.get('EventDataItems'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems()
                self.event_data_items.append(temp_model.from_map(k1))

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItems(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList] = None,
        ts: int = None,
    ):
        self.event_list = event_list
        self.ts = ts

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        if self.ts is not None:
            result['Ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyFactorListRelatedEventDatasEventDataItemsEventList(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        ts: int = None,
    ):
        self.event_name = event_name
        self.event_type = event_type
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.ts is not None:
            result['Ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

class DescribeFaultDiagnosisUserDetailResponseBodyCallInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
    ):
        # App ID。
        self.app_id = app_id
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

