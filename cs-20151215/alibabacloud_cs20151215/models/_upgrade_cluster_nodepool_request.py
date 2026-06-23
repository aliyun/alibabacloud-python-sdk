# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UpgradeClusterNodepoolRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        kubernetes_version: str = None,
        node_names: List[str] = None,
        rolling_policy: main_models.UpgradeClusterNodepoolRequestRollingPolicy = None,
        runtime_type: str = None,
        runtime_version: str = None,
        use_replace: bool = None,
    ):
        # The system image ID of the node.
        self.image_id = image_id
        # The Kubernetes version of the node. You can call [DescribeKubernetesVersionMetadata](https://help.aliyun.com/document_detail/2667899.html) to obtain the current cluster version information from the `KubernetesVersion` field.
        self.kubernetes_version = kubernetes_version
        # The list of nodes to upgrade. If this parameter is not specified, all nodes in the node pool are upgraded.
        self.node_names = node_names
        # The rolling update configuration.
        self.rolling_policy = rolling_policy
        # The runtime type. You can call [DescribeKubernetesVersionMetadata](https://help.aliyun.com/document_detail/2667899.html) to obtain the runtime information from the runtime field.
        self.runtime_type = runtime_type
        # The runtime version of the node. You can call [DescribeKubernetesVersionMetadata](https://help.aliyun.com/document_detail/2667899.html) to obtain the runtime version information from the runtime field.
        self.runtime_version = runtime_version
        # Specifies whether to use system cloud disk replacement for the upgrade. Valid values:
        # - true: Uses system cloud disk replacement to upgrade the node pool. ACK reinitializes the nodes based on the current node pool configurations, such as the logon method, labels, taints, operating system image, and runtime version.
        # - false: Does not use system cloud disk replacement.
        # 
        # Default value: false.
        self.use_replace = use_replace

    def validate(self):
        if self.rolling_policy:
            self.rolling_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.kubernetes_version is not None:
            result['kubernetes_version'] = self.kubernetes_version

        if self.node_names is not None:
            result['node_names'] = self.node_names

        if self.rolling_policy is not None:
            result['rolling_policy'] = self.rolling_policy.to_map()

        if self.runtime_type is not None:
            result['runtime_type'] = self.runtime_type

        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version

        if self.use_replace is not None:
            result['use_replace'] = self.use_replace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('kubernetes_version') is not None:
            self.kubernetes_version = m.get('kubernetes_version')

        if m.get('node_names') is not None:
            self.node_names = m.get('node_names')

        if m.get('rolling_policy') is not None:
            temp_model = main_models.UpgradeClusterNodepoolRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m.get('rolling_policy'))

        if m.get('runtime_type') is not None:
            self.runtime_type = m.get('runtime_type')

        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')

        if m.get('use_replace') is not None:
            self.use_replace = m.get('use_replace')

        return self

class UpgradeClusterNodepoolRequestRollingPolicy(DaraModel):
    def __init__(
        self,
        batch_interval: int = None,
        max_parallelism: int = None,
        pause_policy: str = None,
    ):
        # The interval between batches during the upgrade. This parameter takes effect only when the pause policy is set to `NotPause`.
        # 
        # Valid values: [5,120]. Unit: minutes.
        # 
        # You can set this parameter to 0 to specify no interval between batches.
        self.batch_interval = batch_interval
        # The maximum number of nodes that can be upgraded in parallel per batch. Nodes in the node pool are upgraded in batches.
        # 
        # Valid values: [1,10].
        # 
        # Default value: 10.
        self.max_parallelism = max_parallelism
        # The automatic pause policy during node upgrades. Valid values:
        # - FirstBatch: pauses after the first batch is completed.
        # - EveryBatch: pauses after each batch is completed.
        # - NotPause: does not pause.
        self.pause_policy = pause_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_interval is not None:
            result['batch_interval'] = self.batch_interval

        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism

        if self.pause_policy is not None:
            result['pause_policy'] = self.pause_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batch_interval') is not None:
            self.batch_interval = m.get('batch_interval')

        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')

        if m.get('pause_policy') is not None:
            self.pause_policy = m.get('pause_policy')

        return self

