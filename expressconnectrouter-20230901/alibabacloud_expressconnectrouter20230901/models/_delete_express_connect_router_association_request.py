# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteExpressConnectRouterAssociationRequest(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        client_token: str = None,
        delete_attachment: bool = None,
        dry_run: bool = None,
        ecr_id: str = None,
        version: str = None,
    ):
        # The ID used to associate the Express Connect Router (ECR) with a VPC or transit router.
        # 
        # This parameter is required.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value from your client to ensure that the parameter value is unique among different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to delete the association between the Express Connect Router (ECR) and a transit router or VPC. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.delete_attachment = delete_attachment
        # Specifies whether to only perform a dry run for this request. Valid values:
        # 
        # - **true**: Sends a dry run request and does not modify service resources.
        # 
        # - **false** (default value): Sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
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

        if self.delete_attachment is not None:
            result['DeleteAttachment'] = self.delete_attachment

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteAttachment') is not None:
            self.delete_attachment = m.get('DeleteAttachment')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

