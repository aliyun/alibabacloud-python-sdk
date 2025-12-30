# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SearchIndexJobRerunResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SearchIndexJobRerunResponseBodyData = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code returned.
        self.code = code
        # The response data.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.SearchIndexJobRerunResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchIndexJobRerunResponseBodyData(DaraModel):
    def __init__(
        self,
        media_ids_no_exist: List[str] = None,
    ):
        # The media asset IDs that do not exist.
        self.media_ids_no_exist = media_ids_no_exist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids_no_exist is not None:
            result['MediaIdsNoExist'] = self.media_ids_no_exist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIdsNoExist') is not None:
            self.media_ids_no_exist = m.get('MediaIdsNoExist')

        return self

