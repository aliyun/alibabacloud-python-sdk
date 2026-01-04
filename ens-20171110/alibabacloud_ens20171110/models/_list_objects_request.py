# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListObjectsRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        continuation_token: str = None,
        encoding_type: str = None,
        marker: str = None,
        max_keys: int = None,
        prefix: str = None,
        start_after: str = None,
    ):
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The token used in this list operation. If the number of objects exceeds the value of MaxKeys, the NextContinuationToken is included in the response as the token for the next list operation.
        self.continuation_token = continuation_token
        # The encoding type of the object names in the response. Only URL encoding is supported.
        self.encoding_type = encoding_type
        # The position from which the list operation starts. If this parameter is specified, objects whose names are alphabetically greater than value of Marker are returned. The Marker parameter is used to list the returned objects by page, and its value must be smaller than 1,024 bytes in length.
        # 
        # Even if the value specified for Marker does not exist in the list during a conditional query, the list starts from the object whose name is alphabetically greater than the value of Marker.
        self.marker = marker
        # The maximum number of objects to return. Valid values: 0 to 1000. Default value: 100.
        self.max_keys = max_keys
        # The prefix that must be included in the names of objects you want to list. If you specify a prefix to query objects, the returned object names contain the prefix.
        # 
        # The value of the parameter must be less than 1,000 bytes in length.
        self.prefix = prefix
        # The position from which the list operation starts. If this parameter is specified, objects whose names are alphabetically greater than the value of StartAfter are returned. The StartAfter parameter is used to list the returned objects by page, and its value must be less than 1,000 bytes in length. Even if the value specified for StartAfter does not exist in the list during a conditional query, the list starts from the object whose name is alphabetically greater than the value of StartAfter.
        self.start_after = start_after

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token

        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.start_after is not None:
            result['StartAfter'] = self.start_after

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')

        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('StartAfter') is not None:
            self.start_after = m.get('StartAfter')

        return self

