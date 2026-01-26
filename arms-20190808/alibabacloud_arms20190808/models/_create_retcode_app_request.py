# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateRetcodeAppRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_group_id: str = None,
        retcode_app_name: str = None,
        retcode_app_type: str = None,
        tags: List[main_models.CreateRetcodeAppRequestTags] = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. You can obtain the resource group ID in the **Resource Management** console.
        self.resource_group_id = resource_group_id
        # The name of the application.
        # 
        # This parameter is required.
        self.retcode_app_name = retcode_app_name
        # The type of the application. Valid values:
        # 
        # *   `web`: web application
        # *   `weex`: Weex mobile app
        # *   `mini_dd`: DingTalk mini program
        # *   `mini_alipay`: Alipay mini program
        # *   `mini_wx`: WeChat mini program
        # *   `mini_common`: mini program on other platforms
        # 
        # This parameter is required.
        self.retcode_app_type = retcode_app_type
        # The tags that you want to add to the task.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name

        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')

        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateRetcodeAppRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateRetcodeAppRequestTags(DaraModel):
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

