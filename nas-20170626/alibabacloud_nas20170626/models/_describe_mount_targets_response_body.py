# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeMountTargetsResponseBody(DaraModel):
    def __init__(
        self,
        mount_targets: main_models.DescribeMountTargetsResponseBodyMountTargets = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried mount targets.
        self.mount_targets = mount_targets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of mount targets.
        self.total_count = total_count

    def validate(self):
        if self.mount_targets:
            self.mount_targets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_targets is not None:
            result['MountTargets'] = self.mount_targets.to_map()

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
        if m.get('MountTargets') is not None:
            temp_model = main_models.DescribeMountTargetsResponseBodyMountTargets()
            self.mount_targets = temp_model.from_map(m.get('MountTargets'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMountTargetsResponseBodyMountTargets(DaraModel):
    def __init__(
        self,
        mount_target: List[main_models.DescribeMountTargetsResponseBodyMountTargetsMountTarget] = None,
    ):
        self.mount_target = mount_target

    def validate(self):
        if self.mount_target:
            for v1 in self.mount_target:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountTarget'] = []
        if self.mount_target is not None:
            for k1 in self.mount_target:
                result['MountTarget'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mount_target = []
        if m.get('MountTarget') is not None:
            for k1 in m.get('MountTarget'):
                temp_model = main_models.DescribeMountTargetsResponseBodyMountTargetsMountTarget()
                self.mount_target.append(temp_model.from_map(k1))

        return self

class DescribeMountTargetsResponseBodyMountTargetsMountTarget(DaraModel):
    def __init__(
        self,
        access_group: str = None,
        client_master_nodes: main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes = None,
        dual_stack_mount_target_domain: str = None,
        ipversion: str = None,
        mount_target_domain: str = None,
        network_type: str = None,
        status: str = None,
        tags: main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetTags = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The name of the permission group that is attached to the mount target.
        self.access_group = access_group
        # The information about client management nodes.
        self.client_master_nodes = client_master_nodes
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The type of the mount target.
        # 
        # *   IPv4: an IPv4 mount target
        # *   DualStack: a dual-stack mount target
        self.ipversion = ipversion
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The network type. Valid value: **Vpc**.
        self.network_type = network_type
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # *   Pending: The mount target is being created or modified.
        # *   Deleting: The mount target is being deleted.
        # *   Hibernating: The mount target is being hibernated.
        # *   Hibernated: The mount target is hibernated.
        # 
        # > You can mount a file system only when the mount target of the file system is in the Active state.
        self.status = status
        # An array of tags. The array may contain up to 20 tags. If the array contains multiple tags, each tag key is unique.
        self.tags = tags
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        self.vsw_id = vsw_id

    def validate(self):
        if self.client_master_nodes:
            self.client_master_nodes.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group

        if self.client_master_nodes is not None:
            result['ClientMasterNodes'] = self.client_master_nodes.to_map()

        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain

        if self.ipversion is not None:
            result['IPVersion'] = self.ipversion

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')

        if m.get('ClientMasterNodes') is not None:
            temp_model = main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes()
            self.client_master_nodes = temp_model.from_map(m.get('ClientMasterNodes'))

        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')

        if m.get('IPVersion') is not None:
            self.ipversion = m.get('IPVersion')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        return self

class DescribeMountTargetsResponseBodyMountTargetsMountTargetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMountTargetsResponseBodyMountTargetsMountTargetTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Limits:
        # 
        # *   The tag key cannot be null or an empty string.
        # *   The tag key can be up to 128 characters in length.
        # *   The key value cannot start with aliyun or acs:.
        # *   The key value cannot contain http:// or https://.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # *   The tag value can be up to 128 characters in length.
        # *   The tag value cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodes(DaraModel):
    def __init__(
        self,
        client_master_node: List[main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode] = None,
    ):
        self.client_master_node = client_master_node

    def validate(self):
        if self.client_master_node:
            for v1 in self.client_master_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClientMasterNode'] = []
        if self.client_master_node is not None:
            for k1 in self.client_master_node:
                result['ClientMasterNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_master_node = []
        if m.get('ClientMasterNode') is not None:
            for k1 in m.get('ClientMasterNode'):
                temp_model = main_models.DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode()
                self.client_master_node.append(temp_model.from_map(k1))

        return self

class DescribeMountTargetsResponseBodyMountTargetsMountTargetClientMasterNodesClientMasterNode(DaraModel):
    def __init__(
        self,
        default_passwd: str = None,
        ecs_id: str = None,
        ecs_ip: str = None,
    ):
        # The default logon password of the ECS instance.
        self.default_passwd = default_passwd
        # The ID of the ECS instance on the client management node.
        self.ecs_id = ecs_id
        # The IP address of the ECS instance on the client management node.
        self.ecs_ip = ecs_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_passwd is not None:
            result['DefaultPasswd'] = self.default_passwd

        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id

        if self.ecs_ip is not None:
            result['EcsIp'] = self.ecs_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultPasswd') is not None:
            self.default_passwd = m.get('DefaultPasswd')

        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')

        if m.get('EcsIp') is not None:
            self.ecs_ip = m.get('EcsIp')

        return self

