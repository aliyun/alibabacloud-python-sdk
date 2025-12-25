# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateDigitalEmployeeRequest(DaraModel):
    def __init__(
        self,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        knowledges: main_models.UpdateDigitalEmployeeRequestKnowledges = None,
        role_arn: str = None,
    ):
        self.default_rule = default_rule
        self.description = description
        self.display_name = display_name
        self.knowledges = knowledges
        self.role_arn = role_arn

    def validate(self):
        if self.knowledges:
            self.knowledges.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_rule is not None:
            result['defaultRule'] = self.default_rule

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.knowledges is not None:
            result['knowledges'] = self.knowledges.to_map()

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultRule') is not None:
            self.default_rule = m.get('defaultRule')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('knowledges') is not None:
            temp_model = main_models.UpdateDigitalEmployeeRequestKnowledges()
            self.knowledges = temp_model.from_map(m.get('knowledges'))

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        return self

class UpdateDigitalEmployeeRequestKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.UpdateDigitalEmployeeRequestKnowledgesBailian] = None,
    ):
        self.bailian = bailian

    def validate(self):
        if self.bailian:
            for v1 in self.bailian:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bailian'] = []
        if self.bailian is not None:
            for k1 in self.bailian:
                result['bailian'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bailian = []
        if m.get('bailian') is not None:
            for k1 in m.get('bailian'):
                temp_model = main_models.UpdateDigitalEmployeeRequestKnowledgesBailian()
                self.bailian.append(temp_model.from_map(k1))

        return self

class UpdateDigitalEmployeeRequestKnowledgesBailian(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        index_id: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        self.attributes = attributes
        self.index_id = index_id
        self.region = region
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.index_id is not None:
            result['indexId'] = self.index_id

        if self.region is not None:
            result['region'] = self.region

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('indexId') is not None:
            self.index_id = m.get('indexId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

