# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecretValueResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dbinstance_id: str = None,
        description: str = None,
        message: str = None,
        password: str = None,
        request_id: str = None,
        secret_arn: str = None,
        secret_name: str = None,
        status: str = None,
        username: str = None,
    ):
        # The error code.
        self.code = code
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The description of the access credential.
        self.description = description
        # The returned message.
        self.message = message
        # The password of the database account.
        self.password = password
        # The request ID.
        self.request_id = request_id
        # The ARN of the access credential for the created Data API account. Format: `acs:gpdb:{{region}}:{{accountId}}:secret/{{secretName}}-{{32 digits random string}`.
        self.secret_arn = secret_arn
        # The name of the access credential.
        self.secret_name = secret_name
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status
        # The name of the database account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.message is not None:
            result['Message'] = self.message

        if self.password is not None:
            result['Password'] = self.password

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.status is not None:
            result['Status'] = self.status

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

