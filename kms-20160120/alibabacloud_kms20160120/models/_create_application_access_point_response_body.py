# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationAccessPointResponseBody(DaraModel):
    def __init__(
        self,
        arn: str = None,
        authentication_method: str = None,
        description: str = None,
        name: str = None,
        policies: str = None,
        request_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the AAP.
        self.arn = arn
        # The authentication method.
        self.authentication_method = authentication_method
        # The description of the AAP.
        self.description = description
        # The name of the AAP.
        self.name = name
        # The permission policy.
        self.policies = policies
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.policies is not None:
            result['Policies'] = self.policies

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policies') is not None:
            self.policies = m.get('Policies')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

