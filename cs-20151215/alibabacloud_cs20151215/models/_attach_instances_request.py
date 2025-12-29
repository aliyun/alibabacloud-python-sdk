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
        # The CPU management policy of the node. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later:
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # *   `none`: uses default CPU affinity.
        # 
        # Default value: `none`
        # 
        # >  This parameter is not supported if you specify `nodepool_id`.
        self.cpu_policy = cpu_policy
        # Specifies whether to store container data and images on data disks. Valid value:
        # 
        # *   `true`: stores container data and images on data disks.
        # *   `false`: does not store container data or images on data disks.
        # 
        # Default value: `false`.
        # 
        # How data disks are attached:
        # 
        # *   If the ECS instance is already attached with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4. Then, the system uses the disk to store the data in the /var/lib/docker and /var/lib/kubelet directories.
        # *   If no data disk is attached to the ECS instance, the system does not purchase a new data disk.
        # 
        # >  If you choose to store container data and images on data disks and a data disk is already attached to the ECS instance, the original data on this data disk is cleared. You can back up the disk to prevent data loss.
        self.format_disk = format_disk
        # The custom image ID. If you do not specify this parameter, the default system image is used.
        # 
        # > 
        # 
        # *   If you specify a custom image, the custom image is used to deploy the operating system on the system disk of the node.
        # 
        # *   This parameter is not supported if you specify `nodepool_id`.
        self.image_id = image_id
        # The ECS instances that you want to add.
        # 
        # This parameter is required.
        self.instances = instances
        # Specifies whether the node that you want to add is an Edge Node Service (ENS) node. Valid value:
        # 
        # *   `true`: the node that you want to add is an ENS node.
        # *   `false`: the node that you want to add is not an ENS node.
        # 
        # Default value: `false`.
        # 
        # >  If the node that you want to add is an ENS node, you must set the value to `true`. This allows you to identify the node.
        self.is_edge_worker = is_edge_worker
        # Specifies whether to retain the instance name. Valid value:
        # 
        # *   `true`: retains the instance name.
        # *   `false`: does not retain the instance name.
        # 
        # Default value: `false`.
        self.keep_instance_name = keep_instance_name
        # The name of the key pair used to log on to the ECS instances. You must specify this parameter or `login_password`.
        # 
        # >  This parameter is not supported if you specify `nodepool_id`.
        self.key_pair = key_pair
        # The ID of the node pool to which the node is added. If you do not specify this parameter, the node is added to the default node pool.
        self.nodepool_id = nodepool_id
        # The SSH logon password used to log on to the ECS instances. You must specify this parameter or `key_pair`. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password cannot contain backslashes (\\\\) or double quotation marks (").
        # 
        # The password is encrypted during data transfer to ensure security.
        self.password = password
        # A list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The container runtime.
        # 
        # >  This parameter is not supported if you specify `nodepool_id`.
        self.runtime = runtime
        # The labels that you want to add to the node. When you add labels to a node, the following rules apply:
        # 
        # *   A label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   The key must be unique and cannot exceed 64 characters in length. The value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        # 
        # >  This parameter is not supported if you specify `nodepool_id`.
        self.tags = tags
        # The user-defined data on the node. For more information, see [Use instance user data to automatically run commands or scripts on instance startup](https://help.aliyun.com/document_detail/49121.html).
        # 
        # >  This parameter is not supported if you specify `nodepool_id`.
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

