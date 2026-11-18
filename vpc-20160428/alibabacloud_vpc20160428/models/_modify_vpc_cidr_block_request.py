# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcCidrBlockRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        original_cidr_block: str = None,
        region_id: str = None,
        target_cidr_block: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client and ensure that the value is unique among different requests. The ClientToken parameter supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken** identifier. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for this request. Valid values:
        # - **true**: The system sends a check request and does not modify the CIDR block of the virtual private cloud (VPC). If the check fails, the system returns the corresponding error. If the check succeeds, the system returns the error code `DryRunOperation`.
        # - **false** (default): The system sends a normal request. After the request passes the check, the system returns an HTTP 2xx status code and directly performs the modification.
        self.dry_run = dry_run
        # The CIDR block of the VPC that you want to modify. Both primary and secondary CIDR blocks are supported.
        # 
        # This parameter is required.
        self.original_cidr_block = original_cidr_block
        # The ID of the region where the VPC is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The target CIDR block of the VPC after the modification.
        # 
        # This parameter is required.
        self.target_cidr_block = target_cidr_block
        # The ID of the VPC that you want to modify.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.original_cidr_block is not None:
            result['OriginalCidrBlock'] = self.original_cidr_block

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_cidr_block is not None:
            result['TargetCidrBlock'] = self.target_cidr_block

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OriginalCidrBlock') is not None:
            self.original_cidr_block = m.get('OriginalCidrBlock')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetCidrBlock') is not None:
            self.target_cidr_block = m.get('TargetCidrBlock')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

