# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class CreateAccountResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateAccountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
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
            temp_model = main_models.CreateAccountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class CreateAccountResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        create_time_stamp: int = None,
        instance_id: str = None,
        master_uid: int = None,
        password: str = None,
        remark: str = None,
        user_name: str = None,
    ):
        # The AccessKey ID that is used to create the password.
        self.access_key = access_key
        # The timestamp that indicates when the password was created. Unit: milliseconds.
        self.create_time_stamp = create_time_stamp
        # The ID of the ApsaraMQ for RabbitMQ instance.
        self.instance_id = instance_id
        # The Alibaba Cloud account ID or RAM user to which the AccessKey pair that is used to create the static username and password belongs.
        self.master_uid = master_uid
        # The created static password.
        self.password = password
        self.remark = remark
        # The created static username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.master_uid is not None:
            result['MasterUId'] = self.master_uid

        if self.password is not None:
            result['Password'] = self.password

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MasterUId') is not None:
            self.master_uid = m.get('MasterUId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

