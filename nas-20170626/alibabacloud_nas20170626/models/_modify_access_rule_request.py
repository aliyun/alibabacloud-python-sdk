# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccessRuleRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
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
        # The ID of the permission rule.
        # 
        # This parameter is required.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # - standard (default): General-purpose NAS.
        # - extreme: Extreme NAS.
        self.file_system_type = file_system_type
        # The source IPv6 CIDR block.
        # 
        # IPv6 addresses and CIDR blocks are supported.
        # 
        # > - Only Extreme NAS file systems in the China (Hohhot) region support IPv6 CIDR blocks.
        # > - Only VPCs are supported.
        # > - IPv4 and IPv6 are mutually exclusive. You cannot convert between the two types.
        # > - You must specify either SourceCidrIp or Ipv6SourceCidrIp. You cannot leave both parameters empty, and you cannot specify both parameters at the same time.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the permission rule.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 1 (highest priority).
        self.priority = priority
        # The read and write permission that the authorized object has on the file system.
        # 
        # Valid values:
        # 
        # - RDWR (default): read and write.
        # - RDONLY: read-only.
        self.rwaccess_type = rwaccess_type
        # The IP address or CIDR block.
        # 
        # The value must be a single IP address or a CIDR block.
        # 
        # > You must specify either SourceCidrIp or Ipv6SourceCidrIp. You cannot leave both parameters empty, and you cannot specify both parameters at the same time.
        self.source_cidr_ip = source_cidr_ip
        # The access permissions that the system user of the authorization object has on the file system.
        # 
        # Valid values:
        # 
        # - no_squash: allows access to the file system as the root user.
        # - root_squash: maps the root user to the nobody user when the root user accesses the file system.
        # - all_squash: maps all users to the nobody user regardless of the user identity used to access the file system.
        # 
        # The nobody user is a default user in Linux. This user can access only public content on the server and has low privileges and high security.
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

        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id

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

        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')

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

