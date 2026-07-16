# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class CreateExpressConnectRouterAssociationRequest(DaraModel):
    def __init__(
        self,
        allowed_prefixes: List[str] = None,
        allowed_prefixes_mode: str = None,
        association_region_id: str = None,
        cen_id: str = None,
        client_token: str = None,
        create_attachment: bool = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        tag: List[main_models.CreateExpressConnectRouterAssociationRequestTag] = None,
        transit_router_id: str = None,
        transit_router_owner_id: int = None,
        version: str = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
    ):
        # The allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The route prefix mode. Valid values:
        # 
        # - **MatchMode**: After you distribute new route CIDR blocks to data centers, original specific routes that are distributed are withdrawn.
        # 
        # - **IncrementalMode**: After you distribute new route CIDR blocks to data centers, the original specific routes that fall in the CIDR blocks that you configure are withdrawn, and the original specific routes that do not fall in the CIDR blocks are still distributed.
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The region ID of the resource to be associated.
        # 
        # This parameter is required.
        self.association_region_id = association_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to initiate an association on the TR when the ECR is associated with the TR. Valid values:
        # 
        # *   **true**: You do not need to initiate an association on the TR.
        # *   **false**: You need to initiate an association on the TR.
        self.create_attachment = create_attachment
        # The information about the associated resource. It must be 0 to 128 characters in length.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        self.tag = tag
        # The TR ID.
        self.transit_router_id = transit_router_id
        # The ID of the Alibaba Cloud account that owns the TR. Default value: ID of the Alibaba Cloud account that logs in.
        # 
        # >  If you want to connect to a network instance that belongs to a different account, this parameter is required.
        self.transit_router_owner_id = transit_router_owner_id
        self.version = version
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account that owns the VPC. Default value: ID of the Alibaba Cloud account that logs in.
        # 
        # >  If you want to connect to a network instance that belongs to a different account, this parameter is required.
        self.vpc_owner_id = vpc_owner_id

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
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes

        if self.allowed_prefixes_mode is not None:
            result['AllowedPrefixesMode'] = self.allowed_prefixes_mode

        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.create_attachment is not None:
            result['CreateAttachment'] = self.create_attachment

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_owner_id is not None:
            result['TransitRouterOwnerId'] = self.transit_router_owner_id

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')

        if m.get('AllowedPrefixesMode') is not None:
            self.allowed_prefixes_mode = m.get('AllowedPrefixesMode')

        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CreateAttachment') is not None:
            self.create_attachment = m.get('CreateAttachment')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateExpressConnectRouterAssociationRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterOwnerId') is not None:
            self.transit_router_owner_id = m.get('TransitRouterOwnerId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        return self

class CreateExpressConnectRouterAssociationRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

