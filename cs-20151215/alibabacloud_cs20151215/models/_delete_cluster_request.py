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
        # The options for deleting the resources that are associated with the cluster.
        self.delete_options = delete_options
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
        # The deletion policy for the specified resource type. Valid values:
        # 
        # - delete: Deletes the resources.
        # 
        # - retain: Retains the resources.
        self.delete_mode = delete_mode
        # The type of resource. Valid values:
        # 
        # - SLB: the SLB resources created for Services. These resources are deleted by default, but you can choose to retain them.
        # 
        # - ALB: the ALB resources created by the ALB Ingress controller. These resources are retained by default, but you can choose to delete them.
        # 
        # - SLS_Data: the SLS project used for cluster logs. This resource is retained by default, but you can choose to delete it.
        # 
        # - SLS_ControlPlane: the SLS project used for control plane logs in a managed cluster. This resource is retained by default, but you can choose to delete it.
        # 
        # - PrivateZone: the PrivateZone resource created by an ACK Serverless cluster. This resource is retained by default, but you can choose to delete it.
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

