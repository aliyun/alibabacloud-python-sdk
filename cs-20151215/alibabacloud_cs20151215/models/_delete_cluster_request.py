# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DeleteClusterRequest(DaraModel):
    def __init__(
        self,
        delete_options: List[main_models.DeleteClusterRequestDeleteOptions] = None,
        keep_slb: bool = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
    ):
        # The deletion options for cluster-associated resources.
        self.delete_options = delete_options
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
        self.retain_resources = retain_resources

    def validate(self):
        if self.delete_options:
            for v1 in self.delete_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['delete_options'] = []
        if self.delete_options is not None:
            for k1 in self.delete_options:
                result['delete_options'].append(k1.to_map() if k1 else None)

        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb

        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources

        if self.retain_resources is not None:
            result['retain_resources'] = self.retain_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delete_options = []
        if m.get('delete_options') is not None:
            for k1 in m.get('delete_options'):
                temp_model = main_models.DeleteClusterRequestDeleteOptions()
                self.delete_options.append(temp_model.from_map(k1))

        if m.get('keep_slb') is not None:
            self.keep_slb = m.get('keep_slb')

        if m.get('retain_all_resources') is not None:
            self.retain_all_resources = m.get('retain_all_resources')

        if m.get('retain_resources') is not None:
            self.retain_resources = m.get('retain_resources')

        return self

class DeleteClusterRequestDeleteOptions(DaraModel):
    def __init__(
        self,
        delete_mode: str = None,
        resource_type: str = None,
    ):
        # The deletion policy for this resource type. Valid values:
        # - delete: deletes resources of this type.
        # - retain: retains resources of this type.
        self.delete_mode = delete_mode
        # The resource type. Valid values:
        # - SLB: SLB resources created through services. Deleted by default. You can choose to retain them.
        # - ALB: ALB resources created by ALB Ingress Controller. Retained by default. You can choose to delete them.
        # - SLS_Data: the SLS project used by the cluster logging feature. Retained by default. You can choose to delete it.
        # - SLS_ControlPlane: the SLS project used by the control plane logs of managed clusters. Retained by default. You can choose to delete it.
        # - PrivateZone: PrivateZone resources created by ACK Serverless clusters. Retained by default. You can choose to delete them.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_mode is not None:
            result['delete_mode'] = self.delete_mode

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delete_mode') is not None:
            self.delete_mode = m.get('delete_mode')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        return self

