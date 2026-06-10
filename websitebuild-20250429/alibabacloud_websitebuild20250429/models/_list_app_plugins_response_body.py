# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppPluginsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: List[main_models.ListAppPluginsResponseBodyModule] = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed
        self.allow_retry = allow_retry
        # Application name. Query the application with this name.
        self.app_name = app_name
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic error message used to replace the `%s` placeholder in the **ErrMessage** error message.  
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the provided request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # Returned error parameters
        self.error_args = error_args
        # Number of results per query.  
        # 
        # Value range: 10 to 100. Default value: 20.
        self.max_results = max_results
        # Returned object.
        self.module = module
        # Token for starting the next query. It is empty if there is no next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Error code
        self.root_error_code = root_error_code
        # Abnormal message
        self.root_error_msg = root_error_msg
        # Reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.ListAppPluginsResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAppPluginsResponseBodyModule(DaraModel):
    def __init__(
        self,
        code: str = None,
        config_items: str = None,
        desc: str = None,
        display: int = None,
        enabled: int = None,
        env: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        hooks: str = None,
        icon: str = None,
        id: int = None,
        is_deleted: int = None,
        name: str = None,
        skill_header: str = None,
        tags: str = None,
    ):
        # plugin code
        self.code = code
        # Configuration form in React JSON Schema format
        self.config_items = config_items
        # plugin Description
        self.desc = desc
        # Image display. Valid values:  
        # 
        # - **0** (None): Do not display.  
        # - **1** (Always): Always display.
        self.display = display
        # Indicates whether scheduled delivery of resource snapshots is enabled.  
        # 
        # Valid values:  
        # - true: Enabled.  
        # - false: Shutdown.
        self.enabled = enabled
        # environment
        self.env = env
        # Creation Time
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Updated At
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified_time = gmt_modified_time
        # hook definitions
        self.hooks = hooks
        # plugin Description
        self.icon = icon
        # primary key
        self.id = id
        # Indicates whether the item has been deleted: 0—No, 1—Yes
        self.is_deleted = is_deleted
        # plugin Name
        self.name = name
        # skill header, used by the model for selection
        self.skill_header = skill_header
        # Categorization label
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.config_items is not None:
            result['ConfigItems'] = self.config_items

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.display is not None:
            result['Display'] = self.display

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.env is not None:
            result['Env'] = self.env

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.hooks is not None:
            result['Hooks'] = self.hooks

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_header is not None:
            result['SkillHeader'] = self.skill_header

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConfigItems') is not None:
            self.config_items = m.get('ConfigItems')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Hooks') is not None:
            self.hooks = m.get('Hooks')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillHeader') is not None:
            self.skill_header = m.get('SkillHeader')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

