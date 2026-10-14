# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeElbAvailableResourceInfoResponseBody(DaraModel):
    def __init__(
        self,
        elb_available_resource_info: List[main_models.DescribeElbAvailableResourceInfoResponseBodyElbAvailableResourceInfo] = None,
        request_id: str = None,
    ):
        # The collection of resource information.
        self.elb_available_resource_info = elb_available_resource_info
        # The common parameter. The ID of the request. Each request has a unique ID, which is active for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.elb_available_resource_info:
            for v1 in self.elb_available_resource_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ElbAvailableResourceInfo'] = []
        if self.elb_available_resource_info is not None:
            for k1 in self.elb_available_resource_info:
                result['ElbAvailableResourceInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elb_available_resource_info = []
        if m.get('ElbAvailableResourceInfo') is not None:
            for k1 in m.get('ElbAvailableResourceInfo'):
                temp_model = main_models.DescribeElbAvailableResourceInfoResponseBodyElbAvailableResourceInfo()
                self.elb_available_resource_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeElbAvailableResourceInfoResponseBodyElbAvailableResourceInfo(DaraModel):
    def __init__(
        self,
        ability: List[str] = None,
        area: str = None,
        can_buy_count: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        load_balancer_spec: List[str] = None,
        name: str = None,
        province: str = None,
    ):
        self.ability = ability
        # The area.
        self.area = area
        # The quantity available for purchase.
        self.can_buy_count = can_buy_count
        # The English name of the edge zone.
        self.en_name = en_name
        # The ID of the ENS edge zone.
        self.ens_region_id = ens_region_id
        # The specification of the load balancing instance.
        self.load_balancer_spec = load_balancer_spec
        # The name of the edge zone.
        self.name = name
        # The province.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability is not None:
            result['Ability'] = self.ability

        if self.area is not None:
            result['Area'] = self.area

        if self.can_buy_count is not None:
            result['CanBuyCount'] = self.can_buy_count

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.name is not None:
            result['Name'] = self.name

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ability') is not None:
            self.ability = m.get('Ability')

        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('CanBuyCount') is not None:
            self.can_buy_count = m.get('CanBuyCount')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

