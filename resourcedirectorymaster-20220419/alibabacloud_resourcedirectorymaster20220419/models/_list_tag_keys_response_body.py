# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tags: List[main_models.ListTagKeysResponseBodyTags] = None,
    ):
        # Indicates whether the next query is required.
        # 
        # *   If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # *   If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the tag keys.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTagKeysResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListTagKeysResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # The tag key.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

