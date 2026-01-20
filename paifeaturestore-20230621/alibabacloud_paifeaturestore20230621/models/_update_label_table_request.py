# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class UpdateLabelTableRequest(DaraModel):
    def __init__(
        self,
        datasource_id: str = None,
        fields: List[main_models.UpdateLabelTableRequestFields] = None,
        name: str = None,
    ):
        self.datasource_id = datasource_id
        # This parameter is required.
        self.fields = fields
        self.name = name

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.UpdateLabelTableRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateLabelTableRequestFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.attributes = attributes
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

