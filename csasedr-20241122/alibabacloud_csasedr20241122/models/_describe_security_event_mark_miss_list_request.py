# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityEventMarkMissListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        disposal_way: str = None,
        event_name: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        remark: str = None,
    ):
        # Specifies the page number of the returned page. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The disposal method of the rule. The current query does not filter by this field, and you do not need to set it. Valid values:
        # 
        # - **auto_add_white**: Automatic whitelisting.
        # - **defense_not_notification**: Defense only without notification.
        self.disposal_way = disposal_way
        # The name of the alert event (subtype).
        self.event_name = event_name
        # The maximum number of records to return in a single query. This field is reserved for compatibility. The backend currently uses CurrentPage and PageSize for pagination.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The number of whitelist rules to return on each page in a paging query. Default value: **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # **[Deprecated]** This field is deprecated.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.disposal_way is not None:
            result['DisposalWay'] = self.disposal_way

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DisposalWay') is not None:
            self.disposal_way = m.get('DisposalWay')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

