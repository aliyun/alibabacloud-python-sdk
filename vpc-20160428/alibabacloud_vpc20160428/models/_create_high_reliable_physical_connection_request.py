# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateHighReliablePhysicalConnectionRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        ap_list: List[main_models.CreateHighReliablePhysicalConnectionRequestApList] = None,
        client_token: str = None,
        device_advanced_capacity: List[str] = None,
        dry_run: str = None,
        high_reliable_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateHighReliablePhysicalConnectionRequestTag] = None,
    ):
        # The language to display the results. Valid values:
        # 
        # *   **zh-CN** (default): Chinese
        # *   **en-US**: English
        self.accept_language = accept_language
        # The access points.
        # 
        # This parameter is required.
        self.ap_list = ap_list
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The advanced features of the device.
        self.device_advanced_capacity = device_advanced_capacity
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The high availability mode. Valid values:
        # 
        # - **MultiApMultiDevice** : This mode supports two access points and two devices, and provides the maximum disaster recovery capability.
        # - **MultiApSingleDevice** : This mode supports two access points and one device, and provides robust disaster recovery capability.
        # - **SingleApMultiDevice** : This mode supports one access point and two devices, and is recommended for non-critical business test and development.
        # - **SingleApMultiConnection** : This mode supports one access point, one device, and multiple physical ports. Only users in the whitelist can use this mode. To use this mode, contact your account manager.
        # 
        # This parameter is required.
        self.high_reliable_type = high_reliable_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port type. Valid values:
        # 
        # *   **100Base-T**: 100 Mbit/s copper Ethernet port
        # *   **1000Base-T**: 1,000 Mbit/s copper Ethernet port
        # *   **1000Base-LX**: 1,000 Mbit/s single-mode optical port (10 km)
        # *   **10GBase-T**: 10,000 Mbit/s copper Ethernet port
        # *   **10GBase-LR**: 10,000 Mbit/s single-mode optical port (10 km)
        # *   **40GBase-LR**: 40,000 Mbit/s single-mode optical port
        # *   **100GBase-LR**: 100,000 Mbit/s single-mode optical port
        # 
        # >  To use ports 40GBase-LR and 100GBase-LR, you must first contact your account manager.
        # 
        # This parameter is required.
        self.port_type = port_type
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag

    def validate(self):
        if self.ap_list:
            for v1 in self.ap_list:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        result['ApList'] = []
        if self.ap_list is not None:
            for k1 in self.ap_list:
                result['ApList'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.device_advanced_capacity is not None:
            result['DeviceAdvancedCapacity'] = self.device_advanced_capacity

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.high_reliable_type is not None:
            result['HighReliableType'] = self.high_reliable_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        self.ap_list = []
        if m.get('ApList') is not None:
            for k1 in m.get('ApList'):
                temp_model = main_models.CreateHighReliablePhysicalConnectionRequestApList()
                self.ap_list.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeviceAdvancedCapacity') is not None:
            self.device_advanced_capacity = m.get('DeviceAdvancedCapacity')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HighReliableType') is not None:
            self.high_reliable_type = m.get('HighReliableType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateHighReliablePhysicalConnectionRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateHighReliablePhysicalConnectionRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the resource. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N to add to the resource. Valid values of N: 1 to 20. The tag value cannot be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

class CreateHighReliablePhysicalConnectionRequestApList(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        bandwidth: int = None,
        circuit_code: str = None,
        description: str = None,
        line_operator: str = None,
        name: str = None,
        optical_module_model: str = None,
        peer_location: str = None,
        port_num: int = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the access point that is associated with the Express Connect circuit.
        # 
        # > Two access points must be specified when **HighReliableType** is set to **MultiApMultiDevice** or **MultiApSingleDevice**. One access point must be specified when **HighReliableType** is set to **SingleApMultiDevice** or **SingleApMultiConnection**.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The maximum bandwidth of the hosted connection. Unit: Mbit/s.
        # 
        # Valid values: 50, 100, 200, 300, 400, 500, 1000, 2000, 4000, 5000, 8000, and 10000.
        self.bandwidth = bandwidth
        # The circuit code of the Express Connect circuit, which is provided by the connectivity provider.
        self.circuit_code = circuit_code
        # The description of the Express Connect circuit.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CT**: China Telecom.
        # *   **CU**: China Unicom.
        # *   **CM**: China Mobile.
        # *   **CO**: other connectivity providers in the Chinese mainland.
        # *   **Equinix**: Equinix.
        # *   **Other**: other connectivity providers outside the Chinese mainland.
        # 
        # This parameter is required.
        self.line_operator = line_operator
        # The name of the Express Connect circuit.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter but cannot start with `http://` or` https://`.
        self.name = name
        self.optical_module_model = optical_module_model
        # The geographical location of the data center.
        self.peer_location = peer_location
        # The number of ports. Valid values: 2 to 16. This parameter is required only when **HighReliableType** is set to **SingleApMultiConnection**.
        self.port_num = port_num
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the Express Connect circuit. Default value: **VPC**.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.description is not None:
            result['Description'] = self.description

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.name is not None:
            result['Name'] = self.name

        if self.optical_module_model is not None:
            result['OpticalModuleModel'] = self.optical_module_model

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.port_num is not None:
            result['PortNum'] = self.port_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpticalModuleModel') is not None:
            self.optical_module_model = m.get('OpticalModuleModel')

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('PortNum') is not None:
            self.port_num = m.get('PortNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

