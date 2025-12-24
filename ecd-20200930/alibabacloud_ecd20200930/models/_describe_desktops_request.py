# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopsRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        desktop_group_id: str = None,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_status_list: List[str] = None,
        desktop_type: str = None,
        directory_id: str = None,
        end_user_id: List[str] = None,
        excluded_end_user_id: List[str] = None,
        expired_time: str = None,
        fill_resource_group: bool = None,
        filter_desktop_group: bool = None,
        gpu_instance_group_id: str = None,
        group_id: str = None,
        image_id: List[str] = None,
        include_auto_snapshot_policy: bool = None,
        management_flag: str = None,
        max_results: int = None,
        multi_resource: bool = None,
        next_token: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        only_desktop_group: bool = None,
        os_types: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        policy_group_id: str = None,
        protocol_type: str = None,
        qos_rule_id: str = None,
        query_fota_update: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        snapshot_policy_id: str = None,
        sub_pay_type: str = None,
        tag: List[main_models.DescribeDesktopsRequestTag] = None,
        user_name: str = None,
    ):
        # The billing method of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Postpaid (default): pay-as-you-go
        # *   PrePaid: subscription
        self.charge_type = charge_type
        # The ID of the cloud computer pool. If you specify `OnlyDesktopGroup`, ignore `DesktopGroupId`. If you leave `DesktopId` empty, all IDs of the cloud computers in the cloud computer pool are queried.````
        self.desktop_group_id = desktop_group_id
        # The cloud computer IDs. You can specify the IDs of 1 to 100 cloud computers.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The cloud computer status.
        # 
        # Valid values:
        # 
        # *   Stopped
        # *   Starting
        # *   Rebuilding
        # *   Running
        # *   Stopping
        # *   Expired
        # *   Deleted
        # *   Pending
        self.desktop_status = desktop_status
        # The list of cloud computer status.
        self.desktop_status_list = desktop_status_list
        # The cloud computer type. You can call the [DescribeDesktopTypes](https://help.aliyun.com/document_detail/188882.html) operation to query the IDs of all supported types.
        self.desktop_type = desktop_type
        # The directory ID, which is the same as the office network ID.
        self.directory_id = directory_id
        # The authorized users of the cloud computer. You can specify the IDs of 1 to 100 users.
        # 
        # >  During a specific period of time, only one user can connect to and use the cloud computer.
        self.end_user_id = end_user_id
        # The list of authorized users that you want to exclude from the cloud computer. You can specify the IDs of 1 to 100 users.
        self.excluded_end_user_id = excluded_end_user_id
        # The time when a subscription cloud computer expires.
        self.expired_time = expired_time
        # Specifies whether to query the information about the enterprise resource group.
        self.fill_resource_group = fill_resource_group
        # Specifies whether to exclude pooled cloud computers.
        # 
        # Valid values:
        # 
        # *   true (default)
        # *   false
        self.filter_desktop_group = filter_desktop_group
        # The ID of the elastic GPU pool.
        self.gpu_instance_group_id = gpu_instance_group_id
        # The ID of the cloud computer pool.
        self.group_id = group_id
        # The IDs of the images.
        self.image_id = image_id
        self.include_auto_snapshot_policy = include_auto_snapshot_policy
        # The flag that is used to manage the cloud desktops.
        self.management_flag = management_flag
        # The number of entries per page.
        # 
        # *   Maximum value: 100
        # *   Default value: 10
        self.max_results = max_results
        # Specifies whether the shared group is a multi-cloud computer type.
        # 
        # Valid values:
        # 
        # - true: a multi-cloud computer type.
        # - false: a single-cloud computer type.
        self.multi_resource = multi_resource
        # The token that determines the start point of the next query. If this parameter is left empty, all results are returned.
        self.next_token = next_token
        # The office network ID.
        self.office_site_id = office_site_id
        # The office network name.
        self.office_site_name = office_site_name
        # Specifies whether to query pooled cloud computers.
        self.only_desktop_group = only_desktop_group
        # The operating systems (OSs).
        self.os_types = os_types
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the cloud computer policy.
        self.policy_group_id = policy_group_id
        # The protocol.
        # 
        # Valid values:
        # 
        # *   HDX: High-definition Experience (HDX) protocol
        # *   ASP: in-house Adaptive Streaming Protocol (ASP) (recommended)
        self.protocol_type = protocol_type
        # The ID of the network throttling rule.
        self.qos_rule_id = qos_rule_id
        # Specifies whether to query the image update information about the cloud computer.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.query_fota_update = query_fota_update
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group.
        self.resource_group_id = resource_group_id
        # The ID of the snapshot policy.
        self.snapshot_policy_id = snapshot_policy_id
        # The billing method of the cloud computer.
        # 
        # Valid values:
        # 
        # *   duration: hourly plan (available for users in the whitelist)
        # *   postPaid: pay-as-you-go
        # *   monthPackage: monthly subscription (120-hour or 250-hour computing plan)
        # *   prePaid: monthly subscription (unlimited-hour computing plan)
        self.sub_pay_type = sub_pay_type
        # The tags that you want to add to the cloud computer. A tag is a key-value pair that consists of a tag key and a tag value. Tags are used to identify resources. You can use tags to manage cloud computers by group. This facilitates search and batch operations. For more information, see [Use tags to manage cloud computers](https://help.aliyun.com/document_detail/203781.html).
        self.tag = tag
        # The name of the end user.
        self.user_name = user_name

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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.desktop_status_list is not None:
            result['DesktopStatusList'] = self.desktop_status_list

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.excluded_end_user_id is not None:
            result['ExcludedEndUserId'] = self.excluded_end_user_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.fill_resource_group is not None:
            result['FillResourceGroup'] = self.fill_resource_group

        if self.filter_desktop_group is not None:
            result['FilterDesktopGroup'] = self.filter_desktop_group

        if self.gpu_instance_group_id is not None:
            result['GpuInstanceGroupId'] = self.gpu_instance_group_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.include_auto_snapshot_policy is not None:
            result['IncludeAutoSnapshotPolicy'] = self.include_auto_snapshot_policy

        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.multi_resource is not None:
            result['MultiResource'] = self.multi_resource

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.only_desktop_group is not None:
            result['OnlyDesktopGroup'] = self.only_desktop_group

        if self.os_types is not None:
            result['OsTypes'] = self.os_types

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.query_fota_update is not None:
            result['QueryFotaUpdate'] = self.query_fota_update

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snapshot_policy_id is not None:
            result['SnapshotPolicyId'] = self.snapshot_policy_id

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('DesktopStatusList') is not None:
            self.desktop_status_list = m.get('DesktopStatusList')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExcludedEndUserId') is not None:
            self.excluded_end_user_id = m.get('ExcludedEndUserId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FillResourceGroup') is not None:
            self.fill_resource_group = m.get('FillResourceGroup')

        if m.get('FilterDesktopGroup') is not None:
            self.filter_desktop_group = m.get('FilterDesktopGroup')

        if m.get('GpuInstanceGroupId') is not None:
            self.gpu_instance_group_id = m.get('GpuInstanceGroupId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('IncludeAutoSnapshotPolicy') is not None:
            self.include_auto_snapshot_policy = m.get('IncludeAutoSnapshotPolicy')

        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MultiResource') is not None:
            self.multi_resource = m.get('MultiResource')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('OnlyDesktopGroup') is not None:
            self.only_desktop_group = m.get('OnlyDesktopGroup')

        if m.get('OsTypes') is not None:
            self.os_types = m.get('OsTypes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('QueryFotaUpdate') is not None:
            self.query_fota_update = m.get('QueryFotaUpdate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnapshotPolicyId') is not None:
            self.snapshot_policy_id = m.get('SnapshotPolicyId')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDesktopsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. If you specify the `Tag` parameter, you must also specify the `Key` parameter. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun` and contain only spaces.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
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

