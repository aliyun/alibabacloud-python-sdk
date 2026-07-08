# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudProcessMonitorResponseBody(DaraModel):
    def __init__(
        self,
        process_monitors: List[main_models.DescribeHybridCloudProcessMonitorResponseBodyProcessMonitors] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of application statuses.
        self.process_monitors = process_monitors
        # The request ID.
        self.request_id = request_id
        # > This parameter is deprecated and no longer returns a valid value.
        self.total_count = total_count

    def validate(self):
        if self.process_monitors:
            for v1 in self.process_monitors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProcessMonitors'] = []
        if self.process_monitors is not None:
            for k1 in self.process_monitors:
                result['ProcessMonitors'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.process_monitors = []
        if m.get('ProcessMonitors') is not None:
            for k1 in m.get('ProcessMonitors'):
                temp_model = main_models.DescribeHybridCloudProcessMonitorResponseBodyProcessMonitors()
                self.process_monitors.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudProcessMonitorResponseBodyProcessMonitors(DaraModel):
    def __init__(
        self,
        levle: str = None,
        process_name: str = None,
        process_status: int = None,
    ):
        # The severity level of the application status. Valid values:
        # 
        # - **normal**: normal.
        # 
        # - **critical**: abnormal.
        self.levle = levle
        # The name of the application running on the cluster node. Valid values:
        # 
        # - **tianqingproxy**: the central management service
        # 
        # - **redis**: the storage service
        # 
        # - **scc**: the traffic metering service
        # 
        # - **keeper**: the threat intelligence service
        # 
        # - **node_exporter**: the application log upload service
        # 
        # - **xagent**: the traffic detection service
        # 
        # - **noproxy**: the traffic forwarding service
        # 
        # - **xloge**: the attack log upload service
        # 
        # - **ilogtail**: the log collection service
        # 
        # - **xlogd**: the log analysis service
        self.process_name = process_name
        # The running status of the application. Valid values:
        # 
        # - **0**: abnormal.
        # 
        # - **1**: normal.
        self.process_status = process_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.levle is not None:
            result['Levle'] = self.levle

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Levle') is not None:
            self.levle = m.get('Levle')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        return self

