# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListWarehouseScheduleEventResponseBody(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.ListWarehouseScheduleEventResponseBodyEventList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.event_list = event_list
        self.page_number = page_number
        self.page_size = page_size
        # RequestId
        self.request_id = request_id
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.ListWarehouseScheduleEventResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWarehouseScheduleEventResponseBodyEventList(DaraModel):
    def __init__(
        self,
        cluster_count: int = None,
        cluster_cpu: int = None,
        elastic_cpu: int = None,
        elastic_type: str = None,
        event_name: str = None,
        event_time: str = None,
        failed_reason: str = None,
        init_cluster_count: int = None,
        original_elastic_cpu: int = None,
        reserved_cpu: int = None,
        result: str = None,
        warehouse_name: str = None,
    ):
        self.cluster_count = cluster_count
        self.cluster_cpu = cluster_cpu
        self.elastic_cpu = elastic_cpu
        self.elastic_type = elastic_type
        self.event_name = event_name
        self.event_time = event_time
        self.failed_reason = failed_reason
        self.init_cluster_count = init_cluster_count
        self.original_elastic_cpu = original_elastic_cpu
        self.reserved_cpu = reserved_cpu
        self.result = result
        self.warehouse_name = warehouse_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.cluster_cpu is not None:
            result['ClusterCpu'] = self.cluster_cpu

        if self.elastic_cpu is not None:
            result['ElasticCpu'] = self.elastic_cpu

        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

        if self.init_cluster_count is not None:
            result['InitClusterCount'] = self.init_cluster_count

        if self.original_elastic_cpu is not None:
            result['OriginalElasticCpu'] = self.original_elastic_cpu

        if self.reserved_cpu is not None:
            result['ReservedCpu'] = self.reserved_cpu

        if self.result is not None:
            result['Result'] = self.result

        if self.warehouse_name is not None:
            result['WarehouseName'] = self.warehouse_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('ClusterCpu') is not None:
            self.cluster_cpu = m.get('ClusterCpu')

        if m.get('ElasticCpu') is not None:
            self.elastic_cpu = m.get('ElasticCpu')

        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('InitClusterCount') is not None:
            self.init_cluster_count = m.get('InitClusterCount')

        if m.get('OriginalElasticCpu') is not None:
            self.original_elastic_cpu = m.get('OriginalElasticCpu')

        if m.get('ReservedCpu') is not None:
            self.reserved_cpu = m.get('ReservedCpu')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('WarehouseName') is not None:
            self.warehouse_name = m.get('WarehouseName')

        return self

