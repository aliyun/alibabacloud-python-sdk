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
        # The cool-down duration for scale-in events. This is the time interval from when the system detects a node is eligible for a scale-in to when the scale-in operation is executed.
        # 
        # Valid values: 1 to 60. Unit: minutes.
        # 
        # Default value: 10.
        self.cool_down_duration = cool_down_duration
        # Specifies whether `cluster-autoscaler` evicts DaemonSet Pods from nodes during a scale-in event. Valid values:
        # 
        # - `true`: Perform eviction.
        # 
        # - `false`: Do not perform eviction.
        self.daemonset_eviction_for_nodes = daemonset_eviction_for_nodes
        # The strategy for selecting a node pool for a scale-out when multiple node pools are available. Valid values:
        # 
        # - `least-waste`: The default strategy. The scaler selects the node pool that will have the least idle resources after a scale-out.
        # 
        # - `random`: The scaler selects a random node pool from the list of eligible node pools.
        # 
        # - `priority`: The scaler selects the node pool that has the highest priority. You must configure the priority of each scaling group by using the `priorities` parameter.
        self.expander = expander
        # The GPU utilization threshold for a scale-in on GPU nodes, which is the ratio of requested resources to total allocatable resources on a node.
        # 
        # A GPU node is eligible for a scale-in only if its CPU, memory, and GPU utilization all fall below this threshold.
        # 
        # Valid values: [0.1, 1].
        # 
        # Default value: 0.3 (30%).
        self.gpu_utilization_threshold = gpu_utilization_threshold
        # The maximum duration in seconds that `cluster-autoscaler` waits for Pods to terminate during a node drain for a scale-in event.
        # 
        # Unit: seconds.
        # 
        # Default value: 14400.
        self.max_graceful_termination_sec = max_graceful_termination_sec
        # The minimum number of Pods that must remain for any ReplicaSet after a scale-in operation. Nodes will not be scaled-in if doing so would violate this minimum.
        # 
        # Default value: 0.
        self.min_replica_count = min_replica_count
        # Configures the priorities for scaling groups. This is used when the `expander` strategy is set to `priority`. After you create a node pool and enable autoscaling for it, you can configure the priority of its associated scaling group. For more information, see [Enable node autoscaling](https://help.aliyun.com/document_detail/119099.html).
        # 
        # The priority must be a positive integer from 1 to 100. A larger value indicates a higher priority.
        self.priorities = priorities
        # Specifies whether to delete the Kubernetes Node object after a node is successfully scaled-in using fast scaling mode. For more information, see [Scaling modes](https://help.aliyun.com/document_detail/119099.html). Default value: false. Valid values:
        # 
        # - `true`: The Node object is deleted after the instance is stopped. We do not recommend this setting because it can cause data inconsistencies in Kubernetes.
        # 
        # - `false`: The Node object is retained after the instance is stopped.
        self.recycle_node_deletion_enabled = recycle_node_deletion_enabled
        # Specifies whether to allow node scale-in operations. Valid values:
        # 
        # - `true`: Allows scale-in operations.
        # 
        # - `false`: Disables scale-in operations.
        self.scale_down_enabled = scale_down_enabled
        # Controls whether `cluster-autoscaler` performs a scale-out operation when there are no ready nodes in the cluster. Default value: true. Valid values:
        # 
        # - `true`: A scale-out operation is performed.
        # 
        # - `false`: No scale-out operation is performed.
        self.scale_up_from_zero = scale_up_from_zero
        # The type of scaler to use. In clusters that run Kubernetes 1.24 or later, the default is goatscaler. In clusters that run an earlier version, the default is cluster-autoscaler. Valid values:
        # 
        # - `goatscaler`: The proprietary scaler for fast scaling.
        # 
        # - `cluster-autoscaler`: The standard Kubernetes cluster autoscaler.
        self.scaler_type = scaler_type
        # The frequency at which the system checks for scaling conditions.
        # 
        # Valid values: 15, 30, 60, 120, 180, and 300. Unit: seconds.
        # 
        # Default value: 60.
        self.scan_interval = scan_interval
        # Controls whether `cluster-autoscaler` can scale-in nodes that run Pods using local storage (for example, with `emptyDir` or `hostPath` volumes). Valid values:
        # 
        # - `true`: Prevents these nodes from being scaled-in.
        # 
        # - `false`: Allows these nodes to be scaled-in.
        self.skip_nodes_with_local_storage = skip_nodes_with_local_storage
        # Controls whether `cluster-autoscaler` can scale-in nodes that run Pods from the `kube-system` namespace. This setting does not affect DaemonSet or mirror Pods. Valid values:
        # 
        # - `true`: Prevents these nodes from being scaled-in.
        # 
        # - `false`: Allows these nodes to be scaled-in.
        self.skip_nodes_with_system_pods = skip_nodes_with_system_pods
        # The stabilization window. This is the period after a scale-out event during which the scaler does not perform scale-in operations.
        # 
        # Valid values: 1 to 60. Unit: minutes.
        # 
        # Default value: 10.
        self.unneeded_duration = unneeded_duration
        # The utilization threshold for a scale-in, which is the ratio of requested resources to the total allocatable resources on a node.
        # 
        # A node is eligible for a scale-in only when both its CPU and memory utilization fall below this threshold.
        # 
        # Valid values: [0.1, 1].
        # 
        # Default value: 0.5 (50%).
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

