# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAclsRequest(DaraModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The types of operations allowed by the ACL. Separate multiple operation types with commas (,).
        # - Valid values:
        # - Write
        # - Read
        # - Describe: reads of transactional IDs.
        # - IdempotentWrite: idempotent data writes to clusters.
        # - IDEMPOTENT_WRITE: idempotent data writes to clusters. This value is available only for ApsaraMQ for Kafka V3 instances.
        # - DESCRIBE_CONFIGS: queries of configurations. This value is available only for ApsaraMQ for Kafka V3 instances.
        # > This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_operation_type = acl_operation_type
        # The authorization method. Valid values:
        # - DENY
        # - ALLOW
        # > This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.acl_permission_type = acl_permission_type
        # The resource name.
        # 
        # *   The value can be the name of a topic or consumer group.
        # *   You can use an asterisk (\\*) to specify the names of all topics or consumer groups.
        # 
        # > You can query the resources on which permissions are granted only after you grant the user the required permissions on all resources.
        # 
        # This parameter is required.
        self.acl_resource_name = acl_resource_name
        # The match mode. Valid values:
        # 
        # *   LITERAL: full-name match
        # *   PREFIXED: prefix match
        self.acl_resource_pattern_type = acl_resource_pattern_type
        # The resource type. Valid values:
        # 
        # *   **Topic**
        # *   **Group**
        # 
        # This parameter is required.
        self.acl_resource_type = acl_resource_type
        # The source IP address.
        # >-  You can specify only a specific IP address or use the asterisk (*) wildcard character to specify all IP addresses. CIDR blocks are not supported.
        # > - This parameter is available only for ApsaraMQ for Kafka V3 serverless instances.
        self.host = host
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The username.
        # 
        # *   You can use an asterisk (\\*) to specify all users.
        # 
        # > You can use an asterisk (\\*) to query the authorized users only after you grant the required permissions to all users.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_operation_type is not None:
            result['AclOperationType'] = self.acl_operation_type

        if self.acl_permission_type is not None:
            result['AclPermissionType'] = self.acl_permission_type

        if self.acl_resource_name is not None:
            result['AclResourceName'] = self.acl_resource_name

        if self.acl_resource_pattern_type is not None:
            result['AclResourcePatternType'] = self.acl_resource_pattern_type

        if self.acl_resource_type is not None:
            result['AclResourceType'] = self.acl_resource_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationType') is not None:
            self.acl_operation_type = m.get('AclOperationType')

        if m.get('AclPermissionType') is not None:
            self.acl_permission_type = m.get('AclPermissionType')

        if m.get('AclResourceName') is not None:
            self.acl_resource_name = m.get('AclResourceName')

        if m.get('AclResourcePatternType') is not None:
            self.acl_resource_pattern_type = m.get('AclResourcePatternType')

        if m.get('AclResourceType') is not None:
            self.acl_resource_type = m.get('AclResourceType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

