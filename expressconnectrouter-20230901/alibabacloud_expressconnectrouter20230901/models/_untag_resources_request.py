# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
        version: str = None,
    ):
        # Specifies whether to unbind all tags. This parameter is valid only when **TagKey** is empty. Valid values:
        # 
        # - **true**: Unbinds all tags from the Express Connect Router (ECR) instance.
        # - **false** (default): Does not unbind all tags from the Express Connect Router (ECR) instance.
        # 
        # > You must specify either **TagKey** or **All**.
        self.all = all
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - **true**: Performs a dry run without modifying EPS resources.
        # 
        # - **false** (default): Sends the request normally.
        self.dry_run = dry_run
        # The list of resource instance IDs. You can unbind tags from up to 50 resource instances at a time.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # - **EXPRESSCONNECTROUTER**: Express Connect Router (ECR) instance.
        # - **EXPRESSCONNECTROUTERVPCASSOCIATION**: the associate relationship between an ECR and a VPC.
        # - **EXPRESSCONNECTROUTERTRASSOCIATION**: the associate relationship between an ECR and a transit router.
        # - **ECRFLOWLOG**: ECR flow log.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys of the Express Connect Router (ECR) instance to unbind.
        self.tag_key = tag_key
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

