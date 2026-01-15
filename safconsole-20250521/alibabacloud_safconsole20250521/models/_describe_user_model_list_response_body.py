# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeUserModelListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        http_status_code: int = None,
        page_size: int = None,
        request_id: str = None,
        result_object: List[main_models.DescribeUserModelListResponseBodyResultObject] = None,
        success: bool = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # `code`
        self.code = code
        self.current_page = current_page
        self.http_status_code = http_status_code
        self.page_size = page_size
        self.request_id = request_id
        self.result_object = result_object
        self.success = success
        self.total_item = total_item
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['ResultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_item is not None:
            result['TotalItem'] = self.total_item

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('ResultObject') is not None:
            for k1 in m.get('ResultObject'):
                temp_model = main_models.DescribeUserModelListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeUserModelListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        customer_module_name: str = None,
        description: str = None,
        feature_template: str = None,
        gmt_modified: int = None,
        id: int = None,
        inner_define_status: str = None,
        inner_module_name: str = None,
        is_allow_iterate: bool = None,
        is_allow_rollback: bool = None,
        iteration_version: int = None,
        root_module_id: int = None,
    ):
        self.auth_type = auth_type
        self.customer_module_name = customer_module_name
        self.description = description
        self.feature_template = feature_template
        self.gmt_modified = gmt_modified
        self.id = id
        self.inner_define_status = inner_define_status
        self.inner_module_name = inner_module_name
        self.is_allow_iterate = is_allow_iterate
        self.is_allow_rollback = is_allow_rollback
        self.iteration_version = iteration_version
        self.root_module_id = root_module_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.customer_module_name is not None:
            result['CustomerModuleName'] = self.customer_module_name

        if self.description is not None:
            result['Description'] = self.description

        if self.feature_template is not None:
            result['FeatureTemplate'] = self.feature_template

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.inner_define_status is not None:
            result['InnerDefineStatus'] = self.inner_define_status

        if self.inner_module_name is not None:
            result['InnerModuleName'] = self.inner_module_name

        if self.is_allow_iterate is not None:
            result['IsAllowIterate'] = self.is_allow_iterate

        if self.is_allow_rollback is not None:
            result['IsAllowRollback'] = self.is_allow_rollback

        if self.iteration_version is not None:
            result['IterationVersion'] = self.iteration_version

        if self.root_module_id is not None:
            result['RootModuleId'] = self.root_module_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('CustomerModuleName') is not None:
            self.customer_module_name = m.get('CustomerModuleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeatureTemplate') is not None:
            self.feature_template = m.get('FeatureTemplate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InnerDefineStatus') is not None:
            self.inner_define_status = m.get('InnerDefineStatus')

        if m.get('InnerModuleName') is not None:
            self.inner_module_name = m.get('InnerModuleName')

        if m.get('IsAllowIterate') is not None:
            self.is_allow_iterate = m.get('IsAllowIterate')

        if m.get('IsAllowRollback') is not None:
            self.is_allow_rollback = m.get('IsAllowRollback')

        if m.get('IterationVersion') is not None:
            self.iteration_version = m.get('IterationVersion')

        if m.get('RootModuleId') is not None:
            self.root_module_id = m.get('RootModuleId')

        return self

