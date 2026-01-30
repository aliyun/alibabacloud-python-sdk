# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListPublicKeysResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        public_keys: List[main_models.ListPublicKeysResponseBodyPublicKeys] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.public_keys = public_keys
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.public_keys:
            for v1 in self.public_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PublicKeys'] = []
        if self.public_keys is not None:
            for k1 in self.public_keys:
                result['PublicKeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.public_keys = []
        if m.get('PublicKeys') is not None:
            for k1 in m.get('PublicKeys'):
                temp_model = main_models.ListPublicKeysResponseBodyPublicKeys()
                self.public_keys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublicKeysResponseBodyPublicKeys(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        key_group: str = None,
        key_name: str = None,
        key_type: str = None,
        upload_time: str = None,
    ):
        self.content = content
        self.description = description
        self.key_group = key_group
        self.key_name = key_name
        self.key_type = key_type
        self.upload_time = upload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.key_group is not None:
            result['KeyGroup'] = self.key_group

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyGroup') is not None:
            self.key_group = m.get('KeyGroup')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        return self

