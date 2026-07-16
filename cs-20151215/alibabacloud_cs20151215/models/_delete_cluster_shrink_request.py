# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        delete_options_shrink: str = None,
        keep_slb: bool = None,
        retain_all_resources: bool = None,
        retain_resources_shrink: str = None,
    ):
        # The deletion options for cluster-associated resources.
        self.delete_options_shrink = delete_options_shrink
        # Specifies whether to retain SLB resources. Valid values:
        # 
        # - `true`: retains the created SLB resources.
        # - `false`: does not retain the created SLB resources.
        # 
        # Default value: `false`.
        # Use `SLB` in `delete_options` to manage this setting.
        self.keep_slb = keep_slb
        # Specifies whether to retain all resources. If this parameter is set to `true`, `retain_resources` is ignored, and cloud resources created through the cluster that are queried by the `DescribeClusterResources` operation are retained. If this parameter is set to `false`, resources that are retained by default in `delete_options` are still retained. To delete these resources, set `delete_mode` to `delete` in `delete_options`.
        # 
        # - `true`: retains all resources, including all cloud resources created through the cluster.
        # - `false`: does not retain all resources, except resources defined as retained by default in `delete_options`. For example, `ALB` resources are still retained when this parameter is set to `false`.
        # 
        # Default value: `false`.
        self.retain_all_resources = retain_all_resources
        # The resource list. To retain resources when you delete a cluster, specify the IDs of the resources to retain.
        self.retain_resources_shrink = retain_resources_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_options_shrink is not None:
            result['delete_options'] = self.delete_options_shrink

        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb

        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources

        if self.retain_resources_shrink is not None:
            result['retain_resources'] = self.retain_resources_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delete_options') is not None:
            self.delete_options_shrink = m.get('delete_options')

        if m.get('keep_slb') is not None:
            self.keep_slb = m.get('keep_slb')

        if m.get('retain_all_resources') is not None:
            self.retain_all_resources = m.get('retain_all_resources')

        if m.get('retain_resources') is not None:
            self.retain_resources_shrink = m.get('retain_resources')

        return self

