# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class GetKmsInstanceResponseBody(DaraModel):
    def __init__(
        self,
        kms_instance: main_models.GetKmsInstanceResponseBodyKmsInstance = None,
        request_id: str = None,
    ):
        # The details of the KMS instance.
        self.kms_instance = kms_instance
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use this ID to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.kms_instance:
            self.kms_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_instance is not None:
            result['KmsInstance'] = self.kms_instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsInstance') is not None:
            temp_model = main_models.GetKmsInstanceResponseBodyKmsInstance()
            self.kms_instance = temp_model.from_map(m.get('KmsInstance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetKmsInstanceResponseBodyKmsInstance(DaraModel):
    def __init__(
        self,
        bind_vpcs: main_models.GetKmsInstanceResponseBodyKmsInstanceBindVpcs = None,
        ca_certificate_chain_pem: str = None,
        charge_type: str = None,
        create_time: str = None,
        deletion_protection: bool = None,
        deletion_protection_description: str = None,
        end_date: str = None,
        instance_id: str = None,
        instance_name: str = None,
        key_num: int = None,
        log: int = None,
        log_storage: int = None,
        product_type: str = None,
        product_version: str = None,
        sale_status: str = None,
        secret_num: str = None,
        spec: int = None,
        start_date: str = None,
        status: str = None,
        vpc_id: str = None,
        vpc_num: int = None,
        vswitch_ids: List[str] = None,
        zone_ids: List[str] = None,
    ):
        self.bind_vpcs = bind_vpcs
        # The CA certificate chain for the KMS instance in PEM format.
        self.ca_certificate_chain_pem = ca_certificate_chain_pem
        # The billing method of the instance. Valid values:
        # 
        # - `PREPAY`: subscription
        # 
        # - `POSTPAY`: pay-as-you-go
        self.charge_type = charge_type
        # The creation time of the KMS instance.
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.deletion_protection_description = deletion_protection_description
        # The expiration time of the KMS instance.
        self.end_date = end_date
        # The ID of the KMS instance.
        self.instance_id = instance_id
        # The name of the KMS instance.
        self.instance_name = instance_name
        # The maximum number of keys that can be created in the KMS instance.
        self.key_num = key_num
        # Indicates whether logging is enabled for the KMS instance. Valid values: `1` (enabled) and `0` (disabled).
        self.log = log
        # The log storage capacity. Unit: GB.
        self.log_storage = log_storage
        # The product type.<br>Subscription:<br>`kms_ddi_public_cn`: China site<br>`kms_ddi_public_intl`: international site<br>Pay-as-you-go:<br>`kms_ppi_public_cn`: China site<br>`kms_ppi_public_intl`: international site<br><br><br><br><br><br>
        self.product_type = product_type
        # The version of the KMS instance.
        self.product_version = product_version
        # The sales status of the instance.
        self.sale_status = sale_status
        # The maximum number of credentials that can be created in the KMS instance.
        self.secret_num = secret_num
        # The computing performance of the KMS instance.
        self.spec = spec
        # The time when the KMS instance was enabled.
        self.start_date = start_date
        # The status of the KMS instance. Valid values:
        # 
        # - `Uninitialized`: The instance is not enabled.
        # 
        # - `Connecting`: The instance is connecting.
        # 
        # - `Connected`: The instance is enabled.
        # 
        # - `Disconnected`: The instance is disconnected.
        # 
        # - `Error`: The instance is in an error state.
        self.status = status
        # The VPC to which the KMS instance is attached.
        self.vpc_id = vpc_id
        # The maximum number of VPCs that can be associated with the KMS instance for access control.
        self.vpc_num = vpc_num
        # The vSwitches in the VPC to which the KMS instance is attached.
        self.vswitch_ids = vswitch_ids
        # The zones to which the KMS instance is attached.
        self.zone_ids = zone_ids

    def validate(self):
        if self.bind_vpcs:
            self.bind_vpcs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs.to_map()

        if self.ca_certificate_chain_pem is not None:
            result['CaCertificateChainPem'] = self.ca_certificate_chain_pem

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.key_num is not None:
            result['KeyNum'] = self.key_num

        if self.log is not None:
            result['Log'] = self.log

        if self.log_storage is not None:
            result['LogStorage'] = self.log_storage

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.sale_status is not None:
            result['SaleStatus'] = self.sale_status

        if self.secret_num is not None:
            result['SecretNum'] = self.secret_num

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_num is not None:
            result['VpcNum'] = self.vpc_num

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindVpcs') is not None:
            temp_model = main_models.GetKmsInstanceResponseBodyKmsInstanceBindVpcs()
            self.bind_vpcs = temp_model.from_map(m.get('BindVpcs'))

        if m.get('CaCertificateChainPem') is not None:
            self.ca_certificate_chain_pem = m.get('CaCertificateChainPem')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')

        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('LogStorage') is not None:
            self.log_storage = m.get('LogStorage')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('SaleStatus') is not None:
            self.sale_status = m.get('SaleStatus')

        if m.get('SecretNum') is not None:
            self.secret_num = m.get('SecretNum')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcNum') is not None:
            self.vpc_num = m.get('VpcNum')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class GetKmsInstanceResponseBodyKmsInstanceBindVpcs(DaraModel):
    def __init__(
        self,
        bind_vpc: List[main_models.GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc] = None,
    ):
        self.bind_vpc = bind_vpc

    def validate(self):
        if self.bind_vpc:
            for v1 in self.bind_vpc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindVpc'] = []
        if self.bind_vpc is not None:
            for k1 in self.bind_vpc:
                result['BindVpc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_vpc = []
        if m.get('BindVpc') is not None:
            for k1 in m.get('BindVpc'):
                temp_model = main_models.GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc()
                self.bind_vpc.append(temp_model.from_map(k1))

        return self

class GetKmsInstanceResponseBodyKmsInstanceBindVpcsBindVpc(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_owner_id: str = None,
    ):
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.vpc_owner_id = vpc_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        return self

