# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServicesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        service_name: str = None,
        service_type: str = None,
        tags_shrink: str = None,
    ):
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # Token for the next query, an empty value indicates the last page.
        self.next_token = next_token
        self.resource_group_id = resource_group_id
        self.service_name = service_name
        # Service type
        self.service_type = service_type
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        return self

