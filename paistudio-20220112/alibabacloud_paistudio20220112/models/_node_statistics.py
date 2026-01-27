# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class NodeStatistics(DaraModel):
    def __init__(
        self,
        actual_min_resources: main_models.StatisticsResources = None,
        gpudetails: List[main_models.NodeStatisticsGPUDetails] = None,
        hyper_node_details: List[main_models.NodeStatisticsHyperNodeDetails] = None,
        idle_resources: main_models.StatisticsResources = None,
        schedulable_resources: main_models.StatisticsResources = None,
        system_reserved_resources: main_models.StatisticsResources = None,
    ):
        self.actual_min_resources = actual_min_resources
        self.gpudetails = gpudetails
        self.hyper_node_details = hyper_node_details
        self.idle_resources = idle_resources
        self.schedulable_resources = schedulable_resources
        self.system_reserved_resources = system_reserved_resources

    def validate(self):
        if self.actual_min_resources:
            self.actual_min_resources.validate()
        if self.gpudetails:
            for v1 in self.gpudetails:
                 if v1:
                    v1.validate()
        if self.hyper_node_details:
            for v1 in self.hyper_node_details:
                 if v1:
                    v1.validate()
        if self.idle_resources:
            self.idle_resources.validate()
        if self.schedulable_resources:
            self.schedulable_resources.validate()
        if self.system_reserved_resources:
            self.system_reserved_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_min_resources is not None:
            result['ActualMinResources'] = self.actual_min_resources.to_map()

        result['GPUDetails'] = []
        if self.gpudetails is not None:
            for k1 in self.gpudetails:
                result['GPUDetails'].append(k1.to_map() if k1 else None)

        result['HyperNodeDetails'] = []
        if self.hyper_node_details is not None:
            for k1 in self.hyper_node_details:
                result['HyperNodeDetails'].append(k1.to_map() if k1 else None)

        if self.idle_resources is not None:
            result['IdleResources'] = self.idle_resources.to_map()

        if self.schedulable_resources is not None:
            result['SchedulableResources'] = self.schedulable_resources.to_map()

        if self.system_reserved_resources is not None:
            result['SystemReservedResources'] = self.system_reserved_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualMinResources') is not None:
            temp_model = main_models.StatisticsResources()
            self.actual_min_resources = temp_model.from_map(m.get('ActualMinResources'))

        self.gpudetails = []
        if m.get('GPUDetails') is not None:
            for k1 in m.get('GPUDetails'):
                temp_model = main_models.NodeStatisticsGPUDetails()
                self.gpudetails.append(temp_model.from_map(k1))

        self.hyper_node_details = []
        if m.get('HyperNodeDetails') is not None:
            for k1 in m.get('HyperNodeDetails'):
                temp_model = main_models.NodeStatisticsHyperNodeDetails()
                self.hyper_node_details.append(temp_model.from_map(k1))

        if m.get('IdleResources') is not None:
            temp_model = main_models.StatisticsResources()
            self.idle_resources = temp_model.from_map(m.get('IdleResources'))

        if m.get('SchedulableResources') is not None:
            temp_model = main_models.StatisticsResources()
            self.schedulable_resources = temp_model.from_map(m.get('SchedulableResources'))

        if m.get('SystemReservedResources') is not None:
            temp_model = main_models.StatisticsResources()
            self.system_reserved_resources = temp_model.from_map(m.get('SystemReservedResources'))

        return self

class NodeStatisticsHyperNodeDetails(DaraModel):
    def __init__(
        self,
        count: int = None,
        idle_num: int = None,
    ):
        self.count = count
        self.idle_num = idle_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.idle_num is not None:
            result['IdleNum'] = self.idle_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('IdleNum') is not None:
            self.idle_num = m.get('IdleNum')

        return self

class NodeStatisticsGPUDetails(DaraModel):
    def __init__(
        self,
        count: int = None,
        idle_num: int = None,
    ):
        self.count = count
        self.idle_num = idle_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.idle_num is not None:
            result['IdleNum'] = self.idle_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('IdleNum') is not None:
            self.idle_num = m.get('IdleNum')

        return self

