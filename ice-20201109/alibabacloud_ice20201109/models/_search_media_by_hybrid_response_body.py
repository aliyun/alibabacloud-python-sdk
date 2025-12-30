# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SearchMediaByHybridResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        media_list: List[main_models.SearchMediaByHybridResponseBodyMediaList] = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The status code returned.
        self.code = code
        # The media assets that match the search query.
        self.media_list = media_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success
        # The total number of media assets that match the search criteria.
        self.total = total

    def validate(self):
        if self.media_list:
            for v1 in self.media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['MediaList'] = []
        if self.media_list is not None:
            for k1 in self.media_list:
                result['MediaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.media_list = []
        if m.get('MediaList') is not None:
            for k1 in m.get('MediaList'):
                temp_model = main_models.SearchMediaByHybridResponseBodyMediaList()
                self.media_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchMediaByHybridResponseBodyMediaList(DaraModel):
    def __init__(
        self,
        clip_info: List[main_models.SearchMediaByHybridResponseBodyMediaListClipInfo] = None,
        media_id: str = None,
    ):
        # The information about the relevant clips.
        self.clip_info = clip_info
        # The ID of the media asset.
        self.media_id = media_id

    def validate(self):
        if self.clip_info:
            for v1 in self.clip_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClipInfo'] = []
        if self.clip_info is not None:
            for k1 in self.clip_info:
                result['ClipInfo'].append(k1.to_map() if k1 else None)

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clip_info = []
        if m.get('ClipInfo') is not None:
            for k1 in m.get('ClipInfo'):
                temp_model = main_models.SearchMediaByHybridResponseBodyMediaListClipInfo()
                self.clip_info.append(temp_model.from_map(k1))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class SearchMediaByHybridResponseBodyMediaListClipInfo(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        to: float = None,
    ):
        # The start time of the relevant clip.
        self.from_ = from_
        # The relevance score of the clip for the query.
        self.score = score
        # The end time of the relevant clip.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

