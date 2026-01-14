# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListNacosConfigsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        configurations: List[main_models.ListNacosConfigsResponseBodyConfigurations] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code returned.
        self.code = code
        # The configurations.
        self.configurations = configurations
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of returned instances.
        self.total_count = total_count

    def validate(self):
        if self.configurations:
            for v1 in self.configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Configurations'] = []
        if self.configurations is not None:
            for k1 in self.configurations:
                result['Configurations'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.configurations = []
        if m.get('Configurations') is not None:
            for k1 in m.get('Configurations'):
                temp_model = main_models.ListNacosConfigsResponseBodyConfigurations()
                self.configurations.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNacosConfigsResponseBodyConfigurations(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        config_tags: str = None,
        data_id: str = None,
        description: str = None,
        group: str = None,
        id: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        self.config_tags = config_tags
        # The ID of the configuration.
        self.data_id = data_id
        self.description = description
        # The ID of the group.
        self.group = group
        # The ID of the application.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.config_tags is not None:
            result['ConfigTags'] = self.config_tags

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.description is not None:
            result['Description'] = self.description

        if self.group is not None:
            result['Group'] = self.group

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ConfigTags') is not None:
            self.config_tags = m.get('ConfigTags')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

