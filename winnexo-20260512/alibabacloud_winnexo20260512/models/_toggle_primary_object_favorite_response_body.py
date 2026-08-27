# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class TogglePrimaryObjectFavoriteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        favorite_count: int = None,
        message: str = None,
        request_id: str = None,
        results: List[main_models.TogglePrimaryObjectFavoriteResponseBodyResults] = None,
    ):
        # The status code.
        self.code = code
        # The total number of follows by the user for the specified object type.
        self.favorite_count = favorite_count
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The list of results.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.favorite_count is not None:
            result['favoriteCount'] = self.favorite_count

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('favoriteCount') is not None:
            self.favorite_count = m.get('favoriteCount')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.TogglePrimaryObjectFavoriteResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class TogglePrimaryObjectFavoriteResponseBodyResults(DaraModel):
    def __init__(
        self,
        is_favorited: bool = None,
        message: str = None,
        object_id: str = None,
        success: bool = None,
    ):
        # Indicates whether the object is followed after the operation.
        self.is_favorited = is_favorited
        # The description of the status code.
        self.message = message
        # The ID of the aligned object: target ID or KR ID.
        self.object_id = object_id
        # Indicates whether the operation is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_favorited is not None:
            result['isFavorited'] = self.is_favorited

        if self.message is not None:
            result['message'] = self.message

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isFavorited') is not None:
            self.is_favorited = m.get('isFavorited')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

