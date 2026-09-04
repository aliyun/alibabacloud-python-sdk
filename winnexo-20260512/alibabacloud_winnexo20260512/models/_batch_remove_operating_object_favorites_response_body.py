# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class BatchRemoveOperatingObjectFavoritesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        graph_name: str = None,
        message: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        remaining_count: int = None,
        removed_count: int = None,
        request_id: str = None,
        requested_count: int = None,
        results: List[main_models.BatchRemoveOperatingObjectFavoritesResponseBodyResults] = None,
    ):
        # The status code.
        self.code = code
        # The graph name.
        self.graph_name = graph_name
        # The description of the status code.
        self.message = message
        # The object type, such as customer. This parameter has a value when type is set to mention.
        self.object_type = object_type
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The number of remaining favorited objects within the specified scope.
        self.remaining_count = remaining_count
        # The number of physical favorite records that are actually deleted.
        self.removed_count = removed_count
        # The request ID.
        self.request_id = request_id
        # **The number of requested members before deduplication.**
        self.requested_count = requested_count
        # The relationships between internal and external DingTalk users that failed to be created.
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

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.message is not None:
            result['message'] = self.message

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.remaining_count is not None:
            result['remainingCount'] = self.remaining_count

        if self.removed_count is not None:
            result['removedCount'] = self.removed_count

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.requested_count is not None:
            result['requestedCount'] = self.requested_count

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('remainingCount') is not None:
            self.remaining_count = m.get('remainingCount')

        if m.get('removedCount') is not None:
            self.removed_count = m.get('removedCount')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requestedCount') is not None:
            self.requested_count = m.get('requestedCount')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.BatchRemoveOperatingObjectFavoritesResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self



class BatchRemoveOperatingObjectFavoritesResponseBodyResults(DaraModel):
    def __init__(
        self,
        is_favorited: bool = None,
        object_id: str = None,
        processed: bool = None,
    ):
        # Indicates whether the object is favorited after the operation.
        self.is_favorited = is_favorited
        # The aligned object ID: target ID or KR ID.
        self.object_id = object_id
        # Indicates whether the request has been processed.
        self.processed = processed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_favorited is not None:
            result['isFavorited'] = self.is_favorited

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.processed is not None:
            result['processed'] = self.processed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isFavorited') is not None:
            self.is_favorited = m.get('isFavorited')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('processed') is not None:
            self.processed = m.get('processed')

        return self

