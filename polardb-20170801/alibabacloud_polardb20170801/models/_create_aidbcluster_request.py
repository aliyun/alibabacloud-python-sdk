# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class CreateAIDBClusterRequest(DaraModel):
    def __init__(
        self,
        ack_admin: str = None,
        auto_renew: str = None,
        auto_use_coupon: bool = None,
        client_token: str = None,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        dbnode_class: str = None,
        extension: str = None,
        inference_engine: str = None,
        kube_cluster_id: str = None,
        kube_config: str = None,
        kube_management: str = None,
        kube_type: str = None,
        kubernetes_config: str = None,
        management_mode: str = None,
        model_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        pay_type: str = None,
        period: str = None,
        promotion_code: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        storage_space: int = None,
        storage_type: str = None,
        time_slices: List[main_models.CreateAIDBClusterRequestTimeSlices] = None,
        used_time: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # Specifies whether the cluster is managed by an ACK cluster.
        self.ack_admin = ack_admin
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: Auto-renewal is enabled.
        # 
        # - **false**: Auto-renewal is disabled.
        # 
        # Default value: **false**.
        # 
        # > This parameter takes effect only when **PayType** is set to **Prepaid**.
        self.auto_renew = auto_renew
        # Specifies whether to automatically use a coupon. Valid values:
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the cluster. You can use the description to perform a fuzzy search.
        self.dbcluster_description = dbcluster_description
        # The ID of the PolarDB cluster that the application depends on.
        self.dbcluster_id = dbcluster_id
        # The node specification.
        # 
        # This parameter is required.
        self.dbnode_class = dbnode_class
        # The extension.
        self.extension = extension
        # The inference engine.
        self.inference_engine = inference_engine
        # The Container Service for Kubernetes (ACK) cluster ID.
        self.kube_cluster_id = kube_cluster_id
        # The Kubernetes configuration.
        self.kube_config = kube_config
        # The management mode of the Kubernetes cluster.
        self.kube_management = kube_management
        # The type of the Kubernetes deployment.
        self.kube_type = kube_type
        # The Kubernetes configuration.
        self.kubernetes_config = kubernetes_config
        # The management mode.
        self.management_mode = management_mode
        self.model_name = model_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password.
        self.password = password
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go.
        # 
        # - **Prepaid**: subscription.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The unit of the subscription duration. This parameter is required if **PayType** is set to **Prepaid**. Valid values:
        # 
        # - **Year**
        # 
        # - **Month**
        self.period = period
        # The coupon code. If you do not specify this parameter, the default coupon is used.
        # 
        # - true (default): Use a coupon.
        # 
        # - false: Do not use a coupon.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The storage space. Unit: GB.
        self.storage_space = storage_space
        # The storage type.
        self.storage_type = storage_type
        # The billing intervals for the pay-as-you-go cluster.
        self.time_slices = time_slices
        # The subscription duration. This parameter is required if **PayType** is set to **Prepaid**.
        # 
        # - If **Period** is set to **Month**, the value of **UsedTime** must be an integer from `[1-9]`.
        # 
        # - If **Period** is set to **Year**, the value of **UsedTime** must be an integer from `[1-3]`.
        self.used_time = used_time
        # The virtual private cloud (VPC) ID.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The availability zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.time_slices:
            for v1 in self.time_slices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_admin is not None:
            result['AckAdmin'] = self.ack_admin

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.inference_engine is not None:
            result['InferenceEngine'] = self.inference_engine

        if self.kube_cluster_id is not None:
            result['KubeClusterId'] = self.kube_cluster_id

        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config

        if self.kube_management is not None:
            result['KubeManagement'] = self.kube_management

        if self.kube_type is not None:
            result['KubeType'] = self.kube_type

        if self.kubernetes_config is not None:
            result['KubernetesConfig'] = self.kubernetes_config

        if self.management_mode is not None:
            result['ManagementMode'] = self.management_mode

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        result['TimeSlices'] = []
        if self.time_slices is not None:
            for k1 in self.time_slices:
                result['TimeSlices'].append(k1.to_map() if k1 else None)

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckAdmin') is not None:
            self.ack_admin = m.get('AckAdmin')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('InferenceEngine') is not None:
            self.inference_engine = m.get('InferenceEngine')

        if m.get('KubeClusterId') is not None:
            self.kube_cluster_id = m.get('KubeClusterId')

        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')

        if m.get('KubeManagement') is not None:
            self.kube_management = m.get('KubeManagement')

        if m.get('KubeType') is not None:
            self.kube_type = m.get('KubeType')

        if m.get('KubernetesConfig') is not None:
            self.kubernetes_config = m.get('KubernetesConfig')

        if m.get('ManagementMode') is not None:
            self.management_mode = m.get('ManagementMode')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        self.time_slices = []
        if m.get('TimeSlices') is not None:
            for k1 in m.get('TimeSlices'):
                temp_model = main_models.CreateAIDBClusterRequestTimeSlices()
                self.time_slices.append(temp_model.from_map(k1))

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateAIDBClusterRequestTimeSlices(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
    ):
        # The start time of the billing interval. The time is in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.begin_time = begin_time
        # The end time of the billing interval, which must be later than the start time. The time is in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        return self

