# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageBaselineItemListResponseBody(DaraModel):
    def __init__(
        self,
        baseline_item_infos: List[main_models.DescribeImageBaselineItemListResponseBodyBaselineItemInfos] = None,
        page_info: main_models.DescribeImageBaselineItemListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of baseline check items.
        self.baseline_item_infos = baseline_item_infos
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.baseline_item_infos:
            for v1 in self.baseline_item_infos:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaselineItemInfos'] = []
        if self.baseline_item_infos is not None:
            for k1 in self.baseline_item_infos:
                result['BaselineItemInfos'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baseline_item_infos = []
        if m.get('BaselineItemInfos') is not None:
            for k1 in m.get('BaselineItemInfos'):
                temp_model = main_models.DescribeImageBaselineItemListResponseBodyBaselineItemInfos()
                self.baseline_item_infos.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageBaselineItemListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageBaselineItemListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageBaselineItemListResponseBodyBaselineItemInfos(DaraModel):
    def __init__(
        self,
        baseline_class_alias: str = None,
        baseline_class_key: str = None,
        baseline_item_alias: str = None,
        baseline_item_key: str = None,
        baseline_name_alias: str = None,
        baseline_name_key: str = None,
        status: int = None,
        white_list: int = None,
    ):
        # The alias of the baseline type.
        self.baseline_class_alias = baseline_class_alias
        # The key of the baseline type.
        self.baseline_class_key = baseline_class_key
        # The alias of the baseline check item.
        self.baseline_item_alias = baseline_item_alias
        # The key of the baseline check item.
        self.baseline_item_key = baseline_item_key
        # The alias of the baseline.
        self.baseline_name_alias = baseline_name_alias
        # The key of the baseline name.
        self.baseline_name_key = baseline_name_key
        # The status of the baseline risks. Valid values:
        # 
        # *   **0**: unfixed
        # *   **1**: fixed
        # *   **2**: pending verification
        # *   **3**: fixing failed
        self.status = status
        # Indicates whether the baseline check item is added to the whitelist. Valid values:
        # 
        # *   **0**: The baseline check item is not added to the whitelist.
        # *   **1**: The baseline check item is added to the whitelist.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_class_alias is not None:
            result['BaselineClassAlias'] = self.baseline_class_alias

        if self.baseline_class_key is not None:
            result['BaselineClassKey'] = self.baseline_class_key

        if self.baseline_item_alias is not None:
            result['BaselineItemAlias'] = self.baseline_item_alias

        if self.baseline_item_key is not None:
            result['BaselineItemKey'] = self.baseline_item_key

        if self.baseline_name_alias is not None:
            result['BaselineNameAlias'] = self.baseline_name_alias

        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key

        if self.status is not None:
            result['Status'] = self.status

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineClassAlias') is not None:
            self.baseline_class_alias = m.get('BaselineClassAlias')

        if m.get('BaselineClassKey') is not None:
            self.baseline_class_key = m.get('BaselineClassKey')

        if m.get('BaselineItemAlias') is not None:
            self.baseline_item_alias = m.get('BaselineItemAlias')

        if m.get('BaselineItemKey') is not None:
            self.baseline_item_key = m.get('BaselineItemKey')

        if m.get('BaselineNameAlias') is not None:
            self.baseline_name_alias = m.get('BaselineNameAlias')

        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

