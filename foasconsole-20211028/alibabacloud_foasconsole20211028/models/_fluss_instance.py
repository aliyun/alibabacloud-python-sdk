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
        ha: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        order_state: str = None,
        region_id: str = None,
        resource_create_time: int = None,
        resource_expired_time: int = None,
        tablet_server_model: str = None,
        tablet_server_num: int = None,
        tablet_server_type: str = None,
        tiering_post_cu: int = None,
        tiering_pre_cu: int = None,
        uid: str = None,
        v_switches: List[main_models.FlussVswitch] = None,
        vpc_id: str = None,
    ):
        self.cluster_state = cluster_state
        # The cluster status.
        self.cluster_status = cluster_status
        # The URL of the instance management console.
        self.console_url = console_url
        # The disk size, in GB.
        self.disk_size = disk_size
        # Specifies whether high availability (HA) is enabled.
        self.ha = ha
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The order state.
        self.order_state = order_state
        # The ID of the region.
        self.region_id = region_id
        # The creation time of the resource, as a UNIX timestamp in milliseconds.
        self.resource_create_time = resource_create_time
        # The expiration time of the resource, as a UNIX timestamp in milliseconds.
        self.resource_expired_time = resource_expired_time
        # The tablet server model.
        self.tablet_server_model = tablet_server_model
        # The number of tablet servers.
        self.tablet_server_num = tablet_server_num
        # The tablet server type.
        self.tablet_server_type = tablet_server_type
        # The number of compute units (CUs) for post-tiering.
        self.tiering_post_cu = tiering_post_cu
        # The number of compute units (CUs) for pre-tiering.
        self.tiering_pre_cu = tiering_pre_cu
        # The Alibaba Cloud account ID (UID).
        self.uid = uid
        # The VSwitch details.
        self.v_switches = v_switches
        # The VPC ID.
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

        if self.ha is not None:
            result['Ha'] = self.ha

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

        if self.tiering_post_cu is not None:
            result['TieringPostCu'] = self.tiering_post_cu

        if self.tiering_pre_cu is not None:
            result['TieringPreCu'] = self.tiering_pre_cu

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

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

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

        if m.get('TieringPostCu') is not None:
            self.tiering_post_cu = m.get('TieringPostCu')

        if m.get('TieringPreCu') is not None:
            self.tiering_pre_cu = m.get('TieringPreCu')

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

