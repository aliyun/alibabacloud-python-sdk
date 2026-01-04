# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class ListObjectsResponseBody(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        common_prefixes: List[str] = None,
        contents: List[main_models.ListObjectsResponseBodyContents] = None,
        continuation_token: str = None,
        delimiter: str = None,
        encoding_type: str = None,
        is_truncated: bool = None,
        key_count: int = None,
        marker: str = None,
        max_keys: int = None,
        next_continuation_token: str = None,
        next_marker: str = None,
        prefix: str = None,
        request_id: str = None,
    ):
        # The name of the bucket.
        self.bucket_name = bucket_name
        # If the delimiter parameter is specified in the request, the response contains CommonPrefixes. Objects whose names contain the same string from the prefix to the next occurrence of the delimiter are grouped as a single result element in CommonPrefixes.
        self.common_prefixes = common_prefixes
        # The list of object metadata.
        self.contents = contents
        # The token used in this list operation.
        self.continuation_token = continuation_token
        # The character used to group objects by name.
        self.delimiter = delimiter
        # The encoding type of the object names in the response.
        self.encoding_type = encoding_type
        # Indicates whether the listed objects are truncated. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.is_truncated = is_truncated
        # The number of keys returned for this request.
        self.key_count = key_count
        # The position from which the list operation starts.
        self.marker = marker
        # The maximum number of objects returned.
        self.max_keys = max_keys
        # The token used in the next list operation.
        self.next_continuation_token = next_continuation_token
        # The position from which the next list operation starts.
        self.next_marker = next_marker
        # The prefix contained in the names of returned objects.
        self.prefix = prefix
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.contents:
            for v1 in self.contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.common_prefixes is not None:
            result['CommonPrefixes'] = self.common_prefixes

        result['Contents'] = []
        if self.contents is not None:
            for k1 in self.contents:
                result['Contents'].append(k1.to_map() if k1 else None)

        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token

        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter

        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.key_count is not None:
            result['KeyCount'] = self.key_count

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys

        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token

        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CommonPrefixes') is not None:
            self.common_prefixes = m.get('CommonPrefixes')

        self.contents = []
        if m.get('Contents') is not None:
            for k1 in m.get('Contents'):
                temp_model = main_models.ListObjectsResponseBodyContents()
                self.contents.append(temp_model.from_map(k1))

        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')

        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')

        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('KeyCount') is not None:
            self.key_count = m.get('KeyCount')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')

        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')

        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListObjectsResponseBodyContents(DaraModel):
    def __init__(
        self,
        etag: str = None,
        key: str = None,
        last_modified: str = None,
        size: int = None,
    ):
        # The entity tag (ETag). When an object is created, an ETag is created to identify the content of the object.
        # 
        # *   For an object that is created by calling the PutObject operation, the ETag value of the object is the MD5 hash of the object content.
        # *   For an object that is not created by calling the PutObject operation, the ETag value of the object is the UUID of the object content.
        # *   The ETag of an object can be used to check whether the object content is modified. However, we recommend that you use the MD5 hash of an object rather than the ETag value of the object to verify data integrity.
        self.etag = etag
        # The name of the object.
        self.key = key
        # The time when the object was last modified.
        self.last_modified = last_modified
        # The size of the returned object. Unit: bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.etag is not None:
            result['ETag'] = self.etag

        if self.key is not None:
            result['Key'] = self.key

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

