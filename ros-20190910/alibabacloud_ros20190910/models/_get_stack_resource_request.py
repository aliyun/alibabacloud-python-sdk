# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetStackResourceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        logical_resource_id: str = None,
        region_id: str = None,
        resource_attributes: List[str] = None,
        show_resource_attributes: bool = None,
        stack_id: str = None,
    ):
        # Specifies whether to query the resource properties. Valid values:
        # 
        # *   true
        # *   false
        self.client_token = client_token
        # The name of resource property N that you want to query.
        # 
        # >  Maximum value of N: 20.
        # 
        # This parameter is required.
        self.logical_resource_id = logical_resource_id
        # The logical ID of the resource defined in the template.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The status of the resource. Valid values:
        # 
        # *   CREATE_COMPLETE
        # *   CREATE_FAILED
        # *   CREATE_IN_PROGRESS
        # *   UPDATE_IN_PROGRESS
        # *   UPDATE_FAILED
        # *   UPDATE_COMPLETE
        # *   DELETE_IN_PROGRESS
        # *   DELETE_FAILED
        # *   CHECK_IN_PROGRESS
        # *   CHECK_FAILED
        # *   CHECK_COMPLETE
        # *   IMPORT_IN_PROGRESS
        # *   IMPORT_FAILED
        # *   IMPORT_COMPLETE
        self.resource_attributes = resource_attributes
        # The name of resource property N that you want to query.
        self.show_resource_attributes = show_resource_attributes
        # The ID of the region to which the stack belongs. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_attributes is not None:
            result['ResourceAttributes'] = self.resource_attributes

        if self.show_resource_attributes is not None:
            result['ShowResourceAttributes'] = self.show_resource_attributes

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceAttributes') is not None:
            self.resource_attributes = m.get('ResourceAttributes')

        if m.get('ShowResourceAttributes') is not None:
            self.show_resource_attributes = m.get('ShowResourceAttributes')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

