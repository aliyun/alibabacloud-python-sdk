# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgQueryDefaultTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DsgQueryDefaultTemplatesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DsgQueryDefaultTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DsgQueryDefaultTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        desens_plan_template: Dict[str, List[main_models.DataDesensPlanTemplateValue]] = None,
    ):
        # The sensitive field type.
        self.data_type = data_type
        # The supported data masking methods and parameter descriptions.
        self.desens_plan_template = desens_plan_template

    def validate(self):
        if self.desens_plan_template:
            for v1 in self.desens_plan_template.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        result['DesensPlanTemplate'] = {}
        if self.desens_plan_template is not None:
            for k1, v1 in self.desens_plan_template.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['DesensPlanTemplate'][k1] = l1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        self.desens_plan_template = {}
        if m.get('DesensPlanTemplate') is not None:
            for k1, v1 in m.get('DesensPlanTemplate').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataDesensPlanTemplateValue()
                    l1.append(temp_model.from_map(k2))
                self.desens_plan_template[k1] = l1

        return self

