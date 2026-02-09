# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMappCenterAppResponseBody(DaraModel):
    def __init__(
        self,
        query_mapp_center_app_result: main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_mapp_center_app_result = query_mapp_center_app_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_mapp_center_app_result:
            self.query_mapp_center_app_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_mapp_center_app_result is not None:
            result['QueryMappCenterAppResult'] = self.query_mapp_center_app_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryMappCenterAppResult') is not None:
            temp_model = main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResult()
            self.query_mapp_center_app_result = temp_model.from_map(m.get('QueryMappCenterAppResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryMappCenterAppResponseBodyQueryMappCenterAppResult(DaraModel):
    def __init__(
        self,
        mapp_center_app: main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterApp = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mapp_center_app = mapp_center_app
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mapp_center_app:
            self.mapp_center_app.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mapp_center_app is not None:
            result['MappCenterApp'] = self.mapp_center_app.to_map()

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MappCenterApp') is not None:
            temp_model = main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterApp()
            self.mapp_center_app = temp_model.from_map(m.get('MappCenterApp'))

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterApp(DaraModel):
    def __init__(
        self,
        android_config: main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppAndroidConfig = None,
        app_desc: str = None,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_secret: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        ios_config: main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppIosConfig = None,
        modifier: str = None,
        monitor_json: str = None,
        status: int = None,
        tenant_id: str = None,
        type: int = None,
    ):
        self.android_config = android_config
        self.app_desc = app_desc
        self.app_icon = app_icon
        self.app_id = app_id
        self.app_name = app_name
        self.app_secret = app_secret
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.ios_config = ios_config
        self.modifier = modifier
        self.monitor_json = monitor_json
        self.status = status
        self.tenant_id = tenant_id
        self.type = type

    def validate(self):
        if self.android_config:
            self.android_config.validate()
        if self.ios_config:
            self.ios_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_config is not None:
            result['AndroidConfig'] = self.android_config.to_map()

        if self.app_desc is not None:
            result['AppDesc'] = self.app_desc

        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.ios_config is not None:
            result['IosConfig'] = self.ios_config.to_map()

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.monitor_json is not None:
            result['MonitorJson'] = self.monitor_json

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidConfig') is not None:
            temp_model = main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppAndroidConfig()
            self.android_config = temp_model.from_map(m.get('AndroidConfig'))

        if m.get('AppDesc') is not None:
            self.app_desc = m.get('AppDesc')

        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IosConfig') is not None:
            temp_model = main_models.QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppIosConfig()
            self.ios_config = temp_model.from_map(m.get('IosConfig'))

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('MonitorJson') is not None:
            self.monitor_json = m.get('MonitorJson')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppIosConfig(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
    ):
        self.bundle_id = bundle_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        return self

class QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppAndroidConfig(DaraModel):
    def __init__(
        self,
        cert_rsa: str = None,
        package_name: str = None,
    ):
        self.cert_rsa = cert_rsa
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_rsa is not None:
            result['CertRSA'] = self.cert_rsa

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertRSA') is not None:
            self.cert_rsa = m.get('CertRSA')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        return self

