# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetUserProvisioningConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_provisioning_configuration: main_models.GetUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The global configurations of the RAM user provisioning.
        self.user_provisioning_configuration = user_provisioning_configuration

    def validate(self):
        if self.user_provisioning_configuration:
            self.user_provisioning_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_provisioning_configuration is not None:
            result['UserProvisioningConfiguration'] = self.user_provisioning_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserProvisioningConfiguration') is not None:
            temp_model = main_models.GetUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration()
            self.user_provisioning_configuration = temp_model.from_map(m.get('UserProvisioningConfiguration'))

        return self

class GetUserProvisioningConfigurationResponseBodyUserProvisioningConfiguration(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_landing_page: str = None,
        directory_id: str = None,
        session_duration: int = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The default URL for a CloudSSO user who logs on to the Alibaba Cloud Management Console.
        # 
        # Default value: https://homenew.console.aliyun.com.
        self.default_landing_page = default_landing_page
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The duration of the logon session.
        # 
        # Unit: hours.
        # 
        # Valid values: 1 to 24.
        # 
        # Default value: 6.
        self.session_duration = session_duration
        # The modification time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_landing_page is not None:
            result['DefaultLandingPage'] = self.default_landing_page

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultLandingPage') is not None:
            self.default_landing_page = m.get('DefaultLandingPage')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

