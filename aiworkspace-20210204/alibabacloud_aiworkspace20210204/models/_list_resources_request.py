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
        # The name of the resource group. You can call [ListResources](https://help.aliyun.com/document_detail/449143.html) to obtain the name of the resource group.
        self.group_name = group_name
        # Tag-based filter conditions. Multiple conditions are separated by commas (,). Only resources that meet all the specified tag-based filter conditions are returned.
        # 
        # This parameter is available only for resources whose ProductType is ACS.
        self.labels = labels
        # The operation to perform. Valid values:
        # 
        # *   ListResourceByWorkspace: obtains the resources in the workspace. This is the default value.
        # *   ListResource: obtains the resources of the user.
        self.option = option
        # The page number. The pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # **This field is no longer used and will be removed. Use the ResourceType field instead.
        self.product_types = product_types
        # The quota IDs, which are separated by commas (,). Only resources that contain all the specified quotas are returned.
        # 
        # >  This parameter is available only for resources whose ResourceTypes is ACS.
        self.quota_ids = quota_ids
        # The resource name. The value must meet the following requirements:
        # 
        # *   The name must be 3 to 28 characters in length.
        # *   The name is unique in the region.
        self.resource_name = resource_name
        # The resource types. Valid values:
        # 
        # *   MaxCompute
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        self.resource_types = resource_types
        # Specifies whether to show detailed information, which includes the Quotas field. Valid values:
        # 
        # *   true (default)
        # *   false
        self.verbose = verbose
        # The fields to return. Multiple fields are separated by commas (,). Valid values:
        # 
        # *   Quota
        # *   Label
        # *   IsDefault
        self.verbose_fields = verbose_fields
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # *   This parameter is required when the Option parameter is set to ListResourceByWorkspace.
        # *   You do not need to configure this parameter when the Option parameter is set to ListResource.
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

