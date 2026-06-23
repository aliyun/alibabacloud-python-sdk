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
        # The language of the response. Valid values:
        # 
        # - **zh-CN** (default): Chinese.
        # - **en-US**: English.
        self.accept_language = accept_language
        # The list of access points.
        # 
        # This parameter is required.
        self.ap_list = ap_list
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The list of advanced device capabilities.
        self.device_advanced_capacity = device_advanced_capacity
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without creating the instance. The system checks the required parameters, request format, and instance status. If the check fails, the error code `DRYRUN.FAIL` is returned along with the corresponding error list. If the check succeeds, the code `DRYRUN.SUCCESS` is returned.
        # 
        # - **false** (default): sends the request. After the request passes the check, the instance is created.
        self.dry_run = dry_run
        # The zone-redundancy mode. Valid values:
        # 
        # - **MultiApMultiDevice**: maximum disaster recovery. This mode supports two different access points and two different devices, providing maximum disaster recovery.
        # - **MultiApSingleDevice**: enhanced disaster recovery. This mode supports two different access points and one device, providing enhanced disaster recovery.
        # - **SingleApMultiDevice**: development and testing. This mode supports one access point and two devices. This mode is recommended only for development and testing of non-critical workloads.
        # - **SingleApMultiConnection**: high-bandwidth load balancing. This mode is available only to users in the whitelist. It supports one access point, one device, and multiple physical ports. To use this mode, contact your account manager.
        # 
        # This parameter is required.
        self.high_reliable_type = high_reliable_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port type of the Express Connect circuit. Valid values:
        # 
        # - **1000Base-LX**: GE single-mode optical port (10 km).
        # 
        # - **10GBase-LR**: 10 GE single-mode optical port (10 km).
        # 
        # - **40GBase-LR**: 40 GE single-mode optical port.
        # 
        # - **100GBase-LR**: 100 GE single-mode optical port.
        #     
        # > 40GBase-LR and 100GBase-LR are subject to the actual port availability. For information about port availability, contact your account manager.
        # 
        # This parameter is required.
        self.port_type = port_type
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        self.region_id = region_id
        # The ID of the resource group to which the Express Connect circuit belongs.
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
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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
        # The ID of the access point for the Express Connect circuit.
        # 
        # > When **HighReliableType** is set to **MultiApMultiDevice** or **MultiApSingleDevice**, you must specify two different access points. When **HighReliableType** is set to **SingleApMultiDevice** or **SingleApMultiConnection**, you must specify one access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The bandwidth of the shared Express Connect circuits. Unit: Mbit/s.
        # 
        # Valid values: 50, 100, 200, 300, 400, 500, 1000, 2000, 4000, 5000, 8000, and 10000.
        self.bandwidth = bandwidth
        # The circuit code provided by the connectivity provider for the Express Connect circuit.
        self.circuit_code = circuit_code
        # The description of the Express Connect circuit.
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or Chinese character, but cannot start with `http://` or `https://`.
        self.description = description
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # - **CT**: China Telecom.
        # 
        # - **CU**: China Unicom.
        # 
        # - **CM**: China Mobile.
        # 
        # - **CO**: other Chinese carriers. 
        # 
        # - **Equinix**: Equinix.
        # 
        # - **Other**: other carriers outside the Chinese mainland.
        # 
        # This parameter is required.
        self.line_operator = line_operator
        # The name of the Express Connect circuit.  
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or Chinese character. It can contain digits, underscores (_), and hyphens (-), but cannot start with `http://` or `https://`.
        self.name = name
        # The optical module model supported by the access point of the Express Connect circuit. Valid values:
        # - 1000Base-LX: 
        #   - `SFP-GE-LR-SM1310,10KM`
        #   - `SFP-GE-ER-SM1310,40KM`
        #   - `SFP-GE-ZR-SM1550,80KM`
        # - 10GBase-LR: 
        #   - `SFP-10G-LR-SM1310,10KM`
        #   - `SFP-10G-ER-SM1550,40KM` 
        #   - `SFP-10G-ZR-SM1550,80KM`  
        # - 40GBase-LR: 
        #   - `QSFP-40G-LR4-WDM1300,10KM`
        #   - `QSFP-40G-ER4-WDM1300,40KM`
        #   - `QSFP-40G-ZR4-WDM1300,80KM`
        # - 100GBase-LR: 
        #   - `QSFP28-100G-LR4-WDM1300,10KM`
        #   - `QSFP28-100G-ER4-WDM1300,40KM`
        #   - `QSFP28-100G-ZR4-WDM1300,80KM`.
        self.optical_module_model = optical_module_model
        # The geographic location of the on-premises data center.
        self.peer_location = peer_location
        # The number of ports. This parameter is required only when **HighReliableType** is set to **SingleApMultiConnection**. Valid values: 2 to 16.
        self.port_num = port_num
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
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

