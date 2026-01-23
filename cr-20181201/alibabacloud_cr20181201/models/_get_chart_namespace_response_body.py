# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChartNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        code: str = None,
        default_repo_type: str = None,
        instance_id: str = None,
        is_success: bool = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # Indicates whether a repository was automatically created in the namespace. Valid values:
        # 
        # *   `true`: A repository was automatically created in the namespace.
        # *   `false`: No repository was automatically created in the namespace.
        self.auto_create_repo = auto_create_repo
        # The return value.
        self.code = code
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo

        if self.code is not None:
            result['Code'] = self.code

        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

