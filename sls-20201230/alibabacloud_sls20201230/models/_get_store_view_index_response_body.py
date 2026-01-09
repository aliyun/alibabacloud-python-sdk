# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetStoreViewIndexResponseBody(DaraModel):
    def __init__(
        self,
        indexes: List[main_models.GetStoreViewIndexResponseBodyIndexes] = None,
    ):
        # The index configurations.
        self.indexes = indexes

    def validate(self):
        if self.indexes:
            for v1 in self.indexes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['indexes'] = []
        if self.indexes is not None:
            for k1 in self.indexes:
                result['indexes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.indexes = []
        if m.get('indexes') is not None:
            for k1 in m.get('indexes'):
                temp_model = main_models.GetStoreViewIndexResponseBodyIndexes()
                self.indexes.append(temp_model.from_map(k1))

        return self

class GetStoreViewIndexResponseBodyIndexes(DaraModel):
    def __init__(
        self,
        index: main_models.Index = None,
        logstore: str = None,
        project: str = None,
    ):
        # The index configurations of the Logstore.
        self.index = index
        # The name of the Logstore.
        self.logstore = logstore
        # The name of the project to which the Logstore belongs.
        self.project = project

    def validate(self):
        if self.index:
            self.index.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index.to_map()

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            temp_model = main_models.Index()
            self.index = temp_model.from_map(m.get('index'))

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

