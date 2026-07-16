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
        # The information about assets protected by Cloud Firewall.
        self.assets = assets
        # The request ID.
        self.request_id = request_id
        # The total number of assets protected by Cloud Firewall.
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
        # > The primary account of the Cloud Firewall member account.
        self.ali_uid = ali_uid
        # The ID of the bound asset instance.
        self.bind_instance_id = bind_instance_id
        # The name of the bound asset instance.
        self.bind_instance_name = bind_instance_name
        # The time when Cloud Firewall discovered the asset. Time format: YYYY-MM-DD HH:mm:ss.
        self.create_time_stamp = create_time_stamp
        # The public IP address of the server.
        self.internet_address = internet_address
        # The private IP address of the server.
        self.intranet_address = intranet_address
        # The IP address version of the asset protected by Cloud Firewall.
        # 
        # Valid values:
        # 
        # - **4**: Indicates an IPv4 address.
        # 
        # - **6**: Indicates an IPv6 address.
        self.ip_version = ip_version
        # The outbound traffic in the last 7 days.
        self.last_7day_out_traffic_bytes = last_7day_out_traffic_bytes
        # The UID of the Cloud Firewall member account.
        self.member_uid = member_uid
        # The instance name of the asset protected by Cloud Firewall.
        self.name = name
        # The time when the asset was discovered. Valid values:
        # - **discovered in 1 hour**: The asset was discovered within 1 hour.
        # - **discovered in 1 day**: The asset was discovered within 1 day.
        # - **discovered in 7 days**: The asset was discovered within 7 days.
        self.new_resource_tag = new_resource_tag
        # The remarks of the asset. Valid values:
        # 
        # - **REGION_NOT_SUPPORT**: Region not supported.
        # - **NETWORK_NOT_SUPPORT**: Network not supported.
        self.note = note
        # The firewall status. Valid values:
        # 
        # - **open**: Protected.
        # - **opening**: Protection enabling.
        # - **closed**: Not protected.
        # - **closing**: Protection disabling.
        self.protect_status = protect_status
        # The region ID of the asset.
        self.region_id = region_id
        # Indicates whether the region of the asset supports enabling Cloud Firewall protection. Valid values:
        # 
        # - **enable**: Supported.
        # - **disable**: Not supported.
        self.region_status = region_status
        # The asset instance ID.
        self.resource_instance_id = resource_instance_id
        # The asset type. Valid values:
        # 
        # - **BastionHostEgressIP**: Bastion host egress IP.
        # - **BastionHostIngressIP**: Bastion host ingress IP.
        # - **EcsEIP**: ECS EIP.
        # - **EcsPublicIP**: ECS public IP.
        # - **EIP**: Elastic IP address.
        # - **EniEIP**: Elastic network interface EIP.
        # - **NatEIP**: NAT EIP.
        # - **SlbEIP**: SLB EIP (CLB EIP).
        # - **SlbPublicIP**: SLB public IP (CLB public IP).
        # - **NatPublicIP**: NAT public IP.
        # - **HAVIP**: High-availability virtual IP.
        # - **NlbEIP**: NLB EIP.
        # - **ApiGatewayEIP**: API Gateway public IP.
        # - **AlbEIP**: ALB EIP.
        # - **AiGatewayEIP**: AI Gateway public IP.
        # - **GaEIP**: GA EIP.
        # - **SwasEIP**: Simple Application Server public IP.
        # - **EcdEIP**: Elastic Desktop Service public IP.
        # - **BastionHostIP**: Bastion host IP.
        self.resource_type = resource_type
        # The risk level of the asset. Valid values:
        # 
        # - **low**: Low risk.
        # 
        # - **middle**: Medium risk.
        # 
        # - **hight**: High risk.
        # 
        # > This parameter is returned only when the value of UserType is free.
        self.risk_level = risk_level
        # The status of data leakage detection.
        self.sensitive_data_status = sensitive_data_status
        # The security group policy. Valid values:
        # 
        # - **pass**: Delivered.
        # - **block**: Not delivered.
        # - **unsupport**: Not supported.
        self.sg_status = sg_status
        # The last security group status detection time, in timestamp format. Unit: seconds.
        self.sg_status_time = sg_status_time
        # The traffic diversion support status of the asset. Valid values:
        # 
        # - **enable**: Traffic diversion supported.
        # - **disable**: Traffic diversion not supported.
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

