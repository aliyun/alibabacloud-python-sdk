# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDictInformationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListDictInformationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListDictInformationResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListDictInformationResponseBodyResult(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        oss_object: main_models.ListDictInformationResponseBodyResultOssObject = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.oss_object = oss_object
        self.type = type

    def validate(self):
        if self.oss_object:
            self.oss_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.oss_object is not None:
            result['ossObject'] = self.oss_object.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('ossObject') is not None:
            temp_model = main_models.ListDictInformationResponseBodyResultOssObject()
            self.oss_object = temp_model.from_map(m.get('ossObject'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDictInformationResponseBodyResultOssObject(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        etag: str = None,
        key: str = None,
    ):
        self.bucket_name = bucket_name
        self.etag = etag
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.etag is not None:
            result['etag'] = self.etag

        if self.key is not None:
            result['key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('etag') is not None:
            self.etag = m.get('etag')

        if m.get('key') is not None:
            self.key = m.get('key')

        return self

