# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreatePhysicalConnectionRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        circuit_code: str = None,
        client_token: str = None,
        description: str = None,
        device_advanced_capacity: List[str] = None,
        line_operator: str = None,
        name: str = None,
        optical_module_model: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_location: str = None,
        port_type: str = None,
        redundant_physical_connection_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreatePhysicalConnectionRequestTag] = None,
        type: str = None,
        bandwidth: int = None,
    ):
        # The ID of the access point where the Express Connect circuit is located.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The circuit code provided by the carrier for the Express Connect circuit.
        self.circuit_code = circuit_code
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the Express Connect circuit. 
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # The list of device advanced capabilities.
        self.device_advanced_capacity = device_advanced_capacity
        # The carrier that provides the Express Connect circuit. Valid values:
        # 
        # - **CT**: China Telecom.
        # 
        # - **CU**: China Unicom.
        # 
        # - **CM**: China Mobile.
        # 
        # - **CO**: Other carriers in China. 
        # 
        # - **Equinix**: Equinix.
        # 
        # - **Other**: Other carriers outside China.
        # 
        # This parameter is required.
        self.line_operator = line_operator
        # The name of the Express Connect circuit.  
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-). It cannot start with `http://` or `https://`.
        self.name = name
        # The optical module model supported by the Express Connect circuit access point. Valid values:
        # - 1000Base-LX : 
        #   - `SFP-GE-LR-SM1310,10KM`
        #   - `SFP-GE-ER-SM1310,40KM`
        #   - `SFP-GE-ZR-SM1550,80KM`
        # - 10GBase-LR : 
        #   - `SFP-10G-LR-SM1310,10KM`
        #   - `SFP-10G-ER-SM1550,40KM` 
        #   - `SFP-10G-ZR-SM1550,80KM`  
        # - 40GBase-LR : 
        #   - `QSFP-40G-LR4-WDM1300,10KM`
        #   - `QSFP-40G-ER4-WDM1300,40KM`
        #   - `QSFP-40G-ZR4-WDM1300,80KM`
        # - 100GBase-LR : 
        #   - `QSFP28-100G-LR4-WDM1300,10KM`
        #   - `QSFP28-100G-ER4-WDM1300,40KM`
        #   - `QSFP28-100G-ZR4-WDM1300,80KM`.
        self.optical_module_model = optical_module_model
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The geographical location of the on-premises data center.
        self.peer_location = peer_location
        # The port type of the Express Connect circuit. Valid values:
        # 
        # - **100Base-T**: 100M Ethernet port.
        # 
        # - **1000Base-T**: 1 GE electrical port.
        # 
        # - **1000Base-LX**: GE single-mode optical port (10 km).
        # 
        # - **10GBase-T**: 10 GE electrical port.
        # 
        # - **10GBase-LR**: 10 GE single-mode optical port (10 km).
        # 
        # - **40GBase-LR**: 40 GE single-mode optical port.
        # 
        # - **100GBase-LR**: 100 GE single-mode optical port.
        # 
        # > 40GBase-LR and 100GBase-LR are created based on the actual port availability in the backend. Contact your account manager for port availability details.
        self.port_type = port_type
        # The instance ID of the redundant Express Connect circuit. The redundant circuit must be in the **Allocated**, **Confirmed**, or **Enabled** state.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the Express Connect circuit belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags.
        self.tag = tag
        # The type of the Express Connect circuit. Default value: **VPC**.
        self.type = type
        # The bandwidth of the shared Express Connect circuits. Unit: Mbit/s.
        # 
        # Valid values: **50**, **100**, **200**, **300**, **400**, **500**, **1000**, **2000**, **4000**, **5000**, **8000**, and **10000**.
        self.bandwidth = bandwidth

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.device_advanced_capacity is not None:
            result['DeviceAdvancedCapacity'] = self.device_advanced_capacity

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.name is not None:
            result['Name'] = self.name

        if self.optical_module_model is not None:
            result['OpticalModuleModel'] = self.optical_module_model

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id

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

        if self.type is not None:
            result['Type'] = self.type

        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceAdvancedCapacity') is not None:
            self.device_advanced_capacity = m.get('DeviceAdvancedCapacity')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpticalModuleModel') is not None:
            self.optical_module_model = m.get('OpticalModuleModel')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')

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
                temp_model = main_models.CreatePhysicalConnectionRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')

        return self

class CreatePhysicalConnectionRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

