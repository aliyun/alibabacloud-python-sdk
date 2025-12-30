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
        self.auth_timeout = auth_timeout
        # The business type of the media asset. Valid values:
        # 
        # \\- subtitles
        # 
        # \\- watermark
        # 
        # \\- opening
        # 
        # \\- ending
        # 
        # \\- general
        self.business_type = business_type
        # The end time of utcCreated.
        # 
        # \\- The value is the end of the left-open right-closed interval.
        # 
        # \\- Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. For example, 2017-01-11T12:00:00Z indicates 20:00:00 on January 11, 2017 (UTC +8).
        self.end_time = end_time
        # Specifies whether to return the basic information of the source file.
        self.include_file_basic_info = include_file_basic_info
        # The maximum number of entries to return.
        # 
        # Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The ID of the media asset.
        self.media_id = media_id
        # The type of the media asset. Valid values:
        # 
        # \\- image
        # 
        # \\- video
        # 
        # \\- audio
        # 
        # \\- text
        self.media_type = media_type
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The order of sorting by utcCreated. Default value: desc. Valid values:
        # 
        # \\- desc
        # 
        # \\- asc
        self.sort_by = sort_by
        # The source of the media asset. Valid values:
        # 
        # \\- oss: Object Storage Service (OSS).
        # 
        # \\- vod: ApsaraVideo VOD.
        # 
        # \\- live: ApsaraVideo Live.
        # 
        # \\- general: other sources. This is the default value.
        self.source = source
        # The start time of utcCreated.
        # 
        # \\- The value is the beginning of a left-open right-closed interval.
        # 
        # \\- Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. For example, 2017-01-11T12:00:00Z indicates 20:00:00 on January 11, 2017 (UTC +8).
        self.start_time = start_time
        # The status of the media asset. Valid values:
        # 
        # \\- Init: the initial state, which indicates that the source file is not ready.
        # 
        # \\- Preparing: The source file is being prepared. For example, the file is being uploaded or edited.
        # 
        # \\- PrepareFail: The source file failed to be prepared. For example, the information of the source file failed to be obtained.
        # 
        # \\- Normal: The source file is ready.
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

