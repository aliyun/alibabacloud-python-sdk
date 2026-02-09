# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListMcubeWhitelistsResponseBody(DaraModel):
    def __init__(
        self,
        list_whitelist_result: main_models.ListMcubeWhitelistsResponseBodyListWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_whitelist_result = list_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_whitelist_result:
            self.list_whitelist_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_whitelist_result is not None:
            result['ListWhitelistResult'] = self.list_whitelist_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListWhitelistResult') is not None:
            temp_model = main_models.ListMcubeWhitelistsResponseBodyListWhitelistResult()
            self.list_whitelist_result = temp_model.from_map(m.get('ListWhitelistResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class ListMcubeWhitelistsResponseBodyListWhitelistResult(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        page_size: int = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
        whitelists: List[main_models.ListMcubeWhitelistsResponseBodyListWhitelistResultWhitelists] = None,
    ):
        self.current_page = current_page
        self.has_more = has_more
        self.page_size = page_size
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count
        self.whitelists = whitelists

    def validate(self):
        if self.whitelists:
            for v1 in self.whitelists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Whitelists'] = []
        if self.whitelists is not None:
            for k1 in self.whitelists:
                result['Whitelists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k1 in m.get('Whitelists'):
                temp_model = main_models.ListMcubeWhitelistsResponseBodyListWhitelistResultWhitelists()
                self.whitelists.append(temp_model.from_map(k1))

        return self

class ListMcubeWhitelistsResponseBodyListWhitelistResultWhitelists(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        white_list_count: int = None,
        white_list_name: str = None,
        whitelist_type: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.white_list_count = white_list_count
        self.white_list_name = white_list_name
        self.whitelist_type = whitelist_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.white_list_count is not None:
            result['WhiteListCount'] = self.white_list_count

        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name

        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('WhiteListCount') is not None:
            self.white_list_count = m.get('WhiteListCount')

        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')

        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')

        return self

