# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class PodItem(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_start_time: str = None,
        history_pods: List[main_models.PodItem] = None,
        ip: str = None,
        node_name: str = None,
        pod_id: str = None,
        pod_ip: str = None,
        pod_ips: List[main_models.PodNetworkInterface] = None,
        pod_uid: str = None,
        status: str = None,
        sub_status: str = None,
        type: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_start_time = gmt_start_time
        self.history_pods = history_pods
        self.ip = ip
        self.node_name = node_name
        self.pod_id = pod_id
        self.pod_ip = pod_ip
        self.pod_ips = pod_ips
        self.pod_uid = pod_uid
        self.status = status
        self.sub_status = sub_status
        self.type = type

    def validate(self):
        if self.history_pods:
            for v1 in self.history_pods:
                 if v1:
                    v1.validate()
        if self.pod_ips:
            for v1 in self.pod_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        result['HistoryPods'] = []
        if self.history_pods is not None:
            for k1 in self.history_pods:
                result['HistoryPods'].append(k1.to_map() if k1 else None)

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip

        result['PodIps'] = []
        if self.pod_ips is not None:
            for k1 in self.pod_ips:
                result['PodIps'].append(k1.to_map() if k1 else None)

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        self.history_pods = []
        if m.get('HistoryPods') is not None:
            for k1 in m.get('HistoryPods'):
                temp_model = main_models.PodItem()
                self.history_pods.append(temp_model.from_map(k1))

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')

        self.pod_ips = []
        if m.get('PodIps') is not None:
            for k1 in m.get('PodIps'):
                temp_model = main_models.PodNetworkInterface()
                self.pod_ips.append(temp_model.from_map(k1))

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

