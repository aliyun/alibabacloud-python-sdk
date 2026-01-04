# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIPv6TranslatorEntriesRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_status: str = None,
        acl_type: str = None,
        allocate_ipv_6addr: str = None,
        allocate_ipv_6port: int = None,
        backend_ipv_4addr: str = None,
        backend_ipv_4port: int = None,
        client_token: str = None,
        entry_name: str = None,
        ipv_6translator_entry_id: str = None,
        ipv_6translator_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        trans_protocol: str = None,
    ):
        # The ID of the network ACL.
        self.acl_id = acl_id
        # Specifies whether to enable access control lists (ACLs). Valid values:
        # 
        # *   **on**
        # *   **off**
        self.acl_status = acl_status
        # The ACL type. Valid values:
        # 
        # *   **white**: a whitelist. IPv6 addresses in the ACL are allowed to access backend services.
        # *   **black**: a blacklist. IPv6 addresses in the ACL are not allowed to access backend services.
        self.acl_type = acl_type
        # The IPv6 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_6addr = allocate_ipv_6addr
        # The port used by the IPv6 address allocated to the IPv6 Translation Service instance.
        self.allocate_ipv_6port = allocate_ipv_6port
        # The public IPv4 address that needs to provide IPv6 services.
        self.backend_ipv_4addr = backend_ipv_4addr
        # The port used by the public IPv4 address that needs to provide IPv6 services.
        self.backend_ipv_4port = backend_ipv_4port
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The name of the IPv6 mapping entry.
        self.entry_name = entry_name
        # The ID of the IPv6 mapping entry.
        # 
        # > If **Ipv6TranslatorId** and **Ipv6TranslatorEntryId** are empty, information about all IPv6 mapping entries is returned. If only **Ipv6TranslatorEntryId** is empty, information about the IPv6 mapping entries of the current IPv6 Translation Service instance is returned.
        self.ipv_6translator_entry_id = ipv_6translator_entry_id
        # The ID of the IPv6 Translation Service instance.
        self.ipv_6translator_id = ipv_6translator_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The region of the IPv6 Translation Service instance. You can call the **DescribeRegions** operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The protocol used by the data to be forwarded.
        self.trans_protocol = trans_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.allocate_ipv_6addr is not None:
            result['AllocateIpv6Addr'] = self.allocate_ipv_6addr

        if self.allocate_ipv_6port is not None:
            result['AllocateIpv6Port'] = self.allocate_ipv_6port

        if self.backend_ipv_4addr is not None:
            result['BackendIpv4Addr'] = self.backend_ipv_4addr

        if self.backend_ipv_4port is not None:
            result['BackendIpv4Port'] = self.backend_ipv_4port

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.entry_name is not None:
            result['EntryName'] = self.entry_name

        if self.ipv_6translator_entry_id is not None:
            result['Ipv6TranslatorEntryId'] = self.ipv_6translator_entry_id

        if self.ipv_6translator_id is not None:
            result['Ipv6TranslatorId'] = self.ipv_6translator_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.trans_protocol is not None:
            result['TransProtocol'] = self.trans_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('AllocateIpv6Addr') is not None:
            self.allocate_ipv_6addr = m.get('AllocateIpv6Addr')

        if m.get('AllocateIpv6Port') is not None:
            self.allocate_ipv_6port = m.get('AllocateIpv6Port')

        if m.get('BackendIpv4Addr') is not None:
            self.backend_ipv_4addr = m.get('BackendIpv4Addr')

        if m.get('BackendIpv4Port') is not None:
            self.backend_ipv_4port = m.get('BackendIpv4Port')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EntryName') is not None:
            self.entry_name = m.get('EntryName')

        if m.get('Ipv6TranslatorEntryId') is not None:
            self.ipv_6translator_entry_id = m.get('Ipv6TranslatorEntryId')

        if m.get('Ipv6TranslatorId') is not None:
            self.ipv_6translator_id = m.get('Ipv6TranslatorId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TransProtocol') is not None:
            self.trans_protocol = m.get('TransProtocol')

        return self

