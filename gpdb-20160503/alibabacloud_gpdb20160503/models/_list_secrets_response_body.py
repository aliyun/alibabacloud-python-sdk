# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSecretsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        message: str = None,
        request_id: str = None,
        secrets: main_models.ListSecretsResponseBodySecrets = None,
        status: str = None,
    ):
        # The number of access credentials.
        self.count = count
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The queried access credentials.
        self.secrets = secrets
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.secrets:
            self.secrets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secrets is not None:
            result['Secrets'] = self.secrets.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Secrets') is not None:
            temp_model = main_models.ListSecretsResponseBodySecrets()
            self.secrets = temp_model.from_map(m.get('Secrets'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListSecretsResponseBodySecrets(DaraModel):
    def __init__(
        self,
        secrets: List[main_models.ListSecretsResponseBodySecretsSecrets] = None,
    ):
        self.secrets = secrets

    def validate(self):
        if self.secrets:
            for v1 in self.secrets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Secrets'] = []
        if self.secrets is not None:
            for k1 in self.secrets:
                result['Secrets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secrets = []
        if m.get('Secrets') is not None:
            for k1 in m.get('Secrets'):
                temp_model = main_models.ListSecretsResponseBodySecretsSecrets()
                self.secrets.append(temp_model.from_map(k1))

        return self

class ListSecretsResponseBodySecretsSecrets(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        dbinstance_id: str = None,
        description: str = None,
        region_id: str = None,
        secret_arn: str = None,
        secret_name: str = None,
        username: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The description of the access credential.
        self.description = description
        # The region ID of the instance.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of the access credential for the created Data API account. Format: `acs:gpdb:{{region}}:{{accountId}}:secret/{{secretName}}-{{32 digits random string}`.
        self.secret_arn = secret_arn
        # The name of the access credential.
        self.secret_name = secret_name
        # The name of the database account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secret_arn is not None:
            result['SecretArn'] = self.secret_arn

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecretArn') is not None:
            self.secret_arn = m.get('SecretArn')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

