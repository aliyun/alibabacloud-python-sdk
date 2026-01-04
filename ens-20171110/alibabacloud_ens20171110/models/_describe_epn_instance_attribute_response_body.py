# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEpnInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        conf_versions: List[main_models.DescribeEpnInstanceAttributeResponseBodyConfVersions] = None,
        epninstance_id: str = None,
        epninstance_name: str = None,
        instances: List[main_models.DescribeEpnInstanceAttributeResponseBodyInstances] = None,
        networking_model: str = None,
        request_id: str = None,
        v_switches: List[main_models.DescribeEpnInstanceAttributeResponseBodyVSwitches] = None,
    ):
        # The information about the EPN configurations.
        self.conf_versions = conf_versions
        # The ID of the EPN instance.
        self.epninstance_id = epninstance_id
        # The name of the EPN instance.
        self.epninstance_name = epninstance_name
        # The information about the instance.
        self.instances = instances
        # The networking mode. Valid values:
        # 
        # *   SpeedUp: intelligent acceleration network (Internet)
        # *   Connection: internal network
        # *   SpeedUpAndConnection: intelligent acceleration network and internal network
        self.networking_model = networking_model
        # The request ID.
        self.request_id = request_id
        # Details of the vSwitch.
        self.v_switches = v_switches

    def validate(self):
        if self.conf_versions:
            for v1 in self.conf_versions:
                 if v1:
                    v1.validate()
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfVersions'] = []
        if self.conf_versions is not None:
            for k1 in self.conf_versions:
                result['ConfVersions'].append(k1.to_map() if k1 else None)

        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conf_versions = []
        if m.get('ConfVersions') is not None:
            for k1 in m.get('ConfVersions'):
                temp_model = main_models.DescribeEpnInstanceAttributeResponseBodyConfVersions()
                self.conf_versions.append(temp_model.from_map(k1))

        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeEpnInstanceAttributeResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.DescribeEpnInstanceAttributeResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        return self

class DescribeEpnInstanceAttributeResponseBodyVSwitches(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        ens_region_id: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The CIDR block.
        self.cidr_block = cidr_block
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

class DescribeEpnInstanceAttributeResponseBodyInstances(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        isp: str = None,
        private_ip_address: str = None,
        public_ip_address: str = None,
        status: str = None,
    ):
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The ISP. Valid values:
        # 
        # *   cmcc: China Mobile
        # *   unicom: China Unicom
        # *   telecom: China Telecom
        self.isp = isp
        # The private IP address.
        self.private_ip_address = private_ip_address
        # The public IP address.
        self.public_ip_address = public_ip_address
        # The status of the instance. Valid values:
        # 
        # *   Running
        # *   Stopped
        # *   Expired
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeEpnInstanceAttributeResponseBodyConfVersions(DaraModel):
    def __init__(
        self,
        conf_version: str = None,
        ens_region_id: str = None,
    ):
        # The version number.
        self.conf_version = conf_version
        # The ID of the node.
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conf_version is not None:
            result['ConfVersion'] = self.conf_version

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfVersion') is not None:
            self.conf_version = m.get('ConfVersion')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        return self

