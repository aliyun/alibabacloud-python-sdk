# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeFirewallTemplateApplyResultsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        task_id: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. A client token is generated from your client to ensure uniqueness across different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The firewall template ID.
        self.firewall_template_id = firewall_template_id
        # The page number of the firewall rule list.
        self.page_number = page_number
        # The number of entries per page for a paged query. Default value: 20.
        self.page_size = page_size
        # The region ID of the simple application server. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the template application task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

