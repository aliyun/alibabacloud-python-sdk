# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListPythonModulesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListPythonModulesRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The paging conditions for the paged query.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListPythonModulesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListPythonModulesRequestListQuery(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        python_module_id: int = None,
        python_version: str = None,
    ):
        # The keyword of the third-party package name.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The ID of the Python third-party package.
        self.python_module_id = python_module_id
        # The Python version. Valid values: PYTHON_2_7, PYTHON_3_7, and PYTHON_3_11.
        self.python_version = python_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.python_module_id is not None:
            result['PythonModuleId'] = self.python_module_id

        if self.python_version is not None:
            result['PythonVersion'] = self.python_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PythonModuleId') is not None:
            self.python_module_id = m.get('PythonModuleId')

        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')

        return self

