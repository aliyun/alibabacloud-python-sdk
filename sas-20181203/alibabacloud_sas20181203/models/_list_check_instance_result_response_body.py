# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckInstanceResultResponseBody(DaraModel):
    def __init__(
        self,
        basic_data: List[main_models.ListCheckInstanceResultResponseBodyBasicData] = None,
        checks: List[Dict[str, Any]] = None,
        columns: List[main_models.ListCheckInstanceResultResponseBodyColumns] = None,
        page_info: main_models.ListCheckInstanceResultResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The basic information about the affected instances.
        self.basic_data = basic_data
        # The extended information about the instances.
        self.checks = checks
        # The metadata information about the search conditions that can be used to filter instances.
        self.columns = columns
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.basic_data:
            for v1 in self.basic_data:
                 if v1:
                    v1.validate()
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BasicData'] = []
        if self.basic_data is not None:
            for k1 in self.basic_data:
                result['BasicData'].append(k1.to_map() if k1 else None)

        if self.checks is not None:
            result['Checks'] = self.checks

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.basic_data = []
        if m.get('BasicData') is not None:
            for k1 in m.get('BasicData'):
                temp_model = main_models.ListCheckInstanceResultResponseBodyBasicData()
                self.basic_data.append(temp_model.from_map(k1))

        if m.get('Checks') is not None:
            self.checks = m.get('Checks')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.ListCheckInstanceResultResponseBodyColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCheckInstanceResultResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCheckInstanceResultResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: str = None,
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

class ListCheckInstanceResultResponseBodyColumns(DaraModel):
    def __init__(
        self,
        grids: List[main_models.ListCheckInstanceResultResponseBodyColumnsGrids] = None,
        key: str = None,
        search: bool = None,
        search_key: str = None,
        show_name: str = None,
        type: str = None,
    ):
        # The metadata information about the details of the instance.
        self.grids = grids
        # The search condition.
        self.key = key
        # Indicates whether the search condition is used. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.search = search
        # The search key.
        self.search_key = search_key
        # The display name of the search condition.
        self.show_name = show_name
        # The type of the check result for the instance. Valid values:
        # 
        # *   **text**
        # *   **link**
        self.type = type

    def validate(self):
        if self.grids:
            for v1 in self.grids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Grids'] = []
        if self.grids is not None:
            for k1 in self.grids:
                result['Grids'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['Key'] = self.key

        if self.search is not None:
            result['Search'] = self.search

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grids = []
        if m.get('Grids') is not None:
            for k1 in m.get('Grids'):
                temp_model = main_models.ListCheckInstanceResultResponseBodyColumnsGrids()
                self.grids.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListCheckInstanceResultResponseBodyColumnsGrids(DaraModel):
    def __init__(
        self,
        key: str = None,
        show_name: str = None,
        type: str = None,
    ):
        # The search condition.
        self.key = key
        # The display name of the search condition.
        self.show_name = show_name
        # The format of the check result for the instance. Valid values:
        # 
        # *   **text**
        # *   **link**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListCheckInstanceResultResponseBodyBasicData(DaraModel):
    def __init__(
        self,
        id: int = None,
        instance_id: str = None,
        instance_info: main_models.ListCheckInstanceResultResponseBodyBasicDataInstanceInfo = None,
        instance_name: str = None,
        region_id: str = None,
        status: str = None,
        status_message: str = None,
        vendor_user_name: str = None,
    ):
        # The ID of the check result for the instance.
        self.id = id
        # The instance ID of the server.
        self.instance_id = instance_id
        # The information about the instance on which the check item is used.
        self.instance_info = instance_info
        # The instance name of the server.
        self.instance_name = instance_name
        # The region ID of the instance.
        self.region_id = region_id
        # The states of check items. Multiple states are separated with commas (,). Valid values:
        # 
        # *   **PASS**: passed
        # *   **NOT_PASS**: failed
        # *   **CHECKING**: being checked
        # *   **NOT_CHECK**: not checked
        # *   **WHITELIST**: added to the whitelist
        self.status = status
        # The exception message of the check item.
        self.status_message = status_message
        # The multi-cloud provider account name.
        self.vendor_user_name = vendor_user_name

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.vendor_user_name is not None:
            result['VendorUserName'] = self.vendor_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceInfo') is not None:
            temp_model = main_models.ListCheckInstanceResultResponseBodyBasicDataInstanceInfo()
            self.instance_info = temp_model.from_map(m.get('InstanceInfo'))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('VendorUserName') is not None:
            self.vendor_user_name = m.get('VendorUserName')

        return self

class ListCheckInstanceResultResponseBodyBasicDataInstanceInfo(DaraModel):
    def __init__(
        self,
        config: List[main_models.ListCheckInstanceResultResponseBodyBasicDataInstanceInfoConfig] = None,
        first_update_time: int = None,
        last_update_time: int = None,
    ):
        # The information about the configuration item whose risks are fixed for the instance.
        self.config = config
        # The time of the first check.
        self.first_update_time = first_update_time
        # The time of the last check.
        self.last_update_time = last_update_time

    def validate(self):
        if self.config:
            for v1 in self.config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Config'] = []
        if self.config is not None:
            for k1 in self.config:
                result['Config'].append(k1.to_map() if k1 else None)

        if self.first_update_time is not None:
            result['FirstUpdateTime'] = self.first_update_time

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k1 in m.get('Config'):
                temp_model = main_models.ListCheckInstanceResultResponseBodyBasicDataInstanceInfoConfig()
                self.config.append(temp_model.from_map(k1))

        if m.get('FirstUpdateTime') is not None:
            self.first_update_time = m.get('FirstUpdateTime')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        return self

class ListCheckInstanceResultResponseBodyBasicDataInstanceInfoConfig(DaraModel):
    def __init__(
        self,
        name: str = None,
        show_name: str = None,
        value: str = None,
    ):
        # The name of the configuration item, which is unique.
        self.name = name
        # The display name of the configuration item for internationalization.
        self.show_name = show_name
        # The value of the configuration item specified for the instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

