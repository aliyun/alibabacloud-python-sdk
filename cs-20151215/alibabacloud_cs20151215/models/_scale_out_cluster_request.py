# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ScaleOutClusterRequest(DaraModel):
    def __init__(
        self,
        cloud_monitor_flags: bool = None,
        count: int = None,
        cpu_policy: str = None,
        image_id: str = None,
        key_pair: str = None,
        login_password: str = None,
        rds_instances: List[str] = None,
        runtime: main_models.Runtime = None,
        tags: List[main_models.Tag] = None,
        taints: List[main_models.Taint] = None,
        user_data: str = None,
        vswitch_ids: List[str] = None,
        worker_auto_renew: bool = None,
        worker_auto_renew_period: int = None,
        worker_data_disks: List[main_models.ScaleOutClusterRequestWorkerDataDisks] = None,
        worker_instance_charge_type: str = None,
        worker_instance_types: List[str] = None,
        worker_period: int = None,
        worker_period_unit: str = None,
        worker_system_disk_category: str = None,
        worker_system_disk_size: int = None,
    ):
        # Specifies whether to install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent.
        # *   `false`: does not install the CloudMonitor agent.
        # 
        # Default value: `false`.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The number of worker nodes that you want to add.
        # 
        # This parameter is required.
        self.count = count
        # The CPU management policy of nodes in the node pool. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later:
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # Specifies a custom image for nodes. By default, the image provided by ACK is used. You can select a custom image to replace the default image. For more information, see [Custom images](https://help.aliyun.com/document_detail/146647.html).
        self.image_id = image_id
        # The name of the key pair. You must configure this parameter or the `login_password` parameter.
        # 
        # This parameter is required.
        self.key_pair = key_pair
        # The password for SSH logon. You must configure this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # This parameter is required.
        self.login_password = login_password
        # The ApsaraDB RDS instances. If you specify a list of ApsaraDB RDS instances, ECS instances in the cluster are automatically added to the whitelist of the ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The container runtime.
        self.runtime = runtime
        # The labels that you want to add to the node. When you add labels to a node, the following rules apply:
        # 
        # *   A label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   The key must be unique and cannot exceed 64 characters in length. The value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.tags = tags
        # The taints that you want to add to nodes. Taints can be used together with tolerations to avoid scheduling pods to specified nodes. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # The user-defined data of the node pool. For more information, see [Generate user-defined data](https://help.aliyun.com/document_detail/49121.html).
        self.user_data = user_data
        # The vSwitch IDs. You can select one to three vSwitches when you create a cluster. To ensure the high availability of the cluster, we recommend that you select vSwitches in different zones.
        # 
        # This parameter is required.
        self.vswitch_ids = vswitch_ids
        # Specifies whether to enable auto-renewal for worker nodes. This parameter takes effect and is required only if `worker_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: does not enable auto-renewal.
        # 
        # Default value: `true`
        self.worker_auto_renew = worker_auto_renew
        # The auto-renewal duration of worker nodes. This parameter takes effect and is required only if the subscription billing method is selected for worker nodes.
        # 
        # Valid values: 1, 2, 3, 6, and 12.
        # 
        # Default value: `1`.
        self.worker_auto_renew_period = worker_auto_renew_period
        # The configurations of the data disks that you want to mount to worker nodes. The configurations include the disk type and disk size.
        self.worker_data_disks = worker_data_disks
        # The billing method of worker nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.worker_instance_charge_type = worker_instance_charge_type
        # The instance configurations of worker nodes.
        # 
        # This parameter is required.
        self.worker_instance_types = worker_instance_types
        # The subscription duration of worker nodes. This parameter takes effect and is required only if `worker_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.worker_period = worker_period
        # The billing cycle of worker nodes. This parameter is required only if worker_instance_charge_type is set to `PrePaid`.
        # 
        # Set the value to `Month`.
        self.worker_period_unit = worker_period_unit
        # The system disk category of worker nodes. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: Enterprise SSD (ESSD).
        # 
        # Default value: `cloud_ssd`.
        # 
        # This parameter is required.
        self.worker_system_disk_category = worker_system_disk_category
        # The system disk size of worker nodes. Unit: GiB.
        # 
        # Valid values: 40 to 500.
        # 
        # Default value: `120`.
        # 
        # This parameter is required.
        self.worker_system_disk_size = worker_system_disk_size

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.taints:
            for v1 in self.taints:
                 if v1:
                    v1.validate()
        if self.worker_data_disks:
            for v1 in self.worker_data_disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags

        if self.count is not None:
            result['count'] = self.count

        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.key_pair is not None:
            result['key_pair'] = self.key_pair

        if self.login_password is not None:
            result['login_password'] = self.login_password

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        result['taints'] = []
        if self.taints is not None:
            for k1 in self.taints:
                result['taints'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['user_data'] = self.user_data

        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids

        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew

        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period

        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k1 in self.worker_data_disks:
                result['worker_data_disks'].append(k1.to_map() if k1 else None)

        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type

        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types

        if self.worker_period is not None:
            result['worker_period'] = self.worker_period

        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit

        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category

        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')

        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')

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

        self.taints = []
        if m.get('taints') is not None:
            for k1 in m.get('taints'):
                temp_model = main_models.Taint()
                self.taints.append(temp_model.from_map(k1))

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')

        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')

        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k1 in m.get('worker_data_disks'):
                temp_model = main_models.ScaleOutClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k1))

        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')

        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')

        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')

        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')

        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')

        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')

        return self

class ScaleOutClusterRequestWorkerDataDisks(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        category: str = None,
        encrypted: str = None,
        size: str = None,
    ):
        # The ID of the automatic snapshot policy. The system performs automatic backup for a cloud disk based on the specified automatic snapshot policy.
        # 
        # By default, this parameter is left empty, which indicates that automatic backup is disabled.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The type of the data disk.
        self.category = category
        # Specifies whether to encrypt the data disks. Valid values:
        # 
        # *   `true`: encrypts the data disk.
        # *   `false`: does not encrypt the data disk.
        # 
        # Default value: `false`.
        self.encrypted = encrypted
        # The size of the data disk. Valid values: 40 to 32767.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id

        if self.category is not None:
            result['category'] = self.category

        if self.encrypted is not None:
            result['encrypted'] = self.encrypted

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

