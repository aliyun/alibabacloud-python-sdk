# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAssetListResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.DescribeAssetListResponseBodyAssets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The assets that are protected by Cloud Firewall.
        self.assets = assets
        # The ID of the request.
        self.request_id = request_id
        # The total number of the assets that are protected by Cloud Firewall.
        self.total_count = total_count

    def validate(self):
        if self.assets:
            for v1 in self.assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assets'] = []
        if self.assets is not None:
            for k1 in self.assets:
                result['Assets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.DescribeAssetListResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAssetListResponseBodyAssets(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        bind_instance_id: str = None,
        bind_instance_name: str = None,
        create_time_stamp: str = None,
        internet_address: str = None,
        intranet_address: str = None,
        ip_version: int = None,
        last_7day_out_traffic_bytes: int = None,
        member_uid: int = None,
        name: str = None,
        new_resource_tag: str = None,
        note: str = None,
        protect_status: str = None,
        region_id: str = None,
        region_status: str = None,
        resource_instance_id: str = None,
        resource_type: str = None,
        risk_level: str = None,
        sensitive_data_status: str = None,
        sg_status: str = None,
        sg_status_time: int = None,
        sync_status: str = None,
        type: str = None,
    ):
        # The UID of the Alibaba Cloud account.
        # 
        # >  The value of this parameter indicates the management account to which the member is added.
        self.ali_uid = ali_uid
        # The ID of the cloud resource with which the asset is associated.
        self.bind_instance_id = bind_instance_id
        # The instance name of the asset.
        self.bind_instance_name = bind_instance_name
        # The timestamp when the asset is added to Cloud Firewall.
        self.create_time_stamp = create_time_stamp
        # The public IP address of the server.
        self.internet_address = internet_address
        # The internal IP address of the server.
        self.intranet_address = intranet_address
        # The IP version of the asset that is protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # *   **4**: IPv4
        # *   **6**: IPv6
        self.ip_version = ip_version
        # Outbound traffic in the last 7 days.
        self.last_7day_out_traffic_bytes = last_7day_out_traffic_bytes
        # The UID of the member.
        self.member_uid = member_uid
        # The instance name of the asset that is protected by Cloud Firewall.
        self.name = name
        # The time when the asset was added. Valid values:
        # 
        # *   **discovered in 1 hour**: within one hour.
        # *   **discovered in 1 day**: within one day.
        # *   **discovered in 7 days**: within seven days.
        self.new_resource_tag = new_resource_tag
        # The remarks of the asset. Valid values:
        # 
        # *   **REGION_NOT_SUPPORT**: The region is not supported.
        # *   **NETWORK_NOT_SUPPORT**: The network is not supported.
        self.note = note
        # The status of the firewall. Valid values:
        # 
        # *   **open**: enabled.
        # *   **opening**: being enabled.
        # *   **closed**: disabled.
        # *   **closing**: being disabled.
        self.protect_status = protect_status
        # The ID of the region in which the asset resides.
        self.region_id = region_id
        # Indicates whether the firewall is supported in the region in which the asset resides. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The instance ID of the asset.
        self.resource_instance_id = resource_instance_id
        # The type of the asset. Valid values:
        # 
        # *   **BastionHostEgressIP**: the egress IP address of a bastion host
        # *   **BastionHostIngressIP**: the ingress IP address of a bastion host
        # *   **EcsEIP**: the elastic IP address (EIP) of an Elastic Compute Service (ECS) instance
        # *   **EcsPublicIP**: the public IP address of an ECS instance
        # *   **EIP**: the EIP
        # *   **EniEIP**: the EIP of an elastic network interface (ENI)
        # *   **NatEIP**: the EIP of a NAT gateway
        # *   **SlbEIP**: the EIP of a Server Load Balancer (SLB) instance
        # *   **SlbPublicIP**: the public IP address of an SLB instance
        # *   **NatPublicIP**: the public IP address of a NAT gateway
        # *   **HAVIP**: the high-availability virtual IP address (HAVIP)
        self.resource_type = resource_type
        # The risk level of the asset. Valid values:
        # 
        # *   **low**: low
        # *   **middle**: medium
        # *   **hight**: high
        # 
        # >  The value of this parameter is returned only when the UserType parameter is set to free.
        self.risk_level = risk_level
        # Data leakage detection enabled status.
        self.sensitive_data_status = sensitive_data_status
        # The status of the security group policy. Valid values:
        # 
        # *   **pass**: applied
        # *   **block**: not applied
        # *   **unsupport**: unsupported
        self.sg_status = sg_status
        # The time when the status of the security group was last checked. The value is a UNIX timestamp. Unit: seconds.
        self.sg_status_time = sg_status_time
        # Indicates whether traffic redirection is supported for the asset. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.sync_status = sync_status
        # This parameter is deprecated.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id

        if self.bind_instance_name is not None:
            result['BindInstanceName'] = self.bind_instance_name

        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp

        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address

        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.last_7day_out_traffic_bytes is not None:
            result['Last7DayOutTrafficBytes'] = self.last_7day_out_traffic_bytes

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.name is not None:
            result['Name'] = self.name

        if self.new_resource_tag is not None:
            result['NewResourceTag'] = self.new_resource_tag

        if self.note is not None:
            result['Note'] = self.note

        if self.protect_status is not None:
            result['ProtectStatus'] = self.protect_status

        if self.region_id is not None:
            result['RegionID'] = self.region_id

        if self.region_status is not None:
            result['RegionStatus'] = self.region_status

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sensitive_data_status is not None:
            result['SensitiveDataStatus'] = self.sensitive_data_status

        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status

        if self.sg_status_time is not None:
            result['SgStatusTime'] = self.sg_status_time

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')

        if m.get('BindInstanceName') is not None:
            self.bind_instance_name = m.get('BindInstanceName')

        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')

        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')

        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Last7DayOutTrafficBytes') is not None:
            self.last_7day_out_traffic_bytes = m.get('Last7DayOutTrafficBytes')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewResourceTag') is not None:
            self.new_resource_tag = m.get('NewResourceTag')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ProtectStatus') is not None:
            self.protect_status = m.get('ProtectStatus')

        if m.get('RegionID') is not None:
            self.region_id = m.get('RegionID')

        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SensitiveDataStatus') is not None:
            self.sensitive_data_status = m.get('SensitiveDataStatus')

        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')

        if m.get('SgStatusTime') is not None:
            self.sg_status_time = m.get('SgStatusTime')

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

