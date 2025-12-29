# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableEngineVersionResponseBody(DaraModel):
    def __init__(
        self,
        engine_versions: main_models.DescribeAvailableEngineVersionResponseBodyEngineVersions = None,
        request_id: str = None,
    ):
        # The list of one or more engine versions to which an ApsaraDB for MongoDB instance can be upgraded.
        # 
        # >  An empty string is returned if the latest version is being used.
        self.engine_versions = engine_versions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.engine_versions:
            self.engine_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_versions is not None:
            result['EngineVersions'] = self.engine_versions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineVersions') is not None:
            temp_model = main_models.DescribeAvailableEngineVersionResponseBodyEngineVersions()
            self.engine_versions = temp_model.from_map(m.get('EngineVersions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableEngineVersionResponseBodyEngineVersions(DaraModel):
    def __init__(
        self,
        engine_version: List[str] = None,
    ):
        self.engine_version = engine_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        return self

