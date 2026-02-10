# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAvailableHoneypotResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListAvailableHoneypotResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The number of images that are used for the honeypot.
        self.count = count
        # An array consisting of the information about the images that are used for the honeypot.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
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

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAvailableHoneypotResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAvailableHoneypotResponseBodyData(DaraModel):
    def __init__(
        self,
        honeypot_image_display_name: str = None,
        honeypot_image_id: str = None,
        honeypot_image_name: str = None,
        honeypot_image_type: str = None,
        honeypot_image_version: str = None,
        multiports: str = None,
        proto: str = None,
        service_port: str = None,
        template: str = None,
    ):
        # The display name of the image.
        self.honeypot_image_display_name = honeypot_image_display_name
        # The ID of the image.
        self.honeypot_image_id = honeypot_image_id
        # The name of the image that is used for the honeypot.
        self.honeypot_image_name = honeypot_image_name
        # The type of the image.
        self.honeypot_image_type = honeypot_image_type
        # The version of the image.
        self.honeypot_image_version = honeypot_image_version
        # The port that is supported by the honeypot. The value is in the JSON format. Valid values:
        # 
        # *   **log_type**: the log type
        # *   **proto**: the supported protocol
        # *   **description**: the description
        # *   **ports**: the supported ports
        # *   **port_str**: the supported port number of the string type
        # *   **type**: the type
        self.multiports = multiports
        # The protocol that is supported by the honeypot.
        self.proto = proto
        # The service port of the honeypot.
        self.service_port = service_port
        # The configuration template of the honeypot.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.honeypot_image_display_name is not None:
            result['HoneypotImageDisplayName'] = self.honeypot_image_display_name

        if self.honeypot_image_id is not None:
            result['HoneypotImageId'] = self.honeypot_image_id

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.honeypot_image_type is not None:
            result['HoneypotImageType'] = self.honeypot_image_type

        if self.honeypot_image_version is not None:
            result['HoneypotImageVersion'] = self.honeypot_image_version

        if self.multiports is not None:
            result['Multiports'] = self.multiports

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HoneypotImageDisplayName') is not None:
            self.honeypot_image_display_name = m.get('HoneypotImageDisplayName')

        if m.get('HoneypotImageId') is not None:
            self.honeypot_image_id = m.get('HoneypotImageId')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('HoneypotImageType') is not None:
            self.honeypot_image_type = m.get('HoneypotImageType')

        if m.get('HoneypotImageVersion') is not None:
            self.honeypot_image_version = m.get('HoneypotImageVersion')

        if m.get('Multiports') is not None:
            self.multiports = m.get('Multiports')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

