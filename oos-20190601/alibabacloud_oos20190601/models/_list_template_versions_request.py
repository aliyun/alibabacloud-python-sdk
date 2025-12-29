# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplateVersionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        share_type: str = None,
        template_name: str = None,
    ):
        # The number of entries per page. Valid values: 10 to 100
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The type of the template. Valid values: Private and Public.
        self.share_type = share_type
        # The name of the template.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

