# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyExpressConnectRouterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        name: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a unique value for this parameter from your client. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** as the **ClientToken**. The **RequestId** of each request is unique.
        self.client_token = client_token
        # The description of ECR.
        # 
        # > The description can be empty or 0 to 256 characters in length. It cannot start with http\\:// or https\\://.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Sends a check request without modifying the service resource.
        # - **false** (default): Sends a normal request.
        self.dry_run = dry_run
        # The ID of ECR.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The name of ECR.
        # 
        # > The name can be empty or 0 to 128 characters in length. It cannot start with http\\:// or https\\://.
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

