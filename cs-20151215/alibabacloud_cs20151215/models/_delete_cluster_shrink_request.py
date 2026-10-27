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
        # The deletion options for the resources associated with the cluster.
        self.delete_options_shrink = delete_options_shrink
        # Specifies whether to retain the Server Load Balancer (SLB) instances created by using Services.
        # Valid values:
        # - `true`: retains the created SLB resources.
        # - `false`: does not retain the created SLB resources.
        # 
        # Default value: `false`.
        # **[Deprecated]** Use `SLB` in `delete_options` instead.
        self.keep_slb = keep_slb
        # Specifies whether to retain all resources. If you set this parameter to `true`, the `retain_resources` parameter is ignored, and all cloud resources created by the cluster that are queried by calling the `DescribeClusterResources` operation are retained. If you set this parameter to `false`, note that the resources that are retained by default in `delete_options` are still retained. To delete these resources, set `delete_mode` to `delete` in `delete_options`.
        # 
        # Valid values:
        # - `true`: retains all resources, including all cloud resources created by the cluster.
        # - `false`: does not retain all resources, except for the resources that are retained by default in `delete_options`. For example, ALB resources are still retained even if this parameter is set to `false`.
        # 
        # Default value: `false`.
        self.retain_all_resources = retain_all_resources
        # The list of resources. To retain resources when you delete the cluster, specify the IDs of the corresponding resources.
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

