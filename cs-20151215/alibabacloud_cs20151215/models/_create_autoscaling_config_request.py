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
        # The delay for triggering scale-in. This is the time interval between detecting a scale-in requirement (reaching the scale-in threshold) and actually executing the scale-in operation (reducing the number of pods). Valid values: 1 to 60. Unit: minutes. Default value: 10.
        self.cool_down_duration = cool_down_duration
        # Specifies whether cluster-autoscaler evicts DaemonSet pods on nodes during scale-in. Valid values:
        # - true: The pods are evicted.
        # - false: The pods are not evicted.
        self.daemonset_eviction_for_nodes = daemonset_eviction_for_nodes
        # The node pool scale-out order policy. Valid values:
        # - least-waste: the default policy. If multiple node pools can be scaled out, the system selects the node pool that wastes the least resources.
        # - random: the random policy. If multiple node pools can be scaled out, the system randomly selects a node pool.
        # - priority: the priority policy. If multiple node pools can be scaled out, the system selects the node pool with the highest priority based on the custom scaling group order. The node pool priority is defined by the priorities parameter.
        self.expander = expander
        # The GPU scale-in threshold, which is the ratio of requested resources to total resources on a node. A GPU node can be scaled in only when this ratio is lower than the configured threshold, meaning that the CPU, memory, and GPU utilization of the node are all lower than the GPU scale-in threshold. Valid values: 0.1 to 1. Default value: 0.3, which indicates 30%.
        self.gpu_utilization_threshold = gpu_utilization_threshold
        # The timeout period for cluster-autoscaler to wait for pod termination during node draining in a scale-in scenario. Unit: seconds. Default value: 14400.
        self.max_graceful_termination_sec = max_graceful_termination_sec
        # The minimum number of pods allowed in each ReplicaSet before a node is scaled in. Default value: 0.
        self.min_replica_count = min_replica_count
        # The auto scaling priority configuration. After you create a node pool with auto scaling enabled, you can choose whether to configure the priority policy and priority configuration by referring to [Enable auto scaling for nodes](https://help.aliyun.com/document_detail/119099.html). This allows you to configure priorities for the scaling groups of specified auto scaling node pools. Valid values: 1 to 100. The value must be a positive integer. A larger value indicates a higher priority.
        self.priorities = priorities
        # Specifies whether to delete the corresponding Kubernetes node objects after nodes are successfully scaled in fast mode. For more information about fast mode, see [Scaling modes](https://help.aliyun.com/document_detail/119099.html). Default value: false. Valid values:
        # - true: Kubernetes node objects are also deleted after nodes are stopped in fast mode. Do not set this parameter to true because it may cause data inconsistency of Kubernetes objects.
        # - false: Kubernetes node objects are retained after nodes are stopped in fast mode.
        self.recycle_node_deletion_enabled = recycle_node_deletion_enabled
        # Specifies whether to allow node scale-in. Valid values:
        # - true: Scale-in is allowed.
        # - false: Scale-in is prohibited.
        self.scale_down_enabled = scale_down_enabled
        # Specifies whether cluster-autoscaler performs scale-out when the number of ready nodes in the cluster is 0. Default value: true. Valid values:
        # - true: Scale-out is performed.
        # - false: Scale-out is not performed.
        self.scale_up_from_zero = scale_up_from_zero
        # The auto scaling component type. For clusters of version 1.24 and later, the default value is goatscaler. For clusters of earlier versions, the default value is cluster-autoscaler. Valid values:
        # - goatscaler: instant elasticity.
        # - cluster-autoscaler: auto scaling.
        self.scaler_type = scaler_type
        # The auto scaling sensitivity, which is used to adjust the interval at which the system evaluates scaling. Valid values: 15, 30, 60, 120, 180, and 300. Unit: seconds. Default value: 60.
        self.scan_interval = scan_interval
        # Specifies whether cluster-autoscaler scales in nodes that contain pods with local storage, such as EmptyDir or HostPath. Valid values:
        # - true: The nodes are not scaled in.
        # - false: The nodes are scaled in.
        self.skip_nodes_with_local_storage = skip_nodes_with_local_storage
        # Specifies whether cluster-autoscaler scales in nodes that run pods in the kube-system namespace. This feature does not take effect for DaemonSet pods and mirror pods. Valid values:
        # - true: The nodes are not scaled in.
        # - false: The nodes are scaled in.
        self.skip_nodes_with_system_pods = skip_nodes_with_system_pods
        # The cool-down period. This is the time interval during which the auto scaling component does not perform scale-in after the most recent scale-out is completed. Scaled-out nodes can be evaluated for scale-in only after the cool-down period ends. Valid values: 1 to 60. Unit: minutes. Default value: 10.
        self.unneeded_duration = unneeded_duration
        # The scale-in threshold, which is the ratio of requested resources to total resources on a node. A node can be scaled in only when this ratio is lower than the configured threshold, meaning that the utilization of both CPU and memory resources on the node is lower than the scale-in threshold. Valid values: 0.1 to 1. Default value: 0.5, which indicates 50%.
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

