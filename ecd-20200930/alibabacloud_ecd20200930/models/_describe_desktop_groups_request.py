# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopGroupsRequest(DaraModel):
    def __init__(
        self,
        bundle_id: List[str] = None,
        desktop_group_id: str = None,
        desktop_group_ids: List[str] = None,
        desktop_group_name: str = None,
        desktop_type: str = None,
        end_user_ids: List[str] = None,
        excluded_end_user_ids: List[str] = None,
        image_id: List[str] = None,
        max_results: int = None,
        multi_resource: bool = None,
        next_token: str = None,
        office_site_id: str = None,
        own_type: int = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        protocol_type: str = None,
        qos_rule_id: str = None,
        region_id: str = None,
        status: int = None,
        tag: List[main_models.DescribeDesktopGroupsRequestTag] = None,
    ):
        # The list of cloud computer template IDs.
        self.bundle_id = bundle_id
        # The ID of the shared cloud computer.
        self.desktop_group_id = desktop_group_id
        # The list of shared cloud computer IDs.
        self.desktop_group_ids = desktop_group_ids
        # The name of the shared cloud computer to query. Fuzzy match is supported.
        self.desktop_group_name = desktop_group_name
        # The cloud computer specifications. You can call [DescribeDesktopTypes](~~DescribeDesktopTypes~~) to query the supported specification IDs.
        self.desktop_type = desktop_type
        # The list of authorized user IDs for the shared cloud computer.
        self.end_user_ids = end_user_ids
        # The list of authorized users to exclude.
        self.excluded_end_user_ids = excluded_end_user_ids
        # The list of image IDs.
        self.image_id = image_id
        # The number of entries per page for a paged query.
        self.max_results = max_results
        # Specifies whether the shared cloud computer is a multi-host type.
        # 
        # Valid values:
        # - true: Multi-host shared cloud computer.
        # - false: Single-host shared cloud computer.
        self.multi_resource = multi_resource
        # The token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # The ID of the office network to which the shared cloud computers belong.
        self.office_site_id = office_site_id
        # The type of the shared cloud computer.
        self.own_type = own_type
        # The subscription duration of the shared cloud computer. The unit is specified by `PeriodUnit`.
        self.period = period
        # The unit of the duration for the subscription billing method.
        self.period_unit = period_unit
        # The ID of the policy associated with the shared cloud computer.
        self.policy_group_id = policy_group_id
        # The protocol type.
        self.protocol_type = protocol_type
        # The ID of the QoS rule.
        self.qos_rule_id = qos_rule_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The status of the shared cloud computer.
        self.status = status
        # The list of tags. You can specify 1 to 20 tags.
        self.tag = tag

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
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.excluded_end_user_ids is not None:
            result['ExcludedEndUserIds'] = self.excluded_end_user_ids

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.multi_resource is not None:
            result['MultiResource'] = self.multi_resource

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('ExcludedEndUserIds') is not None:
            self.excluded_end_user_ids = m.get('ExcludedEndUserIds')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MultiResource') is not None:
            self.multi_resource = m.get('MultiResource')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDesktopGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDesktopGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. If you specify this parameter, the value cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
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

