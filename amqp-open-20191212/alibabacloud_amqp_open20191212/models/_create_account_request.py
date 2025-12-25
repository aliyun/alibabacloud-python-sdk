# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountRequest(DaraModel):
    def __init__(
        self,
        remark: str = None,
        account_access_key: str = None,
        create_timestamp: int = None,
        instance_id: str = None,
        secret_sign: str = None,
        signature: str = None,
        user_name: str = None,
    ):
        self.remark = remark
        # The AccessKey ID of your Alibaba Cloud account or RAM user. For information about how to obtain an AccessKey pair, see [Create an AccessKey pair](https://help.aliyun.com/document_detail/116401.html).
        # 
        # >  If you use the pair of static username and password that is created by using the Accesskey pair of a RAM user to access ApsaraMQ for RabbitMQ to send and receive messages, make sure that the RAM user is granted the required permissions. For more information, see [RAM policies](https://help.aliyun.com/document_detail/146559.html).
        # 
        # This parameter is required.
        self.account_access_key = account_access_key
        # The timestamp that indicates when the password is created. Unit: milliseconds.
        # 
        # >  This timestamp is specified by you and is used to generate a static password. The timestamp is not the timestamp that indicates when the system generates the password.
        # 
        # This parameter is required.
        self.create_timestamp = create_timestamp
        # The ID of the instance for which you want to create a pair of static username and password.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The AccessKey secret signature. The system generates a static password based on the signature in the request, the AccessKey secret signature, and the username.
        # 
        # The system uses the HMAC-SHA1 algorithm to generate the AccessKey secret signature based on the timestamp that indicates when the username is created and the AccessKey ID. For more information, see the **"Sample code on how to generate a signature"** section of this topic.
        # 
        # This parameter is required.
        self.secret_sign = secret_sign
        # The signature. The system generates a static password based on the signature in the request, the AccessKey secret signature, and the username.
        # 
        # The system uses the HMAC-SHA1 algorithm to generate the signature based on the timestamp that indicates when the username is created and the AccessKey ID. For more information, see the **"Sample code on how to generate a signature"** section of this topic.
        # 
        # This parameter is required.
        self.signature = signature
        # The static username that you want to create.
        # 
        # The value of this parameter is a Base64-encoded string that is generated based on the instance ID and AccessKey ID. For more information, see the "**Sample code on how to generate a username**" section of this topic.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remark is not None:
            result['Remark'] = self.remark

        if self.account_access_key is not None:
            result['accountAccessKey'] = self.account_access_key

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.secret_sign is not None:
            result['secretSign'] = self.secret_sign

        if self.signature is not None:
            result['signature'] = self.signature

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('accountAccessKey') is not None:
            self.account_access_key = m.get('accountAccessKey')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('secretSign') is not None:
            self.secret_sign = m.get('secretSign')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

