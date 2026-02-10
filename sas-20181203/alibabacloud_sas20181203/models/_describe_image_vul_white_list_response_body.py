# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageVulWhiteListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        image_vul_whitelist: List[main_models.DescribeImageVulWhiteListResponseBodyImageVulWhitelist] = None,
        message: str = None,
        page_info: main_models.DescribeImageVulWhiteListResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        time_cost: int = None,
    ):
        # The status code returned. A value of **200** indicates that the request was successful. Other values indicate that the request failed. You can identify the cause of the failure based on the value of this parameter.
        self.code = code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The information about the whitelist of image vulnerabilities.
        self.image_vul_whitelist = image_vul_whitelist
        # The message returned.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The amount of time that was consumed to process the request. Unit: milliseconds.
        self.time_cost = time_cost

    def validate(self):
        if self.image_vul_whitelist:
            for v1 in self.image_vul_whitelist:
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

        result['ImageVulWhitelist'] = []
        if self.image_vul_whitelist is not None:
            for k1 in self.image_vul_whitelist:
                result['ImageVulWhitelist'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.image_vul_whitelist = []
        if m.get('ImageVulWhitelist') is not None:
            for k1 in m.get('ImageVulWhitelist'):
                temp_model = main_models.DescribeImageVulWhiteListResponseBodyImageVulWhitelist()
                self.image_vul_whitelist.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageVulWhiteListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

class DescribeImageVulWhiteListResponseBodyPageInfo(DaraModel):
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

class DescribeImageVulWhiteListResponseBodyImageVulWhitelist(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        id: int = None,
        name: str = None,
        reason: str = None,
        target: str = None,
        type: str = None,
    ):
        # The alias of the vulnerability that is specified in Common Vulnerabilities and Exposures (CVE).
        self.alias_name = alias_name
        # The primary key ID of the vulnerability.
        self.id = id
        # The name of the vulnerability.
        self.name = name
        # The reason why the vulnerability is added to the whitelist.
        self.reason = reason
        # The object on which the query is performed. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: the object type. The value is fixed to repo.
        # *   **target**: the object content. The value is in the Namespace/Image repository format.
        self.target = target
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: system vulnerability
        # *   **sca**: application vulnerability
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

