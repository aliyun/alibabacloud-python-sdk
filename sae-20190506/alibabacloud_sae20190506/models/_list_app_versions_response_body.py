# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListAppVersionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAppVersionsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The call is successful.
        # 
        # - **3xx**: The call is redirected.
        # 
        # - **4xx**: A request error occurred.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The version information.
        self.data = data
        # The error code.
        # 
        # - This parameter is not returned if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # Additional information about the call.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the historical versions of the application were successfully queried. Valid values:
        # 
        # - **true**: The query was successful.
        # 
        # - **false**: The query failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAppVersionsResponseBodyData(DaraModel):
    def __init__(
        self,
        build_package_url: str = None,
        create_time: str = None,
        id: str = None,
        type: str = None,
        war_url: str = None,
    ):
        # The download URL of the code package. If you uploaded the package using SAE, note the following:
        # 
        # - This URL is not a direct download link. You must call the GetPackageVersionAccessableUrl operation to obtain a downloadable URL that is valid for 10 minutes.
        # 
        # - SAE stores the package for a maximum of 90 days. After this period, the URL is not returned and the package cannot be downloaded.
        self.build_package_url = build_package_url
        # The time when the version was created.
        self.create_time = create_time
        # The version ID.
        self.id = id
        # The application type. Valid values:
        # 
        # - **image**: The application is deployed using an image.
        # 
        # - **url**: The application is deployed using a code package.
        self.type = type
        # The URL of the WAR package.
        self.war_url = war_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_package_url is not None:
            result['BuildPackageUrl'] = self.build_package_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        if self.war_url is not None:
            result['WarUrl'] = self.war_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildPackageUrl') is not None:
            self.build_package_url = m.get('BuildPackageUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')

        return self

