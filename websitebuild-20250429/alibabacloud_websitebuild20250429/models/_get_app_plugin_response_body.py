# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetAppPluginResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.GetAppPluginResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason why access was denied.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retries are allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace the `%s` in the **ErrMessage** response parameter.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The error parameters returned.
        self.error_args = error_args
        # The application module.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The exception message.
        self.root_error_msg = root_error_msg
        # A reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.GetAppPluginResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class GetAppPluginResponseBodyModule(DaraModel):
    def __init__(
        self,
        category: str = None,
        config_items: str = None,
        created_by: str = None,
        description: str = None,
        display: int = None,
        enabled: int = None,
        extend: str = None,
        git_ref: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hooks: str = None,
        hot_count: int = None,
        icon: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        repository_url: str = None,
        skill_header: str = None,
        status: str = None,
        tags: str = None,
        version: str = None,
        visibility: str = None,
    ):
        # The category.
        self.category = category
        # The configuration form in React JSON Schema format.
        self.config_items = config_items
        # The creator.
        self.created_by = created_by
        # The application description.
        self.description = description
        # The image display mode. Valid values:
        # 
        # - **0** (None): Not displayed.
        # - **1** (Always): Always displayed.
        self.display = display
        # Specifies whether scheduled delivery of resource snapshots is enabled.
        # 
        # Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.enabled = enabled
        # The extended information.
        self.extend = extend
        # The version number.
        self.git_ref = git_ref
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The hook definitions.
        self.hooks = hooks
        # The popularity count.
        self.hot_count = hot_count
        # The plug-in description.
        self.icon = icon
        # The bound API Gateway plug-in ID.
        self.plugin_id = plugin_id
        # The plug-in name. The name can contain uppercase and lowercase letters, Chinese characters, digits, and underscores (_). The name must be 4 to 50 characters in length and cannot start with an underscore.
        self.plugin_name = plugin_name
        # The image repository URL.
        self.repository_url = repository_url
        # The skill header information for model selection.
        self.skill_header = skill_header
        # trial,draft,live,refunded,expired,released
        self.status = status
        # The category tags.
        self.tags = tags
        # The application instance version.
        self.version = version
        # **The visibility level.**
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.config_items is not None:
            result['ConfigItems'] = self.config_items

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.description is not None:
            result['Description'] = self.description

        if self.display is not None:
            result['Display'] = self.display

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.git_ref is not None:
            result['GitRef'] = self.git_ref

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.hooks is not None:
            result['Hooks'] = self.hooks

        if self.hot_count is not None:
            result['HotCount'] = self.hot_count

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.repository_url is not None:
            result['RepositoryUrl'] = self.repository_url

        if self.skill_header is not None:
            result['SkillHeader'] = self.skill_header

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.version is not None:
            result['Version'] = self.version

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConfigItems') is not None:
            self.config_items = m.get('ConfigItems')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('GitRef') is not None:
            self.git_ref = m.get('GitRef')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Hooks') is not None:
            self.hooks = m.get('Hooks')

        if m.get('HotCount') is not None:
            self.hot_count = m.get('HotCount')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('RepositoryUrl') is not None:
            self.repository_url = m.get('RepositoryUrl')

        if m.get('SkillHeader') is not None:
            self.skill_header = m.get('SkillHeader')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

