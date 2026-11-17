# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class BridgeTrialWebCallResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BridgeTrialWebCallResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The business processing status code. OK indicates success. When an exception occurs, the corresponding business error code is returned. The error types and mapping rules follow the current API configuration, and no error codes are added or modified this time.
        self.code = code
        # The session, channel, service address, and temporary authentication token for this web voice call. Use the actually returned connection parameters.
        self.data = data
        # The HTTP status code recorded in the business response body. A normal return is 200. To determine whether the business is successful, you must also check Code. You cannot determine that the call is successful solely based on the existence of this field.
        self.http_status_code = http_status_code
        # The business response or error description. It is usually empty or not returned upon success, and it is not required to return a fixed text upon success. Upon failure, it is an error description used to assist troubleshooting, and it is combined with Code and Params to understand the cause of the error. The example is an error message when the trial link visitor token expires (corresponding to the Code Expired.VisitorToken), and is for format reference only.
        self.message = message
        # The list of parameters used for the localized display of error messages. It is not a scenario variable or business result. A normal successful response is usually an empty array. When an error occurs, parameters corresponding to the error template may be returned.
        self.params = params
        # The ID used to associate and troubleshoot this POP request. The value in the response corresponds to this request. System request parameters are injected by the gateway, and the caller does not need to fill in the system fields.
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
            temp_model = main_models.BridgeTrialWebCallResponseBodyData()
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

class BridgeTrialWebCallResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        expiration_time: str = None,
        instance_id: str = None,
        server_url: str = None,
        session_id: str = None,
        token: str = None,
    ):
        # The web voice connection channel ID assigned or returned by the RTC gateway. It is used to associate and connect the voice channel for this call. It is different from the trial channel AccessChannelId. You must use the real value returned by this API.
        self.channel_id = channel_id
        # The expiration time of the web voice connection token for this call. The current POP type is string, and the backend WebCallContext type is long. The code does not mark the time unit. The format and unit must be confirmed according to the actual service provider agreement. The example is only a numeric string and does not represent a verified validity period unit.
        self.expiration_time = expiration_time
        # The instance identity of the associated product. You must use an instance that the invoker has access to and that actually exists. The instance must be consistent with the instance to which the scenario, channel, and session belong. The maximum length is subject to the current POP parameter definition.
        self.instance_id = instance_id
        # The service address used to establish the web voice connection for this call. The format and protocol are determined by the service provider of the RTC gateway. You must use the actual returned value and cannot concatenate it yourself. The example is an unconnectable desensitized address and does not represent a production domain name or protocol guarantee.
        self.server_url = server_url
        # The session ID used to uniquely associate this interaction. For a text session, it is the text- identifier returned when the session is started. For a web voice session, it is the ws- identifier. For a real number outbound call test, it is the test- identifier. Subsequent calls must use the actual returned value.
        self.session_id = session_id
        # The temporary token used to connect to the voice channel for this call. It must be used together with the ServerUrl and ChannelId returned this time. Do not disclose or record the actual token without desensitization. The example is not a valid credential, and the format and validity period are determined by the service provider.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.server_url is not None:
            result['ServerUrl'] = self.server_url

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

