# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs_workbench20220220 import models as main_models
from darabonba.model import DaraModel

class LoginInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        root: main_models.LoginInstanceResponseBodyRoot = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.LoginInstanceResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class LoginInstanceResponseBodyRoot(DaraModel):
    def __init__(
        self,
        disposable_account: main_models.LoginInstanceResponseBodyRootDisposableAccount = None,
        instance_login_info_list: List[main_models.LoginInstanceResponseBodyRootInstanceLoginInfoList] = None,
        session_control: main_models.LoginInstanceResponseBodyRootSessionControl = None,
    ):
        self.disposable_account = disposable_account
        self.instance_login_info_list = instance_login_info_list
        self.session_control = session_control

    def validate(self):
        if self.disposable_account:
            self.disposable_account.validate()
        if self.instance_login_info_list:
            for v1 in self.instance_login_info_list:
                 if v1:
                    v1.validate()
        if self.session_control:
            self.session_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disposable_account is not None:
            result['DisposableAccount'] = self.disposable_account.to_map()

        result['InstanceLoginInfoList'] = []
        if self.instance_login_info_list is not None:
            for k1 in self.instance_login_info_list:
                result['InstanceLoginInfoList'].append(k1.to_map() if k1 else None)

        if self.session_control is not None:
            result['SessionControl'] = self.session_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisposableAccount') is not None:
            temp_model = main_models.LoginInstanceResponseBodyRootDisposableAccount()
            self.disposable_account = temp_model.from_map(m.get('DisposableAccount'))

        self.instance_login_info_list = []
        if m.get('InstanceLoginInfoList') is not None:
            for k1 in m.get('InstanceLoginInfoList'):
                temp_model = main_models.LoginInstanceResponseBodyRootInstanceLoginInfoList()
                self.instance_login_info_list.append(temp_model.from_map(k1))

        if m.get('SessionControl') is not None:
            temp_model = main_models.LoginInstanceResponseBodyRootSessionControl()
            self.session_control = temp_model.from_map(m.get('SessionControl'))

        return self

class LoginInstanceResponseBodyRootSessionControl(DaraModel):
    def __init__(
        self,
        base_url: str = None,
    ):
        self.base_url = base_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        return self

class LoginInstanceResponseBodyRootInstanceLoginInfoList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_login_token: str = None,
        instance_login_view: main_models.LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView = None,
        login_success: bool = None,
    ):
        self.instance_id = instance_id
        self.instance_login_token = instance_login_token
        self.instance_login_view = instance_login_view
        self.login_success = login_success

    def validate(self):
        if self.instance_login_view:
            self.instance_login_view.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_login_token is not None:
            result['InstanceLoginToken'] = self.instance_login_token

        if self.instance_login_view is not None:
            result['InstanceLoginView'] = self.instance_login_view.to_map()

        if self.login_success is not None:
            result['LoginSuccess'] = self.login_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceLoginToken') is not None:
            self.instance_login_token = m.get('InstanceLoginToken')

        if m.get('InstanceLoginView') is not None:
            temp_model = main_models.LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView()
            self.instance_login_view = temp_model.from_map(m.get('InstanceLoginView'))

        if m.get('LoginSuccess') is not None:
            self.login_success = m.get('LoginSuccess')

        return self

class LoginInstanceResponseBodyRootInstanceLoginInfoListInstanceLoginView(DaraModel):
    def __init__(
        self,
        default_view_url: str = None,
    ):
        self.default_view_url = default_view_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_view_url is not None:
            result['DefaultViewUrl'] = self.default_view_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultViewUrl') is not None:
            self.default_view_url = m.get('DefaultViewUrl')

        return self

class LoginInstanceResponseBodyRootDisposableAccount(DaraModel):
    def __init__(
        self,
        login_form_action_url: str = None,
        login_url: str = None,
    ):
        self.login_form_action_url = login_form_action_url
        self.login_url = login_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_form_action_url is not None:
            result['LoginFormActionUrl'] = self.login_form_action_url

        if self.login_url is not None:
            result['LoginUrl'] = self.login_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginFormActionUrl') is not None:
            self.login_form_action_url = m.get('LoginFormActionUrl')

        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')

        return self

