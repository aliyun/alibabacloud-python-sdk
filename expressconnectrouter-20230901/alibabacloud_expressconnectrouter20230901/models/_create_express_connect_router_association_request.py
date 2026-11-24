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
        # The list of allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The route prefix mode. Valid values:
        # - MatchMode: match mode. Only the configured route CIDR blocks are advertised to the data center, and the previously advertised specific routes are withdrawn.
        # - IncrementalMode: incremental mode. The configured route CIDR blocks are advertised to the data center. The previously advertised specific routes that fall within the configured route CIDR blocks are withdrawn, and the specific routes that do not fall within the configured CIDR blocks remain advertised.
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The region where the associated resource resides.
        # 
        # This parameter is required.
        self.association_region_id = association_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        # > If you specify TransitRouterId, CenId is required. You must first call the CreateCen operation of the Cbn (2017-09-12) service to create a CEN instance and obtain the CEN instance ID.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value from your client to ensure that the value is unique among different requests. The client token only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether to initiate an association when the Express Connect Router is associated with the transit router. Valid values:
        # 
        # - **true**: No association is initiated on the transit router side.
        # - **false**: An association is initiated on the transit router side.
        self.create_attachment = create_attachment
        # The description of the associated resource. The description must be 0 to 128 characters in length.
        self.description = description
        # Specifies whether to only perform a dry run for this request. Valid values:
        # 
        # - **true**: The system sends a check request without modifying service resources.
        # 
        # - **false** (default): The system sends a normal request.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The list of tags.
        # 
        # You can add up to 20 tags.
        self.tag = tag
        # The ID of the transit router.
        # > The TransitRouterId and VpcId parameters are mutually exclusive. You must specify one of them. You must first call the CreateTransitRouter operation of the Cbn (2017-09-12) service to create a transit router and obtain the transit router ID.
        self.transit_router_id = transit_router_id
        # The ID of the Alibaba Cloud account to which the transit router instance belongs. The transit router is used to forward routing traffic. Default value: the current logon Alibaba Cloud account ID.
        # 
        # > If you want to load a network instance across accounts, this parameter is required.
        self.transit_router_owner_id = transit_router_owner_id
        self.version = version
        # The instance ID of the VPC-connected instance.
        # > The VpcId and TransitRouterId parameters are mutually exclusive. You must specify one of them.
        # > You must first call the CreateVpc operation of the Vpc (2016-04-28) service to create a VPC and obtain the VPC ID.
        self.vpc_id = vpc_id
        # The Alibaba Cloud account ID to which the VPC-connected instance belongs. Default value: the current logon Alibaba Cloud account ID.
        # 
        # > If you want to load a network instance across accounts, this parameter is required.
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
        # The tag key of the resource. If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. The tag value can be an empty string and can be up to 128 characters in length. It cannot contain `http://` or `https://`.
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

