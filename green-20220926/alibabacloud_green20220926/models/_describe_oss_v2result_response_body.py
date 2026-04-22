# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class DescribeOssV2ResultResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeOssV2ResultResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeOssV2ResultResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOssV2ResultResponseBodyItems(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        code: str = None,
        content_type: str = None,
        freeze: bool = None,
        freeze_status: str = None,
        freeze_type: str = None,
        label_details: List[main_models.DescribeOssV2ResultResponseBodyItemsLabelDetails] = None,
        label_details_2: List[main_models.DescribeOssV2ResultResponseBodyItemsLabelDetails2] = None,
        labels: List[str] = None,
        labels_2: List[str] = None,
        manual_freeze_action: str = None,
        manual_operate_time: str = None,
        manual_operator: str = None,
        md_5: str = None,
        object: str = None,
        request_id: str = None,
        risk_level: str = None,
        risk_level_0: str = None,
        risk_level_2: str = None,
        scan_result: str = None,
        service_code: str = None,
        sys_disposal_status: str = None,
        task_id: str = None,
        url: str = None,
    ):
        self.bucket = bucket
        self.code = code
        self.content_type = content_type
        self.freeze = freeze
        self.freeze_status = freeze_status
        self.freeze_type = freeze_type
        self.label_details = label_details
        self.label_details_2 = label_details_2
        self.labels = labels
        self.labels_2 = labels_2
        self.manual_freeze_action = manual_freeze_action
        self.manual_operate_time = manual_operate_time
        self.manual_operator = manual_operator
        self.md_5 = md_5
        self.object = object
        self.request_id = request_id
        self.risk_level = risk_level
        self.risk_level_0 = risk_level_0
        self.risk_level_2 = risk_level_2
        self.scan_result = scan_result
        # Service code。
        self.service_code = service_code
        self.sys_disposal_status = sys_disposal_status
        self.task_id = task_id
        self.url = url

    def validate(self):
        if self.label_details:
            for v1 in self.label_details:
                 if v1:
                    v1.validate()
        if self.label_details_2:
            for v1 in self.label_details_2:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.code is not None:
            result['Code'] = self.code

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.freeze is not None:
            result['Freeze'] = self.freeze

        if self.freeze_status is not None:
            result['FreezeStatus'] = self.freeze_status

        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type

        result['LabelDetails'] = []
        if self.label_details is not None:
            for k1 in self.label_details:
                result['LabelDetails'].append(k1.to_map() if k1 else None)

        result['LabelDetails2'] = []
        if self.label_details_2 is not None:
            for k1 in self.label_details_2:
                result['LabelDetails2'].append(k1.to_map() if k1 else None)

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.labels_2 is not None:
            result['Labels2'] = self.labels_2

        if self.manual_freeze_action is not None:
            result['ManualFreezeAction'] = self.manual_freeze_action

        if self.manual_operate_time is not None:
            result['ManualOperateTime'] = self.manual_operate_time

        if self.manual_operator is not None:
            result['ManualOperator'] = self.manual_operator

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.object is not None:
            result['Object'] = self.object

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_level_0 is not None:
            result['RiskLevel0'] = self.risk_level_0

        if self.risk_level_2 is not None:
            result['RiskLevel2'] = self.risk_level_2

        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.sys_disposal_status is not None:
            result['SysDisposalStatus'] = self.sys_disposal_status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Freeze') is not None:
            self.freeze = m.get('Freeze')

        if m.get('FreezeStatus') is not None:
            self.freeze_status = m.get('FreezeStatus')

        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')

        self.label_details = []
        if m.get('LabelDetails') is not None:
            for k1 in m.get('LabelDetails'):
                temp_model = main_models.DescribeOssV2ResultResponseBodyItemsLabelDetails()
                self.label_details.append(temp_model.from_map(k1))

        self.label_details_2 = []
        if m.get('LabelDetails2') is not None:
            for k1 in m.get('LabelDetails2'):
                temp_model = main_models.DescribeOssV2ResultResponseBodyItemsLabelDetails2()
                self.label_details_2.append(temp_model.from_map(k1))

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Labels2') is not None:
            self.labels_2 = m.get('Labels2')

        if m.get('ManualFreezeAction') is not None:
            self.manual_freeze_action = m.get('ManualFreezeAction')

        if m.get('ManualOperateTime') is not None:
            self.manual_operate_time = m.get('ManualOperateTime')

        if m.get('ManualOperator') is not None:
            self.manual_operator = m.get('ManualOperator')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskLevel0') is not None:
            self.risk_level_0 = m.get('RiskLevel0')

        if m.get('RiskLevel2') is not None:
            self.risk_level_2 = m.get('RiskLevel2')

        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('SysDisposalStatus') is not None:
            self.sys_disposal_status = m.get('SysDisposalStatus')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeOssV2ResultResponseBodyItemsLabelDetails2(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class DescribeOssV2ResultResponseBodyItemsLabelDetails(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

