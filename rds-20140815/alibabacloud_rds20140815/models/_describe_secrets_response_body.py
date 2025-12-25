# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSecretsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        secrets: List[main_models.DescribeSecretsResponseBodySecrets] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The details of the credential.
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Secrets'] = []
        if self.secrets is not None:
            for k1 in self.secrets:
                result['Secrets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.secrets = []
        if m.get('Secrets') is not None:
            for k1 in m.get('Secrets'):
                temp_model = main_models.DescribeSecretsResponseBodySecrets()
                self.secrets.append(temp_model.from_map(k1))

        return self

class DescribeSecretsResponseBodySecrets(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        description: str = None,
        region_id: str = None,
        secret_arn: str = None,
        secret_name: str = None,
        username: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The description of the credential.
        self.description = description
        # The region ID.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of the credential for the created Data API account.
        self.secret_arn = secret_arn
        # The name of the credential.
        self.secret_name = secret_name
        # The username that is used to access the database.
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

