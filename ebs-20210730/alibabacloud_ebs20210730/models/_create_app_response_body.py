# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        app_id: str = None,
        app_name: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_code: str = None,
    ):
        # The detailed reason why access was denied.
        self.access_denied_detail = access_denied_detail
        # The app ID.
        self.app_id = app_id
        # The app name.
        self.app_name = app_name
        # The status code. A value of 200 indicates success.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not in use. Ignore this parameter.
        self.dynamic_message = dynamic_message
        # The error code description.
        self.http_status_code = http_status_code
        # The additional information. If the request is successful, "success" is returned. If the request fails, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the app was created successfully. Valid values: true: The app was created successfully. false: The app failed to be created.
        self.success = success
        # The status code.
        self.user_code = user_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_code is not None:
            result['UserCode'] = self.user_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserCode') is not None:
            self.user_code = m.get('UserCode')

        return self

