# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecWorkflowConnectivityRequest(DaraModel):
    def __init__(
        self,
        ds_config: str = None,
        ds_name: str = None,
        ds_type: str = None,
        ds_version: str = None,
        id: int = None,
        is_modified: bool = None,
    ):
        # The datasource config. The value is a JSON character string whose structure is defined by each dsType. Parse the JSON string before use. Sensitive fields such as tokens are masked in the response.
        self.ds_config = ds_config
        # The data source name. Exact match and fuzzy match are supported.
        self.ds_name = ds_name
        # The data source type, such as Hive or MaxCompute.
        self.ds_type = ds_type
        # The data source version number.
        self.ds_version = ds_version
        # The primary key ID that uniquely identifies a record.
        self.id = id
        # Specifies whether the configuration has been modified.
        self.is_modified = is_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_config is not None:
            result['dsConfig'] = self.ds_config

        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.ds_version is not None:
            result['dsVersion'] = self.ds_version

        if self.id is not None:
            result['id'] = self.id

        if self.is_modified is not None:
            result['isModified'] = self.is_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dsConfig') is not None:
            self.ds_config = m.get('dsConfig')

        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('dsVersion') is not None:
            self.ds_version = m.get('dsVersion')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isModified') is not None:
            self.is_modified = m.get('isModified')

        return self

