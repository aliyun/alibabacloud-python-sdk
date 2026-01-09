# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ETLConfigurationSink(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        datasets: List[str] = None,
        endpoint: str = None,
        logstore: str = None,
        name: str = None,
        project: str = None,
        role_arn: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.datasets = datasets
        self.endpoint = endpoint
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project = project
        # This parameter is required.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret

        if self.datasets is not None:
            result['datasets'] = self.datasets

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.name is not None:
            result['name'] = self.name

        if self.project is not None:
            result['project'] = self.project

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')

        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')

        if m.get('datasets') is not None:
            self.datasets = m.get('datasets')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        return self

