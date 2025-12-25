# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListAuditContentErrorTypesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAuditContentErrorTypesResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAuditContentErrorTypesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuditContentErrorTypesResponseBodyData(DaraModel):
    def __init__(
        self,
        major_class_code: str = None,
        major_class_name: str = None,
        sub_classes: List[main_models.ListAuditContentErrorTypesResponseBodyDataSubClasses] = None,
    ):
        self.major_class_code = major_class_code
        self.major_class_name = major_class_name
        self.sub_classes = sub_classes

    def validate(self):
        if self.sub_classes:
            for v1 in self.sub_classes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.major_class_code is not None:
            result['MajorClassCode'] = self.major_class_code

        if self.major_class_name is not None:
            result['MajorClassName'] = self.major_class_name

        result['SubClasses'] = []
        if self.sub_classes is not None:
            for k1 in self.sub_classes:
                result['SubClasses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MajorClassCode') is not None:
            self.major_class_code = m.get('MajorClassCode')

        if m.get('MajorClassName') is not None:
            self.major_class_name = m.get('MajorClassName')

        self.sub_classes = []
        if m.get('SubClasses') is not None:
            for k1 in m.get('SubClasses'):
                temp_model = main_models.ListAuditContentErrorTypesResponseBodyDataSubClasses()
                self.sub_classes.append(temp_model.from_map(k1))

        return self

class ListAuditContentErrorTypesResponseBodyDataSubClasses(DaraModel):
    def __init__(
        self,
        class_code: str = None,
        class_name: str = None,
    ):
        self.class_code = class_code
        self.class_name = class_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        return self

