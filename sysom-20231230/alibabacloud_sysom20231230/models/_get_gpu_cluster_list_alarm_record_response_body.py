# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetGpuClusterListAlarmRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetGpuClusterListAlarmRecordResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: str = None,
    ):
        # The value is "Success" or "Sysom.ServerError".
        self.code = code
        # The list of alert data.
        self.data = data
        # When code is not "Success", message contains the error information.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The total number of returned records.
        self.total = total

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetGpuClusterListAlarmRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetGpuClusterListAlarmRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        alarm_cluster: str = None,
        alarm_ext_info: Any = None,
        alarm_id: str = None,
        alarm_log: str = None,
        alarm_task: str = None,
        alarm_time: str = None,
        alarm_topology: Any = None,
        alarm_type: str = None,
        status: str = None,
        uid: str = None,
    ):
        # The cluster where the alert was triggered.
        self.alarm_cluster = alarm_cluster
        # The additional information about the alert.
        self.alarm_ext_info = alarm_ext_info
        # The unique ID of the alert.
        self.alarm_id = alarm_id
        # The event log associated with the alert.
        self.alarm_log = alarm_log
        # The ID of the task where the anomaly occurred.
        self.alarm_task = alarm_task
        # The date and time when the alert was triggered.
        self.alarm_time = alarm_time
        # The topology snapshot.
        self.alarm_topology = alarm_topology
        # The Alarm Metric for alerting.
        self.alarm_type = alarm_type
        # The task status.
        self.status = status
        # The UUID of the cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_cluster is not None:
            result['alarmCluster'] = self.alarm_cluster

        if self.alarm_ext_info is not None:
            result['alarmExtInfo'] = self.alarm_ext_info

        if self.alarm_id is not None:
            result['alarmId'] = self.alarm_id

        if self.alarm_log is not None:
            result['alarmLog'] = self.alarm_log

        if self.alarm_task is not None:
            result['alarmTask'] = self.alarm_task

        if self.alarm_time is not None:
            result['alarmTime'] = self.alarm_time

        if self.alarm_topology is not None:
            result['alarmTopology'] = self.alarm_topology

        if self.alarm_type is not None:
            result['alarmType'] = self.alarm_type

        if self.status is not None:
            result['status'] = self.status

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmCluster') is not None:
            self.alarm_cluster = m.get('alarmCluster')

        if m.get('alarmExtInfo') is not None:
            self.alarm_ext_info = m.get('alarmExtInfo')

        if m.get('alarmId') is not None:
            self.alarm_id = m.get('alarmId')

        if m.get('alarmLog') is not None:
            self.alarm_log = m.get('alarmLog')

        if m.get('alarmTask') is not None:
            self.alarm_task = m.get('alarmTask')

        if m.get('alarmTime') is not None:
            self.alarm_time = m.get('alarmTime')

        if m.get('alarmTopology') is not None:
            self.alarm_topology = m.get('alarmTopology')

        if m.get('alarmType') is not None:
            self.alarm_type = m.get('alarmType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

