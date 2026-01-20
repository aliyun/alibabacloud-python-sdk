# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class GetLabelTableResponseBody(DaraModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        fields: List[main_models.GetLabelTableResponseBodyFields] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        related_model_features: List[str] = None,
        request_id: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.fields = fields
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.related_model_features = related_model_features
        self.request_id = request_id

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

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.related_model_features is not None:
            result['RelatedModelFeatures'] = self.related_model_features

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetLabelTableResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RelatedModelFeatures') is not None:
            self.related_model_features = m.get('RelatedModelFeatures')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLabelTableResponseBodyFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
    ):
        self.attributes = attributes
        self.name = name
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

