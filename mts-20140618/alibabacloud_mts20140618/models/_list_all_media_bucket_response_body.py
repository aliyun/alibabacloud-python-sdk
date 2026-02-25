# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListAllMediaBucketResponseBody(DaraModel):
    def __init__(
        self,
        media_bucket_list: main_models.ListAllMediaBucketResponseBodyMediaBucketList = None,
        next_page_token: str = None,
        request_id: str = None,
    ):
        self.media_bucket_list = media_bucket_list
        # The returned value of NextPageToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_page_token = next_page_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_bucket_list:
            self.media_bucket_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_bucket_list is not None:
            result['MediaBucketList'] = self.media_bucket_list.to_map()

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaBucketList') is not None:
            temp_model = main_models.ListAllMediaBucketResponseBodyMediaBucketList()
            self.media_bucket_list = temp_model.from_map(m.get('MediaBucketList'))

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAllMediaBucketResponseBodyMediaBucketList(DaraModel):
    def __init__(
        self,
        media_bucket: List[main_models.ListAllMediaBucketResponseBodyMediaBucketListMediaBucket] = None,
    ):
        self.media_bucket = media_bucket

    def validate(self):
        if self.media_bucket:
            for v1 in self.media_bucket:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaBucket'] = []
        if self.media_bucket is not None:
            for k1 in self.media_bucket:
                result['MediaBucket'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_bucket = []
        if m.get('MediaBucket') is not None:
            for k1 in m.get('MediaBucket'):
                temp_model = main_models.ListAllMediaBucketResponseBodyMediaBucketListMediaBucket()
                self.media_bucket.append(temp_model.from_map(k1))

        return self

class ListAllMediaBucketResponseBodyMediaBucketListMediaBucket(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        referer: str = None,
        type: str = None,
    ):
        self.bucket = bucket
        self.referer = referer
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

