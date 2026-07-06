# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAclRequest(DaraModel):
    def __init__(
        self,
        acl_operation_type: str = None,
        acl_operation_types: str = None,
        acl_permission_type: str = None,
        acl_resource_name: str = None,
        acl_resource_pattern_type: str = None,
        acl_resource_type: str = None,
        host: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # Operation type. Valid values:
        # 
        # - **Write**: write
        # 
        # - **Read**: read
        # 
        # - **Describe**: read TransactionalId
        # 
        # - **IdempotentWrite**: idempotent write to Cluster
        # 
        # - **IDEMPOTENT_WRITE**: idempotent write to Cluster, only available for Serverless instances.
        # 
        # - **DESCRIBE_CONFIGS**: query configuration, only available for Serverless instances.
        # 
        # This parameter is required.
        self.acl_operation_type = acl_operation_type
        # Batch authorization operation types. Multiple operations are separated by commas (,).
        # 
        # Valid values:
        # 
        # - **Write**: read
        # 
        # - **Read**: write
        # 
        # - **Describe**: read TransactionalId
        # 
        # - **IdempotentWrite**: idempotent write to Cluster
        # 
        # - **IDEMPOTENT_WRITE**: idempotent write to Cluster, only available for Serverless instances.
        # 
        # - **DESCRIBE_CONFIGS**: query configuration, only available for Serverless instances.
        # 
        # > This parameter is only supported for Serverless instances.
        self.acl_operation_types = acl_operation_types
        # Authorization method. Valid values:
        # 
        # - **DENY**: deny.
        # 
        # - **ALLOW**: allow.
        # 
        # > This parameter is only supported for Serverless instances.
        self.acl_permission_type = acl_permission_type
        # Resource name.
        # 
        # - The name of the resource, which can be a topic name, Group ID, cluster name, or transaction ID.
        # 
        # - You can use an asterisk (\\*) to represent all resources of this type.
        # 
        # > * Only after authorization is granted to all resources can you query the authorized resources using an asterisk (\\*).
        # 
        # This parameter is required.
        self.acl_resource_name = acl_resource_name
        # Matching pattern. Valid values:
        # 
        # - **LITERAL**: exact match
        # 
        # - **PREFIXED**: prefix match
        # 
        # This parameter is required.
        self.acl_resource_pattern_type = acl_resource_pattern_type
        # Resource type. Valid values:
        # 
        # - **Topic**: message topic.
        # 
        # - **Group**: consumer group.
        # 
        # - **Cluster**: instance.
        # 
        # - **TransactionalId**: transaction ID.
        # 
        # This parameter is required.
        self.acl_resource_type = acl_resource_type
        # Source IP.
        # 
        # > - Only specific IP addresses or \\* (all IPs) are supported. IP address ranges are not supported.
        # >
        # > - This parameter is only supported for Serverless instances.
        self.host = host
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Username.
        # 
        # - You can use an asterisk (\\*) to represent all usernames.
        # 
        # > * Only after authorization is granted to all users can you query the authorized users using an asterisk (\\*).
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

        if self.acl_operation_types is not None:
            result['AclOperationTypes'] = self.acl_operation_types

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

        if m.get('AclOperationTypes') is not None:
            self.acl_operation_types = m.get('AclOperationTypes')

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

