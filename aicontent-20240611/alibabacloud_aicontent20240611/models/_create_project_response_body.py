# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class CreateProjectResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateProjectResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateProjectResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateProjectResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        project_apps: List[main_models.CreateProjectResponseBodyDataProjectApps] = None,
        project_id: str = None,
        project_name: str = None,
        project_sdk: List[main_models.CreateProjectResponseBodyDataProjectSDK] = None,
        project_type: str = None,
    ):
        self.create_time = create_time
        self.project_apps = project_apps
        self.project_id = project_id
        self.project_name = project_name
        self.project_sdk = project_sdk
        self.project_type = project_type

    def validate(self):
        if self.project_apps:
            for v1 in self.project_apps:
                 if v1:
                    v1.validate()
        if self.project_sdk:
            for v1 in self.project_sdk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['ProjectApps'] = []
        if self.project_apps is not None:
            for k1 in self.project_apps:
                result['ProjectApps'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        result['ProjectSDK'] = []
        if self.project_sdk is not None:
            for k1 in self.project_sdk:
                result['ProjectSDK'].append(k1.to_map() if k1 else None)

        if self.project_type is not None:
            result['ProjectType'] = self.project_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.project_apps = []
        if m.get('ProjectApps') is not None:
            for k1 in m.get('ProjectApps'):
                temp_model = main_models.CreateProjectResponseBodyDataProjectApps()
                self.project_apps.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        self.project_sdk = []
        if m.get('ProjectSDK') is not None:
            for k1 in m.get('ProjectSDK'):
                temp_model = main_models.CreateProjectResponseBodyDataProjectSDK()
                self.project_sdk.append(temp_model.from_map(k1))

        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')

        return self

class CreateProjectResponseBodyDataProjectSDK(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        demo_url: str = None,
        deploy_mode: str = None,
        develop_language: str = None,
        doc_url: str = None,
        sdk_name: str = None,
        sdk_url: str = None,
        sdk_version: str = None,
    ):
        self.create_time = create_time
        self.demo_url = demo_url
        self.deploy_mode = deploy_mode
        self.develop_language = develop_language
        self.doc_url = doc_url
        self.sdk_name = sdk_name
        self.sdk_url = sdk_url
        self.sdk_version = sdk_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.demo_url is not None:
            result['DemoUrl'] = self.demo_url

        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.develop_language is not None:
            result['DevelopLanguage'] = self.develop_language

        if self.doc_url is not None:
            result['DocUrl'] = self.doc_url

        if self.sdk_name is not None:
            result['SdkName'] = self.sdk_name

        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url

        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DemoUrl') is not None:
            self.demo_url = m.get('DemoUrl')

        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('DevelopLanguage') is not None:
            self.develop_language = m.get('DevelopLanguage')

        if m.get('DocUrl') is not None:
            self.doc_url = m.get('DocUrl')

        if m.get('SdkName') is not None:
            self.sdk_name = m.get('SdkName')

        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')

        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')

        return self

class CreateProjectResponseBodyDataProjectApps(DaraModel):
    def __init__(
        self,
        application_access_ids: List[main_models.CreateProjectResponseBodyDataProjectAppsApplicationAccessIds] = None,
        id: str = None,
        project_id: str = None,
    ):
        self.application_access_ids = application_access_ids
        self.id = id
        self.project_id = project_id

    def validate(self):
        if self.application_access_ids:
            for v1 in self.application_access_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationAccessIds'] = []
        if self.application_access_ids is not None:
            for k1 in self.application_access_ids:
                result['ApplicationAccessIds'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_access_ids = []
        if m.get('ApplicationAccessIds') is not None:
            for k1 in m.get('ApplicationAccessIds'):
                temp_model = main_models.CreateProjectResponseBodyDataProjectAppsApplicationAccessIds()
                self.application_access_ids.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class CreateProjectResponseBodyDataProjectAppsApplicationAccessIds(DaraModel):
    def __init__(
        self,
        application_access_id: str = None,
        application_access_secret: str = None,
    ):
        self.application_access_id = application_access_id
        self.application_access_secret = application_access_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id

        if self.application_access_secret is not None:
            result['applicationAccessSecret'] = self.application_access_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')

        if m.get('applicationAccessSecret') is not None:
            self.application_access_secret = m.get('applicationAccessSecret')

        return self

