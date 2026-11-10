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
        # The AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The end time of the query. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The query keyword. The query is performed based on the MessageId, Title, and Body fields. The system performs Chinese word segmentation on the title and body of the push, and uses the segmented words for the query instead of substring matching.
        self.keyword = keyword
        # **[Deprecated]** This parameter is deprecated and no longer used.
        self.next_token = next_token
        # The current page number of the push records. Default value: 1. Maximum value: 10000.
        self.page = page
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The push type. Valid values:
        # 
        # - **MESSAGE**: message
        # 
        # - **NOTICE**: notification
        # 
        # - **LIVE_ACTIVITY**: live activity
        self.push_type = push_type
        # The push source. Valid values:
        # 
        # - **API**: push initiated by OpenAPI, including pushes initiated from the OpenAPI platform console
        # - **CONSOLE**: push initiated from the Mobile Push console
        # - **OpenAPIExplorer**: push initiated from the Alibaba Cloud OpenAPI Explorer platform
        self.source = source
        # The start time of the query. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The push target. Valid values:
        # 
        # - **DEVICE**: push by device
        # 
        # - **ACCOUNT**: push by account
        # 
        # - **ALIAS**: push by alias
        # 
        # - **TAG**: push by tag
        # 
        # - **ALL**: push to all devices
        # 
        # - **TBD**: initialize continuous push, where the push target is specified by the subsequent ContinuouslyPush operation
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

