# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticityAssuranceInstancesResponseBody(DaraModel):
    def __init__(
        self,
        elasticity_assurance_item: main_models.DescribeElasticityAssuranceInstancesResponseBodyElasticityAssuranceItem = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the instances that match and use the elasticity assurance.
        self.elasticity_assurance_item = elasticity_assurance_item
        # The number of entries returned per page.
        self.max_results = max_results
        # The token used to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.elasticity_assurance_item:
            self.elasticity_assurance_item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elasticity_assurance_item is not None:
            result['ElasticityAssuranceItem'] = self.elasticity_assurance_item.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticityAssuranceItem') is not None:
            temp_model = main_models.DescribeElasticityAssuranceInstancesResponseBodyElasticityAssuranceItem()
            self.elasticity_assurance_item = temp_model.from_map(m.get('ElasticityAssuranceItem'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeElasticityAssuranceInstancesResponseBodyElasticityAssuranceItem(DaraModel):
    def __init__(
        self,
        instance_id_set: List[main_models.DescribeElasticityAssuranceInstancesResponseBodyElasticityAssuranceItemInstanceIdSet] = None,
    ):
        self.instance_id_set = instance_id_set

    def validate(self):
        if self.instance_id_set:
            for v1 in self.instance_id_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceIdSet'] = []
        if self.instance_id_set is not None:
            for k1 in self.instance_id_set:
                result['InstanceIdSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_id_set = []
        if m.get('InstanceIdSet') is not None:
            for k1 in m.get('InstanceIdSet'):
                temp_model = main_models.DescribeElasticityAssuranceInstancesResponseBodyElasticityAssuranceItemInstanceIdSet()
                self.instance_id_set.append(temp_model.from_map(k1))

        return self

class DescribeElasticityAssuranceInstancesResponseBodyElasticityAssuranceItemInstanceIdSet(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The instance ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

