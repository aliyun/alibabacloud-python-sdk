# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PictureSearchPictureRequest(DaraModel):
    def __init__(
        self,
        app_instance_id: str = None,
        contain_pic_url: bool = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        picture_search_type: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        threshold: float = None,
    ):
        # Instance ID of the image search application instance. You can call the [QueryPictureSearchApps](https://help.aliyun.com/document_detail/206608.html) operation to query instance ID.
        # 
        # This parameter is required.
        self.app_instance_id = app_instance_id
        # Specifies whether the response includes the image URL.
        # 
        # > Currently, the response is returned regardless of whether this parameter is set to true or false.
        # 
        # This parameter is required.
        self.contain_pic_url = contain_pic_url
        # The page number of the page to return. Pages start from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end time of the search range. The time is a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of entries to return on each page. Maximum value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The search type. Valid values:
        # - **1** (default): face
        # - **0**: human body
        self.picture_search_type = picture_search_type
        # The URL of the image to search for.
        # 
        # This parameter is required.
        self.search_pic_url = search_pic_url
        # The start time of the search range. The time is a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The search threshold. Valid values: 0 to 1.
        # 
        # > Set the search threshold to a value greater than or equal to 0.3 to ensure a match with the detected object.
        # 
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.contain_pic_url is not None:
            result['ContainPicUrl'] = self.contain_pic_url

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type

        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('ContainPicUrl') is not None:
            self.contain_pic_url = m.get('ContainPicUrl')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')

        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

