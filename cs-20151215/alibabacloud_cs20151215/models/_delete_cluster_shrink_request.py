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
        # The options for deleting the resources that are associated with the cluster.
        self.delete_options_shrink = delete_options_shrink
        # Whether to retain SLB resources. Valid values:
        # 
        # - `true`: Retains the SLB resources that are created for the cluster.
        # 
        # - `false`: Does not retain the SLB resources that are created for the cluster.
        # 
        # Default value: `false`.
        # Use the `delete_options` parameter to manage `SLB` resources instead.
        self.keep_slb = keep_slb
        # Whether to retain all associated resources. If you set this parameter to `true`, the `retain_resources` parameter is ignored, and all cloud resources that are created with the cluster and can be queried by calling `DescribeClusterResources` are retained. If you set this parameter to `false`, note that resources that are configured to be retained by default in the `delete_options` parameter are still retained. To delete these resources, you must explicitly set the `delete_mode` parameter to `delete` for them in `delete_options`.
        # 
        # - `true`: Retains all associated cloud resources that are created with the cluster.
        # 
        # - `false`: Does not retain all associated cloud resources. Resources that are configured to be retained by default in the `delete_options` parameter, such as `ALB`, are still retained when this parameter is set to `false`.
        # 
        # Default value: `false`.
        self.retain_all_resources = retain_all_resources
        # The IDs of resources to retain when the cluster is deleted.
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

