# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        client_version: str = None,
        cluster_custom_configuration_shrink: str = None,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        deletion_protection: bool = None,
        enable_scale_in: bool = None,
        enable_scale_out: bool = None,
        grow_interval: int = None,
        idle_interval: int = None,
        max_core_count: int = None,
        max_count: int = None,
        monitor_spec_shrink: str = None,
        scheduler_spec_shrink: str = None,
    ):
        # Specifies whether to enable auto scale-out for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.client_version = client_version
        # Specifies whether to enable auto scale-in for the cluster. Valid values:
        # 
        # *   true
        # *   false
        self.cluster_custom_configuration_shrink = cluster_custom_configuration_shrink
        # The URL that is used to download the post-processing script.
        self.cluster_description = cluster_description
        # The client version. By default, the latest version is used.
        self.cluster_id = cluster_id
        # The post-processing script of the cluster.
        self.cluster_name = cluster_name
        # The idle duration of the compute nodes allowed by the cluster.
        self.deletion_protection = deletion_protection
        # The request result. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.enable_scale_in = enable_scale_in
        # The response parameters.
        self.enable_scale_out = enable_scale_out
        # The scheduler specifications of the cluster.
        self.grow_interval = grow_interval
        # Specifies whether to enable the topology awareness feature. Valid values:
        # 
        # *   true
        # *   false
        self.idle_interval = idle_interval
        # The interval at which the cluster is automatically scaled out.
        self.max_core_count = max_core_count
        # The arguments that are used to run the post-processing script.
        self.max_count = max_count
        # The monitoring details of the cluster.
        self.monitor_spec_shrink = monitor_spec_shrink
        # The scheduler specifications of the cluster.
        self.scheduler_spec_shrink = scheduler_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.cluster_custom_configuration_shrink is not None:
            result['ClusterCustomConfiguration'] = self.cluster_custom_configuration_shrink

        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.enable_scale_in is not None:
            result['EnableScaleIn'] = self.enable_scale_in

        if self.enable_scale_out is not None:
            result['EnableScaleOut'] = self.enable_scale_out

        if self.grow_interval is not None:
            result['GrowInterval'] = self.grow_interval

        if self.idle_interval is not None:
            result['IdleInterval'] = self.idle_interval

        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.monitor_spec_shrink is not None:
            result['MonitorSpec'] = self.monitor_spec_shrink

        if self.scheduler_spec_shrink is not None:
            result['SchedulerSpec'] = self.scheduler_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('ClusterCustomConfiguration') is not None:
            self.cluster_custom_configuration_shrink = m.get('ClusterCustomConfiguration')

        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('EnableScaleIn') is not None:
            self.enable_scale_in = m.get('EnableScaleIn')

        if m.get('EnableScaleOut') is not None:
            self.enable_scale_out = m.get('EnableScaleOut')

        if m.get('GrowInterval') is not None:
            self.grow_interval = m.get('GrowInterval')

        if m.get('IdleInterval') is not None:
            self.idle_interval = m.get('IdleInterval')

        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MonitorSpec') is not None:
            self.monitor_spec_shrink = m.get('MonitorSpec')

        if m.get('SchedulerSpec') is not None:
            self.scheduler_spec_shrink = m.get('SchedulerSpec')

        return self

