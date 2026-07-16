# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAccessGatewayOspfRouteRequest(DaraModel):
    def __init__(
        self,
        area_id: int = None,
        authentication_type: str = None,
        cross_account: bool = None,
        dead_time: int = None,
        hello_time: int = None,
        interface_name: str = None,
        md_5key: str = None,
        md_5key_id: int = None,
        networks: str = None,
        ospf_cost: int = None,
        ospf_network_type: str = None,
        password: str = None,
        redistribute_protocol: str = None,
        region_id: str = None,
        resource_uid: str = None,
        router_id: str = None,
        sag_ins_id: str = None,
        sag_sn: str = None,
    ):
        # The OSPF area ID.
        # 
        # The value must be an integer from **1** to **2147483647**.
        # 
        # This parameter is required.
        self.area_id = area_id
        # The authentication method. Valid values:
        # 
        # - **NONE**: No authentication is configured.
        # - **CLEARTEXT**: Plaintext authentication is used.
        # - **MD5**: MD5 authentication is used.
        # 
        # This parameter is required.
        self.authentication_type = authentication_type
        # Specifies whether to query only the SAG instances that belong to other Alibaba Cloud accounts. Valid values:
        # 
        # - **false** (default): No.
        # - **true**: Yes.
        self.cross_account = cross_account
        # The dead interval. Unit: seconds.
        # 
        # The value must be an integer from **1** to **65535**.
        # 
        # This parameter is required.
        self.dead_time = dead_time
        # The interval at which Hello packets are sent. Unit: seconds.
        # 
        # The value must be an integer from **1** to **65535**.
        # 
        # This parameter is required.
        self.hello_time = hello_time
        # The port name.
        # 
        # > This parameter is not in use.
        self.interface_name = interface_name
        # The MD5 key.
        # 
        # The value must be 1 to **47** characters in length.
        # 
        # > This parameter is required only when you set **AuthenticationType** to **MD5**.
        self.md_5key = md_5key
        # The MD5 key ID.
        # 
        # The value must be an integer from 1 to **2147483647**.
        # 
        # > This parameter is required only when you set **AuthenticationType** to **MD5**.
        self.md_5key_id = md_5key_id
        # The network segment.
        # 
        # > This parameter is not in use.
        self.networks = networks
        # The cost of the OSPF route.
        # 
        # > This parameter is not in use.
        self.ospf_cost = ospf_cost
        # The OSPF network type.
        # 
        # > This parameter is not in use.
        self.ospf_network_type = ospf_network_type
        # The password for plaintext authentication.
        # 
        # The password must be 1 to 8 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # > This parameter is required only when you set **AuthenticationType** to **CLEARTEXT**.
        self.password = password
        # The route redistribution protocol.
        # 
        # > This parameter is not in use.
        self.redistribute_protocol = redistribute_protocol
        # The ID of the region where the SAG instance is deployed.
        # 
        # For more information, see [DescribeRegions](https://help.aliyun.com/document_detail/69813.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.resource_uid = resource_uid
        # The OSPF router ID.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.sag_ins_id = sag_ins_id
        # The serial number of the SAG device.
        # 
        # This parameter is required.
        self.sag_sn = sag_sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.cross_account is not None:
            result['CrossAccount'] = self.cross_account

        if self.dead_time is not None:
            result['DeadTime'] = self.dead_time

        if self.hello_time is not None:
            result['HelloTime'] = self.hello_time

        if self.interface_name is not None:
            result['InterfaceName'] = self.interface_name

        if self.md_5key is not None:
            result['Md5Key'] = self.md_5key

        if self.md_5key_id is not None:
            result['Md5KeyId'] = self.md_5key_id

        if self.networks is not None:
            result['Networks'] = self.networks

        if self.ospf_cost is not None:
            result['OspfCost'] = self.ospf_cost

        if self.ospf_network_type is not None:
            result['OspfNetworkType'] = self.ospf_network_type

        if self.password is not None:
            result['Password'] = self.password

        if self.redistribute_protocol is not None:
            result['RedistributeProtocol'] = self.redistribute_protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_uid is not None:
            result['ResourceUid'] = self.resource_uid

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.sag_ins_id is not None:
            result['SagInsId'] = self.sag_ins_id

        if self.sag_sn is not None:
            result['SagSn'] = self.sag_sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('CrossAccount') is not None:
            self.cross_account = m.get('CrossAccount')

        if m.get('DeadTime') is not None:
            self.dead_time = m.get('DeadTime')

        if m.get('HelloTime') is not None:
            self.hello_time = m.get('HelloTime')

        if m.get('InterfaceName') is not None:
            self.interface_name = m.get('InterfaceName')

        if m.get('Md5Key') is not None:
            self.md_5key = m.get('Md5Key')

        if m.get('Md5KeyId') is not None:
            self.md_5key_id = m.get('Md5KeyId')

        if m.get('Networks') is not None:
            self.networks = m.get('Networks')

        if m.get('OspfCost') is not None:
            self.ospf_cost = m.get('OspfCost')

        if m.get('OspfNetworkType') is not None:
            self.ospf_network_type = m.get('OspfNetworkType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RedistributeProtocol') is not None:
            self.redistribute_protocol = m.get('RedistributeProtocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceUid') is not None:
            self.resource_uid = m.get('ResourceUid')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('SagInsId') is not None:
            self.sag_ins_id = m.get('SagInsId')

        if m.get('SagSn') is not None:
            self.sag_sn = m.get('SagSn')

        return self

