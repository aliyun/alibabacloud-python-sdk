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
        # Indicates whether the historical versions of the application were obtained. Valid values:
        # 
        # *   **true**: indicates that the historical versions of the application were obtained.
        # *   **false**: indicates that the historical versions of the application could not be obtained.
        self.code = code
        # The information about the versions.
        self.data = data
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.error_code = error_code
        # The ID of the request.
        self.message = message
        # The information about the versions.
        self.request_id = request_id
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
        # The URL of the code package. If you use the SAE console to upload the code package, take note of the following items:
        # 
        # *   You cannot download the URL. You must call the GetPackageVersionAccessableUrl operation to obtain the URL. The obtained URL is valid for 10 minutes.
        # *   SAE can retain the package up to 90 days. After 90 days, the URL cannot be returned or downloaded.
        self.build_package_url = build_package_url
        # The download link of the WAR or JAR package. This parameter is returned when the **Type** parameter is set to **url**.
        self.create_time = create_time
        # The error code.
        # 
        # *   The **ErrorCode** parameter is not returned when the request succeeds.
        # *   The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.id = id
        # The deployment method of the application. Valid values:
        # 
        # *   **image**: indicates that the application is deployed by using an image.
        # *   **url**: indicates that the application is deployed by using a code package.
        self.type = type
        # The URL of the image.
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

