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
        # The type of cluster resource that you want to delete or retain.
        self.delete_options = delete_options
        # Specifies whether to retain the Server Load Balancer (SLB) resources that are created by the cluster.
        # 
        # *   `true`: retains the SLB instances that are created by the cluster.
        # *   `false`: does not retain the SLB instances that are created by the cluster.
        # 
        # Default value: `false`. Set resource_type to `SLB` in the `delete_options` parameter to manage SLB instances.
        self.keep_slb = keep_slb
        # Specifies whether to retain all resources. If you set the parameter to `true`, the `retain_resources` parameter is ignored. The cloud resources that are created by the cluster are retained. You can call the `DescribeClusterResources` operation to query cloud resources created by the cluster. If you set the parameter to `false`, resources to be retained by default in the `delete_options` parameter are still retained. To delete these resources, set `delete_mode` to `delete` in `delete_options`.
        # 
        # *   `true`: retains all resources, including cloud resources created by the cluster.
        # *   `false`: does not retain all resources. Resources to be retained by default in the `delete_options` parameter are retained. For example, `ALB` instances are retained when this parameter is set to `false`.
        # 
        # Default value: `false`.
        self.retain_all_resources = retain_all_resources
        # The list of resources. To retain resources when you delete a cluster, you need to specify the IDs of the resources to be retained.
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
        # The deletion policy for the specified type of resource. Valid values:
        # 
        # *   delete: deletes the specified type of resource.
        # *   retain: retains the specified type of resource.
        self.delete_mode = delete_mode
        # The type of the resource. Valid values:
        # 
        # *   SLB: SLB resources created for Services. By default, the SLB resources are automatically deleted.
        # *   ALB: Application Load Balancer (ALB) resources created by the ALB Ingress controller. By default, the ALB resources are retained.
        # *   SLS_Data: Simple Log Service projects used by the cluster logging feature. By default, the Simple Log Service projects are retained.
        # *   SLS_ControlPlane: Simple Log Service projects used to store the logs of control planes in ACK managed clusters. By default, the Simple Log Service projects are retained.
        # *   PrivateZone: PrivateZone resources created by ACK Serverless clusters. By default, the PrivateZone resources are retained.
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

