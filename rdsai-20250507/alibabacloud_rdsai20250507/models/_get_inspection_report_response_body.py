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
    ):
        # The details of the result.
        self.data = data
        # The report text in the markdown format.
        self.markdown_text = markdown_text
        # The request ID.
        self.request_id = request_id
        # The inspection report ID.
        self.task_id = task_id

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
        # The returned results.
        self.data = data
        # The end time of the inspection. Specify the time in the YYYY-MM-DDTHH:mm:ssZ format.
        self.end_time = end_time
        # The engine type.
        self.engine_type = engine_type
        # The description of the instance.
        self.instance_desc = instance_desc
        # The instance ID.
        self.instance_id = instance_id
        # The hierarchical summary of the report.
        self.level_summary = level_summary
        # The report text in the markdown format.
        # 
        # *   If the InstanceId parameter is not specified, all content of the inspection report is returned. However, the MarkdownText field is empty.
        # *   If the InstanceId parameter is specified, the content related to the instance is returned in the MarkdownText field.
        self.markdown_text = markdown_text
        # The region where the instance resides.
        self.region = region
        # The start time of the inspection task. Specify the time in the YYYY-MM-DDTHH:mm:ssZ format.
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
        # The number of errors in the report.
        self.error = error
        # The number of failures in the report.
        self.failed = failed
        # The number of normal records in the report.
        self.normal = normal
        # The number of warnings in the report.
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
        # The items in the result.
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
        # The returned results.
        self.data = data
        # The level of the alert.
        self.level = level
        # The response message.
        self.message = message
        # The name of the category.
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

