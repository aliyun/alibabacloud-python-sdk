# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListWarehouseScheduleTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        schedule_task_list: List[main_models.ListWarehouseScheduleTaskResponseBodyScheduleTaskList] = None,
    ):
        self.request_id = request_id
        self.schedule_task_list = schedule_task_list

    def validate(self):
        if self.schedule_task_list:
            for v1 in self.schedule_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScheduleTaskList'] = []
        if self.schedule_task_list is not None:
            for k1 in self.schedule_task_list:
                result['ScheduleTaskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.schedule_task_list = []
        if m.get('ScheduleTaskList') is not None:
            for k1 in m.get('ScheduleTaskList'):
                temp_model = main_models.ListWarehouseScheduleTaskResponseBodyScheduleTaskList()
                self.schedule_task_list.append(temp_model.from_map(k1))

        return self

class ListWarehouseScheduleTaskResponseBodyScheduleTaskList(DaraModel):
    def __init__(
        self,
        elastic_type: str = None,
        plans: List[main_models.ListWarehouseScheduleTaskResponseBodyScheduleTaskListPlans] = None,
        reserved_cpu: int = None,
        status: str = None,
        warehouse_id: str = None,
        warehouse_name: str = None,
    ):
        self.elastic_type = elastic_type
        self.plans = plans
        self.reserved_cpu = reserved_cpu
        self.status = status
        self.warehouse_id = warehouse_id
        self.warehouse_name = warehouse_name

    def validate(self):
        if self.plans:
            for v1 in self.plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        result['Plans'] = []
        if self.plans is not None:
            for k1 in self.plans:
                result['Plans'].append(k1.to_map() if k1 else None)

        if self.reserved_cpu is not None:
            result['ReservedCpu'] = self.reserved_cpu

        if self.status is not None:
            result['Status'] = self.status

        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id

        if self.warehouse_name is not None:
            result['WarehouseName'] = self.warehouse_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        self.plans = []
        if m.get('Plans') is not None:
            for k1 in m.get('Plans'):
                temp_model = main_models.ListWarehouseScheduleTaskResponseBodyScheduleTaskListPlans()
                self.plans.append(temp_model.from_map(k1))

        if m.get('ReservedCpu') is not None:
            self.reserved_cpu = m.get('ReservedCpu')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        if m.get('WarehouseName') is not None:
            self.warehouse_name = m.get('WarehouseName')

        return self

class ListWarehouseScheduleTaskResponseBodyScheduleTaskListPlans(DaraModel):
    def __init__(
        self,
        description: str = None,
        elastic_cu: int = None,
        end_time: str = None,
        id: str = None,
        start_time: str = None,
    ):
        self.description = description
        self.elastic_cu = elastic_cu
        self.end_time = end_time
        self.id = id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.elastic_cu is not None:
            result['ElasticCu'] = self.elastic_cu

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ElasticCu') is not None:
            self.elastic_cu = m.get('ElasticCu')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

