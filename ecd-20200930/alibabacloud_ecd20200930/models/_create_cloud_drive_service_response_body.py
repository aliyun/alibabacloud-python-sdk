# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateCloudDriveServiceResponseBody(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        cds_name: str = None,
        cen_id: str = None,
        conflict_cds_and_order: main_models.CreateCloudDriveServiceResponseBodyConflictCdsAndOrder = None,
        domain_name: str = None,
        error_code: str = None,
        max_size: str = None,
        office_site_type: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the enterprise drive.
        self.cds_id = cds_id
        # The name of the cloud disk that is created in Cloud Drive Service.
        self.cds_name = cds_name
        # The ID of the CEN instance.
        # 
        # >  To allow end users to connect to cloud computers via virtual private clouds (VPCs), attach your office network to a CEN instance. The CEN instance connects to your on-premises network through VPN Gateway or Express Connect.
        self.cen_id = cen_id
        # The existing enterprise drive or its order that conflicts with the enterprise drive being created.
        self.conflict_cds_and_order = conflict_cds_and_order
        # The domain name of the enterprise AD office network.
        self.domain_name = domain_name
        # The error code.
        self.error_code = error_code
        # The maximum storage capacity of the enterprise drive. Unit: bytes.
        self.max_size = max_size
        # The type of the office network.
        # 
        # Valid values:
        # 
        # *   SIMPLE: convenience office network.
        # *   AD_CONNECTOR: enterprise AD office network.
        self.office_site_type = office_site_type
        # The ID of the order. You can obtain an order ID on the Orders page in the Expenses and Costs console.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.conflict_cds_and_order:
            self.conflict_cds_and_order.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.cds_name is not None:
            result['CdsName'] = self.cds_name

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.conflict_cds_and_order is not None:
            result['ConflictCdsAndOrder'] = self.conflict_cds_and_order.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('CdsName') is not None:
            self.cds_name = m.get('CdsName')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ConflictCdsAndOrder') is not None:
            temp_model = main_models.CreateCloudDriveServiceResponseBodyConflictCdsAndOrder()
            self.conflict_cds_and_order = temp_model.from_map(m.get('ConflictCdsAndOrder'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateCloudDriveServiceResponseBodyConflictCdsAndOrder(DaraModel):
    def __init__(
        self,
        conflict_cds: List[main_models.CreateCloudDriveServiceResponseBodyConflictCdsAndOrderConflictCds] = None,
        conflict_order: List[main_models.CreateCloudDriveServiceResponseBodyConflictCdsAndOrderConflictOrder] = None,
    ):
        # The conflicting enterprise drive.
        self.conflict_cds = conflict_cds
        # The subscription orders of the conflicting enterprise drives that are unpaid.
        self.conflict_order = conflict_order

    def validate(self):
        if self.conflict_cds:
            for v1 in self.conflict_cds:
                 if v1:
                    v1.validate()
        if self.conflict_order:
            for v1 in self.conflict_order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConflictCds'] = []
        if self.conflict_cds is not None:
            for k1 in self.conflict_cds:
                result['ConflictCds'].append(k1.to_map() if k1 else None)

        result['ConflictOrder'] = []
        if self.conflict_order is not None:
            for k1 in self.conflict_order:
                result['ConflictOrder'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflict_cds = []
        if m.get('ConflictCds') is not None:
            for k1 in m.get('ConflictCds'):
                temp_model = main_models.CreateCloudDriveServiceResponseBodyConflictCdsAndOrderConflictCds()
                self.conflict_cds.append(temp_model.from_map(k1))

        self.conflict_order = []
        if m.get('ConflictOrder') is not None:
            for k1 in m.get('ConflictOrder'):
                temp_model = main_models.CreateCloudDriveServiceResponseBodyConflictCdsAndOrderConflictOrder()
                self.conflict_order.append(temp_model.from_map(k1))

        return self

class CreateCloudDriveServiceResponseBodyConflictCdsAndOrderConflictOrder(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        order_id: str = None,
        region_id: str = None,
    ):
        # The ID of the enterprise drive. The enterprise drive cannot be used if the order is unpaid.
        self.cds_id = cds_id
        # The ID of the order. You can obtain an order ID on the **Orders** page in the Expenses and Costs console.
        self.order_id = order_id
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateCloudDriveServiceResponseBodyConflictCdsAndOrderConflictCds(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        region_id: str = None,
    ):
        # The ID of the enterprise drive.
        self.cds_id = cds_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

