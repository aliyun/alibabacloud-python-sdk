# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerSpecResponseBody(DaraModel):
    def __init__(
        self,
        load_balancer_specs: List[main_models.DescribeLoadBalancerSpecResponseBodyLoadBalancerSpecs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The specifications. Valid values:
        self.load_balancer_specs = load_balancer_specs
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.load_balancer_specs:
            for v1 in self.load_balancer_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancerSpecs'] = []
        if self.load_balancer_specs is not None:
            for k1 in self.load_balancer_specs:
                result['LoadBalancerSpecs'].append(k1.to_map() if k1 else None)

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
        self.load_balancer_specs = []
        if m.get('LoadBalancerSpecs') is not None:
            for k1 in m.get('LoadBalancerSpecs'):
                temp_model = main_models.DescribeLoadBalancerSpecResponseBodyLoadBalancerSpecs()
                self.load_balancer_specs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLoadBalancerSpecResponseBodyLoadBalancerSpecs(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        load_balancer_spec: str = None,
    ):
        # The display name of the instance type.
        self.display_name = display_name
        # The specifications of the ELB instance.
        self.load_balancer_spec = load_balancer_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        return self

