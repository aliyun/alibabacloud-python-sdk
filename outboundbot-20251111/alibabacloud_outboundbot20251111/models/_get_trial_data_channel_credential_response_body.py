# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class GetTrialDataChannelCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTrialDataChannelCredentialResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The business processing status code. OK indicates success. When an exception occurs, the corresponding business error code is returned. The error types and mapping rules follow the current API configuration. No error codes are added or modified in this operation.
        self.code = code
        # The data channel connection and authentication information for the specified device. Use the actual return values and do not deduce topics or credentials manually.
        self.data = data
        # The HTTP status code recorded in the business response body. A normal return value is 200. To determine whether the business operation is successful, you must also check Code. You cannot determine the success of the call solely based on the presence of this field.
        self.http_status_code = http_status_code
        # The business response or error description. It is usually empty or not returned upon success, and no fixed text is returned upon success. Upon failure, it provides an error description to assist in troubleshooting. Combine it with Code and Params to understand the cause of the error. The example is an error message when the trial link visitor token expires (corresponding to the Code Expired.VisitorToken) and is for format reference only.
        self.message = message
        # The list of parameters used for the localized display of error messages. It is not a scenario variable or business result. A normal successful response is usually an empty array. When an error occurs, parameters corresponding to the error template may be returned.
        self.params = params
        # The ID used to correlate and troubleshoot this POP request. The value in the response corresponds to this request. System request parameters are injected by the gateway, and the caller does not need to fill in system fields.
        self.request_id = request_id

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTrialDataChannelCredentialResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTrialDataChannelCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        device_id: str = None,
        endpoint: str = None,
        expiration_time: int = None,
        password: str = None,
        topic: str = None,
        user_name: str = None,
    ):
        # The client connection ID returned by the data channel service. It must be used together with the address, username, and password returned in this response. The example is a desensitized placeholder value and does not declare a fixed naming rule.
        self.client_id = client_id
        # The ID of the client device that initiates web voice calls or receives data channel events. The same client must use the same DeviceId when retrieving data channel credentials and initiating calls. The example is only a business device ID and not a real credential assigned by the platform.
        self.device_id = device_id
        # The access endpoint of the data channel. The actual address, protocol, port, and authentication method are subject to the return values of the RTC gateway and client conventions. Local code only delegates to the gateway service and cannot be used to confirm a fixed production domain name or MQTT/WebSocket protocol.
        self.endpoint = endpoint
        # The expiration time of the temporary credentials for the data channel. The current POP maps to expirationTime, while the local RTC second-party package field is expiredTime. The field mapping compatibility and time unit must be verified against the actual gateway version. Do not assume that the field is always returned or interpret it as milliseconds without authorization. The example only demonstrates the integer format.
        self.expiration_time = expiration_time
        # The temporary authentication password used to connect to the data channel. It must be used together with UserName and within the validity period. It is a sensitive credential and the real value must not be disclosed. The example is a placeholder value that cannot be used for authentication.
        self.password = password
        # The topic ID returned by the data channel service. The client subscribes to or receives events based on the actual protocol and this topic. The client must not deduce the topic based on DeviceId or treat the example as a real available topic.
        self.topic = topic
        # The temporary authentication username used to connect to the data channel. It must be used together with the Password and Endpoint returned in the same response. The example placeholder value cannot be used for logon.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.password is not None:
            result['Password'] = self.password

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

