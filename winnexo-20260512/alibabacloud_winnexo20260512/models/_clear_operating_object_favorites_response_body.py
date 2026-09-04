# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearOperatingObjectFavoritesResponseBody(DaraModel):
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
        verified: bool = None,
    ):
        # The status code. SUCCESS indicates success. In case of failure, the corresponding error type is returned, such as ERR_BAD_REQUEST, ERR_VALIDATION_FAILED, or ERR_INTERNAL_SERVER_ERROR.
        self.code = code
        # The graph name. You can call listGraphs to obtain the value.
        self.graph_name = graph_name
        # The status code description.
        self.message = message
        # The object type, such as customer. This parameter has a value when type is set to mention.
        self.object_type = object_type
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The number of remaining followed objects within the specified scope.
        self.remaining_count = remaining_count
        # The number of physical follow records that were actually deleted.
        self.removed_count = removed_count
        # The request ID.
        self.request_id = request_id
        # Indicates whether the remaining record count has been verified as zero within the same transaction.
        self.verified = verified

    def validate(self):
        pass

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

        if self.verified is not None:
            result['verified'] = self.verified

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

        if m.get('verified') is not None:
            self.verified = m.get('verified')

        return self

