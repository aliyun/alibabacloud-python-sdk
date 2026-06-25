# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourcesRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        labels: str = None,
        option: str = None,
        page_number: int = None,
        page_size: int = None,
        product_types: str = None,
        quota_ids: str = None,
        resource_name: str = None,
        resource_types: str = None,
        verbose: bool = None,
        verbose_fields: str = None,
        workspace_id: str = None,
    ):
        # The name of the resource group. To get the resource group name, see [ListResources](https://help.aliyun.com/document_detail/449143.html).
        self.group_name = group_name
        # A comma-separated list of labels. This operation returns only the resources that have all the specified labels.
        # 
        # This parameter is available only for resources whose `ResourceTypes` is set to `ACS`.
        self.labels = labels
        # The option to query resources. Valid values:
        # 
        # - `ListResourceByWorkspace` (Default): lists the resources in a workspace.
        # 
        # - `ListResource`: lists the resources of the current user.
        self.option = option
        # The page number. The value must be greater than or equal to 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # **Deprecated.** This parameter is deprecated. Use the `ResourceType` parameter instead.
        self.product_types = product_types
        # A comma-separated list of quota IDs. This operation returns only the resources that are associated with all the specified quota IDs.
        # 
        # > This parameter is available only for resources whose `ResourceTypes` is set to `ACS`.
        self.quota_ids = quota_ids
        # The resource name. The name must meet the following requirements:
        # 
        # - The name must be 3 to 28 characters in length.
        # 
        # - The name must be unique within a region.
        self.resource_name = resource_name
        # The resource types. Valid values:
        # 
        # - `MaxCompute`: MaxCompute resources.
        # 
        # - `ECS`: ECS resources.
        # 
        # - `Lingjun`: Lingjun computing resources.
        # 
        # - `ACS`: ACS computing resources.
        # 
        # - `Flink`: Flink resources.
        # 
        # - `SelfManagedAckPro`: self-managed AckPro cluster resources.
        # 
        # - `SelfManagedAckLingjun`: self-managed AckLingjun cluster resources.
        # 
        # - `SelfManagedASI`: self-managed ASI cluster resources from a third-party cloud.
        self.resource_types = resource_types
        # Specifies whether to return detailed information. The detailed information includes the `Quotas` field. Valid values:
        # 
        # - `true` (Default): returns detailed information.
        # 
        # - `false`: does not return detailed information.
        self.verbose = verbose
        # A comma-separated list of fields that you want to return. Valid values:
        # 
        # - `Quota`
        # 
        # - `Label`
        # 
        # - `IsDefault`
        self.verbose_fields = verbose_fields
        # The ID of the workspace. To get the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # 
        # - This parameter is required if `Option` is set to `ListResourceByWorkspace`.
        # 
        # - This parameter is not required if `Option` is set to `ListResource`.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.option is not None:
            result['Option'] = self.option

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_types is not None:
            result['ProductTypes'] = self.product_types

        if self.quota_ids is not None:
            result['QuotaIds'] = self.quota_ids

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.verbose_fields is not None:
            result['VerboseFields'] = self.verbose_fields

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductTypes') is not None:
            self.product_types = m.get('ProductTypes')

        if m.get('QuotaIds') is not None:
            self.quota_ids = m.get('QuotaIds')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('VerboseFields') is not None:
            self.verbose_fields = m.get('VerboseFields')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

