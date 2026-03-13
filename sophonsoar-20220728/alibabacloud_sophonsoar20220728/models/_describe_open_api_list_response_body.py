# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenApiListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeOpenApiListResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenApiListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenApiListResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        directories: Any = None,
        version: str = None,
        versions: Any = None,
    ):
        # The response code. Valid values:
        # 
        # *   200: successful.
        # *   500: failed.
        self.code = code
        # The information about the returned APIs.
        self.directories = directories
        # The version number of the API.
        self.version = version
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.directories is not None:
            result['Directories'] = self.directories

        if self.version is not None:
            result['Version'] = self.version

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Directories') is not None:
            self.directories = m.get('Directories')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

