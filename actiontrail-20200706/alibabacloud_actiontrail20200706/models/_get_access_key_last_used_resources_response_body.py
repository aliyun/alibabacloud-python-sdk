# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyLastUsedResourcesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resources: List[main_models.GetAccessKeyLastUsedResourcesResponseBodyResources] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The list of returned resources.
        # 
        # This parameter is required.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.GetAccessKeyLastUsedResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class GetAccessKeyLastUsedResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        detail: str = None,
        resource_name: str = None,
        resource_type: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # The event details.
        self.detail = detail
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type
        # The source of the last usage record.
        # 
        # Valid values:
        # 
        # - Internal
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   Other event
        # 
        #   <!-- -->
        # 
        # - ManagementEvent
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   Management event
        # 
        #   <!-- -->
        # 
        # - DataEvent
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   Data event
        # 
        #   <!-- -->
        self.source = source
        # The timestamp when the resource was used. Unit: milliseconds.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source is not None:
            result['Source'] = self.source

        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')

        return self

