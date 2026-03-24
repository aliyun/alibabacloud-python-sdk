# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateDigitalEmployeeRequest(DaraModel):
    def __init__(
        self,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        knowledges: main_models.CreateDigitalEmployeeRequestKnowledges = None,
        name: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        tags: List[main_models.Tag] = None,
    ):
        # The default rule.
        self.default_rule = default_rule
        # The description of the digital employee.
        self.description = description
        # The display name of the digital employee.
        self.display_name = display_name
        # The list of knowledge bases.
        self.knowledges = knowledges
        # The name of the digital employee.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        # 
        # This parameter is required.
        self.role_arn = role_arn
        # The tags.
        self.tags = tags

    def validate(self):
        if self.knowledges:
            self.knowledges.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.CreateDigitalEmployeeRequestKnowledges()
            self.knowledges = temp_model.from_map(m.get('knowledges'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateDigitalEmployeeRequestKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.CreateDigitalEmployeeRequestKnowledgesBailian] = None,
        sop: List[Dict[str, Any]] = None,
    ):
        # The list of Bailian knowledge bases.
        self.bailian = bailian
        # The list of Standard Operating Procedure (SOP) knowledge bases.
        self.sop = sop

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

        if self.sop is not None:
            result['sop'] = self.sop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bailian = []
        if m.get('bailian') is not None:
            for k1 in m.get('bailian'):
                temp_model = main_models.CreateDigitalEmployeeRequestKnowledgesBailian()
                self.bailian.append(temp_model.from_map(k1))

        if m.get('sop') is not None:
            self.sop = m.get('sop')

        return self

class CreateDigitalEmployeeRequestKnowledgesBailian(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        index_id: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # The properties of the knowledge base.
        self.attributes = attributes
        # The ID of the Bailian index.
        self.index_id = index_id
        # The region of the Bailian knowledge base.
        self.region = region
        # The ID of the Bailian workspace.
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

