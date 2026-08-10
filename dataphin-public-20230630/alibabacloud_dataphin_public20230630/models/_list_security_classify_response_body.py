# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListSecurityClassifyResponseBody(DaraModel):
    def __init__(
        self,
        classify_list_result: main_models.ListSecurityClassifyResponseBodyClassifyListResult = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of the data classification list.
        self.classify_list_result = classify_list_result
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend error.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.classify_list_result:
            self.classify_list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify_list_result is not None:
            result['ClassifyListResult'] = self.classify_list_result.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassifyListResult') is not None:
            temp_model = main_models.ListSecurityClassifyResponseBodyClassifyListResult()
            self.classify_list_result = temp_model.from_map(m.get('ClassifyListResult'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSecurityClassifyResponseBodyClassifyListResult(DaraModel):
    def __init__(
        self,
        classify_list: List[main_models.ListSecurityClassifyResponseBodyClassifyListResultClassifyList] = None,
        total_count: int = None,
    ):
        # The list of data classifications.
        self.classify_list = classify_list
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.classify_list:
            for v1 in self.classify_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClassifyList'] = []
        if self.classify_list is not None:
            for k1 in self.classify_list:
                result['ClassifyList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.classify_list = []
        if m.get('ClassifyList') is not None:
            for k1 in m.get('ClassifyList'):
                temp_model = main_models.ListSecurityClassifyResponseBodyClassifyListResultClassifyList()
                self.classify_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSecurityClassifyResponseBodyClassifyListResultClassifyList(DaraModel):
    def __init__(
        self,
        catalog_path: str = None,
        description: str = None,
        effective_field_count: int = None,
        id: int = None,
        is_bind_desensitize_rule: bool = None,
        level_id: int = None,
        level_name: str = None,
        name: str = None,
        priority: int = None,
        short_name: str = None,
        status: str = None,
    ):
        # The catalog path of the classification.
        self.catalog_path = catalog_path
        # The classification description.
        self.description = description
        # The number of effective fields.
        self.effective_field_count = effective_field_count
        # The classification ID.
        self.id = id
        # Indicates whether a masking rule is bound.
        self.is_bind_desensitize_rule = is_bind_desensitize_rule
        # The level ID.
        self.level_id = level_id
        # The level name.
        self.level_name = level_name
        # The classification name.
        self.name = name
        # The priority.
        self.priority = priority
        # The short name of the classification.
        self.short_name = short_name
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_path is not None:
            result['CatalogPath'] = self.catalog_path

        if self.description is not None:
            result['Description'] = self.description

        if self.effective_field_count is not None:
            result['EffectiveFieldCount'] = self.effective_field_count

        if self.id is not None:
            result['Id'] = self.id

        if self.is_bind_desensitize_rule is not None:
            result['IsBindDesensitizeRule'] = self.is_bind_desensitize_rule

        if self.level_id is not None:
            result['LevelId'] = self.level_id

        if self.level_name is not None:
            result['LevelName'] = self.level_name

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.short_name is not None:
            result['ShortName'] = self.short_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogPath') is not None:
            self.catalog_path = m.get('CatalogPath')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveFieldCount') is not None:
            self.effective_field_count = m.get('EffectiveFieldCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsBindDesensitizeRule') is not None:
            self.is_bind_desensitize_rule = m.get('IsBindDesensitizeRule')

        if m.get('LevelId') is not None:
            self.level_id = m.get('LevelId')

        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

