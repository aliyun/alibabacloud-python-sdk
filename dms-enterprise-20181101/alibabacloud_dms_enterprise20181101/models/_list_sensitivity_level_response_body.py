# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSensitivityLevelResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitivity_level_list: List[main_models.ListSensitivityLevelResponseBodySensitivityLevelList] = None,
        success: bool = None,
    ):
        # The status code.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # The sensitivity levels.
        self.sensitivity_level_list = sensitivity_level_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.sensitivity_level_list:
            for v1 in self.sensitivity_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SensitivityLevelList'] = []
        if self.sensitivity_level_list is not None:
            for k1 in self.sensitivity_level_list:
                result['SensitivityLevelList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sensitivity_level_list = []
        if m.get('SensitivityLevelList') is not None:
            for k1 in m.get('SensitivityLevelList'):
                temp_model = main_models.ListSensitivityLevelResponseBodySensitivityLevelList()
                self.sensitivity_level_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSensitivityLevelResponseBodySensitivityLevelList(DaraModel):
    def __init__(
        self,
        is_plain: bool = None,
        name: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        # Indicates whether the fields of the sensitive level are displayed in plaintext.
        self.is_plain = is_plain
        # The name of the sensitive level.
        self.name = name
        # The ID of the classification template.
        self.template_id = template_id
        # The type of the classification template. Valid values:
        # 
        # *   **INNER**: a built-in template.
        # *   **USER_DEFINE**: a custom template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_plain is not None:
            result['IsPlain'] = self.is_plain

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPlain') is not None:
            self.is_plain = m.get('IsPlain')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

