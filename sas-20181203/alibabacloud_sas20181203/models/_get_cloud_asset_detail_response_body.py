# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCloudAssetDetailResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        instances: List[main_models.GetCloudAssetDetailResponseBodyInstances] = None,
        request_id: str = None,
    ):
        # The number of instances in the list of cloud assets returned.
        self.count = count
        # An array that consists of the details of the cloud assets.
        self.instances = instances
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.GetCloudAssetDetailResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudAssetDetailResponseBodyInstances(DaraModel):
    def __init__(
        self,
        alarm_status: str = None,
        asset_sub_type: int = None,
        asset_sub_type_name: str = None,
        asset_type: int = None,
        asset_type_name: str = None,
        created_time: int = None,
        detail_link: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        original_asset_info: str = None,
        region_id: str = None,
        risk_status: str = None,
        security_info: str = None,
        vendor: int = None,
        vendor_uid: str = None,
        vendor_user_name: str = None,
    ):
        # Indicates whether alerts are generated for the current cloud asset. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.alarm_status = alarm_status
        # The subtype of the cloud asset.
        self.asset_sub_type = asset_sub_type
        # The name of the cloud asset subtype.
        self.asset_sub_type_name = asset_sub_type_name
        # The type of the cloud asset. Valid values:
        # 
        # *   **0**: ECS.
        # *   **1**: SLB.
        # *   **3**: ApsaraDB RDS.
        # *   **4**: ApsaraDB for MongoDB.
        # *   **5**: ApsaraDB for Redis.
        # *   **6**: Container Registry.
        # *   **8**: Container Service for Kubernetes.
        # *   **9**: VPC.
        # *   **11**: ActionTrail.
        # *   **12**: CDN.
        # *   **13**: Certificate Management Service.
        # *   **14**: Apsara Devops.
        # *   **15**: RAM.
        # *   **16**: Anti-DDoS.
        # *   **17**: WAF.
        # *   **18**: OSS.
        # *   **19**: PolarDB.
        # *   **20**: ApsaraDB RDS for PostgreSQL.
        # *   **21**: MSE.
        # *   **22**: NAS.
        # *   **23**: DSC.
        # *   **24**: EIP.
        # *   **25**: IDaaS-EIAM.
        # *   **26**: PolarDB-X.
        # *   **27**: Elasticsearch.
        self.asset_type = asset_type
        # The name of the cloud asset type.
        self.asset_type_name = asset_type_name
        # The time when the instance was created. The value is a timestamp.
        self.created_time = created_time
        # The detailed address of the cloud asset.
        self.detail_link = detail_link
        # The instance ID of the cloud asset.
        self.instance_id = instance_id
        # The instance name of the cloud asset.
        self.instance_name = instance_name
        # The public IP address of the instance.
        self.internet_ip = internet_ip
        # Detailed asset information.
        self.original_asset_info = original_asset_info
        # The region in which the cloud asset resides.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # Indicates whether risks are detected on the current cloud asset. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.risk_status = risk_status
        # The security information about the cloud asset.
        self.security_info = security_info
        # The service provider of the cloud asset. Valid values:
        # 
        # *   **0**: Alibaba Cloud.
        # *   **1**: service provider that is unrecognized.
        # *   **2**: data center.
        # *   **3**, **4**, **5**, and **7**: third-party service provider.
        # *   **8**: simple application server.
        self.vendor = vendor
        # Account id for multi-cloud instances.
        self.vendor_uid = vendor_uid
        # The account name of the multi-cloud instance.
        self.vendor_user_name = vendor_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status

        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_sub_type_name is not None:
            result['AssetSubTypeName'] = self.asset_sub_type_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.asset_type_name is not None:
            result['AssetTypeName'] = self.asset_type_name

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.detail_link is not None:
            result['DetailLink'] = self.detail_link

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.original_asset_info is not None:
            result['OriginalAssetInfo'] = self.original_asset_info

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.security_info is not None:
            result['SecurityInfo'] = self.security_info

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_uid is not None:
            result['VendorUid'] = self.vendor_uid

        if self.vendor_user_name is not None:
            result['VendorUserName'] = self.vendor_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')

        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetSubTypeName') is not None:
            self.asset_sub_type_name = m.get('AssetSubTypeName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AssetTypeName') is not None:
            self.asset_type_name = m.get('AssetTypeName')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DetailLink') is not None:
            self.detail_link = m.get('DetailLink')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('OriginalAssetInfo') is not None:
            self.original_asset_info = m.get('OriginalAssetInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SecurityInfo') is not None:
            self.security_info = m.get('SecurityInfo')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorUid') is not None:
            self.vendor_uid = m.get('VendorUid')

        if m.get('VendorUserName') is not None:
            self.vendor_user_name = m.get('VendorUserName')

        return self

