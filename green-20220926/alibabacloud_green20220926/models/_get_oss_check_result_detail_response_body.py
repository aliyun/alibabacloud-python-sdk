# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetOssCheckResultDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetOssCheckResultDetailResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code, consistent with HTTP status.
        self.code = code
        # Detailed data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # Backend-assigned ID used to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetOssCheckResultDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOssCheckResultDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        code: str = None,
        content_type: str = None,
        copy_from: str = None,
        freeze_status: str = None,
        freeze_type: str = None,
        image_url: str = None,
        is_copy: bool = None,
        job_name: str = None,
        label_details: List[main_models.GetOssCheckResultDetailResponseBodyDataLabelDetails] = None,
        label_details_2: List[main_models.GetOssCheckResultDetailResponseBodyDataLabelDetails2] = None,
        labels: List[str] = None,
        labels_2: List[str] = None,
        manual_freeze_action: str = None,
        manual_operate_time: str = None,
        manual_operator: str = None,
        md_5: str = None,
        msg: str = None,
        object: str = None,
        risk_level: str = None,
        risk_level_0: str = None,
        risk_level_2: str = None,
        scan_result: str = None,
        scan_service_infos: List[main_models.GetOssCheckResultDetailResponseBodyDataScanServiceInfos] = None,
        service_code: str = None,
        service_name: str = None,
        task_id: str = None,
        url: str = None,
    ):
        # Bucket name.
        self.bucket = bucket
        # Error code, consistent with HTTP status.
        self.code = code
        # Audio and video detection type.
        self.content_type = content_type
        # Primary service.
        self.copy_from = copy_from
        # Freeze status.
        self.freeze_status = freeze_status
        # Freeze type.
        self.freeze_type = freeze_type
        # Image URL.
        self.image_url = image_url
        # Whether to copy.
        self.is_copy = is_copy
        # Job name.
        self.job_name = job_name
        # Labels.
        self.label_details = label_details
        # Labels.
        self.label_details_2 = label_details_2
        # Image labels.
        self.labels = labels
        # Text labels.
        self.labels_2 = labels_2
        # Manual handling status.
        self.manual_freeze_action = manual_freeze_action
        # Handling time.
        self.manual_operate_time = manual_operate_time
        # Handler.
        self.manual_operator = manual_operator
        # File MD5.
        self.md_5 = md_5
        # Further description of the error code.
        self.msg = msg
        # Object name.
        self.object = object
        # Image risk level
        self.risk_level = risk_level
        # Overall risk level.
        self.risk_level_0 = risk_level_0
        # Text risk level
        self.risk_level_2 = risk_level_2
        # Detailed scan results.
        self.scan_result = scan_result
        # Detection service information
        self.scan_service_infos = scan_service_infos
        # Service code.
        self.service_code = service_code
        # Service name.
        self.service_name = service_name
        # Task ID.
        self.task_id = task_id
        # Task URL.
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
        if self.scan_service_infos:
            for v1 in self.scan_service_infos:
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

        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from

        if self.freeze_status is not None:
            result['FreezeStatus'] = self.freeze_status

        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy

        if self.job_name is not None:
            result['JobName'] = self.job_name

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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.object is not None:
            result['Object'] = self.object

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_level_0 is not None:
            result['RiskLevel0'] = self.risk_level_0

        if self.risk_level_2 is not None:
            result['RiskLevel2'] = self.risk_level_2

        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result

        result['ScanServiceInfos'] = []
        if self.scan_service_infos is not None:
            for k1 in self.scan_service_infos:
                result['ScanServiceInfos'].append(k1.to_map() if k1 else None)

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

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

        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')

        if m.get('FreezeStatus') is not None:
            self.freeze_status = m.get('FreezeStatus')

        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        self.label_details = []
        if m.get('LabelDetails') is not None:
            for k1 in m.get('LabelDetails'):
                temp_model = main_models.GetOssCheckResultDetailResponseBodyDataLabelDetails()
                self.label_details.append(temp_model.from_map(k1))

        self.label_details_2 = []
        if m.get('LabelDetails2') is not None:
            for k1 in m.get('LabelDetails2'):
                temp_model = main_models.GetOssCheckResultDetailResponseBodyDataLabelDetails2()
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

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskLevel0') is not None:
            self.risk_level_0 = m.get('RiskLevel0')

        if m.get('RiskLevel2') is not None:
            self.risk_level_2 = m.get('RiskLevel2')

        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')

        self.scan_service_infos = []
        if m.get('ScanServiceInfos') is not None:
            for k1 in m.get('ScanServiceInfos'):
                temp_model = main_models.GetOssCheckResultDetailResponseBodyDataScanServiceInfos()
                self.scan_service_infos.append(temp_model.from_map(k1))

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetOssCheckResultDetailResponseBodyDataScanServiceInfos(DaraModel):
    def __init__(
        self,
        copy_from: str = None,
        is_copy: bool = None,
        service_code: str = None,
        service_name: str = None,
    ):
        # Main service.
        self.copy_from = copy_from
        # Whether to copy.
        self.is_copy = is_copy
        # Service code.
        self.service_code = service_code
        # Service name.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from

        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')

        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class GetOssCheckResultDetailResponseBodyDataLabelDetails2(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # Confidence score, 0 to 100, retained to two decimal places.
        self.confidence = confidence
        # Label description.
        self.description = description
        # Label.
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

class GetOssCheckResultDetailResponseBodyDataLabelDetails(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # Confidence score, 0 to 100, retained to two decimal places.
        self.confidence = confidence
        # Label description.
        self.description = description
        # Label.
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

