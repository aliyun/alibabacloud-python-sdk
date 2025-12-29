# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from darabonba.model import DaraModel

class CreateAutoscalingConfigRequest(DaraModel):
    def __init__(
        self,
        cool_down_duration: str = None,
        daemonset_eviction_for_nodes: bool = None,
        expander: str = None,
        gpu_utilization_threshold: str = None,
        max_graceful_termination_sec: int = None,
        min_replica_count: int = None,
        priorities: Dict[str, List[str]] = None,
        recycle_node_deletion_enabled: bool = None,
        scale_down_enabled: bool = None,
        scale_up_from_zero: bool = None,
        scaler_type: str = None,
        scan_interval: str = None,
        skip_nodes_with_local_storage: bool = None,
        skip_nodes_with_system_pods: bool = None,
        unneeded_duration: str = None,
        utilization_threshold: str = None,
    ):
        # The waiting time before the auto scaling feature performs a scale-in activity. It is an interval between the time when the scale-in threshold is reached and the time when the scale-in activity (reducing the number of pods) starts. Unit: minutes. Default value: 10.
        self.cool_down_duration = cool_down_duration
        # Specifies whether to evict pods created by DaemonSets when the cluster autoscaler performs a scale-in activity. Valid values:
        # 
        # *   `true`: evicts DaemonSet pods.
        # *   `false`: does not evict DaemonSet pods.
        self.daemonset_eviction_for_nodes = daemonset_eviction_for_nodes
        # The node pool scale-out policy. Valid values:
        # 
        # *   `least-waste`: the default policy. If multiple node pools meet the requirement, this policy selects the node pool that will have the least idle resources after the scale-out activity is completed.
        # *   `random`: the random policy. If multiple node pools meet the requirement, this policy selects a random node pool for the scale-out activity.
        # *   `priority`: the priority-based policy If multiple node pools meet the requirement, this policy selects the node pool with the highest priority for the scale-out activity. The priority setting is stored in the ConfigMap named `cluster-autoscaler-priority-expander` in the kube-system namespace. When a scale-out activity is triggered, the policy obtains the node pool priorities from the ConfigMap based on the node pool IDs and then selects the node pool with the highest priority for the scale-out activity.
        self.expander = expander
        # The scale-in threshold of GPU utilization. This threshold specifies the ratio of the GPU resources that are requested by pods to the total GPU resources on the node.
        # 
        # A scale-in activity is performed only when the CPU utilization, memory utilization, and GPU utilization of a GPU-accelerated node are lower than the scale-in threshold of GPU utilization.
        self.gpu_utilization_threshold = gpu_utilization_threshold
        # The maximum amount of time to wait for pods on a node to terminate during a scale-in activity. Unit: seconds.
        self.max_graceful_termination_sec = max_graceful_termination_sec
        # The minimum number of pods allowed in each ReplicaSet before a scale-in activity is performed.
        self.min_replica_count = min_replica_count
        # Auto-scaling priority configuration. After creating a node pool with elasticity enabled, you can choose whether to configure a priority strategy and priority settings through [Enabling Node Auto-scaling](https://help.aliyun.com/document_detail/119099.html). This allows you to set priorities for the specified auto-scaling node pool scaling group. The priority value range is [1, 100] and must be a positive integer.
        self.priorities = priorities
        # Specifies whether to delete the corresponding Kubernetes node objects after nodes are removed in swift mode. For more information about the swift mode, see [Scaling mode](https://help.aliyun.com/document_detail/119099.html). Default value: false Valid values:
        # 
        # *   `true`: deletes the corresponding Kubernetes node objects after nodes are removed in swift mode. We recommend that you do not set the value to true because data inconsistency may occur in Kubernetes objects.
        # *   `false`: retains the corresponding Kubernetes node objects after nodes are removed in swift mode.
        self.recycle_node_deletion_enabled = recycle_node_deletion_enabled
        # Specifies whether to allow node scale-in activities. Valid values:
        # 
        # *   `true`: allows node scale-in activities.
        # *   `false`: does not allow node scale-in activities.
        self.scale_down_enabled = scale_down_enabled
        # Specifies whether the cluster autoscaler performs a scale-out activity when the number of ready nodes in the cluster is 0. Default value: true. Valid values:
        # 
        # *   `true`: performs a scale-out activity.
        # *   `false`: does not perform a scale-out activity.
        self.scale_up_from_zero = scale_up_from_zero
        # Elastic component type, default is goatscaler for cluster version 1.24 and above, and cluster-autoscaler below that. Values:
        # 
        # - `goatscaler`: Instant elasticity. 
        # - `cluster-autoscaler`: Auto-scaling.
        self.scaler_type = scaler_type
        # The interval at which the system scans for events that trigger scaling activities. Unit: seconds. Default value: 60.
        self.scan_interval = scan_interval
        # Specifies whether the cluster autoscaler scales in nodes that host pods mounted with local volumes, such as EmptyDir or HostPath volumes. Valid values:
        # 
        # *   `true`: does not allow the cluster autoscaler to scale in these nodes.
        # *   `false`: allows the cluster autoscaler to scale in these nodes.
        self.skip_nodes_with_local_storage = skip_nodes_with_local_storage
        # Specifies whether the cluster autoscaler scales in nodes that host pods in the kube-system namespace. This parameter does not take effect on pods created by DaemonSets and mirror pods. Valid values:
        # 
        # *   `true`: does not allow the cluster autoscaler to scale in these nodes.
        # *   `false`: allows the cluster autoscaler to scale in these nodes.
        self.skip_nodes_with_system_pods = skip_nodes_with_system_pods
        # The cooldown period. After the autoscaler performs a scale-out activity, the autoscaler waits a cooldown period before it can perform a scale-in activity. Newly added nodes can be removed in scale-in activities only after the cooldown period ends. Unit: minutes.
        self.unneeded_duration = unneeded_duration
        # The scale-in threshold. This threshold specifies the ratio of the resources that are requested by pods to the total resources on the node.
        # 
        # A scale-in activity is performed only when the CPU utilization and memory utilization of a node are lower than the scale-in threshold.
        self.utilization_threshold = utilization_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cool_down_duration is not None:
            result['cool_down_duration'] = self.cool_down_duration

        if self.daemonset_eviction_for_nodes is not None:
            result['daemonset_eviction_for_nodes'] = self.daemonset_eviction_for_nodes

        if self.expander is not None:
            result['expander'] = self.expander

        if self.gpu_utilization_threshold is not None:
            result['gpu_utilization_threshold'] = self.gpu_utilization_threshold

        if self.max_graceful_termination_sec is not None:
            result['max_graceful_termination_sec'] = self.max_graceful_termination_sec

        if self.min_replica_count is not None:
            result['min_replica_count'] = self.min_replica_count

        if self.priorities is not None:
            result['priorities'] = self.priorities

        if self.recycle_node_deletion_enabled is not None:
            result['recycle_node_deletion_enabled'] = self.recycle_node_deletion_enabled

        if self.scale_down_enabled is not None:
            result['scale_down_enabled'] = self.scale_down_enabled

        if self.scale_up_from_zero is not None:
            result['scale_up_from_zero'] = self.scale_up_from_zero

        if self.scaler_type is not None:
            result['scaler_type'] = self.scaler_type

        if self.scan_interval is not None:
            result['scan_interval'] = self.scan_interval

        if self.skip_nodes_with_local_storage is not None:
            result['skip_nodes_with_local_storage'] = self.skip_nodes_with_local_storage

        if self.skip_nodes_with_system_pods is not None:
            result['skip_nodes_with_system_pods'] = self.skip_nodes_with_system_pods

        if self.unneeded_duration is not None:
            result['unneeded_duration'] = self.unneeded_duration

        if self.utilization_threshold is not None:
            result['utilization_threshold'] = self.utilization_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cool_down_duration') is not None:
            self.cool_down_duration = m.get('cool_down_duration')

        if m.get('daemonset_eviction_for_nodes') is not None:
            self.daemonset_eviction_for_nodes = m.get('daemonset_eviction_for_nodes')

        if m.get('expander') is not None:
            self.expander = m.get('expander')

        if m.get('gpu_utilization_threshold') is not None:
            self.gpu_utilization_threshold = m.get('gpu_utilization_threshold')

        if m.get('max_graceful_termination_sec') is not None:
            self.max_graceful_termination_sec = m.get('max_graceful_termination_sec')

        if m.get('min_replica_count') is not None:
            self.min_replica_count = m.get('min_replica_count')

        if m.get('priorities') is not None:
            self.priorities = m.get('priorities')

        if m.get('recycle_node_deletion_enabled') is not None:
            self.recycle_node_deletion_enabled = m.get('recycle_node_deletion_enabled')

        if m.get('scale_down_enabled') is not None:
            self.scale_down_enabled = m.get('scale_down_enabled')

        if m.get('scale_up_from_zero') is not None:
            self.scale_up_from_zero = m.get('scale_up_from_zero')

        if m.get('scaler_type') is not None:
            self.scaler_type = m.get('scaler_type')

        if m.get('scan_interval') is not None:
            self.scan_interval = m.get('scan_interval')

        if m.get('skip_nodes_with_local_storage') is not None:
            self.skip_nodes_with_local_storage = m.get('skip_nodes_with_local_storage')

        if m.get('skip_nodes_with_system_pods') is not None:
            self.skip_nodes_with_system_pods = m.get('skip_nodes_with_system_pods')

        if m.get('unneeded_duration') is not None:
            self.unneeded_duration = m.get('unneeded_duration')

        if m.get('utilization_threshold') is not None:
            self.utilization_threshold = m.get('utilization_threshold')

        return self

