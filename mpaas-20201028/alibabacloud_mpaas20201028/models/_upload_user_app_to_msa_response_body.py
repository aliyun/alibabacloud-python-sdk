# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class UploadUserAppToMsaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.UploadUserAppToMsaResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.UploadUserAppToMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class UploadUserAppToMsaResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UploadUserAppToMsaResponseBodyResultContentData = None,
        extra: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.extra = extra
        self.message = message
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

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UploadUserAppToMsaResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UploadUserAppToMsaResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        apk_info: main_models.UploadUserAppToMsaResponseBodyResultContentDataApkInfo = None,
        enhance_task_id: int = None,
        id: int = None,
        progress: int = None,
        status: int = None,
    ):
        self.apk_info = apk_info
        self.enhance_task_id = enhance_task_id
        self.id = id
        self.progress = progress
        self.status = status

    def validate(self):
        if self.apk_info:
            self.apk_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apk_info is not None:
            result['ApkInfo'] = self.apk_info.to_map()

        if self.enhance_task_id is not None:
            result['EnhanceTaskId'] = self.enhance_task_id

        if self.id is not None:
            result['Id'] = self.id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkInfo') is not None:
            temp_model = main_models.UploadUserAppToMsaResponseBodyResultContentDataApkInfo()
            self.apk_info = temp_model.from_map(m.get('ApkInfo'))

        if m.get('EnhanceTaskId') is not None:
            self.enhance_task_id = m.get('EnhanceTaskId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class UploadUserAppToMsaResponseBodyResultContentDataApkInfo(DaraModel):
    def __init__(
        self,
        after_md_5: str = None,
        after_size: int = None,
        app_code: str = None,
        app_package: str = None,
        before_md_5: str = None,
        before_size: int = None,
        class_forest: str = None,
        enhance_mapping: main_models.UploadUserAppToMsaResponseBodyResultContentDataApkInfoEnhanceMapping = None,
        enhance_rules: List[str] = None,
        enhanced_classes: List[str] = None,
        id: int = None,
        label: str = None,
        progress: int = None,
        status: int = None,
        task_type: str = None,
        version_code: str = None,
        version_name: str = None,
    ):
        self.after_md_5 = after_md_5
        self.after_size = after_size
        self.app_code = app_code
        self.app_package = app_package
        self.before_md_5 = before_md_5
        self.before_size = before_size
        self.class_forest = class_forest
        self.enhance_mapping = enhance_mapping
        self.enhance_rules = enhance_rules
        self.enhanced_classes = enhanced_classes
        self.id = id
        self.label = label
        self.progress = progress
        self.status = status
        self.task_type = task_type
        self.version_code = version_code
        self.version_name = version_name

    def validate(self):
        if self.enhance_mapping:
            self.enhance_mapping.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_md_5 is not None:
            result['AfterMd5'] = self.after_md_5

        if self.after_size is not None:
            result['AfterSize'] = self.after_size

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_package is not None:
            result['AppPackage'] = self.app_package

        if self.before_md_5 is not None:
            result['BeforeMd5'] = self.before_md_5

        if self.before_size is not None:
            result['BeforeSize'] = self.before_size

        if self.class_forest is not None:
            result['ClassForest'] = self.class_forest

        if self.enhance_mapping is not None:
            result['EnhanceMapping'] = self.enhance_mapping.to_map()

        if self.enhance_rules is not None:
            result['EnhanceRules'] = self.enhance_rules

        if self.enhanced_classes is not None:
            result['EnhancedClasses'] = self.enhanced_classes

        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterMd5') is not None:
            self.after_md_5 = m.get('AfterMd5')

        if m.get('AfterSize') is not None:
            self.after_size = m.get('AfterSize')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')

        if m.get('BeforeMd5') is not None:
            self.before_md_5 = m.get('BeforeMd5')

        if m.get('BeforeSize') is not None:
            self.before_size = m.get('BeforeSize')

        if m.get('ClassForest') is not None:
            self.class_forest = m.get('ClassForest')

        if m.get('EnhanceMapping') is not None:
            temp_model = main_models.UploadUserAppToMsaResponseBodyResultContentDataApkInfoEnhanceMapping()
            self.enhance_mapping = temp_model.from_map(m.get('EnhanceMapping'))

        if m.get('EnhanceRules') is not None:
            self.enhance_rules = m.get('EnhanceRules')

        if m.get('EnhancedClasses') is not None:
            self.enhanced_classes = m.get('EnhancedClasses')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class UploadUserAppToMsaResponseBodyResultContentDataApkInfoEnhanceMapping(DaraModel):
    def __init__(
        self,
        info: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.info = info
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

