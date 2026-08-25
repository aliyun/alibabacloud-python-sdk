# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServerIdeEcsSpecsRequest(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # The accelerator type. Valid values:
        # - CPU: uses only CPU.
        # - GPU: uses GPU acceleration.
        self.accelerator_type = accelerator_type
        # The maximum number of records to return in a single request.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The DataWorks resource group identifier. You can specify the numeric ID of the resource group or the full identifier in the Serverless_res_group_{tenantId}_{resgId} format.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

