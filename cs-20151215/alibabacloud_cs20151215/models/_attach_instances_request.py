# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class AttachInstancesRequest(DaraModel):
    def __init__(
        self,
        cpu_policy: str = None,
        format_disk: bool = None,
        image_id: str = None,
        instances: List[str] = None,
        is_edge_worker: bool = None,
        keep_instance_name: bool = None,
        key_pair: str = None,
        nodepool_id: str = None,
        password: str = None,
        rds_instances: List[str] = None,
        runtime: main_models.Runtime = None,
        tags: List[main_models.Tag] = None,
        user_data: str = None,
    ):
        # The CPU management policy of the node. The following policies are supported for clusters of version 1.12.6 or later:
        # 
        # - `static`: Allows pods with certain resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # - `none`: Uses the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        # 
        # > After you specify `nodepool_id`, this parameter is not supported.
        self.cpu_policy = cpu_policy
        # Specifies whether to store container data and images on a data cloud disk. Valid values:
        # 
        # - `true`: Stores container data and images on a data cloud disk.
        # 
        # - `false`: Does not store container data and images on a data cloud disk.
        # 
        # Default value: `false`.
        # 
        # 
        # Data cloud disk mounting rules:
        # 
        # - If the ECS instance has data cloud disks mounted and the file system of the last data cloud disk is not initialized, the system automatically formats the data cloud disk to EXT4 to store the content of /var/lib/docker and /var/lib/kubelet (the default data directories for the Docker container runtime and the kubelet component, respectively).
        # - If the ECS instance has no data cloud disks mounted, no new data cloud disk is mounted.
        # > If you choose to store data on a data cloud disk and the ECS instance already has data cloud disks mounted, existing data on the data cloud disk is lost. Back up your data in advance.
        self.format_disk = format_disk
        # The custom image ID.
        # 
        # - If you specify a custom image ID, the system cloud disk image of the instance is replaced with the custom image.
        # 
        # - If you do not specify this parameter, the default system image is used.
        # 
        # > After you specify `nodepool_id`, this parameter is not supported.
        self.image_id = image_id
        # The list of ECS instances to be added.
        # 
        # This parameter is required.
        self.instances = instances
        # Specifies whether the node to be added is an edge node, that is, an Edge Node Service (ENS) node. Valid values:
        # 
        # - `true`: The node to be added is an edge node.
        # 
        # - `false`: The node to be added is not an edge node.
        # 
        # Default value: `false`.
        # 
        # > If the node is an edge node, set this parameter to `true` to identify the node type as an ENS node.
        self.is_edge_worker = is_edge_worker
        # Specifies whether to retain the original instance name. Valid values:
        # 
        # - `true`: Retains the instance name.
        # 
        # - `false`: Does not retain the instance name.
        # 
        # Default value: `false`.
        self.keep_instance_name = keep_instance_name
        # The name of the key pair for the instances to be added. Specify either key_pair or password. You can also leave both parameters empty.
        # > After you specify `nodepool_id`, this parameter is not supported.
        self.key_pair = key_pair
        # The node pool ID. If you do not specify this parameter, the node is added to the default node pool.
        self.nodepool_id = nodepool_id
        # The SSH logon password for the instances to be added. Specify either key_pair or password. You can also leave both parameters empty.
        # 
        # The password must meet the following requirements:
        # - The password must be 8 to 30 characters in length.
        # - The password must contain uppercase letters, lowercase letters, digits, and special characters at the same time.
        # - The password cannot contain backslashes (\\) or double quotation marks (").
        # 
        # The password is encrypted during transmission for security purposes.
        self.password = password
        # The list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The container runtime.
        # > After you specify `nodepool_id`, this parameter is not supported.
        # 
        # name: The name of the container runtime. ACK supports the following three container runtimes:
        # 
        # - containerd: Recommended. Supported by all cluster versions.
        # - Sandboxed-Container.runv: Sandboxed container that provides higher isolation. Supported by clusters of version 1.24 or earlier.
        # - docker: Supported by clusters of version 1.22 or earlier.
        # 
        # Default value: containerd.
        # 
        # containerd: The container runtime version. Default value: the latest version.
        # 
        # For more information about changes to the sandboxed container runtime, see [Release notes for the sandboxed container runtime](https://help.aliyun.com/document_detail/160312.html).
        self.runtime = runtime
        # The node labels. Label definition rules:
        # 
        # - Labels are case-sensitive key-value pairs. You can set up to 20 labels.
        # - Label keys cannot be duplicate and can be up to 64 characters in length.
        # - Label values can be empty and can be up to 128 characters in length.
        # - Label keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`.
        # 
        # For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        # > After you specify `nodepool_id`, this parameter is not supported.
        self.tags = tags
        # The instance user data of the node. For more information, see [Generate instance user data](https://help.aliyun.com/document_detail/49121.html).
        # 
        # > After you specify `nodepool_id`, this parameter is not supported.
        self.user_data = user_data

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy

        if self.format_disk is not None:
            result['format_disk'] = self.format_disk

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.instances is not None:
            result['instances'] = self.instances

        if self.is_edge_worker is not None:
            result['is_edge_worker'] = self.is_edge_worker

        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name

        if self.key_pair is not None:
            result['key_pair'] = self.key_pair

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.password is not None:
            result['password'] = self.password

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['user_data'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')

        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('is_edge_worker') is not None:
            self.is_edge_worker = m.get('is_edge_worker')

        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')

        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('runtime') is not None:
            temp_model = main_models.Runtime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        return self

