# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePictureSearchJobRequest(DaraModel):
    def __init__(
        self,
        app_instance_id: str = None,
        body_threshold: float = None,
        end_time: int = None,
        picture_search_type: int = None,
        search_pic_url: str = None,
        start_time: int = None,
        threshold: float = None,
    ):
        # Instance ID of the image search application instance. You can call the [QueryPictureSearchApps](https://help.aliyun.com/document_detail/206608.html) operation to query instance ID.
        # 
        # This parameter is required.
        self.app_instance_id = app_instance_id
        # The threshold for human body search. Valid values: 0 to 1.
        # 
        # To ensure the accuracy of search results, set this parameter to a value greater than or equal to 0.8. If this parameter is not specified, the value of the Threshold parameter is used.
        self.body_threshold = body_threshold
        # The end time of the search range. The time is a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The search type. Valid values:
        # 
        # - 1: face
        # - 0: human body
        # 
        # Default value: 1.
        self.picture_search_type = picture_search_type
        # The URL of the image to be searched.
        # 
        # This parameter is required.
        self.search_pic_url = search_pic_url
        # The start time of the search range. The time is a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The threshold for face search. Valid values: 0 to 1.
        # 
        # To ensure the accuracy of search results, set this parameter to a value between 0.3 and 0.6.
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

        if self.body_threshold is not None:
            result['BodyThreshold'] = self.body_threshold

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if m.get('BodyThreshold') is not None:
            self.body_threshold = m.get('BodyThreshold')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')

        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

