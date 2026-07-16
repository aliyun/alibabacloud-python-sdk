# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccessRuleRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
        priority: int = None,
        rwaccess_type: str = None,
        source_cidr_ip: str = None,
        user_access_type: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The type of the file system.
        # 
        # Valid values:
        # 
        # - standard (default): General-purpose NAS.
        # - extreme: Extreme NAS.
        self.file_system_type = file_system_type
        # The source IPv6 CIDR block.
        # 
        # The value supports CIDR format and IPv6 format address range.
        # 
        # > - The IPv6 feature is supported only by Extreme NAS file systems in regions in the Chinese mainland, and IPv6 must be enabled for the file system.
        # >- Only VPC networks are supported.
        # >- IPv4 and IPv6 are mutually exclusive.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the permission rule.
        # 
        # If an authorized address matches multiple rules, the rule with the highest priority takes effect.
        # 
        # Valid values: 1 to 100. The value 1 indicates the highest priority.
        self.priority = priority
        # The read and write permissions of the authorized address on the file system.
        # 
        # Valid values:
        # - RDWR (default): read and write.
        # - RDONLY: read-only.
        self.rwaccess_type = rwaccess_type
        # The IP address or CIDR block of the authorized address.
        # 
        # The value must be a single IP address or a CIDR block.
        # > Permission groups of the classic network type support only IP addresses.
        self.source_cidr_ip = source_cidr_ip
        # The access permissions of the system user of the authorized address on the file system.
        # 
        # Valid values:
        # - no_squash (default): allows access to the file system as the root user.
        # - root_squash: maps the root user to the nobody user when the root user accesses the file system.
        # - all_squash: maps all users to the nobody user regardless of the user identity.
        # 
        # The nobody user is a default user in Linux. The nobody user can access only public content on the server and has low privileges and high security. Authorization is required for the system user to access the file system.
        self.user_access_type = user_access_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.ipv_6source_cidr_ip is not None:
            result['Ipv6SourceCidrIp'] = self.ipv_6source_cidr_ip

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.user_access_type is not None:
            result['UserAccessType'] = self.user_access_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('Ipv6SourceCidrIp') is not None:
            self.ipv_6source_cidr_ip = m.get('Ipv6SourceCidrIp')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('UserAccessType') is not None:
            self.user_access_type = m.get('UserAccessType')

        return self

