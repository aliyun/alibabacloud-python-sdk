# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsRegionIdResourceResponseBody(DaraModel):
    def __init__(
        self,
        ens_region_id_resources: main_models.DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned data. For more information, see EnsRegionIdResources in sample JSON responses.
        self.ens_region_id_resources = ens_region_id_resources
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of queried nodes.
        self.total_count = total_count

    def validate(self):
        if self.ens_region_id_resources:
            self.ens_region_id_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id_resources is not None:
            result['EnsRegionIdResources'] = self.ens_region_id_resources.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionIdResources') is not None:
            temp_model = main_models.DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources()
            self.ens_region_id_resources = temp_model.from_map(m.get('EnsRegionIdResources'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResources(DaraModel):
    def __init__(
        self,
        ens_region_id_resource: List[main_models.DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource] = None,
    ):
        self.ens_region_id_resource = ens_region_id_resource

    def validate(self):
        if self.ens_region_id_resource:
            for v1 in self.ens_region_id_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnsRegionIdResource'] = []
        if self.ens_region_id_resource is not None:
            for k1 in self.ens_region_id_resource:
                result['EnsRegionIdResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_region_id_resource = []
        if m.get('EnsRegionIdResource') is not None:
            for k1 in m.get('EnsRegionIdResource'):
                temp_model = main_models.DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource()
                self.ens_region_id_resource.append(temp_model.from_map(k1))

        return self

class DescribeEnsRegionIdResourceResponseBodyEnsRegionIdResourcesEnsRegionIdResource(DaraModel):
    def __init__(
        self,
        area: str = None,
        area_code: str = None,
        biz_date: str = None,
        ens_region_id: str = None,
        ens_region_id_name: str = None,
        instance_count: int = None,
        internet_bandwidth: int = None,
        isp: str = None,
        vcpu: int = None,
    ):
        # The region. Set the value to West.
        self.area = area
        # The code of the region.
        self.area_code = area_code
        # The date when the transaction was processed.
        self.biz_date = biz_date
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The name of the node.
        self.ens_region_id_name = ens_region_id_name
        # The number of instances.
        self.instance_count = instance_count
        # The public bandwidth of the instance. Unit: Bits/s.
        self.internet_bandwidth = internet_bandwidth
        # The ISP. Valid values:
        # 
        # *   cmcc: China Mobile
        # *   unicom: China Unicom
        # *   telecom: China Telecom
        # *   multiCarrier: multi-line ISP
        self.isp = isp
        # The number of vCPUs.
        self.vcpu = vcpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_id_name is not None:
            result['EnsRegionIdName'] = self.ens_region_id_name

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.internet_bandwidth is not None:
            result['InternetBandwidth'] = self.internet_bandwidth

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.vcpu is not None:
            result['VCpu'] = self.vcpu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIdName') is not None:
            self.ens_region_id_name = m.get('EnsRegionIdName')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InternetBandwidth') is not None:
            self.internet_bandwidth = m.get('InternetBandwidth')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('VCpu') is not None:
            self.vcpu = m.get('VCpu')

        return self

