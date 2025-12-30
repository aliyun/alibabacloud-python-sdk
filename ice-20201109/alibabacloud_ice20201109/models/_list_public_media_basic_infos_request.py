# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublicMediaBasicInfosRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        include_file_basic_info: bool = None,
        max_results: int = None,
        media_tag_id: str = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The business type of the media asset. Valid values:
        # 
        # *   sticker
        # *   bgm
        # *   bgi
        self.business_type = business_type
        # Specifies whether to return the basic information of the media asset.
        self.include_file_basic_info = include_file_basic_info
        # The maximum number of entries to return.
        # 
        # Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The media tag. All media assets that contain the specified media tag are returned. Valid values:
        # 
        # *   Sticker tags:
        # 
        #     *   sticker-atmosphere
        #     *   sticker-bubble
        #     *   sticker-cute
        #     *   sticker-daily
        #     *   sticker-expression
        #     *   sticker-gif
        # 
        # *   Background music (BGM) tags:
        # 
        #     *   bgm-romantic
        #     *   bgm-cuisine
        #     *   bgm-chinese-style
        #     *   bgm-upbeat
        #     *   bgm-dynamic
        #     *   bgm-relaxing
        #     *   bgm-quirky
        #     *   bgm-beauty
        # 
        # *   Background image (BGI) tags:
        # 
        #     *   bgi-grad
        #     *   bgi-solid
        #     *   bgi-pic
        self.media_tag_id = media_tag_id
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The page number. Default value: 1
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.include_file_basic_info is not None:
            result['IncludeFileBasicInfo'] = self.include_file_basic_info

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('IncludeFileBasicInfo') is not None:
            self.include_file_basic_info = m.get('IncludeFileBasicInfo')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

