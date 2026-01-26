# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRetcodeAppByPidResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_app: main_models.GetRetcodeAppByPidResponseBodyRetcodeApp = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned application data.
        self.retcode_app = retcode_app

    def validate(self):
        if self.retcode_app:
            self.retcode_app.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retcode_app is not None:
            result['RetcodeApp'] = self.retcode_app.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetcodeApp') is not None:
            temp_model = main_models.GetRetcodeAppByPidResponseBodyRetcodeApp()
            self.retcode_app = temp_model.from_map(m.get('RetcodeApp'))

        return self

class GetRetcodeAppByPidResponseBodyRetcodeApp(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        pid: str = None,
        resource_group_id: str = None,
        retcode_app_type: str = None,
        tags: List[main_models.GetRetcodeAppByPidResponseBodyRetcodeAppTags] = None,
    ):
        # The ID of the application. The parameter is an auto-increment parameter.
        self.app_id = app_id
        # The name of the application that is monitored by Browser Monitoring.
        self.app_name = app_name
        # The process identifier (PID) of the application.
        self.pid = pid
        # The ID of the resource group. You can obtain the resource group ID in the **Resource Management** console.
        self.resource_group_id = resource_group_id
        # The type of the application that is monitored by Browser Monitoring. Valid values:
        # 
        # *   `web`: web application
        # *   `weex`: Weex mobile app
        # *   `mini_dd`: DingTalk mini program
        # *   `mini_alipay`: Alipay mini program
        # *   `mini_wx`: WeChat mini program
        # *   `mini_common`: mini program on other platforms
        self.retcode_app_type = retcode_app_type
        # The tags that are attached to the instance.
        self.tags = tags

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

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetRetcodeAppByPidResponseBodyRetcodeAppTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetRetcodeAppByPidResponseBodyRetcodeAppTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

