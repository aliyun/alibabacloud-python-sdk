# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetAppPluginConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.GetAppPluginConfigResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Module') is not None:
            temp_model = main_models.GetAppPluginConfigResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAppPluginConfigResponseBodyModule(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        plugin_config: str = None,
        plugin_desc: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.plugin_config = plugin_config
        self.plugin_desc = plugin_desc
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.plugin_config is not None:
            result['PluginConfig'] = self.plugin_config

        if self.plugin_desc is not None:
            result['PluginDesc'] = self.plugin_desc

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PluginConfig') is not None:
            self.plugin_config = m.get('PluginConfig')

        if m.get('PluginDesc') is not None:
            self.plugin_desc = m.get('PluginDesc')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

