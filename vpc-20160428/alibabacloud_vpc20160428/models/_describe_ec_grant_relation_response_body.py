# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeEcGrantRelationResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ec_grant_relations: List[main_models.DescribeEcGrantRelationResponseBodyEcGrantRelations] = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The query results.
        self.ec_grant_relations = ec_grant_relations
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ec_grant_relations:
            for v1 in self.ec_grant_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['EcGrantRelations'] = []
        if self.ec_grant_relations is not None:
            for k1 in self.ec_grant_relations:
                result['EcGrantRelations'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ec_grant_relations = []
        if m.get('EcGrantRelations') is not None:
            for k1 in m.get('EcGrantRelations'):
                temp_model = main_models.DescribeEcGrantRelationResponseBodyEcGrantRelations()
                self.ec_grant_relations.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEcGrantRelationResponseBodyEcGrantRelations(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        gmt_create: str = None,
        grant_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_router_id: str = None,
        region_no: str = None,
        status: str = None,
        vbr_instance_id: str = None,
        vbr_owner_uid: int = None,
        vbr_region_no: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.ali_uid = ali_uid
        # The time when permissions on the VPC were granted to the VBR.
        self.gmt_create = gmt_create
        # The VBRs that have permissions on the VPC. Valid values:
        # 
        # *   **All**: VBRs that reside in the specified region and belong to the specified Alibaba Cloud account all have permissions on the VPC.
        # *   **Specify**: Only the specified VBR has permissions on the VPC.
        self.grant_type = grant_type
        # The ID of the VPC.
        self.instance_id = instance_id
        # The name of the VPC.
        self.instance_name = instance_name
        # The ID of the vRouter.
        self.instance_router_id = instance_router_id
        # The ID of the region where the VPC is deployed.
        self.region_no = region_no
        # The query result. Valid values:
        # 
        # *   **Created**: The VBR has permissions on the VPC.
        # *   **Deleted**: The VBR does not have permissions on the VPC.
        self.status = status
        # The ID of the VBR.
        self.vbr_instance_id = vbr_instance_id
        # The ID of the Alibaba Cloud account to which the VBR belongs.
        self.vbr_owner_uid = vbr_owner_uid
        # The ID of the region where the VBR is deployed.
        self.vbr_region_no = vbr_region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.grant_type is not None:
            result['GrantType'] = self.grant_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_router_id is not None:
            result['InstanceRouterId'] = self.instance_router_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.status is not None:
            result['Status'] = self.status

        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id

        if self.vbr_owner_uid is not None:
            result['VbrOwnerUid'] = self.vbr_owner_uid

        if self.vbr_region_no is not None:
            result['VbrRegionNo'] = self.vbr_region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceRouterId') is not None:
            self.instance_router_id = m.get('InstanceRouterId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')

        if m.get('VbrOwnerUid') is not None:
            self.vbr_owner_uid = m.get('VbrOwnerUid')

        if m.get('VbrRegionNo') is not None:
            self.vbr_region_no = m.get('VbrRegionNo')

        return self

