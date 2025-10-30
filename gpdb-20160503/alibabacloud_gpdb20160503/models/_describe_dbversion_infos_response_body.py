# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBVersionInfosResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        version_details: main_models.DescribeDBVersionInfosResponseBodyVersionDetails = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried minor versions.
        self.version_details = version_details

    def validate(self):
        if self.version_details:
            self.version_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.version_details is not None:
            result['VersionDetails'] = self.version_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VersionDetails') is not None:
            temp_model = main_models.DescribeDBVersionInfosResponseBodyVersionDetails()
            self.version_details = temp_model.from_map(m.get('VersionDetails'))

        return self

class DescribeDBVersionInfosResponseBodyVersionDetails(DaraModel):
    def __init__(
        self,
        serverless: Any = None,
        storage_elastic: Any = None,
    ):
        # The queried minor version information about the instance in Serverless mode.
        self.serverless = serverless
        # The queried minor version information about the instance in elastic storage mode.
        self.storage_elastic = storage_elastic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serverless is not None:
            result['Serverless'] = self.serverless

        if self.storage_elastic is not None:
            result['StorageElastic'] = self.storage_elastic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Serverless') is not None:
            self.serverless = m.get('Serverless')

        if m.get('StorageElastic') is not None:
            self.storage_elastic = m.get('StorageElastic')

        return self

