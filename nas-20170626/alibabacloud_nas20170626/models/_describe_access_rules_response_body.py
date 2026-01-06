# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessRulesResponseBody(DaraModel):
    def __init__(
        self,
        access_rules: main_models.DescribeAccessRulesResponseBodyAccessRules = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The rules in the permission group.
        self.access_rules = access_rules
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of rules.
        self.total_count = total_count

    def validate(self):
        if self.access_rules:
            self.access_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_rules is not None:
            result['AccessRules'] = self.access_rules.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessRules') is not None:
            temp_model = main_models.DescribeAccessRulesResponseBodyAccessRules()
            self.access_rules = temp_model.from_map(m.get('AccessRules'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccessRulesResponseBodyAccessRules(DaraModel):
    def __init__(
        self,
        access_rule: List[main_models.DescribeAccessRulesResponseBodyAccessRulesAccessRule] = None,
    ):
        self.access_rule = access_rule

    def validate(self):
        if self.access_rule:
            for v1 in self.access_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessRule'] = []
        if self.access_rule is not None:
            for k1 in self.access_rule:
                result['AccessRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_rule = []
        if m.get('AccessRule') is not None:
            for k1 in m.get('AccessRule'):
                temp_model = main_models.DescribeAccessRulesResponseBodyAccessRulesAccessRule()
                self.access_rule.append(temp_model.from_map(k1))

        return self

class DescribeAccessRulesResponseBodyAccessRulesAccessRule(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_rule_id: str = None,
        file_system_type: str = None,
        ipv_6source_cidr_ip: str = None,
        priority: int = None,
        rwaccess: str = None,
        region_id: str = None,
        source_cidr_ip: str = None,
        user_access: str = None,
    ):
        # The name of the permission group.
        self.access_group_name = access_group_name
        # The ID of the rule.
        self.access_rule_id = access_rule_id
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose File Storage NAS (NAS) file system
        # *   extreme: Extreme NAS file system
        self.file_system_type = file_system_type
        # The IPv6 address or CIDR block of the authorized object.
        self.ipv_6source_cidr_ip = ipv_6source_cidr_ip
        # The priority of the rule.
        # 
        # If multiple rules are attached to the authorized object, the rule with the highest priority takes effect.
        # 
        # Valid values: 1 to 100. The value 1 indicates the highest priority.
        self.priority = priority
        # The access permissions of the authorized object on the file system.
        # 
        # Valid values:
        # 
        # *   RDWR (default): the read and write permissions
        # *   RDONLY: the read-only permissions
        self.rwaccess = rwaccess
        # The region ID.
        self.region_id = region_id
        # The IP address or CIDR block of the authorized object.
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
        self.user_access = user_access

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

        if self.rwaccess is not None:
            result['RWAccess'] = self.rwaccess

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.user_access is not None:
            result['UserAccess'] = self.user_access

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

        if m.get('RWAccess') is not None:
            self.rwaccess = m.get('RWAccess')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('UserAccess') is not None:
            self.user_access = m.get('UserAccess')

        return self

