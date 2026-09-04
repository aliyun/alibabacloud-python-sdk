# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResolveModelDataSource(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
    ):
        # The Logstore name.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The project name.
        # 
        # This parameter is required.
        self.project = project
        # The region ID.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

