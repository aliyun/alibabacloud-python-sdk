# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetAuthCodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAuthCodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. It is returned when the request fails. A success response may not contain this field.
        self.code = code
        # The business data returned by the operation.
        self.data = data
        # The error or result message. It describes the cause when the request fails. A success response may not contain this field.
        self.message = message
        # The unique identifier of the request. You can provide this value for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A value of true indicates that the request was processed successfully. To check whether an asynchronous task is completed, you must query the task status separately.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAuthCodeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAuthCodeResponseBodyData(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_version_id: str = None,
        auth_code: str = None,
        product_type: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The network access type supported by the connection resource.
        # 
        # - **INTERNET**: Supports Internet access.
        # - **VPC**: Supports virtual private cloud (VPC) access.
        # - **ANY**: Supports both Internet and VPC access.
        self.access_type = access_type
        # The application ID, which is used for subsequent application queries or unbinding the image.
        self.app_id = app_id
        # The delivery group ID of the creation or validation resource. It is used together with the user and application information in this response during connection.
        self.app_instance_group_id = app_instance_group_id
        # The application version ID, which is used to locate a specific version of the application. This field is not the image version ID.
        self.app_version_id = app_version_id
        # The authorization code used to connect to the creation or validation resource. **The validity period is 180 seconds (3 minutes) from the time of issuance. Use it promptly after obtaining it.** Use it together with the user, delivery group, and application information in the same response, and keep it confidential as a connection credential.
        # 
        # Do not reuse the authorization code after it is redeemed. If it has been used or expired, call this operation again to obtain a new one.
        self.auth_code = auth_code
        # The purpose type of the connection resource.
        # 
        # - **ImageBuilder**: Image or application creation resource.
        # - **ImageValidate**: Image or application validation resource.
        self.product_type = product_type
        # The region ID in this response.
        self.region_id = region_id
        # The user ID used when connecting to the creation or validation environment. Use the value returned in this response.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

