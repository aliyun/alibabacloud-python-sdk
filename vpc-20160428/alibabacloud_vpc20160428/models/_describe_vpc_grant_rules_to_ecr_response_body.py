# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcGrantRulesToEcrResponseBody(DaraModel):
    def __init__(
        self,
        grant_rule_models: List[main_models.DescribeVpcGrantRulesToEcrResponseBodyGrantRuleModels] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The authorization information.
        self.grant_rule_models = grant_rule_models
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   ****
        self.next_token = next_token
        # The unique ID that Alibaba Cloud generates for the request.
        self.request_id = request_id
        # The total number of instances queried. If you specify the MaxResults and NextToken request parameters to perform a paged query, the value of the TotalCount response parameter is invalid.
        self.total_count = total_count

    def validate(self):
        if self.grant_rule_models:
            for v1 in self.grant_rule_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantRuleModels'] = []
        if self.grant_rule_models is not None:
            for k1 in self.grant_rule_models:
                result['GrantRuleModels'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_rule_models = []
        if m.get('GrantRuleModels') is not None:
            for k1 in m.get('GrantRuleModels'):
                temp_model = main_models.DescribeVpcGrantRulesToEcrResponseBodyGrantRuleModels()
                self.grant_rule_models.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcGrantRulesToEcrResponseBodyGrantRuleModels(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        ecr_id: str = None,
        ecr_owner_id: int = None,
        instance_id: str = None,
        instance_uid: int = None,
        region_no: str = None,
        type: str = None,
    ):
        # The creation time in milliseconds.
        self.creation_time = creation_time
        # The ECR ID.
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account to which the ECR belongs.
        self.ecr_owner_id = ecr_owner_id
        # The ID of the network instance.
        self.instance_id = instance_id
        # The ID of the Alibaba Cloud account to which the instance belongs.
        self.instance_uid = instance_uid
        # The ID of the region where the instance is deployed.
        self.region_no = region_no
        # The type of instance. Valid values:
        # 
        # *   **VBR**: queries the permissions that are granted to a VBR.
        # *   **VPC**: queries the permissions that are granted from a VPC.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.ecr_owner_id is not None:
            result['EcrOwnerId'] = self.ecr_owner_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_uid is not None:
            result['InstanceUid'] = self.instance_uid

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('EcrOwnerId') is not None:
            self.ecr_owner_id = m.get('EcrOwnerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceUid') is not None:
            self.instance_uid = m.get('InstanceUid')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

