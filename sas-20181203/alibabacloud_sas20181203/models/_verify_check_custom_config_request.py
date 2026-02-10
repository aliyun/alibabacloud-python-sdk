# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class VerifyCheckCustomConfigRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        custom_check_config: main_models.VerifyCheckCustomConfigRequestCustomCheckConfig = None,
        custom_configs: List[main_models.VerifyCheckCustomConfigRequestCustomConfigs] = None,
        repair_configs: List[main_models.VerifyCheckCustomConfigRequestRepairConfigs] = None,
        type: str = None,
    ):
        # Check item ID.
        self.check_id = check_id
        # Custom check item to validate input parameters.
        self.custom_check_config = custom_check_config
        # List of custom configuration items for the check item.
        self.custom_configs = custom_configs
        # Repair parameters supported by the check item\\"s repair function.
        self.repair_configs = repair_configs
        # Situation Awareness parameter validation types: 
        # - **REPAIR_CONFIG**: Repair and custom parameter validation (default) 
        # - **CHECK_ITEM_CONFIG**: Custom check item validation
        self.type = type

    def validate(self):
        if self.custom_check_config:
            self.custom_check_config.validate()
        if self.custom_configs:
            for v1 in self.custom_configs:
                 if v1:
                    v1.validate()
        if self.repair_configs:
            for v1 in self.repair_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.custom_check_config is not None:
            result['CustomCheckConfig'] = self.custom_check_config.to_map()

        result['CustomConfigs'] = []
        if self.custom_configs is not None:
            for k1 in self.custom_configs:
                result['CustomConfigs'].append(k1.to_map() if k1 else None)

        result['RepairConfigs'] = []
        if self.repair_configs is not None:
            for k1 in self.repair_configs:
                result['RepairConfigs'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CustomCheckConfig') is not None:
            temp_model = main_models.VerifyCheckCustomConfigRequestCustomCheckConfig()
            self.custom_check_config = temp_model.from_map(m.get('CustomCheckConfig'))

        self.custom_configs = []
        if m.get('CustomConfigs') is not None:
            for k1 in m.get('CustomConfigs'):
                temp_model = main_models.VerifyCheckCustomConfigRequestCustomConfigs()
                self.custom_configs.append(temp_model.from_map(k1))

        self.repair_configs = []
        if m.get('RepairConfigs') is not None:
            for k1 in m.get('RepairConfigs'):
                temp_model = main_models.VerifyCheckCustomConfigRequestRepairConfigs()
                self.repair_configs.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class VerifyCheckCustomConfigRequestRepairConfigs(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # ID of the repair process during the repair.
        self.flow_id = flow_id
        # Name of the repair parameter for the check item, unique within the same check item.
        self.name = name
        # Operation type for the custom configuration item of the check item. Only pass DELETE when deleting; no need to pass for creation or update.
        self.operation = operation
        # User-configured value string for the repair parameter of the check item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class VerifyCheckCustomConfigRequestCustomConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation: str = None,
        value: str = None,
    ):
        # Name of the custom configuration item for the check item, unique within the same check item.
        self.name = name
        # Operation type for the custom configuration item of the check item. Only pass DELETE when deleting; no need to pass for creation or update.
        self.operation = operation
        # User-configured value string for the custom configuration item of the check item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class VerifyCheckCustomConfigRequestCustomCheckConfig(DaraModel):
    def __init__(
        self,
        check_rule: str = None,
        cloud_asset_instance: main_models.VerifyCheckCustomConfigRequestCustomCheckConfigCloudAssetInstance = None,
        instance_sub_type: str = None,
        instance_type: str = None,
        vendor: str = None,
    ):
        # Define rules for custom inspection items.
        self.check_rule = check_rule
        # Asset instance that requires testing rules
        self.cloud_asset_instance = cloud_asset_instance
        # Asset subtype of the cloud product
        self.instance_sub_type = instance_sub_type
        # Asset types of cloud products. Values:
        # - **ECS**: Elastic Compute Service 
        # - **SLB**: Server Load Balancer 
        # - **RDS**: Relational Database Service 
        # - **MONGODB**: MongoDB Database 
        # - **KVSTORE**: Redis Database 
        # - **ACR**: Container Registry 
        # - **CSK**: CSK 
        # - **VPC**: Virtual Private Cloud 
        # - **ACTIONTRAIL**: Action Trail 
        # - **CDN**: Content Delivery Network 
        # - **CAS**: Digital Certificate Management Service [formerly SSL Certificates] 
        # - **RDC**: DevOps 
        # - **RAM**: Resource Access Management 
        # - **DDOS**: Distributed Denial of Service 
        # - **WAF**: Web Application Firewall 
        # - **OSS**: Object Storage Service 
        # - **POLARDB**: POLARDB 
        # - **POSTGRESQL**: PostgreSQL 
        # - **MSE**: MSE 
        # - **NAS**: Network Attached Storage 
        # - **SDDP**: Sensitive Data Discovery and Protection 
        # - **EIP**: Elastic IP
        self.instance_type = instance_type
        # Cloud asset vendor. Values: 
        # - **ALIYUN**: Alibaba Cloud 
        # - **Tencent**: Tencent Cloud 
        # - **HUAWEICLOUD**: Huawei Cloud 
        # - **Azure**: Microsoft 
        # - **AWS**: Amazon Web Services (AWS)
        self.vendor = vendor

    def validate(self):
        if self.cloud_asset_instance:
            self.cloud_asset_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_rule is not None:
            result['CheckRule'] = self.check_rule

        if self.cloud_asset_instance is not None:
            result['CloudAssetInstance'] = self.cloud_asset_instance.to_map()

        if self.instance_sub_type is not None:
            result['InstanceSubType'] = self.instance_sub_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRule') is not None:
            self.check_rule = m.get('CheckRule')

        if m.get('CloudAssetInstance') is not None:
            temp_model = main_models.VerifyCheckCustomConfigRequestCustomCheckConfigCloudAssetInstance()
            self.cloud_asset_instance = temp_model.from_map(m.get('CloudAssetInstance'))

        if m.get('InstanceSubType') is not None:
            self.instance_sub_type = m.get('InstanceSubType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class VerifyCheckCustomConfigRequestCustomCheckConfigCloudAssetInstance(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Instance ID of the asset.
        self.instance_id = instance_id
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

