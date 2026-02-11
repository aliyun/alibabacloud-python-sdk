# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListAllProdsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListAllProdsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListAllProdsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAllProdsResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        prod_list: List[main_models.ListAllProdsResponseBodyDataProdList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The cloud services.
        self.prod_list = prod_list
        # The total number of logs.
        self.total_count = total_count

    def validate(self):
        if self.prod_list:
            for v1 in self.prod_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ProdList'] = []
        if self.prod_list is not None:
            for k1 in self.prod_list:
                result['ProdList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.prod_list = []
        if m.get('ProdList') is not None:
            for k1 in m.get('ProdList'):
                temp_model = main_models.ListAllProdsResponseBodyDataProdList()
                self.prod_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAllProdsResponseBodyDataProdList(DaraModel):
    def __init__(
        self,
        cloud_code: str = None,
        imported_log_count: int = None,
        modify_time: str = None,
        prod_code: str = None,
        total_log_count: int = None,
    ):
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud.
        # *   aliyun: Alibaba Cloud.
        # *   hcloud: Huawei Cloud.
        self.cloud_code = cloud_code
        # The number of logs within the cloud service that are added to the threat analysis feature.
        self.imported_log_count = imported_log_count
        # The time when the logs within the cloud service were last added to the threat analysis feature.
        self.modify_time = modify_time
        # The code of the cloud service.
        self.prod_code = prod_code
        # The total number of logs within the cloud service.
        self.total_log_count = total_log_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.imported_log_count is not None:
            result['ImportedLogCount'] = self.imported_log_count

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.total_log_count is not None:
            result['TotalLogCount'] = self.total_log_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('ImportedLogCount') is not None:
            self.imported_log_count = m.get('ImportedLogCount')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('TotalLogCount') is not None:
            self.total_log_count = m.get('TotalLogCount')

        return self

