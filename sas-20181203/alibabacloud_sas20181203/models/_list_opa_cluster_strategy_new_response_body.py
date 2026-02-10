# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListOpaClusterStrategyNewResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListOpaClusterStrategyNewResponseBodyList] = None,
        message: str = None,
        page_info: main_models.ListOpaClusterStrategyNewResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The rules.
        self.list = list
        # The message that shows the export task result. The value is fixed as **success**, which indicates that the export task is successful.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListOpaClusterStrategyNewResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListOpaClusterStrategyNewResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListOpaClusterStrategyNewResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
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

class ListOpaClusterStrategyNewResponseBodyList(DaraModel):
    def __init__(
        self,
        action: int = None,
        cluster_count: int = None,
        cluster_id_list: List[str] = None,
        description: str = None,
        image_name: List[str] = None,
        label: List[str] = None,
        malicious_image: bool = None,
        strategy_id: int = None,
        strategy_name: str = None,
        un_scaned_image: bool = None,
    ):
        # The action of the rule. Valid values:
        # 
        # *   **1**: trigger alerts
        # *   **2**: block
        # *   **3**: allow
        self.action = action
        # The number of clusters on which the rule takes effect.
        self.cluster_count = cluster_count
        # The clusters on which the rule takes effect.
        self.cluster_id_list = cluster_id_list
        # The description.
        self.description = description
        # The image names.
        self.image_name = image_name
        # The tags that are added to the container.
        self.label = label
        # Indicates whether the rule supports malicious Internet images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.malicious_image = malicious_image
        # The rule ID.
        self.strategy_id = strategy_id
        # The rule name.
        self.strategy_name = strategy_name
        # Indicates whether the rule supports unscanned images. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.un_scaned_image = un_scaned_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.cluster_id_list is not None:
            result['ClusterIdList'] = self.cluster_id_list

        if self.description is not None:
            result['Description'] = self.description

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.label is not None:
            result['Label'] = self.label

        if self.malicious_image is not None:
            result['MaliciousImage'] = self.malicious_image

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.un_scaned_image is not None:
            result['UnScanedImage'] = self.un_scaned_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('ClusterIdList') is not None:
            self.cluster_id_list = m.get('ClusterIdList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('MaliciousImage') is not None:
            self.malicious_image = m.get('MaliciousImage')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('UnScanedImage') is not None:
            self.un_scaned_image = m.get('UnScanedImage')

        return self

