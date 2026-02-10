# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListVulAutoRepairConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_info: main_models.ListVulAutoRepairConfigResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        vul_auto_repair_config_list: List[main_models.ListVulAutoRepairConfigResponseBodyVulAutoRepairConfigList] = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # An array consisting of the existing configurations of vulnerabilities that can be automatically fixed.
        self.vul_auto_repair_config_list = vul_auto_repair_config_list

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.vul_auto_repair_config_list:
            for v1 in self.vul_auto_repair_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['VulAutoRepairConfigList'] = []
        if self.vul_auto_repair_config_list is not None:
            for k1 in self.vul_auto_repair_config_list:
                result['VulAutoRepairConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListVulAutoRepairConfigResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.vul_auto_repair_config_list = []
        if m.get('VulAutoRepairConfigList') is not None:
            for k1 in m.get('VulAutoRepairConfigList'):
                temp_model = main_models.ListVulAutoRepairConfigResponseBodyVulAutoRepairConfigList()
                self.vul_auto_repair_config_list.append(temp_model.from_map(k1))

        return self

class ListVulAutoRepairConfigResponseBodyVulAutoRepairConfigList(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        id: int = None,
        name: str = None,
        reason: str = None,
        type: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The configuration ID of the vulnerability.
        self.id = id
        # The name of the vulnerability.
        self.name = name
        # The reason why the vulnerability can be automatically fixed.
        self.reason = reason
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: Linux software vulnerability
        # *   **sys**: Windows system vulnerability
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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListVulAutoRepairConfigResponseBodyPageInfo(DaraModel):
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
        # The number of entries returned per page. Default value: **10**.
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

