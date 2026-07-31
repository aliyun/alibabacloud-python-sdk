# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetInspectionReportResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetInspectionReportResponseBodyData] = None,
        markdown_text: str = None,
        request_id: str = None,
        task_id: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        # The result details.
        self.data = data
        # The Markdown text.
        self.markdown_text = markdown_text
        # The request ID.
        self.request_id = request_id
        # The inspection report ID.
        self.task_id = task_id
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.markdown_text is not None:
            result['MarkdownText'] = self.markdown_text

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetInspectionReportResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MarkdownText') is not None:
            self.markdown_text = m.get('MarkdownText')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class GetInspectionReportResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetInspectionReportResponseBodyDataData] = None,
        end_time: str = None,
        engine_type: str = None,
        instance_desc: str = None,
        instance_id: str = None,
        level_summary: main_models.GetInspectionReportResponseBodyDataLevelSummary = None,
        markdown_text: str = None,
        region: str = None,
        start_time: str = None,
    ):
        # The request result.
        self.data = data
        # The inspection end time in the format of YYYY-MM-DDTHH:mm:ssZ.
        self.end_time = end_time
        # The engine type.
        self.engine_type = engine_type
        # The instance description.
        self.instance_desc = instance_desc
        # The instance ID.
        self.instance_id = instance_id
        # The level summary.
        self.level_summary = level_summary
        # The Markdown text.
        # * If the InstanceId parameter is not specified: the reports for all instances in the inspection report are returned, but the MarkdownText field is empty ("").
        # * If the InstanceId parameter is specified: the report for the specified instance is returned, and the MarkdownText field contains the specific content.
        self.markdown_text = markdown_text
        # The region information.
        self.region = region
        # The inspection start time in the format of YYYY-MM-DDTHH:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.level_summary:
            self.level_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_desc is not None:
            result['InstanceDesc'] = self.instance_desc

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.level_summary is not None:
            result['LevelSummary'] = self.level_summary.to_map()

        if self.markdown_text is not None:
            result['MarkdownText'] = self.markdown_text

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetInspectionReportResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceDesc') is not None:
            self.instance_desc = m.get('InstanceDesc')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LevelSummary') is not None:
            temp_model = main_models.GetInspectionReportResponseBodyDataLevelSummary()
            self.level_summary = temp_model.from_map(m.get('LevelSummary'))

        if m.get('MarkdownText') is not None:
            self.markdown_text = m.get('MarkdownText')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetInspectionReportResponseBodyDataLevelSummary(DaraModel):
    def __init__(
        self,
        error: int = None,
        failed: int = None,
        normal: int = None,
        warning: int = None,
    ):
        # The number of error items.
        self.error = error
        # The number of failed items.
        self.failed = failed
        # The number of normal items.
        self.normal = normal
        # The number of warning items.
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.normal is not None:
            result['Normal'] = self.normal

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Normal') is not None:
            self.normal = m.get('Normal')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

class GetInspectionReportResponseBodyDataData(DaraModel):
    def __init__(
        self,
        group: str = None,
        items: List[main_models.GetInspectionReportResponseBodyDataDataItems] = None,
    ):
        # The group ID.
        self.group = group
        # The attached resource names.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetInspectionReportResponseBodyDataDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class GetInspectionReportResponseBodyDataDataItems(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetInspectionReportResponseBodyDataDataItemsData] = None,
        level: str = None,
        message: str = None,
        name: str = None,
    ):
        # The request result.
        self.data = data
        # The alert level.
        self.level = level
        # The result message.
        self.message = message
        # The category name.
        self.name = name

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetInspectionReportResponseBodyDataDataItemsData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetInspectionReportResponseBodyDataDataItemsData(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

