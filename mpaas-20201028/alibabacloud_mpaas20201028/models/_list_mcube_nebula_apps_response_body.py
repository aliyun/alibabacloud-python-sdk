# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMcubeNebulaAppsResponseBody(DaraModel):
    def __init__(
        self,
        list_mcube_nebula_apps_result: main_models.ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mcube_nebula_apps_result = list_mcube_nebula_apps_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mcube_nebula_apps_result:
            self.list_mcube_nebula_apps_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_mcube_nebula_apps_result is not None:
            result['ListMcubeNebulaAppsResult'] = self.list_mcube_nebula_apps_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMcubeNebulaAppsResult') is not None:
            temp_model = main_models.ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResult()
            self.list_mcube_nebula_apps_result = temp_model.from_map(m.get('ListMcubeNebulaAppsResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResult(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        error_code: str = None,
        has_more: bool = None,
        nebula_app_infos: List[main_models.ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResultNebulaAppInfos] = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.error_code = error_code
        self.has_more = has_more
        self.nebula_app_infos = nebula_app_infos
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.nebula_app_infos:
            for v1 in self.nebula_app_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['NebulaAppInfos'] = []
        if self.nebula_app_infos is not None:
            for k1 in self.nebula_app_infos:
                result['NebulaAppInfos'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.nebula_app_infos = []
        if m.get('NebulaAppInfos') is not None:
            for k1 in m.get('NebulaAppInfos'):
                temp_model = main_models.ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResultNebulaAppInfos()
                self.nebula_app_infos.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResultNebulaAppInfos(DaraModel):
    def __init__(
        self,
        h_5id: str = None,
        h_5name: str = None,
    ):
        self.h_5id = h_5id
        self.h_5name = h_5name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        return self

