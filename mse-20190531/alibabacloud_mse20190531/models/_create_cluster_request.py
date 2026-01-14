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
        # The language type of the returned information:
        # 
        # - zh: Chinese
        # - en: English
        self.accept_language = accept_language
        # Billing method, including PREPAY (Subscription) and POSTPAY (Pay-As-You-Go).
        # 
        # This parameter is ignored for the Serverless edition.
        self.charge_type = charge_type
        # Engine specifications, with the following values:
        # 
        # [Professional Edition] 
        # 
        # - `MSE_SC_2_4_60_c`: 2 cores, 4GB
        # - `MSE_SC_1_2_60_c`: 1 core, 2GB
        # - `MSE_SC_4_8_60_c`: 4 cores, 8GB
        # - `MSE_SC_8_16_60_c`: 8 cores, 16GB
        # - `MSE_SC_16_32_60_c`: 16 cores, 32GB
        # 
        # [Developer Edition] 
        # 
        # - `MSE_SC_1_2_60_c`: 1 core, 2GB
        # - `MSE_SC_2_4_60_c`: 2 cores, 4GB
        # 
        # [Serverless Edition]
        # 
        # Ignore this parameter, or you can fill in `MSE_SC_SERVERLESS`.
        # 
        # This parameter is required.
        self.cluster_specification = cluster_specification
        # Cluster type, including ZooKeeper, Nacos-Ans.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # Cluster version, with the following values:
        # 
        # [Professional Edition] 
        # 
        # - `NACOS_2_0_0`: indicates Nacos 2.x.x version.
        # - `ZooKeeper_3_8_0`: indicates ZooKeeper 3.8.x version.
        # 
        # [Developer Edition] 
        # 
        # - `NACOS_2_0_0`: indicates Nacos 2.x version.
        # - `ZooKeeper_3_8_0`: indicates ZooKeeper 3.8.x version.
        # 
        # [Serverless Edition]
        # 
        # - `NACOS_2_0_0`: indicates Nacos 2.x version.
        # - `ZooKeeper_3_8_0`: indicates ZooKeeper 3.8.x version.
        # 
        # This parameter is required.
        self.cluster_version = cluster_version
        # Network access type, `slb` or `single_eni`; some regions\\" Developer Edition only support the `single_eni` type.
        self.connection_type = connection_type
        # No longer in use
        self.disk_type = disk_type
        # Valid when `ConnectionType` is `single_eni`, indicating whether to enable public network access (Elastic IP).
        self.eip_enabled = eip_enabled
        # Number of instance nodes, with a range limit of 1 to 9.
        # 
        # [Professional Edition] 
        # - The number of instances must be 3 or more and must be an odd number.
        # 
        # [Developer Edition] 
        # - The number of instances can only be 1.
        # 
        # [Serverless Edition]
        # 
        # Ignore this parameter.
        # 
        # This parameter is required.
        self.instance_count = instance_count
        # Custom instance name
        self.instance_name = instance_name
        # Required unless under special circumstances, with the following values:
        # 
        # - `mse_pro`: indicates Professional Edition.
        # - `mse_dev`: indicates Developer Edition.
        # - `mse_serverless`: indicates Serverless Edition.
        self.mse_version = mse_version
        # Network type, with the following values:
        # - `privatenet`: indicates a private network.
        # - `pubnet`: indicates a public network.
        # 
        # This parameter is required.
        self.net_type = net_type
        # No longer in use
        self.private_slb_specification = private_slb_specification
        # Valid when `ConnectionType` is `slb`. 0 indicates no public network access SLB creation, and values above 1 indicate a fixed bandwidth for public network access SLB; unit: Mbps.
        # 
        # Value range: 0~5000.
        self.pub_network_flow = pub_network_flow
        # No longer in use
        self.pub_slb_specification = pub_slb_specification
        # The region where the cluster is located, including but not limited to the following regions:
        # - `cn-hangzhou`: Hangzhou
        # - `cn-beijing`: Beijing
        # - `cn-shanghai`: Shanghai
        # - `cn-zhangjiakou`: Zhangjiakou
        # - `cn-shenzhen`: Shenzhen
        self.region = region
        # Extended request parameters, in JSON format.
        self.request_pars = request_pars
        # Resource group ID. For more details about the resource group, see [Basic Information of Resource Group](https://help.aliyun.com/document_detail/457230.html).
        self.resource_group_id = resource_group_id
        # Valid when `ConnectionType` is `single_eni`, indicating the security group type of the instance.
        self.security_group_type = security_group_type
        # List of tags to be added. Contains up to 20 items.
        self.tag = tag
        # Switch ID.
        self.v_switch_id = v_switch_id
        # VPC ID.
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
        # Tag key.
        self.key = key
        # Tag value.
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

