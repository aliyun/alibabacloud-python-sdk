# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class UpdateNetworkAclEntriesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_acl_entries: List[main_models.UpdateNetworkAclEntriesRequestEgressAclEntries] = None,
        ingress_acl_entries: List[main_models.UpdateNetworkAclEntriesRequestIngressAclEntries] = None,
        network_acl_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        update_egress_acl_entries: bool = None,
        update_ingress_acl_entries: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the request for potential issues, including the AccessKey pair, the permissions of the RAM user, and the required parameters. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The information about the outbound rules.
        self.egress_acl_entries = egress_acl_entries
        # The information about the inbound rule.
        self.ingress_acl_entries = ingress_acl_entries
        # The ID of the network ACL.
        # 
        # This parameter is required.
        self.network_acl_id = network_acl_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the network ACL.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to update outbound rules. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  This parameter cannot be used to add outbound rules to ACLs. If you want to add more outbound rules to ACLs, specify both the existing rule and the rule that you want to add when you call this API operation. If you specify only the rule that you want to add, it overwrites the existing rule.
        self.update_egress_acl_entries = update_egress_acl_entries
        # Specifies whether to update inbound rules. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  This parameter cannot be used to add inbound rules to ACLs. If you want to add more inbound rules to ACLs, you must specify both the existing rule and the rule that you want to add when you call this API operation. If you specify only the rule that you want to add, it overwrites the existing rule.
        self.update_ingress_acl_entries = update_ingress_acl_entries

    def validate(self):
        if self.egress_acl_entries:
            for v1 in self.egress_acl_entries:
                 if v1:
                    v1.validate()
        if self.ingress_acl_entries:
            for v1 in self.ingress_acl_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['EgressAclEntries'] = []
        if self.egress_acl_entries is not None:
            for k1 in self.egress_acl_entries:
                result['EgressAclEntries'].append(k1.to_map() if k1 else None)

        result['IngressAclEntries'] = []
        if self.ingress_acl_entries is not None:
            for k1 in self.ingress_acl_entries:
                result['IngressAclEntries'].append(k1.to_map() if k1 else None)

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.update_egress_acl_entries is not None:
            result['UpdateEgressAclEntries'] = self.update_egress_acl_entries

        if self.update_ingress_acl_entries is not None:
            result['UpdateIngressAclEntries'] = self.update_ingress_acl_entries

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.egress_acl_entries = []
        if m.get('EgressAclEntries') is not None:
            for k1 in m.get('EgressAclEntries'):
                temp_model = main_models.UpdateNetworkAclEntriesRequestEgressAclEntries()
                self.egress_acl_entries.append(temp_model.from_map(k1))

        self.ingress_acl_entries = []
        if m.get('IngressAclEntries') is not None:
            for k1 in m.get('IngressAclEntries'):
                temp_model = main_models.UpdateNetworkAclEntriesRequestIngressAclEntries()
                self.ingress_acl_entries.append(temp_model.from_map(k1))

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UpdateEgressAclEntries') is not None:
            self.update_egress_acl_entries = m.get('UpdateEgressAclEntries')

        if m.get('UpdateIngressAclEntries') is not None:
            self.update_ingress_acl_entries = m.get('UpdateIngressAclEntries')

        return self

class UpdateNetworkAclEntriesRequestIngressAclEntries(DaraModel):
    def __init__(
        self,
        description: str = None,
        entry_type: str = None,
        ip_version: str = None,
        network_acl_entry_id: str = None,
        network_acl_entry_name: str = None,
        policy: str = None,
        port: str = None,
        protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The description of the inbound rule.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        # The type of the rule. Set the value to **custom**, which specifies custom rules.
        self.entry_type = entry_type
        # The IP version. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **IPv6**
        self.ip_version = ip_version
        # The ID of the inbound rule.
        # 
        # Valid values of **N**: **0** to **99**. You can specify at most 100 inbound rules.
        self.network_acl_entry_id = network_acl_entry_id
        # The name of the inbound rule.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.network_acl_entry_name = network_acl_entry_name
        # The action to be performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**
        # *   **drop**
        self.policy = policy
        # The source port range of the inbound rule.
        # 
        # *   If the **protocol** of the inbound rule is set to **all**, **icmp**, or **gre**, the port range is -1/-1, which specifies all ports.
        # *   If the **protocol** of the inbound rule is set to **tcp** or **udp**, set the port range in the following format: **1/200** or **80/80**, which specifies port 1 to port 200 or port 80. Valid ports: **1** to **65535**.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   **icmp**
        # *   **gre**
        # *   **tcp**
        # *   **udp**
        # *   **all**
        self.protocol = protocol
        # The source CIDR block.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entry_type is not None:
            result['EntryType'] = self.entry_type

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntryType') is not None:
            self.entry_type = m.get('EntryType')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        return self

class UpdateNetworkAclEntriesRequestEgressAclEntries(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_ip: str = None,
        entry_type: str = None,
        ip_version: str = None,
        network_acl_entry_id: str = None,
        network_acl_entry_name: str = None,
        policy: str = None,
        port: str = None,
        protocol: str = None,
    ):
        # The description of the outbound rule.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        # The destination CIDR block.
        self.destination_cidr_ip = destination_cidr_ip
        # The type of the rule. Set the value to **custom**, which specifies custom rules.
        self.entry_type = entry_type
        # The IP version. Valid values:
        # 
        # *   **IPv4** (default)
        # *   **IPv6**
        self.ip_version = ip_version
        # The ID of the outbound rule.
        # 
        # Valid values of **N**: **0** to **99**. You can specify at most 100 outbound rules.
        self.network_acl_entry_id = network_acl_entry_id
        # The name of the outbound rule.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.network_acl_entry_name = network_acl_entry_name
        # The action to be performed on network traffic that matches the rule. Valid values:
        # 
        # *   **accept**
        # *   **drop**
        self.policy = policy
        # The destination port range of the outbound traffic.
        # 
        # *   If the **protocol** of the outbound rule is set to **all**, **icmp**, or **gre**, the port range is -1/-1, which specified all ports.
        # *   If the **protocol** of the outbound rule is set to **tcp** or **udp**, set the port range in the following format: **1/200** or **80/80**, which specifies port 1 to port 200 or port 80. Valid values for a port: **1** to **65535**.
        self.port = port
        # The protocol. Valid values:
        # 
        # *   **icmp**
        # *   **gre**
        # *   **tcp**
        # *   **udp**
        # *   **all**
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_ip is not None:
            result['DestinationCidrIp'] = self.destination_cidr_ip

        if self.entry_type is not None:
            result['EntryType'] = self.entry_type

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.network_acl_entry_id is not None:
            result['NetworkAclEntryId'] = self.network_acl_entry_id

        if self.network_acl_entry_name is not None:
            result['NetworkAclEntryName'] = self.network_acl_entry_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrIp') is not None:
            self.destination_cidr_ip = m.get('DestinationCidrIp')

        if m.get('EntryType') is not None:
            self.entry_type = m.get('EntryType')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('NetworkAclEntryId') is not None:
            self.network_acl_entry_id = m.get('NetworkAclEntryId')

        if m.get('NetworkAclEntryName') is not None:
            self.network_acl_entry_name = m.get('NetworkAclEntryName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

