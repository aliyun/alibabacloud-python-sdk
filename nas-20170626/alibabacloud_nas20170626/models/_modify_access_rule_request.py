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
        # The rule ID.
        # 
        # This parameter is required.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system.
        # *   extreme: Extreme NAS file system.
        self.file_system_type = file_system_type
        # The IPv6 address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IPv6 IP address or CIDR block.
        # 
        # > *   Only Extreme NAS file systems that reside in the China (Hohhot) region support IPv6.
        # >*   Only permission groups that reside in virtual private clouds (VPCs) support IPv6.
        # >*   This parameter is unavailable if you specify the SourceCidrIp parameter.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the rule.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 1, which indicates the highest priority.
        self.priority = priority
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions.
        # *   RDONLY: the read-only permissions.
        self.rwaccess_type = rwaccess_type
        # The IP address or CIDR block of the authorized object.
        # 
        # You must set this parameter to an IP address or CIDR block.
        self.source_cidr_ip = source_cidr_ip
        # The access permissions for different types of users in the authorized object.
        # 
        # Valid values:
        # 
        # *   no_squash: allows access from root users to the file system.
        # *   root_squash: grants root users the least permissions as the nobody user.
        # *   all_squash: grants all users the least permissions as the nobody user.
        # 
        # The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system.
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

