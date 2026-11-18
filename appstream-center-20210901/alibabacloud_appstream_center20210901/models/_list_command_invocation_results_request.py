# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCommandInvocationResultsRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_ids: List[str] = None,
        app_instance_persistent_ids: List[str] = None,
        invocation_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The ID of the delivery group. Queries the command execution results under this delivery group. This parameter must be specified when AppInstanceGroupIds is not specified. If both are specified, AppInstanceGroupIds takes precedence and this parameter does not take effect.
        self.app_instance_group_id = app_instance_group_id
        # The list of delivery group IDs. A maximum of 200 IDs can be specified, and all delivery groups must be in the same region. When specified, it takes precedence over AppInstanceGroupId and queries the command execution results of all persistent sessions under these delivery groups. The list cannot contain null values.
        self.app_instance_group_ids = app_instance_group_ids
        # The list of persistent session IDs. A maximum of 100 IDs can be specified. It is used to query only the command execution results of the specified persistent sessions. When AppInstanceGroupIds is specified, only persistent sessions belonging to these delivery groups are retained. If no matching persistent sessions are found, an empty list is returned.
        self.app_instance_persistent_ids = app_instance_persistent_ids
        # The command execution ID, which is the InvocationId returned when you call RunAppInstanceCommand to deliver a command.
        # 
        # This parameter is required.
        self.invocation_id = invocation_id
        # This parameter does not take effect in the current version and does not affect the query results if passed. Use PageNumber and PageSize for pagination.
        self.max_results = max_results
        # This parameter does not take effect in the current version and does not affect the query results if passed. Use PageNumber and PageSize for pagination.
        self.next_token = next_token
        # The page number of the query results to display. It is used together with PageSize for paging in a paged query. If not specified, the default value is 0, which indicates the first page.
        self.page_number = page_number
        # The number of query results per page. Default value: 200.
        self.page_size = page_size
        # The product type. Currently, only WuyingServer is supported. If you specify other values, a parameter error is returned.
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_ids is not None:
            result['AppInstanceGroupIds'] = self.app_instance_group_ids

        if self.app_instance_persistent_ids is not None:
            result['AppInstancePersistentIds'] = self.app_instance_persistent_ids

        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupIds') is not None:
            self.app_instance_group_ids = m.get('AppInstanceGroupIds')

        if m.get('AppInstancePersistentIds') is not None:
            self.app_instance_persistent_ids = m.get('AppInstancePersistentIds')

        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

