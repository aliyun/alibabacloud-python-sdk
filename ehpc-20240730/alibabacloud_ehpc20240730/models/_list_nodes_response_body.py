# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListNodesResponseBody(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.ListNodesResponseBodyNodes] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the nodes.
        self.nodes = nodes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

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
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        add_time: str = None,
        deployment_set_id: str = None,
        expired_time: str = None,
        hostname: str = None,
        ht_enabled: bool = None,
        id: str = None,
        image_id: str = None,
        instance_type: str = None,
        ip_address: str = None,
        keep_alive: bool = None,
        public_ip_address: str = None,
        queue_name: str = None,
        spot_strategy: str = None,
        state_in_sched: str = None,
        status: str = None,
        total_resources: main_models.ListNodesResponseBodyNodesTotalResources = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The time when the node was created.
        self.add_time = add_time
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The time when the node expires.
        self.expired_time = expired_time
        # The hostname of the node.
        self.hostname = hostname
        # Indicates whether hyper-threading is enabled.
        self.ht_enabled = ht_enabled
        # The instance ID of the node.
        self.id = id
        # The image ID of the node.
        self.image_id = image_id
        # The instance type of the node.
        self.instance_type = instance_type
        # The VPC IP address of the node.
        self.ip_address = ip_address
        # Indicates whether deletion protection is enabled for the node. Valid values:
        # 
        # *   true
        # *   false
        self.keep_alive = keep_alive
        # The public IP address of the node.
        self.public_ip_address = public_ip_address
        # The name of the queue to which the node belongs.
        self.queue_name = queue_name
        # The bidding policy of the node. Valid values:
        # 
        # *   NoSpot: The instances of the compute node are pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are created as preemptible instances with a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The node is a preemptible instance for which the market price at the time of purchase is automatically used as the bidding price.
        self.spot_strategy = spot_strategy
        # The node state in the scheduler.
        self.state_in_sched = state_in_sched
        # The node state. Valid values:
        # 
        # *   uninit: The node is being installed.
        # *   initing: The node is being initialized.
        # *   running: The node is running.
        # *   releasing: The node is being released.
        # *   stopped: The node is stopped.
        # *   exception: The node has run into an exception.
        # *   untracking: The node is not added to the cluster.
        self.status = status
        # The hardware configurations of the node.
        self.total_resources = total_resources
        # The vSwitch ID of the node.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID of the node.
        self.zone_id = zone_id

    def validate(self):
        if self.total_resources:
            self.total_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_time is not None:
            result['AddTime'] = self.add_time

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.ht_enabled is not None:
            result['HtEnabled'] = self.ht_enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.keep_alive is not None:
            result['KeepAlive'] = self.keep_alive

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.state_in_sched is not None:
            result['StateInSched'] = self.state_in_sched

        if self.status is not None:
            result['Status'] = self.status

        if self.total_resources is not None:
            result['TotalResources'] = self.total_resources.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HtEnabled') is not None:
            self.ht_enabled = m.get('HtEnabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('KeepAlive') is not None:
            self.keep_alive = m.get('KeepAlive')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StateInSched') is not None:
            self.state_in_sched = m.get('StateInSched')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalResources') is not None:
            temp_model = main_models.ListNodesResponseBodyNodesTotalResources()
            self.total_resources = temp_model.from_map(m.get('TotalResources'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListNodesResponseBodyNodesTotalResources(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        gpu: int = None,
        memory: int = None,
    ):
        # The number of vCPUs.
        self.cpu = cpu
        # The number of GPUs.
        self.gpu = gpu
        # The amount of memory. Unit: GiB.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

