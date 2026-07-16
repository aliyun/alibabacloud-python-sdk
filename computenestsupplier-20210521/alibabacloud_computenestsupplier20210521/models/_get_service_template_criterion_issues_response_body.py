# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetServiceTemplateCriterionIssuesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risky_template_count: int = None,
        template_criterion_issue_list: List[main_models.GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueList] = None,
        total_criterion_issue_count: int = None,
        total_mandatory_criterion_issue_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The number of templates with criterion issues in the service.
        self.risky_template_count = risky_template_count
        # The list of criterion issues in the template.
        self.template_criterion_issue_list = template_criterion_issue_list
        # The total number of criterion issues in the service template.
        self.total_criterion_issue_count = total_criterion_issue_count
        # The number of mandatory criterion issues in the service template.
        self.total_mandatory_criterion_issue_count = total_mandatory_criterion_issue_count

    def validate(self):
        if self.template_criterion_issue_list:
            for v1 in self.template_criterion_issue_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risky_template_count is not None:
            result['RiskyTemplateCount'] = self.risky_template_count

        result['TemplateCriterionIssueList'] = []
        if self.template_criterion_issue_list is not None:
            for k1 in self.template_criterion_issue_list:
                result['TemplateCriterionIssueList'].append(k1.to_map() if k1 else None)

        if self.total_criterion_issue_count is not None:
            result['TotalCriterionIssueCount'] = self.total_criterion_issue_count

        if self.total_mandatory_criterion_issue_count is not None:
            result['TotalMandatoryCriterionIssueCount'] = self.total_mandatory_criterion_issue_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskyTemplateCount') is not None:
            self.risky_template_count = m.get('RiskyTemplateCount')

        self.template_criterion_issue_list = []
        if m.get('TemplateCriterionIssueList') is not None:
            for k1 in m.get('TemplateCriterionIssueList'):
                temp_model = main_models.GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueList()
                self.template_criterion_issue_list.append(temp_model.from_map(k1))

        if m.get('TotalCriterionIssueCount') is not None:
            self.total_criterion_issue_count = m.get('TotalCriterionIssueCount')

        if m.get('TotalMandatoryCriterionIssueCount') is not None:
            self.total_mandatory_criterion_issue_count = m.get('TotalMandatoryCriterionIssueCount')

        return self

class GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueList(DaraModel):
    def __init__(
        self,
        criterion_issues: List[main_models.GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueListCriterionIssues] = None,
        template_name: str = None,
        template_url: int = None,
        total_criterion_issue_count: int = None,
        total_mandatory_criterion_issue_count: int = None,
    ):
        # The list of criterion issues.
        self.criterion_issues = criterion_issues
        # The name of the template.
        self.template_name = template_name
        # The URL of the template.
        self.template_url = template_url
        # The total number of criterion issues in the service template.
        self.total_criterion_issue_count = total_criterion_issue_count
        # The number of mandatory criterion issues in the service template.
        self.total_mandatory_criterion_issue_count = total_mandatory_criterion_issue_count

    def validate(self):
        if self.criterion_issues:
            for v1 in self.criterion_issues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CriterionIssues'] = []
        if self.criterion_issues is not None:
            for k1 in self.criterion_issues:
                result['CriterionIssues'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url

        if self.total_criterion_issue_count is not None:
            result['TotalCriterionIssueCount'] = self.total_criterion_issue_count

        if self.total_mandatory_criterion_issue_count is not None:
            result['TotalMandatoryCriterionIssueCount'] = self.total_mandatory_criterion_issue_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criterion_issues = []
        if m.get('CriterionIssues') is not None:
            for k1 in m.get('CriterionIssues'):
                temp_model = main_models.GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueListCriterionIssues()
                self.criterion_issues.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')

        if m.get('TotalCriterionIssueCount') is not None:
            self.total_criterion_issue_count = m.get('TotalCriterionIssueCount')

        if m.get('TotalMandatoryCriterionIssueCount') is not None:
            self.total_mandatory_criterion_issue_count = m.get('TotalMandatoryCriterionIssueCount')

        return self

class GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueListCriterionIssues(DaraModel):
    def __init__(
        self,
        extend_info: main_models.GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueListCriterionIssuesExtendInfo = None,
        level: str = None,
        position: str = None,
        type: str = None,
    ):
        # The supplementary information about the criterion issue.
        self.extend_info = extend_info
        # The severity level of the issue. Valid values:
        # 
        # - Mandatory: The issue must be fixed.
        # 
        # - Recommended: You are advised to fix the issue.
        self.level = level
        # The position where the issue exists.
        self.position = position
        # The type of the criterion issue.
        self.type = type

    def validate(self):
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()

        if self.level is not None:
            result['Level'] = self.level

        if self.position is not None:
            result['Position'] = self.position

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            temp_model = main_models.GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueListCriterionIssuesExtendInfo()
            self.extend_info = temp_model.from_map(m.get('ExtendInfo'))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetServiceTemplateCriterionIssuesResponseBodyTemplateCriterionIssueListCriterionIssuesExtendInfo(DaraModel):
    def __init__(
        self,
        association_property: str = None,
        property: str = None,
        property_value: str = None,
    ):
        # The AssociationProperty of the ROS parameter.
        self.association_property = association_property
        # The resource property.
        self.property = property
        # The value of the resource property.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_property is not None:
            result['AssociationProperty'] = self.association_property

        if self.property is not None:
            result['Property'] = self.property

        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationProperty') is not None:
            self.association_property = m.get('AssociationProperty')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        return self

