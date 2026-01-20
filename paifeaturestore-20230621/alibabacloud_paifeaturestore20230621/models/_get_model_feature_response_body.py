# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class GetModelFeatureResponseBody(DaraModel):
    def __init__(
        self,
        export_training_set_table_script: str = None,
        features: List[main_models.GetModelFeatureResponseBodyFeatures] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_priority_level: int = None,
        label_table_id: str = None,
        label_table_name: str = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        project_name: str = None,
        relations: main_models.GetModelFeatureResponseBodyRelations = None,
        request_id: str = None,
        training_set_fgtable: str = None,
        training_set_table: str = None,
    ):
        self.export_training_set_table_script = export_training_set_table_script
        self.features = features
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_priority_level = label_priority_level
        self.label_table_id = label_table_id
        self.label_table_name = label_table_name
        self.name = name
        self.owner = owner
        self.project_id = project_id
        self.project_name = project_name
        self.relations = relations
        self.request_id = request_id
        self.training_set_fgtable = training_set_fgtable
        self.training_set_table = training_set_table

    def validate(self):
        if self.features:
            for v1 in self.features:
                 if v1:
                    v1.validate()
        if self.relations:
            self.relations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_training_set_table_script is not None:
            result['ExportTrainingSetTableScript'] = self.export_training_set_table_script

        result['Features'] = []
        if self.features is not None:
            for k1 in self.features:
                result['Features'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.label_priority_level is not None:
            result['LabelPriorityLevel'] = self.label_priority_level

        if self.label_table_id is not None:
            result['LabelTableId'] = self.label_table_id

        if self.label_table_name is not None:
            result['LabelTableName'] = self.label_table_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.relations is not None:
            result['Relations'] = self.relations.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.training_set_fgtable is not None:
            result['TrainingSetFGTable'] = self.training_set_fgtable

        if self.training_set_table is not None:
            result['TrainingSetTable'] = self.training_set_table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTrainingSetTableScript') is not None:
            self.export_training_set_table_script = m.get('ExportTrainingSetTableScript')

        self.features = []
        if m.get('Features') is not None:
            for k1 in m.get('Features'):
                temp_model = main_models.GetModelFeatureResponseBodyFeatures()
                self.features.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LabelPriorityLevel') is not None:
            self.label_priority_level = m.get('LabelPriorityLevel')

        if m.get('LabelTableId') is not None:
            self.label_table_id = m.get('LabelTableId')

        if m.get('LabelTableName') is not None:
            self.label_table_name = m.get('LabelTableName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Relations') is not None:
            temp_model = main_models.GetModelFeatureResponseBodyRelations()
            self.relations = temp_model.from_map(m.get('Relations'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrainingSetFGTable') is not None:
            self.training_set_fgtable = m.get('TrainingSetFGTable')

        if m.get('TrainingSetTable') is not None:
            self.training_set_table = m.get('TrainingSetTable')

        return self

class GetModelFeatureResponseBodyRelations(DaraModel):
    def __init__(
        self,
        domains: List[main_models.GetModelFeatureResponseBodyRelationsDomains] = None,
        links: List[main_models.GetModelFeatureResponseBodyRelationsLinks] = None,
    ):
        self.domains = domains
        self.links = links

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()
        if self.links:
            for v1 in self.links:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        result['Links'] = []
        if self.links is not None:
            for k1 in self.links:
                result['Links'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.GetModelFeatureResponseBodyRelationsDomains()
                self.domains.append(temp_model.from_map(k1))

        self.links = []
        if m.get('Links') is not None:
            for k1 in m.get('Links'):
                temp_model = main_models.GetModelFeatureResponseBodyRelationsLinks()
                self.links.append(temp_model.from_map(k1))

        return self

class GetModelFeatureResponseBodyRelationsLinks(DaraModel):
    def __init__(
        self,
        from_: str = None,
        link: str = None,
        to: str = None,
    ):
        self.from_ = from_
        self.link = link
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.link is not None:
            result['Link'] = self.link

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class GetModelFeatureResponseBodyRelationsDomains(DaraModel):
    def __init__(
        self,
        domain_type: str = None,
        id: str = None,
        name: str = None,
    ):
        self.domain_type = domain_type
        # Domain ID。
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetModelFeatureResponseBodyFeatures(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        feature_view_id: str = None,
        feature_view_name: str = None,
        name: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        self.feature_view_id = feature_view_id
        self.feature_view_name = feature_view_name
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id

        if self.feature_view_name is not None:
            result['FeatureViewName'] = self.feature_view_name

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')

        if m.get('FeatureViewName') is not None:
            self.feature_view_name = m.get('FeatureViewName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

