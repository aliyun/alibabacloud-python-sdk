# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRayLogsRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        delimiter: str = None,
        marker: str = None,
        max_keys: int = None,
        prefix: str = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The character used to group object names. All objects whose names contain the specified prefix and between which the delimiter character appears for the first time are grouped as a set of elements (CommonPrefixes).
        self.delimiter = delimiter
        # The marker after which the returned objects are listed in alphabetical order.
        self.marker = marker
        # The maximum number of objects to return. If the listing cannot be completed in a single request due to the max-keys setting, a NextMarker element is included in the response as the marker for the next listing request.
        # 
        # Valid values: greater than 0 and less than 1000.
        # 
        # Default value: 100.
        self.max_keys = max_keys
        # The prefix that the keys of the returned files must start with.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.delimiter is not None:
            result['delimiter'] = self.delimiter

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys

        if self.prefix is not None:
            result['prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('delimiter') is not None:
            self.delimiter = m.get('delimiter')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        return self

