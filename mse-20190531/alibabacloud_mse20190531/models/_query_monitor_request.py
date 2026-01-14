# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMonitorRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        end_time: int = None,
        instance_id: str = None,
        monitor_type: str = None,
        request_pars: str = None,
        start_time: int = None,
        step: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The timestamp when the monitoring ends.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The metric type. The following metric types are supported:
        # 
        # [Basic system metrics]
        # 
        # *   cpuUsage
        # *   memoryUsage
        # *   diskUsage
        # *   gcCount
        # *   gcTime
        # 
        # [Nacos registry]
        # 
        # *   serviceCount
        # *   writeCostTime
        # *   readCostTime
        # *   TPS regCenterTps
        # *   QPS regCenterQps
        # 
        # [Nacos configuration center]
        # 
        # *   publish
        # *   getConfig
        # 
        # [zookeeper]
        # 
        # *   TPS zk_TpsCount
        # *   QPS zk_QpsCount
        # *   zookeeper_AvgRequestLatency
        # 
        # This parameter is required.
        self.monitor_type = monitor_type
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        # The timestamp when the monitoring starts.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The interval between data points. Unit: seconds.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

