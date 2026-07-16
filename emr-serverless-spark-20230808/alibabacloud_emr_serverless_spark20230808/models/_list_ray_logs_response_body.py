# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListRayLogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListRayLogsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code. The value 1000000 indicates success.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListRayLogsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRayLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        delimiter: str = None,
        is_truncated: bool = None,
        marker: str = None,
        max_keys: int = None,
        next_marker: str = None,
        object_list: List[main_models.ListRayLogsResponseBodyDataObjectList] = None,
        prefix: str = None,
    ):
        # The OSS bucket name.
        self.bucket_name = bucket_name
        # The character used to group object names. All objects whose names contain the specified prefix and between which the delimiter character appears for the first time are grouped as a set of elements (CommonPrefixes).
        self.delimiter = delimiter
        # Indicates whether the results returned in the request are truncated.
        self.is_truncated = is_truncated
        # The marker after which the returned objects are listed in alphabetical order.
        self.marker = marker
        # The maximum number of objects to return.
        self.max_keys = max_keys
        # The marker from which the next listing of files starts.
        self.next_marker = next_marker
        # The list of object metadata.
        self.object_list = object_list
        # The prefix that the keys of the returned files must start with.
        self.prefix = prefix

    def validate(self):
        if self.object_list:
            for v1 in self.object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.delimiter is not None:
            result['delimiter'] = self.delimiter

        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys

        if self.next_marker is not None:
            result['nextMarker'] = self.next_marker

        result['objectList'] = []
        if self.object_list is not None:
            for k1 in self.object_list:
                result['objectList'].append(k1.to_map() if k1 else None)

        if self.prefix is not None:
            result['prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('delimiter') is not None:
            self.delimiter = m.get('delimiter')

        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')

        if m.get('nextMarker') is not None:
            self.next_marker = m.get('nextMarker')

        self.object_list = []
        if m.get('objectList') is not None:
            for k1 in m.get('objectList'):
                temp_model = main_models.ListRayLogsResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        return self

class ListRayLogsResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        is_dir: bool = None,
        name: str = None,
        path: str = None,
        size: int = None,
        time_modified: int = None,
    ):
        # Indicates whether the entry is a directory.
        self.is_dir = is_dir
        # The name.
        self.name = name
        # The file path.
        self.path = path
        # The file size, in bytes.
        self.size = size
        # The modification time. The value is a UNIX timestamp in milliseconds.
        self.time_modified = time_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_dir is not None:
            result['isDir'] = self.is_dir

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        if self.size is not None:
            result['size'] = self.size

        if self.time_modified is not None:
            result['timeModified'] = self.time_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isDir') is not None:
            self.is_dir = m.get('isDir')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('timeModified') is not None:
            self.time_modified = m.get('timeModified')

        return self

