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
        # The remarks on the static user.
        self.remark = remark
        # The AccessKey ID of your Alibaba Cloud account or RAM user. For more information about how to obtain an AccessKey ID, see [Create an AccessKey](https://help.aliyun.com/document_detail/116401.html).
        # 
        # > If you use the AccessKey of a RAM user to create a static username and password to access ApsaraMQ for RabbitMQ and to send and receive messages, make sure that the RAM user is granted the required permissions. For more information, see [RAM access policies](https://help.aliyun.com/document_detail/146559.html).
        # 
        # This parameter is required.
        self.account_access_key = account_access_key
        # The timestamp that indicates when the username and password are created. Unit: milliseconds.
        # 
        # > This timestamp is used to calculate the static password. You can customize this value. This is not the timestamp that the system generates when the username and password are created.
        # 
        # This parameter is required.
        self.create_timestamp = create_timestamp
        # The ID of the ApsaraMQ for RabbitMQ instance. This specifies the instance for which you want to create a static username and password.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The signature of the AccessKey secret. The system calculates the static password based on the signature, the AccessKey secret signature, and the username.
        # 
        # The AccessKey secret signature is calculated using the HmacSHA1 algorithm on the creation timestamp of the specified username and the AccessKey ID. For more information about how to calculate the signature, see the **Signature algorithm sample code** section in this topic.
        # 
        # This parameter is required.
        self.secret_sign = secret_sign
        # The signature. The system calculates the static password based on the signature, the AccessKey secret signature, and the username.
        # 
        # The signature is calculated using the HmacSHA1 algorithm on the creation timestamp of the specified username and the AccessKey ID. For more information about how to calculate the signature, see the **Signature algorithm sample code** section in this topic.
        # 
        # This parameter is required.
        self.signature = signature
        # The static username that you want to create.
        # 
        # The value of this parameter is a Base64-encoded string that is constructed from the instance ID and the AccessKey ID. For more information about how to calculate the value, see the **Username calculation sample code** section in this topic.
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

