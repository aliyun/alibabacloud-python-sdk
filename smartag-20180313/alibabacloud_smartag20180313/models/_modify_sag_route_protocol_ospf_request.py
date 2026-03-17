# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySagRouteProtocolOspfRequest(DaraModel):
    def __init__(
        self,
        area_id: int = None,
        authentication_type: str = None,
        dead_time: int = None,
        hello_time: int = None,
        md_5key: str = None,
        md_5key_id: int = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        router_id: str = None,
        smart_agid: str = None,
        smart_agsn: str = None,
    ):
        # The ID of the OSPF area.
        # 
        # Valid values: **1 to 2147483647**.
        # 
        # This parameter is required.
        self.area_id = area_id
        # The authentication method. Valid values:
        # 
        # *   **NONE**: does not enable authentication.
        # *   **CLEARTEXT**: uses plaintext authentication. You must enter the plaintext password.
        # *   **MD5**: uses MD5 authentication. You must enter the MD5 key ID and the MD5 key.
        # 
        # This parameter is required.
        self.authentication_type = authentication_type
        # The timeout period of OSPF. Unit: seconds.
        # 
        # Valid values: **1 to 65535**.
        # 
        # This parameter is required.
        self.dead_time = dead_time
        # The time interval at which Hello packets are sent. Unit: seconds.
        # 
        # Valid values: **1 to 65535**.
        # 
        # This parameter is required.
        self.hello_time = hello_time
        # The MD5 key value.
        # 
        # Valid values: **1 to 47**.
        # 
        # >  This parameter is required only if **AuthenticationType** is set to **MD5**.
        self.md_5key = md_5key
        # The ID of the MD5 key.
        # 
        # Valid values: **1 to 2147483647**.
        # 
        # >  This parameter is required only if **AuthenticationType** is set to **MD5**.
        self.md_5key_id = md_5key_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The plaintext password.
        # 
        # The password must be 1 to 8 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # >  This parameter is required only if **AuthenticationType** is set to **CLEARTEXT**.
        self.password = password
        # The ID of the region where the SAG instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the router that has OSPF enabled.
        # 
        # Set the value to an IPv4 address.
        # 
        # This parameter is required.
        self.router_id = router_id
        # The ID of the SAG instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The serial number of the SAG device associated with the SAG instance.
        # 
        # This parameter is required.
        self.smart_agsn = smart_agsn

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

        if self.dead_time is not None:
            result['DeadTime'] = self.dead_time

        if self.hello_time is not None:
            result['HelloTime'] = self.hello_time

        if self.md_5key is not None:
            result['Md5Key'] = self.md_5key

        if self.md_5key_id is not None:
            result['Md5KeyId'] = self.md_5key_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.smart_agsn is not None:
            result['SmartAGSn'] = self.smart_agsn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('DeadTime') is not None:
            self.dead_time = m.get('DeadTime')

        if m.get('HelloTime') is not None:
            self.hello_time = m.get('HelloTime')

        if m.get('Md5Key') is not None:
            self.md_5key = m.get('Md5Key')

        if m.get('Md5KeyId') is not None:
            self.md_5key_id = m.get('Md5KeyId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SmartAGSn') is not None:
            self.smart_agsn = m.get('SmartAGSn')

        return self

