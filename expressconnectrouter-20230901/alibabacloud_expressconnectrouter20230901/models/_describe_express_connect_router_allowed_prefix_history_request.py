# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExpressConnectRouterAllowedPrefixHistoryRequest(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        version: str = None,
    ):
        # The instance ID of the VPC or transit router (TR) associated with the Express Connect Router (ECR) for forward routing.
        # 
        # > You must specify either the **InstanceId** parameter or the **AssociationId** parameter.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value from your client to ensure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether it is only a dry run for this request. Valid values:
        # 
        # - **true**: Performs a dry run for the request without modifying EPS resources.
        # 
        # - **false** (default): Sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The instance ID to load into the Express Connect Router (ECR).
        # 
        # > You must specify either the **InstanceId** parameter or the **AssociationId** parameter.
        self.instance_id = instance_id
        # The type of the network instance. Valid values:
        # - **VPC**: VPC instance.
        # - **TR**: Transit router instance.
        self.instance_type = instance_type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

