# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServerIdeInstancesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        related_user_id: str = None,
        resource_group_id: str = None,
        sub_type: str = None,
    ):
        # The keyword for fuzzy match by instance ID or instance name.
        self.keyword = keyword
        # The maximum number of records to return in a single request.
        self.max_results = max_results
        # The pagination token for the next query. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The page number. Minimum value: 1.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The account ID of the user who owns the instance. Used to filter instances by owner.
        self.related_user_id = related_user_id
        # The DataWorks resource group identifier. You can specify a numeric resource group ID or a full identifier in the format of Serverless_res_group_{tenantId}_{resgId}.
        self.resource_group_id = resource_group_id
        # The instance subtype. Valid values:
        # - PERSONAL_DEV: personal development environment.
        # - DATA_AGENT: Data Agent.
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.related_user_id is not None:
            result['RelatedUserId'] = self.related_user_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RelatedUserId') is not None:
            self.related_user_id = m.get('RelatedUserId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

