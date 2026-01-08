# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListInstagramPostsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.ListInstagramPostsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListInstagramPostsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstagramPostsResponseBodyData(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        full_picture: str = None,
        id: str = None,
        media_type: str = None,
        media_url: str = None,
        message: str = None,
        permalink_url: str = None,
    ):
        self.created_time = created_time
        self.full_picture = full_picture
        self.id = id
        self.media_type = media_type
        self.media_url = media_url
        self.message = message
        self.permalink_url = permalink_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.full_picture is not None:
            result['FullPicture'] = self.full_picture

        if self.id is not None:
            result['Id'] = self.id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.media_url is not None:
            result['MediaUrl'] = self.media_url

        if self.message is not None:
            result['Message'] = self.message

        if self.permalink_url is not None:
            result['PermalinkUrl'] = self.permalink_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('FullPicture') is not None:
            self.full_picture = m.get('FullPicture')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PermalinkUrl') is not None:
            self.permalink_url = m.get('PermalinkUrl')

        return self

