# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricRuleTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        templates: main_models.DescribeMetricRuleTemplateListResponseBodyTemplates = None,
        total: int = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The queried alert templates.
        self.templates = templates
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.templates is not None:
            result['Templates'] = self.templates.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Templates') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateListResponseBodyTemplates()
            self.templates = temp_model.from_map(m.get('Templates'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMetricRuleTemplateListResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        template: List[main_models.DescribeMetricRuleTemplateListResponseBodyTemplatesTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['Template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k1 in m.get('Template'):
                temp_model = main_models.DescribeMetricRuleTemplateListResponseBodyTemplatesTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleTemplateListResponseBodyTemplatesTemplate(DaraModel):
    def __init__(
        self,
        apply_histories: main_models.DescribeMetricRuleTemplateListResponseBodyTemplatesTemplateApplyHistories = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        name: str = None,
        rest_version: int = None,
        template_id: int = None,
    ):
        # The history of applying the alert templates to application groups.
        self.apply_histories = apply_histories
        # The description of the alert template.
        self.description = description
        # The timestamp when the alert template was created.
        # 
        # Unit: milliseconds.
        self.gmt_create = gmt_create
        # The timestamp when the alert template was modified.
        # 
        # Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The name of the alert template.
        self.name = name
        # The version of the alert template.
        # 
        # Default value: 0.
        self.rest_version = rest_version
        # The ID of the alert template.
        self.template_id = template_id

    def validate(self):
        if self.apply_histories:
            self.apply_histories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_histories is not None:
            result['ApplyHistories'] = self.apply_histories.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.rest_version is not None:
            result['RestVersion'] = self.rest_version

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyHistories') is not None:
            temp_model = main_models.DescribeMetricRuleTemplateListResponseBodyTemplatesTemplateApplyHistories()
            self.apply_histories = temp_model.from_map(m.get('ApplyHistories'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RestVersion') is not None:
            self.rest_version = m.get('RestVersion')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class DescribeMetricRuleTemplateListResponseBodyTemplatesTemplateApplyHistories(DaraModel):
    def __init__(
        self,
        apply_history: List[main_models.DescribeMetricRuleTemplateListResponseBodyTemplatesTemplateApplyHistoriesApplyHistory] = None,
    ):
        self.apply_history = apply_history

    def validate(self):
        if self.apply_history:
            for v1 in self.apply_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplyHistory'] = []
        if self.apply_history is not None:
            for k1 in self.apply_history:
                result['ApplyHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_history = []
        if m.get('ApplyHistory') is not None:
            for k1 in m.get('ApplyHistory'):
                temp_model = main_models.DescribeMetricRuleTemplateListResponseBodyTemplatesTemplateApplyHistoriesApplyHistory()
                self.apply_history.append(temp_model.from_map(k1))

        return self

class DescribeMetricRuleTemplateListResponseBodyTemplatesTemplateApplyHistoriesApplyHistory(DaraModel):
    def __init__(
        self,
        apply_time: int = None,
        group_id: int = None,
        group_name: str = None,
    ):
        # The timestamp when the alert template was applied to the application group.
        # 
        # Unit: milliseconds.
        self.apply_time = apply_time
        # The ID of the application group.
        self.group_id = group_id
        # The name of the application group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

