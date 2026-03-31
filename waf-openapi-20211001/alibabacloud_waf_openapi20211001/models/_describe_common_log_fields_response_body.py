# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeCommonLogFieldsResponseBody(DaraModel):
    def __init__(
        self,
        log_field_list: List[main_models.DescribeCommonLogFieldsResponseBodyLogFieldList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.log_field_list = log_field_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.log_field_list:
            for v1 in self.log_field_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogFieldList'] = []
        if self.log_field_list is not None:
            for k1 in self.log_field_list:
                result['LogFieldList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_field_list = []
        if m.get('LogFieldList') is not None:
            for k1 in m.get('LogFieldList'):
                temp_model = main_models.DescribeCommonLogFieldsResponseBodyLogFieldList()
                self.log_field_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCommonLogFieldsResponseBodyLogFieldList(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        is_required: bool = None,
        log_key: str = None,
        status: bool = None,
    ):
        self.is_default = is_default
        self.is_required = is_required
        self.log_key = log_key
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.is_required is not None:
            result['IsRequired'] = self.is_required

        if self.log_key is not None:
            result['LogKey'] = self.log_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IsRequired') is not None:
            self.is_required = m.get('IsRequired')

        if m.get('LogKey') is not None:
            self.log_key = m.get('LogKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

