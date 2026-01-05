# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateAINodesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbnodes: List[main_models.CreateAINodesRequestDBNodes] = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.dbnodes = dbnodes

    def validate(self):
        if self.dbnodes:
            for v1 in self.dbnodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k1 in self.dbnodes:
                result['DBNodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k1 in m.get('DBNodes'):
                temp_model = main_models.CreateAINodesRequestDBNodes()
                self.dbnodes.append(temp_model.from_map(k1))

        return self

class CreateAINodesRequestDBNodes(DaraModel):
    def __init__(
        self,
        dbnode_class: str = None,
    ):
        self.dbnode_class = dbnode_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        return self

