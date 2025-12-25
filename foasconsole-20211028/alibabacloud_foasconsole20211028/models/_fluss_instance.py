# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class FlussInstance(DaraModel):
    def __init__(
        self,
        cluster_state: main_models.ClusterState = None,
        cluster_status: str = None,
        console_url: str = None,
        disk_size: int = None,
        instance_id: str = None,
        instance_name: str = None,
        order_state: str = None,
        region_id: str = None,
        resource_create_time: int = None,
        resource_expired_time: int = None,
        tablet_server_model: str = None,
        tablet_server_num: int = None,
        tablet_server_type: str = None,
        uid: str = None,
        v_switches: List[main_models.FlussVswitch] = None,
        vpc_id: str = None,
    ):
        self.cluster_state = cluster_state
        self.cluster_status = cluster_status
        self.console_url = console_url
        self.disk_size = disk_size
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.order_state = order_state
        self.region_id = region_id
        self.resource_create_time = resource_create_time
        self.resource_expired_time = resource_expired_time
        self.tablet_server_model = tablet_server_model
        self.tablet_server_num = tablet_server_num
        self.tablet_server_type = tablet_server_type
        self.uid = uid
        self.v_switches = v_switches
        self.vpc_id = vpc_id

    def validate(self):
        if self.cluster_state:
            self.cluster_state.validate()
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_state is not None:
            result['ClusterState'] = self.cluster_state.to_map()

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.console_url is not None:
            result['ConsoleUrl'] = self.console_url

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.order_state is not None:
            result['OrderState'] = self.order_state

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time

        if self.resource_expired_time is not None:
            result['ResourceExpiredTime'] = self.resource_expired_time

        if self.tablet_server_model is not None:
            result['TabletServerModel'] = self.tablet_server_model

        if self.tablet_server_num is not None:
            result['TabletServerNum'] = self.tablet_server_num

        if self.tablet_server_type is not None:
            result['TabletServerType'] = self.tablet_server_type

        if self.uid is not None:
            result['Uid'] = self.uid

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterState') is not None:
            temp_model = main_models.ClusterState()
            self.cluster_state = temp_model.from_map(m.get('ClusterState'))

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('ConsoleUrl') is not None:
            self.console_url = m.get('ConsoleUrl')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('OrderState') is not None:
            self.order_state = m.get('OrderState')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')

        if m.get('ResourceExpiredTime') is not None:
            self.resource_expired_time = m.get('ResourceExpiredTime')

        if m.get('TabletServerModel') is not None:
            self.tablet_server_model = m.get('TabletServerModel')

        if m.get('TabletServerNum') is not None:
            self.tablet_server_num = m.get('TabletServerNum')

        if m.get('TabletServerType') is not None:
            self.tablet_server_type = m.get('TabletServerType')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.FlussVswitch()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

