# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterResourcesResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeClusterResourcesResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeClusterResourcesResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeClusterResourcesResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        created: str = None,
        instance_id: str = None,
        resource_info: str = None,
        resource_type: str = None,
        state: str = None,
        auto_create: int = None,
        dependencies: List[main_models.DescribeClusterResourcesResponseBodyDependencies] = None,
        associated_object: main_models.DescribeClusterResourcesResponseBodyAssociatedObject = None,
        delete_behavior: main_models.DescribeClusterResourcesResponseBodyDeleteBehavior = None,
        creator_type: str = None,
        extra_info: Dict[str, Any] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The time when the resource was created.
        self.created = created
        # The resource ID.
        self.instance_id = instance_id
        # Information about the resource. For more details about its source, see [ListStackResources](https://help.aliyun.com/document_detail/133836.html).
        self.resource_info = resource_info
        # The resource type.
        self.resource_type = resource_type
        # The state of the resource. Valid values:
        # 
        # - `CREATE_COMPLETE`: The resource is successfully created.
        # 
        # - `CREATE_FAILED`: The resource fails to be created.
        # 
        # - `CREATE_IN_PROGRESS`: The resource is being created.
        # 
        # - `DELETE_FAILED`: The resource fails to be deleted.
        # 
        # - `DELETE_IN_PROGRESS`: The resource is being deleted.
        # 
        # - `ROLLBACK_COMPLETE`: The rollback is successful.
        # 
        # - `ROLLBACK_FAILED`: The rollback fails.
        # 
        # - `ROLLBACK_IN_PROGRESS`: The rollback is in progress.
        self.state = state
        # Indicates whether the resource is created by ACK. Valid values:
        # 
        # - 1: The resource is created by ACK.
        # 
        # - 0: The resource is an existing resource.
        self.auto_create = auto_create
        # The list of dependent resources.
        self.dependencies = dependencies
        # The Kubernetes object that is associated with the resource.
        self.associated_object = associated_object
        # The deletion behavior of the resource when the cluster is deleted.
        self.delete_behavior = delete_behavior
        # The type of the creator of the resource. Valid values:
        # 
        # - user: The resource is created by a user.
        # 
        # - system: The resource is created by the ACK control plane.
        # 
        # - addon: The resource is created by an add-on.
        self.creator_type = creator_type
        # Extra information about the resource.
        self.extra_info = extra_info

    def validate(self):
        if self.dependencies:
            for v1 in self.dependencies:
                 if v1:
                    v1.validate()
        if self.associated_object:
            self.associated_object.validate()
        if self.delete_behavior:
            self.delete_behavior.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.created is not None:
            result['created'] = self.created

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.resource_info is not None:
            result['resource_info'] = self.resource_info

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.state is not None:
            result['state'] = self.state

        if self.auto_create is not None:
            result['auto_create'] = self.auto_create

        result['dependencies'] = []
        if self.dependencies is not None:
            for k1 in self.dependencies:
                result['dependencies'].append(k1.to_map() if k1 else None)

        if self.associated_object is not None:
            result['associated_object'] = self.associated_object.to_map()

        if self.delete_behavior is not None:
            result['delete_behavior'] = self.delete_behavior.to_map()

        if self.creator_type is not None:
            result['creator_type'] = self.creator_type

        if self.extra_info is not None:
            result['extra_info'] = self.extra_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('resource_info') is not None:
            self.resource_info = m.get('resource_info')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('auto_create') is not None:
            self.auto_create = m.get('auto_create')

        self.dependencies = []
        if m.get('dependencies') is not None:
            for k1 in m.get('dependencies'):
                temp_model = main_models.DescribeClusterResourcesResponseBodyDependencies()
                self.dependencies.append(temp_model.from_map(k1))

        if m.get('associated_object') is not None:
            temp_model = main_models.DescribeClusterResourcesResponseBodyAssociatedObject()
            self.associated_object = temp_model.from_map(m.get('associated_object'))

        if m.get('delete_behavior') is not None:
            temp_model = main_models.DescribeClusterResourcesResponseBodyDeleteBehavior()
            self.delete_behavior = temp_model.from_map(m.get('delete_behavior'))

        if m.get('creator_type') is not None:
            self.creator_type = m.get('creator_type')

        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')

        return self

class DescribeClusterResourcesResponseBodyDeleteBehavior(DaraModel):
    def __init__(
        self,
        delete_by_default: bool = None,
        changeable: bool = None,
    ):
        # Indicates whether to delete the resource by default when the cluster is deleted. Valid values:
        # 
        # - true: The resource is deleted by default.
        # 
        # - false: The resource is not deleted by default.
        self.delete_by_default = delete_by_default
        # Indicates whether the default behavior specified by the `delete_by_default` parameter can be changed. Valid values:
        # 
        # - true: The default behavior can be changed.
        # 
        # - false: The default behavior cannot be changed.
        self.changeable = changeable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_by_default is not None:
            result['delete_by_default'] = self.delete_by_default

        if self.changeable is not None:
            result['changeable'] = self.changeable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('delete_by_default') is not None:
            self.delete_by_default = m.get('delete_by_default')

        if m.get('changeable') is not None:
            self.changeable = m.get('changeable')

        return self

class DescribeClusterResourcesResponseBodyAssociatedObject(DaraModel):
    def __init__(
        self,
        kind: str = None,
        namespace: str = None,
        name: str = None,
    ):
        # The type of the Kubernetes object.
        self.kind = kind
        # The namespace of the Kubernetes object.
        self.namespace = namespace
        # The name of the Kubernetes object.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kind is not None:
            result['kind'] = self.kind

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class DescribeClusterResourcesResponseBodyDependencies(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_type: str = None,
        instance_id: str = None,
    ):
        # The cluster ID of the dependent resource.
        self.cluster_id = cluster_id
        # The type of the dependent resource.
        self.resource_type = resource_type
        # The instance ID of the dependent resource.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        return self

