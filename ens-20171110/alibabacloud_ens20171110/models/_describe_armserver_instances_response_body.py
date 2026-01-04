# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeARMServerInstancesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        servers: List[main_models.DescribeARMServerInstancesResponseBodyServers] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The information about the servers and the AIC instances.
        self.servers = servers
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.servers:
            for v1 in self.servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Servers'] = []
        if self.servers is not None:
            for k1 in self.servers:
                result['Servers'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.servers = []
        if m.get('Servers') is not None:
            for k1 in m.get('Servers'):
                temp_model = main_models.DescribeARMServerInstancesResponseBodyServers()
                self.servers.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeARMServerInstancesResponseBodyServers(DaraModel):
    def __init__(
        self,
        aicinstances: List[main_models.DescribeARMServerInstancesResponseBodyServersAICInstances] = None,
        creation_time: str = None,
        ens_region_id: str = None,
        expired_time: str = None,
        latest_action: str = None,
        name: str = None,
        namespace: str = None,
        pay_type: str = None,
        server_id: str = None,
        spec_name: str = None,
        state: str = None,
        status: str = None,
        tags: List[main_models.DescribeARMServerInstancesResponseBodyServersTags] = None,
    ):
        # The information about the AIC instances.
        self.aicinstances = aicinstances
        # The time when the instance was created.
        self.creation_time = creation_time
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The time when the instance expires.
        self.expired_time = expired_time
        # The operation that was most recently performed.
        self.latest_action = latest_action
        # The name of the server.
        self.name = name
        # The namespace of the cluster to which the server belongs.
        self.namespace = namespace
        # The billing method.
        self.pay_type = pay_type
        # The ID of the server.
        self.server_id = server_id
        # The server specification.
        self.spec_name = spec_name
        # The operation status of the server. Valid values:
        # 
        # *   **success**
        # *   **failed**
        # *   **creating**
        # *   **releasing**
        # *   **rebooting**
        # *   **upgrading**
        self.state = state
        # The running status of the server. Valid values:
        # 
        # *   **running**
        # *   **stopping**
        # *   **down**
        # *   **starting**
        self.status = status
        self.tags = tags

    def validate(self):
        if self.aicinstances:
            for v1 in self.aicinstances:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AICInstances'] = []
        if self.aicinstances is not None:
            for k1 in self.aicinstances:
                result['AICInstances'].append(k1.to_map() if k1 else None)

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.latest_action is not None:
            result['LatestAction'] = self.latest_action

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aicinstances = []
        if m.get('AICInstances') is not None:
            for k1 in m.get('AICInstances'):
                temp_model = main_models.DescribeARMServerInstancesResponseBodyServersAICInstances()
                self.aicinstances.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('LatestAction') is not None:
            self.latest_action = m.get('LatestAction')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeARMServerInstancesResponseBodyServersTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeARMServerInstancesResponseBodyServersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeARMServerInstancesResponseBodyServersAICInstances(DaraModel):
    def __init__(
        self,
        frequency: int = None,
        image_id: str = None,
        instance_id: str = None,
        latest_action: str = None,
        name: str = None,
        network_attributes: main_models.DescribeARMServerInstancesResponseBodyServersAICInstancesNetworkAttributes = None,
        resolution: str = None,
        sdg_deploy_info: main_models.DescribeARMServerInstancesResponseBodyServersAICInstancesSdgDeployInfo = None,
        spec: str = None,
        state: str = None,
        status: str = None,
    ):
        # The refresh rate of the AIC instance. Unit: Hz.
        self.frequency = frequency
        # The ID of the AIC image.
        self.image_id = image_id
        # The ID of the AIC instance.
        self.instance_id = instance_id
        # The operation that was most recently performed.
        self.latest_action = latest_action
        # The name of the container.
        self.name = name
        # The network attributes of the AIC instance.
        self.network_attributes = network_attributes
        # The resolution of the AIC instance.
        self.resolution = resolution
        # The information about the shared data group (SDG) that is deployed on the AIC instance.
        self.sdg_deploy_info = sdg_deploy_info
        # The specification of the AIC instance.
        self.spec = spec
        # The operation status of the AIC instance. Valid values:
        # 
        # *   **success**
        # *   **failed**
        # *   **creating**
        # *   **releasing**
        # *   **rebooting**
        # *   **reseting**
        self.state = state
        # The running status of the AIC instance. Valid values:
        # 
        # *   **running**
        # *   **pending**
        # *   **terminating**
        self.status = status

    def validate(self):
        if self.network_attributes:
            self.network_attributes.validate()
        if self.sdg_deploy_info:
            self.sdg_deploy_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.latest_action is not None:
            result['LatestAction'] = self.latest_action

        if self.name is not None:
            result['Name'] = self.name

        if self.network_attributes is not None:
            result['NetworkAttributes'] = self.network_attributes.to_map()

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.sdg_deploy_info is not None:
            result['SdgDeployInfo'] = self.sdg_deploy_info.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LatestAction') is not None:
            self.latest_action = m.get('LatestAction')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkAttributes') is not None:
            temp_model = main_models.DescribeARMServerInstancesResponseBodyServersAICInstancesNetworkAttributes()
            self.network_attributes = temp_model.from_map(m.get('NetworkAttributes'))

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('SdgDeployInfo') is not None:
            temp_model = main_models.DescribeARMServerInstancesResponseBodyServersAICInstancesSdgDeployInfo()
            self.sdg_deploy_info = temp_model.from_map(m.get('SdgDeployInfo'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeARMServerInstancesResponseBodyServersAICInstancesSdgDeployInfo(DaraModel):
    def __init__(
        self,
        sdgid: str = None,
        status: str = None,
    ):
        # The ID of the SDG.
        self.sdgid = sdgid
        # The deployment status of the SDG. Valid values:
        # 
        # *   **sdg_deploying**
        # *   **failed**
        # *   **success**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeARMServerInstancesResponseBodyServersAICInstancesNetworkAttributes(DaraModel):
    def __init__(
        self,
        ip_address: str = None,
        network_id: str = None,
        v_switch_id: str = None,
    ):
        # The IP address of the AIC instance.
        self.ip_address = ip_address
        # The network ID of the AIC instance.
        self.network_id = network_id
        # The vSwitch ID of the AIC instance.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

