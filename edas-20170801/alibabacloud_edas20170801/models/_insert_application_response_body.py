# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class InsertApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application_info: main_models.InsertApplicationResponseBodyApplicationInfo = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The application object that is returned after the application is created.
        self.application_info = application_info
        # The status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_info:
            self.application_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_info is not None:
            result['ApplicationInfo'] = self.application_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationInfo') is not None:
            temp_model = main_models.InsertApplicationResponseBodyApplicationInfo()
            self.application_info = temp_model.from_map(m.get('ApplicationInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InsertApplicationResponseBodyApplicationInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        change_order_id: str = None,
        dockerize: bool = None,
        owner: str = None,
        port: int = None,
        region_name: str = None,
        user_id: str = None,
    ):
        # The ID of the application. This ID is the unique identifier of an EDAS application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The ID of the change process.
        self.change_order_id = change_order_id
        # Indicates whether the application is a Docker application. Valid values:
        # 
        # - **true**: The application is a Docker application.
        # 
        # - **false**: The application is not a Docker application.
        self.dockerize = dockerize
        # The owner of the application. This is the user who created the application.
        self.owner = owner
        # The default port of the application is 8080. You can call the UpdateContainerConfiguration operation to change the port. For more information, see [UpdateContainerConfiguration](https://help.aliyun.com/document_detail/149403.html).
        self.port = port
        # The name of the region.
        self.region_name = region_name
        # The user ID of the application owner.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.dockerize is not None:
            result['Dockerize'] = self.dockerize

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.port is not None:
            result['Port'] = self.port

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('Dockerize') is not None:
            self.dockerize = m.get('Dockerize')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

