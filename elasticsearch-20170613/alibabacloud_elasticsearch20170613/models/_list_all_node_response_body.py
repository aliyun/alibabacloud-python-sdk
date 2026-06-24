# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListAllNodeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListAllNodeResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListAllNodeResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListAllNodeResponseBodyResult(DaraModel):
    def __init__(
        self,
        cpu_percent: str = None,
        disk_used_percent: str = None,
        health: str = None,
        heap_percent: str = None,
        host: str = None,
        load_one_m: str = None,
        node_type: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        # The CPU usage.
        # > When **extended** is set to **true** and the monitoring information of the node is being synchronized, the parameter value returns null. In this case, wait 10 seconds and send the request again to retrieve the value.
        self.cpu_percent = cpu_percent
        # The disk usage.
        self.disk_used_percent = disk_used_percent
        # The health status of the node. Valid values: GREEN, YELLOW, RED, and GRAY.
        self.health = health
        # The JVM memory usage.
        self.heap_percent = heap_percent
        # The IP address of the node.
        self.host = host
        # The one-minute load average.
        self.load_one_m = load_one_m
        # The node type. Valid values:
        # 
        # - MASTER: dedicated master node
        # - WORKER: hot node
        # - WORKER_WARM: warm node
        # - COORDINATING: client node
        # - KIBANA: Kibana node.
        self.node_type = node_type
        # The access port of the node.
        self.port = port
        # The zone where the node resides.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_percent is not None:
            result['cpuPercent'] = self.cpu_percent

        if self.disk_used_percent is not None:
            result['diskUsedPercent'] = self.disk_used_percent

        if self.health is not None:
            result['health'] = self.health

        if self.heap_percent is not None:
            result['heapPercent'] = self.heap_percent

        if self.host is not None:
            result['host'] = self.host

        if self.load_one_m is not None:
            result['loadOneM'] = self.load_one_m

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.port is not None:
            result['port'] = self.port

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuPercent') is not None:
            self.cpu_percent = m.get('cpuPercent')

        if m.get('diskUsedPercent') is not None:
            self.disk_used_percent = m.get('diskUsedPercent')

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('heapPercent') is not None:
            self.heap_percent = m.get('heapPercent')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('loadOneM') is not None:
            self.load_one_m = m.get('loadOneM')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

