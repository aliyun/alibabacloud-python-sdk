# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterAssociationRequest(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        association_node_type: str = None,
        association_region_id: str = None,
        cen_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
        tag: List[main_models.DescribeExpressConnectRouterAssociationRequestTag] = None,
        transit_router_id: str = None,
        version: str = None,
        vpc_id: str = None,
    ):
        # The ID used to associate the Express Connect Router (ECR) with a VPC or TR.
        self.association_id = association_id
        # The type of the associated resource. Valid values:
        # 
        # - **VPC**: VPC.
        # 
        # - **TR**: transit router.
        self.association_node_type = association_node_type
        # The region where the VPC or TR resides.
        self.association_region_id = association_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value from your client. Make sure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether this is a dry run. Valid values:
        # - **true**: sends a check request and does not modify service resources.
        # - **false** (default): sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # > You can call the CreateExpressConnectRouter API operation to create an ECR instance and obtain the EcrId.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # - If this is the first query or no next query is required, leave this parameter empty.
        # - If a next query is required, set the value to the NextToken value returned from the previous API call.
        self.next_token = next_token
        # The list of tags.
        # 
        # You can add up to 20 tags.
        self.tag = tag
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        self.version = version
        # The ID of the VPC-connected instance.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type

        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')

        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeExpressConnectRouterAssociationRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeExpressConnectRouterAssociationRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. The tag key cannot be an empty string. It can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. The tag value can be an empty string. It can be up to 128 characters in length, and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

