# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeEventDisposeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEventDisposeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeEventDisposeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEventDisposeResponseBodyData(DaraModel):
    def __init__(
        self,
        event_dispose: List[Any] = None,
        receiver_info: main_models.DescribeEventDisposeResponseBodyDataReceiverInfo = None,
        remark: str = None,
        status: int = None,
    ):
        # An array consisting of JSON objects that are configured for event handling.
        self.event_dispose = event_dispose
        # The JSON object that is configured for an alert recipient.
        self.receiver_info = receiver_info
        # The description of the event.
        self.remark = remark
        # The status of the event. Valid values:
        # 
        # *   0: not handled
        # *   1: handing
        # *   5: handling failed
        # *   10: handled
        self.status = status

    def validate(self):
        if self.receiver_info:
            self.receiver_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose

        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info.to_map()

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')

        if m.get('ReceiverInfo') is not None:
            temp_model = main_models.DescribeEventDisposeResponseBodyDataReceiverInfo()
            self.receiver_info = temp_model.from_map(m.get('ReceiverInfo'))

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeEventDisposeResponseBodyDataReceiverInfo(DaraModel):
    def __init__(
        self,
        channel: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        message_title: str = None,
        receiver: str = None,
        status: int = None,
    ):
        # The channel of the contact information. Valid values:
        # 
        # *   message
        # *   mail
        self.channel = channel
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The ID of the recipient who receives the event handling result.
        self.id = id
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # The message title.
        self.message_title = message_title
        # The contact information of the recipient.
        self.receiver = receiver
        # Indicates whether the message is sent. Valid values:
        # 
        # *   0: not sent
        # *   1: sent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.message_title is not None:
            result['MessageTitle'] = self.message_title

        if self.receiver is not None:
            result['Receiver'] = self.receiver

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('MessageTitle') is not None:
            self.message_title = m.get('MessageTitle')

        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

