# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPushRecordsRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        end_time: str = None,
        keyword: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        push_type: str = None,
        source: str = None,
        start_time: str = None,
        target: str = None,
    ):
        # The AppKey of the application.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The end time for the query. Specify the time in UTC, using the ISO-8601 format `YYYY-MM-DDThh:mm:ssZ`.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The keyword used for the query. The search covers the `MessageId`, `Title`, and `Body` fields. For `Title` and `Body`, the system applies Chinese word segmentation and matches whole tokens instead of substrings.
        self.keyword = keyword
        # This parameter is deprecated.
        self.next_token = next_token
        # The page number to query. Default: 1. Maximum: 10,000.
        self.page = page
        # The number of entries to return on each page. Default: 20. Maximum: 100.
        self.page_size = page_size
        # The push type. Valid values:
        # 
        # - **MESSAGE**: A message.
        # 
        # - **NOTICE**: A notification.
        # 
        # - **LIVE_ACTIVITY**: A Live Activity.
        self.push_type = push_type
        # The push source. Valid values:
        # 
        # - **API**: Pushes initiated via an OpenAPI call.
        # 
        # - **CONSOLE**: Pushes initiated from the Mobile Push console.
        # 
        # - **OpenAPIExplorer**: Pushes initiated from Alibaba Cloud OpenAPI Explorer.
        self.source = source
        # The start time for the query. Specify the time in UTC, using the ISO-8601 format `YYYY-MM-DDThh:mm:ssZ`.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The push target. Valid values:
        # 
        # - **DEVICE**: Push to devices.
        # 
        # - **ACCOUNT**: Push to accounts.
        # 
        # - **ALIAS**: Push to aliases.
        # 
        # - **TAG**: Push to tags.
        # 
        # - **ALL**: Push to all devices.
        # 
        # - **TBD**: Initializes a continuous push. The push target is specified in a subsequent call to the `ContinuouslyPush` API operation.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.push_type is not None:
            result['PushType'] = self.push_type

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

