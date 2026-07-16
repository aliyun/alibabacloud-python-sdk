# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExpressConnectRouterChildInstanceRequest(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        child_instance_id: str = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
        version: str = None,
    ):
        # The ID of the association between the ECR and the virtual private cloud (VPC) or transit router (TR).
        self.association_id = association_id
        # The ID of the network instance to be queried.
        self.child_instance_id = child_instance_id
        # The region ID of the network instance.
        self.child_instance_region_id = child_instance_region_id
        # The type of network instance. Set the value to VBR.
        self.child_instance_type = child_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value of NextToken is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
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

        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id

        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')

        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

