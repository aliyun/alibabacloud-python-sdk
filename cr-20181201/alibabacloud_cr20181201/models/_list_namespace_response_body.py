# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        namespaces: List[main_models.ListNamespaceResponseBodyNamespaces] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The queried namespaces.
        self.namespaces = namespaces
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of the queried namespaces.
        self.total_count = total_count

    def validate(self):
        if self.namespaces:
            for v1 in self.namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        result['Namespaces'] = []
        if self.namespaces is not None:
            for k1 in self.namespaces:
                result['Namespaces'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k1 in m.get('Namespaces'):
                temp_model = main_models.ListNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNamespaceResponseBodyNamespaces(DaraModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_configuration: main_models.RepoConfiguration = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        resource_group_id: str = None,
    ):
        # Indicates whether the automatically creating repositories feature is enabled for the namespace.
        self.auto_create_repo = auto_create_repo
        self.default_repo_configuration = default_repo_configuration
        # The default type of repositories in the namespace. Valid values:
        # 
        # *   `PUBLIC`: public repositories.
        # *   `PRIVATE`: private repositories.
        self.default_repo_type = default_repo_type
        # The instance ID.
        self.instance_id = instance_id
        # The namespace ID.
        self.namespace_id = namespace_id
        # The namespace name.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.default_repo_configuration:
            self.default_repo_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo

        if self.default_repo_configuration is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration.to_map()

        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')

        if m.get('DefaultRepoConfiguration') is not None:
            temp_model = main_models.RepoConfiguration()
            self.default_repo_configuration = temp_model.from_map(m.get('DefaultRepoConfiguration'))

        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

