# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SearchMediaByFaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        media_info_list: List[main_models.SearchMediaByFaceResponseBodyMediaInfoList] = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The status code returned.
        self.code = code
        # The media assets that meet the conditions.
        self.media_info_list = media_info_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true false
        self.success = success
        # The total number of data records that meet the specified filter condition.
        self.total = total

    def validate(self):
        if self.media_info_list:
            for v1 in self.media_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['MediaInfoList'] = []
        if self.media_info_list is not None:
            for k1 in self.media_info_list:
                result['MediaInfoList'].append(k1.to_map() if k1 else None)

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

        self.media_info_list = []
        if m.get('MediaInfoList') is not None:
            for k1 in m.get('MediaInfoList'):
                temp_model = main_models.SearchMediaByFaceResponseBodyMediaInfoList()
                self.media_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchMediaByFaceResponseBodyMediaInfoList(DaraModel):
    def __init__(
        self,
        media_id: str = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

