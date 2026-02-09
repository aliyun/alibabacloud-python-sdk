# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetMdsMiniConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.GetMdsMiniConfigResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.GetMdsMiniConfigResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class GetMdsMiniConfigResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.GetMdsMiniConfigResponseBodyResultContentData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMdsMiniConfigResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMdsMiniConfigResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        content: main_models.GetMdsMiniConfigResponseBodyResultContentDataContent = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.GetMdsMiniConfigResponseBodyResultContentDataContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMdsMiniConfigResponseBodyResultContentDataContent(DaraModel):
    def __init__(
        self,
        api_config_list: List[main_models.GetMdsMiniConfigResponseBodyResultContentDataContentApiConfigList] = None,
        app_code: str = None,
        enable_server_domain_count: str = None,
        h_5id: str = None,
        h_5name: str = None,
        privilege_switch: main_models.GetMdsMiniConfigResponseBodyResultContentDataContentPrivilegeSwitch = None,
        server_domain_config_list: List[main_models.GetMdsMiniConfigResponseBodyResultContentDataContentServerDomainConfigList] = None,
        webview_domain_config_list: List[main_models.GetMdsMiniConfigResponseBodyResultContentDataContentWebviewDomainConfigList] = None,
    ):
        self.api_config_list = api_config_list
        self.app_code = app_code
        self.enable_server_domain_count = enable_server_domain_count
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.privilege_switch = privilege_switch
        self.server_domain_config_list = server_domain_config_list
        self.webview_domain_config_list = webview_domain_config_list

    def validate(self):
        if self.api_config_list:
            for v1 in self.api_config_list:
                 if v1:
                    v1.validate()
        if self.privilege_switch:
            self.privilege_switch.validate()
        if self.server_domain_config_list:
            for v1 in self.server_domain_config_list:
                 if v1:
                    v1.validate()
        if self.webview_domain_config_list:
            for v1 in self.webview_domain_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiConfigList'] = []
        if self.api_config_list is not None:
            for k1 in self.api_config_list:
                result['ApiConfigList'].append(k1.to_map() if k1 else None)

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.enable_server_domain_count is not None:
            result['EnableServerDomainCount'] = self.enable_server_domain_count

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.privilege_switch is not None:
            result['PrivilegeSwitch'] = self.privilege_switch.to_map()

        result['ServerDomainConfigList'] = []
        if self.server_domain_config_list is not None:
            for k1 in self.server_domain_config_list:
                result['ServerDomainConfigList'].append(k1.to_map() if k1 else None)

        result['WebviewDomainConfigList'] = []
        if self.webview_domain_config_list is not None:
            for k1 in self.webview_domain_config_list:
                result['WebviewDomainConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_config_list = []
        if m.get('ApiConfigList') is not None:
            for k1 in m.get('ApiConfigList'):
                temp_model = main_models.GetMdsMiniConfigResponseBodyResultContentDataContentApiConfigList()
                self.api_config_list.append(temp_model.from_map(k1))

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('EnableServerDomainCount') is not None:
            self.enable_server_domain_count = m.get('EnableServerDomainCount')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('PrivilegeSwitch') is not None:
            temp_model = main_models.GetMdsMiniConfigResponseBodyResultContentDataContentPrivilegeSwitch()
            self.privilege_switch = temp_model.from_map(m.get('PrivilegeSwitch'))

        self.server_domain_config_list = []
        if m.get('ServerDomainConfigList') is not None:
            for k1 in m.get('ServerDomainConfigList'):
                temp_model = main_models.GetMdsMiniConfigResponseBodyResultContentDataContentServerDomainConfigList()
                self.server_domain_config_list.append(temp_model.from_map(k1))

        self.webview_domain_config_list = []
        if m.get('WebviewDomainConfigList') is not None:
            for k1 in m.get('WebviewDomainConfigList'):
                temp_model = main_models.GetMdsMiniConfigResponseBodyResultContentDataContentWebviewDomainConfigList()
                self.webview_domain_config_list.append(temp_model.from_map(k1))

        return self

class GetMdsMiniConfigResponseBodyResultContentDataContentWebviewDomainConfigList(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class GetMdsMiniConfigResponseBodyResultContentDataContentServerDomainConfigList(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class GetMdsMiniConfigResponseBodyResultContentDataContentPrivilegeSwitch(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class GetMdsMiniConfigResponseBodyResultContentDataContentApiConfigList(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

