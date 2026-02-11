# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeLogFieldsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.DescribeLogFieldsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeLogFieldsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeLogFieldsResponseBodyData(DaraModel):
    def __init__(
        self,
        activity_name: str = None,
        field_desc: str = None,
        field_name: str = None,
        field_type: str = None,
        log_code: str = None,
    ):
        # The type of the log to which the field belongs.
        self.activity_name = activity_name
        # The internal code of the field description.
        self.field_desc = field_desc
        # The name of the field.
        self.field_name = field_name
        # The data type of the field. Valid values:
        # 
        # *   varchar
        # *   bigint
        self.field_type = field_type
        # The log source to which the field belongs.
        self.log_code = log_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.field_desc is not None:
            result['FieldDesc'] = self.field_desc

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('FieldDesc') is not None:
            self.field_desc = m.get('FieldDesc')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        return self

