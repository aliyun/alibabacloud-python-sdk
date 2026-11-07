# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class CreateClusterRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        charge_type: str = None,
        cluster_specification: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        connection_type: str = None,
        disk_type: str = None,
        eip_enabled: bool = None,
        instance_count: int = None,
        instance_name: str = None,
        mse_version: str = None,
        net_type: str = None,
        private_slb_specification: str = None,
        pub_network_flow: str = None,
        pub_slb_specification: str = None,
        region: str = None,
        request_pars: str = None,
        resource_group_id: str = None,
        security_group_type: str = None,
        tag: List[main_models.CreateClusterRequestTag] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.accept_language = accept_language
        # The billing method. Valid values: PREPAY (subscription) and POSTPAY (pay-as-you-go). This parameter is ignored for Serverless Edition.
        self.charge_type = charge_type
        # The engine specifications. Valid values:
        # 
        # This parameter is required.
        self.cluster_specification = cluster_specification
        # The cluster type. Valid values: ZooKeeper and Nacos-Ans.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The cluster version. Valid values:
        # 
        # This parameter is required.
        self.cluster_version = cluster_version
        # The network access type. Valid values: `slb` and `single_eni`. In some regions, Developer Edition supports only `single_eni`.
        self.connection_type = connection_type
        # This parameter is deprecated.
        self.disk_type = disk_type
        # Specifies whether to enable public network access by using an elastic IP address (EIP). This parameter takes effect only when ConnectionType is set to `single_eni`.
        self.eip_enabled = eip_enabled
        # The number of nodes in the instance. Valid values: 1 to 9.
        # [Professional Edition] 
        # 
        # -  `NACOS_2_0_0`: Nacos 2.x.x.
        # - `ZooKeeper_3_8_0`: ZooKeeper 3.8.x.
        # [Developer Edition] 
        # 
        # -  `NACOS_2_0_0`: Nacos 2.x.
        # - `ZooKeeper_3_8_0`: ZooKeeper 3.8.x.
        # [Serverless Edition]
        # 
        # -  `NACOS_2_0_0`: Nacos 2.x.
        # - `ZooKeeper_3_8_0`: ZooKeeper 3.8.x.
        # 
        # This parameter is required.
        self.instance_count = instance_count
        # The custom name of the instance.
        self.instance_name = instance_name
        # The instance edition. This parameter is required unless otherwise specified. Valid values:
        # 
        # - `mse_pro`: Professional Edition.
        # - `mse_dev`: Developer Edition.
        # - `mse_serverless`: Serverless Edition.
        self.mse_version = mse_version
        # The network type. Valid values:
        # - `privatenet`: virtual private cloud (VPC).
        # - `pubnet`: Internet.
        # 
        # This parameter is required.
        self.net_type = net_type
        # This parameter is deprecated.
        self.private_slb_specification = private_slb_specification
        # The bandwidth of the Internet-facing Server Load Balancer (SLB) instance. This parameter takes effect only when ConnectionType is set to `slb`. A value of 0 indicates that no Internet-facing SLB instance is created. A value greater than 1 indicates the fixed bandwidth of the Internet-facing SLB instance. Unit: Mbit/s. Valid values: 0 to 5000.
        self.pub_network_flow = pub_network_flow
        # This parameter is deprecated.
        self.pub_slb_specification = pub_slb_specification
        # The region where the cluster is deployed. Valid values include but are not limited to:
        # - `cn-hangzhou`: China (Hangzhou)
        # - `cn-beijing`: China (Beijing)
        # - `cn-shanghai`: China (Shanghai)
        # - `cn-zhangjiakou`: China (Zhangjiakou)
        # - `cn-shenzhen`: China (Shenzhen)
        self.region = region
        # The extended request parameters in JSON format.
        self.request_pars = request_pars
        # The resource group ID. For more information, see [View the basic information of a resource group](https://help.aliyun.com/document_detail/457230.html).
        self.resource_group_id = resource_group_id
        # The type of the security group to which the instance belongs. This parameter takes effect only when ConnectionType is set to `single_eni`. Valid values:
        self.security_group_type = security_group_type
        # The tags to be added. You can add up to 20 tags.
        self.tag = tag
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

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
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_specification is not None:
            result['ClusterSpecification'] = self.cluster_specification

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cluster_version is not None:
            result['ClusterVersion'] = self.cluster_version

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.eip_enabled is not None:
            result['EipEnabled'] = self.eip_enabled

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.private_slb_specification is not None:
            result['PrivateSlbSpecification'] = self.private_slb_specification

        if self.pub_network_flow is not None:
            result['PubNetworkFlow'] = self.pub_network_flow

        if self.pub_slb_specification is not None:
            result['PubSlbSpecification'] = self.pub_slb_specification

        if self.region is not None:
            result['Region'] = self.region

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_type is not None:
            result['SecurityGroupType'] = self.security_group_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterSpecification') is not None:
            self.cluster_specification = m.get('ClusterSpecification')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ClusterVersion') is not None:
            self.cluster_version = m.get('ClusterVersion')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EipEnabled') is not None:
            self.eip_enabled = m.get('EipEnabled')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('PrivateSlbSpecification') is not None:
            self.private_slb_specification = m.get('PrivateSlbSpecification')

        if m.get('PubNetworkFlow') is not None:
            self.pub_network_flow = m.get('PubNetworkFlow')

        if m.get('PubSlbSpecification') is not None:
            self.pub_slb_specification = m.get('PubSlbSpecification')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupType') is not None:
            self.security_group_type = m.get('SecurityGroupType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateClusterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateClusterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

