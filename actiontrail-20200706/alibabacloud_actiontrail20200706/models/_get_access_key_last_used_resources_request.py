# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccessKeyLastUsedResourcesRequest(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        next_token: str = None,
        page_size: str = None,
        service_name: str = None,
    ):
        # The AccessKey ID.
        # 
        # This parameter is required.
        self.access_key = access_key
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # > The request parameters must be the same as those of the last request.
        self.next_token = next_token
        # The number of entries per page.
        # 
        # - Valid values: 0 to 100.
        # 
        # - Default value: 20.
        self.page_size = page_size
        # The Alibaba Cloud service. For more information about the Alibaba Cloud services supported by ActionTrail, see [Supported Alibaba Cloud services](https://help.aliyun.com/document_detail/28829.html).
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

