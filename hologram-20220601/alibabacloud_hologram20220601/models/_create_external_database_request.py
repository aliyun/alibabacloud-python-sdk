# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class CreateExternalDatabaseRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        database_name: str = None,
        default_user_mapping: str = None,
        external_config: List[main_models.CreateExternalDatabaseRequestExternalConfig] = None,
        metastore_type: str = None,
    ):
        self.comment = comment
        self.database_name = database_name
        self.default_user_mapping = default_user_mapping
        self.external_config = external_config
        self.metastore_type = metastore_type

    def validate(self):
        if self.external_config:
            for v1 in self.external_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.default_user_mapping is not None:
            result['defaultUserMapping'] = self.default_user_mapping

        result['externalConfig'] = []
        if self.external_config is not None:
            for k1 in self.external_config:
                result['externalConfig'].append(k1.to_map() if k1 else None)

        if self.metastore_type is not None:
            result['metastoreType'] = self.metastore_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('defaultUserMapping') is not None:
            self.default_user_mapping = m.get('defaultUserMapping')

        self.external_config = []
        if m.get('externalConfig') is not None:
            for k1 in m.get('externalConfig'):
                temp_model = main_models.CreateExternalDatabaseRequestExternalConfig()
                self.external_config.append(temp_model.from_map(k1))

        if m.get('metastoreType') is not None:
            self.metastore_type = m.get('metastoreType')

        return self



class CreateExternalDatabaseRequestExternalConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

