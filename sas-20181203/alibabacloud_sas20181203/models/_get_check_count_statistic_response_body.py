# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckCountStatisticResponseBody(DaraModel):
    def __init__(
        self,
        check_count_statistic_dto: main_models.GetCheckCountStatisticResponseBodyCheckCountStatisticDTO = None,
        request_id: str = None,
    ):
        # The risk item statistics.
        self.check_count_statistic_dto = check_count_statistic_dto
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_count_statistic_dto:
            self.check_count_statistic_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_count_statistic_dto is not None:
            result['CheckCountStatisticDTO'] = self.check_count_statistic_dto.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCountStatisticDTO') is not None:
            temp_model = main_models.GetCheckCountStatisticResponseBodyCheckCountStatisticDTO()
            self.check_count_statistic_dto = temp_model.from_map(m.get('CheckCountStatisticDTO'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCheckCountStatisticResponseBodyCheckCountStatisticDTO(DaraModel):
    def __init__(
        self,
        check_count_statistic_items: List[main_models.GetCheckCountStatisticResponseBodyCheckCountStatisticDTOCheckCountStatisticItems] = None,
        statistic_type: str = None,
    ):
        # The risk item statistics.
        self.check_count_statistic_items = check_count_statistic_items
        # The type of the statistics. Valid values:
        # 
        # *   **user**: the top five users that are granted excessive permissions.
        # *   **role**: the top five roles that are granted excessive permissions.
        # *   **instance**: the top five cloud services on which risks are detected.
        self.statistic_type = statistic_type

    def validate(self):
        if self.check_count_statistic_items:
            for v1 in self.check_count_statistic_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckCountStatisticItems'] = []
        if self.check_count_statistic_items is not None:
            for k1 in self.check_count_statistic_items:
                result['CheckCountStatisticItems'].append(k1.to_map() if k1 else None)

        if self.statistic_type is not None:
            result['StatisticType'] = self.statistic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_count_statistic_items = []
        if m.get('CheckCountStatisticItems') is not None:
            for k1 in m.get('CheckCountStatisticItems'):
                temp_model = main_models.GetCheckCountStatisticResponseBodyCheckCountStatisticDTOCheckCountStatisticItems()
                self.check_count_statistic_items.append(temp_model.from_map(k1))

        if m.get('StatisticType') is not None:
            self.statistic_type = m.get('StatisticType')

        return self

class GetCheckCountStatisticResponseBodyCheckCountStatisticDTOCheckCountStatisticItems(DaraModel):
    def __init__(
        self,
        cores: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_sub_type: int = None,
        instance_sub_type_name: str = None,
        instance_type: int = None,
        instance_type_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        os: str = None,
        region_id: str = None,
        risk_count: int = None,
        uuid: str = None,
        vendor: int = None,
        vpc_instance_id: str = None,
    ):
        # The number of the CPU cores used by the host instance.
        self.cores = cores
        # The instance ID of the cloud service.
        self.instance_id = instance_id
        # The instance name of the asset.
        self.instance_name = instance_name
        # The subtype of the cloud service.
        self.instance_sub_type = instance_sub_type
        # The asset subtype of the cloud service. Valid values:
        # 
        # *   If **InstanceTypeName** is set to **ECS**, this parameter supports the following valid values:
        # 
        #     *   **INSTANCE**
        #     *   **DISK**
        #     *   **SECURITY_GROUP**
        # 
        # *   If **InstanceTypeName** is set to **ACR**, this parameter supports the following valid values:
        # 
        #     *   **REPOSITORY_ENTERPRISE**
        #     *   **REPOSITORY_PERSON**
        # 
        # *   If **InstanceTypeName** is set to **RAM**, this parameter supports the following valid values:
        # 
        #     *   **ALIAS**
        #     *   **USER**
        #     *   **POLICY**
        #     *   **GROUP**
        # 
        # *   If **InstanceTypeName** is set to **WAF**, this parameter supports the following valid value:
        # 
        #     *   **DOMAIN**
        # 
        # *   If **InstanceTypeName** is set to other values, this parameter supports the following valid values:
        # 
        #     *   **INSTANCE**
        self.instance_sub_type_name = instance_sub_type_name
        # The asset type. Valid values:
        # 
        # *   **0**: Elastic Compute Service (ECS) instance.
        # *   **1**: Server Load Balancer (SLB) instance.
        # *   **2**: NAT gateway.
        # *   **3**: ApsaraDB RDS instance.
        # *   **4**: ApsaraDB for MongoDB (MongoDB) instance.
        # *   **5**: Tair (Redis OSS-compatible) (Tair) instance.
        # *   **6**: container image.
        # *   **7**: container.
        self.instance_type = instance_type
        # The asset type of the cloud service. Valid values:
        # 
        # *   **ECS**: ECS.
        # *   **SLB**: SLB.
        # *   **RDS**: ApsaraDB RDS.
        # *   **MONGODB**: ApsaraDB for MongoDB.
        # *   **KVSTORE**: Tair.
        # *   **ACR**: Container Registry.
        # *   **CSK**: Container Service for Kubernetes (ACK).
        # *   **VPC**: Virtual Private Cloud (VPC).
        # *   **ACTIONTRAIL**: ActionTrail.
        # *   **CDN**: Alibaba Cloud CDN (CDN).
        # *   **CAS**: Certificate Management Service (formerly SSL Certificates Service).
        # *   **RDC**: Alibaba Cloud DevOps.
        # *   **RAM**: Resource Access Management (RAM).
        # *   **DDOS**: Anti-DDoS.
        # *   **WAF**: Web Application Firewall (WAF).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **POLARDB**: PolarDB.
        # *   **POSTGRESQL**: ApsaraDB RDS for PostgreSQL.
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NAS**: File Storage NAS (NAS).
        # *   **SDDP**: Sensitive Data Discovery and Protection (SDDP).
        # *   **EIP**: Elastic IP Address (EIP).
        self.instance_type_name = instance_type_name
        # The public IP address of the host instance.
        self.internet_ip = internet_ip
        # The private IP address of the host instance.
        self.intranet_ip = intranet_ip
        # The version of the operating system that the host instance runs.
        self.os = os
        # The region.
        self.region_id = region_id
        # The number of risk items.
        self.risk_count = risk_count
        # The UUID of the host instance.
        self.uuid = uuid
        # The cloud service provider. Valid values:
        # 
        # *   **ALIYUN**: Alibaba Cloud.
        # *   **TENCENT**: Tencent Cloud.
        # *   **MICROSOFT**: Microsoft Azure.
        # *   **AWS**: AWS.
        self.vendor = vendor
        # The ID of the VPC to which the host instance belongs.
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_sub_type is not None:
            result['InstanceSubType'] = self.instance_sub_type

        if self.instance_sub_type_name is not None:
            result['InstanceSubTypeName'] = self.instance_sub_type_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_name is not None:
            result['InstanceTypeName'] = self.instance_type_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.os is not None:
            result['Os'] = self.os

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSubType') is not None:
            self.instance_sub_type = m.get('InstanceSubType')

        if m.get('InstanceSubTypeName') is not None:
            self.instance_sub_type_name = m.get('InstanceSubTypeName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeName') is not None:
            self.instance_type_name = m.get('InstanceTypeName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        return self

