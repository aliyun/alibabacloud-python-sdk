# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMediaBasicInfosRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        business_type: str = None,
        end_time: str = None,
        include_file_basic_info: bool = None,
        max_results: int = None,
        media_id: str = None,
        media_type: str = None,
        next_token: str = None,
        sort_by: str = None,
        source: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The authentication expiration time, in seconds.
        # 
        # - Minimum value: 1.
        # 
        # - Maximum value: 86400.
        # 
        # - Default value: 3600.
        self.auth_timeout = auth_timeout
        # The business type. Valid values:
        # 
        # - `subtitles`: subtitles
        # 
        # - `watermark`: watermark
        # 
        # - `opening`: opening
        # 
        # - `ending`: ending
        # 
        # - `general`: General
        self.business_type = business_type
        # The end time of the query range, based on the creation time (`utcCreated`).
        # 
        # - The query returns results created at or before this time (inclusive).
        # 
        # - The time must be in UTC and comply with the ISO 8601 standard. The format is `YYYY-MM-DD\\"T\\"HH:mm:ss\\"Z\\"`. For example, `2017-01-11T12:00:00Z` corresponds to 20:00:00 on January 11, 2017 (UTC+8).
        self.end_time = end_time
        # Set to `true` to include basic file information in the response.
        self.include_file_basic_info = include_file_basic_info
        # The maximum number of results to return per page.
        # 
        # Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The media ID.
        self.media_id = media_id
        # The media type. Valid values:
        # 
        # - `image`: image
        # 
        # - `video`: video
        # 
        # - `audio`: audio
        # 
        # - `text`: text
        self.media_type = media_type
        # The pagination token used to retrieve the next page of results. An empty value indicates that all results have been returned.
        self.next_token = next_token
        # The sort order for results based on the creation time (`utcCreated`). The default is descending. Valid values:
        # 
        # - `desc`: Descending order
        # 
        # - `asc`: Ascending order
        self.sort_by = sort_by
        # The source. Valid values:
        # 
        # - `oss`: OSS
        # 
        # - `vod`: video on demand
        # 
        # - `live`: live streaming
        # 
        # - `general`: Other sources (default).
        self.source = source
        # The start time of the query range, based on the creation time (`utcCreated`).
        # 
        # - The query returns results created after this time (exclusive).
        # 
        # - The time must be in UTC and comply with the ISO 8601 standard. The format is `YYYY-MM-DD\\"T\\"HH:mm:ss\\"Z\\"`. For example, `2017-01-11T12:00:00Z` corresponds to 20:00:00 on January 11, 2017 (UTC+8).
        self.start_time = start_time
        # The media status. Valid values:
        # 
        # - `Init`: The source file is not ready.
        # 
        # - `Preparing`: The source file is being prepared. For example, it is being uploaded or composited.
        # 
        # - `PrepareFail`: The source file failed to prepare. This may occur, for example, if the system fails to retrieve information about the source file.
        # 
        # - `Normal`: The source file is ready.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

