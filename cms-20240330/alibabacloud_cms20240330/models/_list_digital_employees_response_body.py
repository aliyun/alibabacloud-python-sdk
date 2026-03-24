# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListDigitalEmployeesResponseBody(DaraModel):
    def __init__(
        self,
        digital_employees: List[main_models.ListDigitalEmployeesResponseBodyDigitalEmployees] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # List of digital employees.
        self.digital_employees = digital_employees
        # Maximum number of results returned.
        self.max_results = max_results
        # Token for the next page of results.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # Total number of records.
        self.total = total

    def validate(self):
        if self.digital_employees:
            for v1 in self.digital_employees:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['digitalEmployees'] = []
        if self.digital_employees is not None:
            for k1 in self.digital_employees:
                result['digitalEmployees'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.digital_employees = []
        if m.get('digitalEmployees') is not None:
            for k1 in m.get('digitalEmployees'):
                temp_model = main_models.ListDigitalEmployeesResponseBodyDigitalEmployees()
                self.digital_employees.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListDigitalEmployeesResponseBodyDigitalEmployees(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        employee_type: str = None,
        knowledges: main_models.ListDigitalEmployeesResponseBodyDigitalEmployeesKnowledges = None,
        name: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        tags: List[main_models.Tag] = None,
        update_time: str = None,
    ):
        # Creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # Default rule.
        self.default_rule = default_rule
        # Description.
        self.description = description
        # Digital employee display name.
        self.display_name = display_name
        # Digital employee type.
        self.employee_type = employee_type
        # List of knowledge bases.
        self.knowledges = knowledges
        # Digital employee name.
        self.name = name
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Role ARN.
        self.role_arn = role_arn
        # Tags.
        self.tags = tags
        # Update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

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
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.default_rule is not None:
            result['defaultRule'] = self.default_rule

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.employee_type is not None:
            result['employeeType'] = self.employee_type

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

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('defaultRule') is not None:
            self.default_rule = m.get('defaultRule')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('employeeType') is not None:
            self.employee_type = m.get('employeeType')

        if m.get('knowledges') is not None:
            temp_model = main_models.ListDigitalEmployeesResponseBodyDigitalEmployeesKnowledges()
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

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ListDigitalEmployeesResponseBodyDigitalEmployeesKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.ListDigitalEmployeesResponseBodyDigitalEmployeesKnowledgesBailian] = None,
        sop: List[Dict[str, Any]] = None,
    ):
        # Bailian knowledge base list.
        self.bailian = bailian
        # SOP knowledge base list.
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
                temp_model = main_models.ListDigitalEmployeesResponseBodyDigitalEmployeesKnowledgesBailian()
                self.bailian.append(temp_model.from_map(k1))

        if m.get('sop') is not None:
            self.sop = m.get('sop')

        return self

class ListDigitalEmployeesResponseBodyDigitalEmployeesKnowledgesBailian(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        index_id: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # Knowledge base attributes.
        self.attributes = attributes
        # Bailian index ID.
        self.index_id = index_id
        # Region of the Bailian knowledge base.
        self.region = region
        # Bailian workspace ID.
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

