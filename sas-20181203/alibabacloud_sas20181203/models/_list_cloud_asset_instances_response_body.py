# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCloudAssetInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListCloudAssetInstancesResponseBodyInstances] = None,
        page_info: main_models.ListCloudAssetInstancesResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the cloud assets.
        self.instances = instances
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListCloudAssetInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCloudAssetInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCloudAssetInstancesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of cloud assets.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAssetInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        alarm_status: str = None,
        asset_sub_type: str = None,
        asset_sub_type_name: str = None,
        asset_type: int = None,
        asset_type_name: str = None,
        created_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        region_id: str = None,
        risk_status: str = None,
        security_info: str = None,
        tags: List[str] = None,
        vendor: int = None,
        vendor_uid: str = None,
        vendor_user_name: str = None,
    ):
        # Indicates whether alerts are generated for the cloud asset. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.alarm_status = alarm_status
        # The subtype of the cloud service. The subtype of the cloud asset. Valid values:
        # 
        # *   **0**: ECS
        # 
        #     *   **0**: instance
        #     *   **1**: disk (storage)
        #     *   **2**: security group
        # 
        # *   **1**: SLB
        # 
        #     *   **0**: SLB
        #     *   **1**: Application Load Balancer (ALB)
        # 
        # *   **3**: ApsaraDB RDS
        # 
        #     *   **0**: instance
        # 
        # *   **4**: ApsaraDB for MongoDB
        # 
        #     *   **0**: instance
        # 
        # *   **5**: ApsaraDB for Redis
        # 
        #     *   **0**: instance
        # 
        # *   **6**: Container Registry
        # 
        #     *   **1**: Enterprise Edition
        #     *   **2**: Personal Edition
        # 
        # *   **8**: ACK
        # 
        #     *   **0**: cluster
        # 
        # *   **9**: VPC
        # 
        #     *   **0**: NAT gateway
        #     *   **1**: EIP
        #     *   **2**: VPN
        #     *   **3**: FLOW_LOG
        # 
        # *   **11**: ActionTrail
        # 
        #     *   **0**: trail
        # 
        # *   **12**: Alibaba Cloud CDN
        # 
        #     *   **0**: instance
        # 
        # *   **13**: Certificate Management Service (formerly SSL Certificates Service)
        # 
        #     *   **0**: certificate
        # 
        # *   **14**: Apsara Devops
        # 
        #     *   **0**: organization
        # 
        # *   **16**: Anti-DDoS
        # 
        #     *   **0**: instance
        # 
        # *   **17**: WAF
        # 
        #     *   **0**: domain name
        # 
        # *   **18**: OSS
        # 
        #     *   **0**: bucket
        # 
        # *   **19**: PolarDB
        # 
        #     *   **0**: cluster
        # 
        # *   **20**: ApsaraDB RDS for PostgreSQL
        # 
        #     *   **0**: instance
        # 
        # *   **21**: MSE
        # 
        #     *   **0**: cluster
        # 
        # *   **22**: NAS
        # 
        #     *   **0**: file system
        # 
        # *   **23**: DSC
        # 
        #     *   **0**: instance
        # 
        # *   **24**: EIP
        # 
        #     *   **0**: Anycast EIP
        # 
        # *   **25**: IDaaS EIAM
        # 
        #     *   **0**: instance
        # 
        # *   **26**: PolarDB-X
        # 
        #     *   **0**: instance
        # 
        # *   **27**: Elasticsearch
        # 
        #     *   **0**: instance
        self.asset_sub_type = asset_sub_type
        # The subtype name of the cloud asset.
        self.asset_sub_type_name = asset_sub_type_name
        # The type of the cloud asset. Valid values:
        # 
        # *   **0**: Elastic Compute Service (ECS)
        # *   **1**: Server Load Balancer (SLB)
        # *   **3**: ApsaraDB RDS
        # *   **4**: ApsaraDB for MongoDB
        # *   **5**: ApsaraDB for Redis
        # *   **6**: Container Registry
        # *   **8**: Container Service for Kubernetes (ACK)
        # *   **9**: Virtual Private Cloud (VPC)
        # *   **11**: ActionTrail
        # *   **12**: Alibaba Cloud CDN
        # *   **13**: Certificate Management Service (formerly SSL Certificates Service)
        # *   **14**: Apsara Devops
        # *   **16**: Anti-DDoS
        # *   **17**: Web Application Firewall (WAF)
        # *   **18**: Object Storage Service (OSS)
        # *   **19**: PolarDB
        # *   **20**: ApsaraDB RDS for PostgreSQL
        # *   **21**: Microservices Engine (MSE)
        # *   **22**: File Storage NAS (NAS)
        # *   **23**: Data Security Center (DSC)
        # *   **24**: Elastic IP Address (EIP)
        # *   **25**: Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM)
        # *   **26**: PolarDB-X
        # *   **27**: Elasticsearch
        self.asset_type = asset_type
        # The type name of the cloud asset.
        self.asset_type_name = asset_type_name
        # The time when the instance was created.
        self.created_time = created_time
        # The instance ID of the cloud asset.
        self.instance_id = instance_id
        # The instance name of the cloud asset.
        self.instance_name = instance_name
        # The public IP address of the cloud asset.
        self.internet_ip = internet_ip
        # The ID of the region to which the cloud asset belongs.
        self.region_id = region_id
        # Indicates whether risks are detected on the cloud asset. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.risk_status = risk_status
        # The security information about the cloud asset.
        self.security_info = security_info
        # Tag list.
        self.tags = tags
        # The service provider (SP) of the cloud asset. Valid values:
        # 
        # *   **0**: a cloud asset provided by Alibaba Cloud
        # *   **1**: a third-party cloud asset
        # *   **2**: a cloud asset in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight cloud asset
        self.vendor = vendor
        # The account ID of the multi-cloud instance.
        self.vendor_uid = vendor_uid
        # The user name of the multi-cloud instance.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.security_info is not None:
            result['SecurityInfo'] = self.security_info

        if self.tags is not None:
            result['Tags'] = self.tags

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SecurityInfo') is not None:
            self.security_info = m.get('SecurityInfo')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorUid') is not None:
            self.vendor_uid = m.get('VendorUid')

        if m.get('VendorUserName') is not None:
            self.vendor_user_name = m.get('VendorUserName')

        return self

