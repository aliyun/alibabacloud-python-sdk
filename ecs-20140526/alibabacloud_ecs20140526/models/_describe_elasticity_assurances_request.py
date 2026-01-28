# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticityAssurancesRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.DescribeElasticityAssurancesRequestPrivatePoolOptions = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        package_type: str = None,
        platform: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tag: List[main_models.DescribeElasticityAssurancesRequestTag] = None,
        zone_id: str = None,
    ):
        self.private_pool_options = private_pool_options
        # The billing method of the instance. Set the value to PostPaid. Only pay-as-you-go instances can be created by using elasticity assurances.
        # 
        # Default value: PostPaid.
        self.instance_charge_type = instance_charge_type
        # The instance type.
        self.instance_type = instance_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The type of the elasticity assurance. Valid values:
        # 
        # *   ElasticityAssurance: the general-purpose elasticity assurance. RecurrenceRules is not specified for a general-purpose elasticity assurance.
        # *   TimeDivisionElasticityAssurance: the time-segmented elasticity assurance. RecurrenceRules is specified for a time-segmented assurance.
        self.package_type = package_type
        # > This parameter is deprecated.
        self.platform = platform
        # The region ID of the elasticity assurances. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If you configure this parameter to query resources, up to 1,000 resources that belong to the specified resource group can be displayed in the response.
        # 
        # > Resources in the default resource group are displayed in the response regardless of whether you configure this parameter.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the elasticity assurance. Valid values:
        # 
        # *   All: All states.
        # *   Deactivated: The elasticity assurance is pending activation. This state is in invitational preview.
        # *   Preparing: The elasticity assurance is being prepared.
        # *   Prepared: The elasticity assurance is to take effect.
        # *   Active: The elasticity assurance is in effect.
        # *   Released: The elasticity assurance is released.
        # 
        # If you do not specify this parameter, elasticity assurances in states other than Pending and Released are queried.
        self.status = status
        # The tags.
        self.tag = tag
        # The zone ID of the elasticity assurances.
        self.zone_id = zone_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.DescribeElasticityAssurancesRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeElasticityAssurancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeElasticityAssurancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: 1 to 20.
        # 
        # If you specify a tag to query resources, up to 1,000 resources with this tag are returned in the response. If you specify multiple tags to query resources, up to 1,000 resources with all these tags are returned in the response. To query more than 1,000 resources that have specified tags added, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
        self.key = key
        # The value of tag N. Valid values of N: 1 to 20.
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

class DescribeElasticityAssurancesRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # The IDs of the elasticity assurances. The value can be a JSON array that consists of up to 100 elasticity assurance IDs. Separate the IDs with commas (,).
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        return self

