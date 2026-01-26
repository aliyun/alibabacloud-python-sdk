# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchRetcodeAppByPageResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.SearchRetcodeAppByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned page information.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.SearchRetcodeAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchRetcodeAppByPageResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        retcode_apps: List[main_models.SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The browser monitoring tasks that are returned.
        self.retcode_apps = retcode_apps
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.retcode_apps:
            for v1 in self.retcode_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k1 in self.retcode_apps:
                result['RetcodeApps'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k1 in m.get('RetcodeApps'):
                temp_model = main_models.SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        nick_name: str = None,
        pid: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        retcode_app_type: str = None,
        tags: List[main_models.SearchRetcodeAppByPageResponseBodyPageBeanRetcodeAppsTags] = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The ID of the application. The parameter is an auto-increment parameter.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The time when the task was created.
        self.create_time = create_time
        # The alias of the application.
        self.nick_name = nick_name
        # The process identifier (PID) of the application.
        self.pid = pid
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of the application. Valid values:
        # 
        # *   `web`: web application
        # *   `weex`: Weex mobile app
        # *   `mini_dd`: DingTalk mini program
        # *   `mini_alipay`: Alipay mini program
        # *   `mini_wx`: WeChat mini program
        # *   `mini_common`: mini program on other platforms
        self.retcode_app_type = retcode_app_type
        # The tag.
        self.tags = tags
        # The type of the monitoring task. Valid values:
        # 
        # *   `TRACE`: Application Monitoring
        # *   `RETCODE`: Browser Monitoring
        self.type = type
        # The time when the task was updated.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.SearchRetcodeAppByPageResponseBodyPageBeanRetcodeAppsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class SearchRetcodeAppByPageResponseBodyPageBeanRetcodeAppsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

