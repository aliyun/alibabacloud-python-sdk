# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListInstanceResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListInstanceResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListInstanceResponseBodyResult] = None,
    ):
        # The response headers.
        self.headers = headers
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListInstanceResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListInstanceResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        advanced_dedicate_master: bool = None,
        arch_type: str = None,
        client_node_configuration: main_models.ListInstanceResponseBodyResultClientNodeConfiguration = None,
        created_at: str = None,
        dedicate_master: bool = None,
        description: str = None,
        domain: str = None,
        elastic_data_node_configuration: main_models.ListInstanceResponseBodyResultElasticDataNodeConfiguration = None,
        end_time: int = None,
        es_version: str = None,
        extend_configs: List[Dict[str, Any]] = None,
        instance_id: str = None,
        is_new_deployment: str = None,
        kibana_configuration: main_models.ListInstanceResponseBodyResultKibanaConfiguration = None,
        kibana_ipwhitelist: List[str] = None,
        kibana_private_ipwhitelist: List[str] = None,
        master_configuration: main_models.ListInstanceResponseBodyResultMasterConfiguration = None,
        network_config: main_models.ListInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.ListInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        port: str = None,
        postpaid_service_status: str = None,
        private_network_ip_white_list: List[str] = None,
        protocol: str = None,
        public_ip_whitelist: List[str] = None,
        resource_group_id: str = None,
        service_vpc: bool = None,
        status: str = None,
        tags: List[main_models.ListInstanceResponseBodyResultTags] = None,
        updated_at: str = None,
        vpc_instance_id: str = None,
        zone_count: int = None,
        zone_infos: List[main_models.ListInstanceResponseBodyResultZoneInfos] = None,
    ):
        # Indicates whether the instance contains dedicated master nodes. Valid values:
        # 
        # - true: The instance contains dedicated master nodes.
        # 
        # - false: The instance does not contain dedicated master nodes.
        self.advanced_dedicate_master = advanced_dedicate_master
        # The deployment mode and architecture type:
        # exclusive: basic management and control
        # public: cloud-native management and control
        self.arch_type = arch_type
        # The configuration of client nodes.
        self.client_node_configuration = client_node_configuration
        # The time when the instance was created.
        self.created_at = created_at
        # Indicates whether the instance contains dedicated master nodes (deprecated). Valid values:
        # 
        # - true: The instance contains dedicated master nodes.
        # 
        # - false: The instance does not contain dedicated master nodes.
        self.dedicate_master = dedicate_master
        # The instance name.
        self.description = description
        # The internal endpoint of the instance.
        self.domain = domain
        # The configuration of elastic data nodes.
        self.elastic_data_node_configuration = elastic_data_node_configuration
        # The expiration time of the instance.
        self.end_time = end_time
        # The instance version.
        self.es_version = es_version
        # The extended configurations of the cluster.
        self.extend_configs = extend_configs
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the instance uses the new deployment architecture.
        self.is_new_deployment = is_new_deployment
        # The configuration of Kibana nodes.
        self.kibana_configuration = kibana_configuration
        # The public network access whitelist for Kibana nodes of the cluster.
        self.kibana_ipwhitelist = kibana_ipwhitelist
        # The private network access whitelist for Kibana nodes of the cluster.
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist
        # The configuration of master nodes.
        self.master_configuration = master_configuration
        # The network configuration.
        self.network_config = network_config
        # The number of data nodes in the instance.
        self.node_amount = node_amount
        # The configuration of data nodes.
        self.node_spec = node_spec
        # The billing method of the instance. Valid values:
        # 
        # - **prepaid**: subscription
        # 
        # - **postpaid**: pay-as-you-go
        self.payment_type = payment_type
        # The access port of the instance.
        # >Notice: When the instance is being created or the instance status is abnormal, this value may be empty or 0.
        self.port = port
        # The status of the pay-as-you-go service that is overlaid on a subscription instance. Valid values:
        # 
        # - **active**: normal
        # 
        # - **closed**: closed
        # 
        # - **indebt**: frozen due to overdue payment
        self.postpaid_service_status = postpaid_service_status
        # The private network access whitelist for the Elasticsearch cluster.
        self.private_network_ip_white_list = private_network_ip_white_list
        # The access protocol. Valid values: HTTP and HTTPS.
        self.protocol = protocol
        # The public network access whitelist for the Elasticsearch cluster.
        self.public_ip_whitelist = public_ip_whitelist
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether the instance is a service VPC.
        self.service_vpc = service_vpc
        # The status of the instance. Valid values:
        # 
        # - active: normal
        # 
        # - activating: taking effect
        # 
        # - inactive: frozen
        # 
        # - invalid: invalid. The cluster does not exist or is inaccessible. In this case, some fields in the API response may be missing, such as domain and kibanaDomain.
        # 
        # - unknown: unknown. The cluster does not exist or is inaccessible. In this case, some fields in the API response may be missing, such as domain and kibanaDomain.
        self.status = status
        # The instance tags.
        self.tags = tags
        # The time when the instance was last updated.
        self.updated_at = updated_at
        # The VPC ID.
        self.vpc_instance_id = vpc_instance_id
        self.zone_count = zone_count
        self.zone_infos = zone_infos

    def validate(self):
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zone_infos:
            for v1 in self.zone_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_dedicate_master is not None:
            result['advancedDedicateMaster'] = self.advanced_dedicate_master

        if self.arch_type is not None:
            result['archType'] = self.arch_type

        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.dedicate_master is not None:
            result['dedicateMaster'] = self.dedicate_master

        if self.description is not None:
            result['description'] = self.description

        if self.domain is not None:
            result['domain'] = self.domain

        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.is_new_deployment is not None:
            result['isNewDeployment'] = self.is_new_deployment

        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()

        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist

        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist

        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.port is not None:
            result['port'] = self.port

        if self.postpaid_service_status is not None:
            result['postpaidServiceStatus'] = self.postpaid_service_status

        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.service_vpc is not None:
            result['serviceVpc'] = self.service_vpc

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id

        if self.zone_count is not None:
            result['zoneCount'] = self.zone_count

        result['zoneInfos'] = []
        if self.zone_infos is not None:
            for k1 in self.zone_infos:
                result['zoneInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedDedicateMaster') is not None:
            self.advanced_dedicate_master = m.get('advancedDedicateMaster')

        if m.get('archType') is not None:
            self.arch_type = m.get('archType')

        if m.get('clientNodeConfiguration') is not None:
            temp_model = main_models.ListInstanceResponseBodyResultClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m.get('clientNodeConfiguration'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = main_models.ListInstanceResponseBodyResultElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m.get('elasticDataNodeConfiguration'))

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('isNewDeployment') is not None:
            self.is_new_deployment = m.get('isNewDeployment')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.ListInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m.get('kibanaConfiguration'))

        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')

        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')

        if m.get('masterConfiguration') is not None:
            temp_model = main_models.ListInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m.get('masterConfiguration'))

        if m.get('networkConfig') is not None:
            temp_model = main_models.ListInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.ListInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('postpaidServiceStatus') is not None:
            self.postpaid_service_status = m.get('postpaidServiceStatus')

        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')

        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')

        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k1 in m.get('zoneInfos'):
                temp_model = main_models.ListInstanceResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k1))

        return self

class ListInstanceResponseBodyResultZoneInfos(DaraModel):
    def __init__(
        self,
        status: str = None,
        zone_id: str = None,
    ):
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class ListInstanceResponseBodyResultTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class ListInstanceResponseBodyResultNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        performance_level: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        # The storage size of the node. Unit: GB.
        self.disk = disk
        # Indicates whether disk encryption is used. Valid values:
        # 
        # - true: Disk encryption is used.
        # - false: Disk encryption is not used.
        self.disk_encryption = disk_encryption
        # The storage type of the node. Valid values:
        # 
        # - cloud_ssd: standard SSD
        # 
        # - cloud_efficiency: ultra disk
        self.disk_type = disk_type
        # The performance level of the ESSD. This parameter is required when diskType is cloud_essd. Valid values: PL1, PL2, and PL3.
        self.performance_level = performance_level
        # The node specifications. For more information about the specifications, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
        self.spec = spec
        # The description of node specifications.
        self.spec_info = spec_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_info is not None:
            result['specInfo'] = self.spec_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specInfo') is not None:
            self.spec_info = m.get('specInfo')

        return self

class ListInstanceResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
        white_ip_group_list: List[main_models.ListInstanceResponseBodyResultNetworkConfigWhiteIpGroupList] = None,
    ):
        # The network type. Only Virtual Private Cloud (VPC) is supported.
        self.type = type
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone where the instance is deployed.
        self.vs_area = vs_area
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The whitelist group settings for the public and private networks of the cluster.
        self.white_ip_group_list = white_ip_group_list

    def validate(self):
        if self.white_ip_group_list:
            for v1 in self.white_ip_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k1 in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k1 in m.get('whiteIpGroupList'):
                temp_model = main_models.ListInstanceResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k1))

        return self

class ListInstanceResponseBodyResultNetworkConfigWhiteIpGroupList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # The group name.
        self.group_name = group_name
        # The IP address whitelist.
        self.ips = ips
        # The network type. PRIVATE_ES: Elasticsearch private network. PUBLIC_KIBANA: Kibana public network. PUBLIC_ES: Elasticsearch public network. PRIVATE_KIBANA: Kibana private network.
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.ips is not None:
            result['ips'] = self.ips

        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('ips') is not None:
            self.ips = m.get('ips')

        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')

        return self

class ListInstanceResponseBodyResultMasterConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        # The number of nodes.
        self.amount = amount
        # The storage size of the node. Unit: GB.
        self.disk = disk
        # The storage type of the node. Only cloud_ssd (standard SSD) is supported.
        self.disk_type = disk_type
        # The node specifications. For more information about the specifications, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
        self.spec = spec
        # The description of node specifications.
        self.spec_info = spec_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_info is not None:
            result['specInfo'] = self.spec_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specInfo') is not None:
            self.spec_info = m.get('specInfo')

        return self

class ListInstanceResponseBodyResultKibanaConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        # The number of nodes.
        self.amount = amount
        # The storage size of the node. Unit: GB.
        self.disk = disk
        # The storage type of the node.
        self.disk_type = disk_type
        # The node specifications. For more information about the specifications, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
        self.spec = spec
        # The description of node specifications.
        self.spec_info = spec_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_info is not None:
            result['specInfo'] = self.spec_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specInfo') is not None:
            self.spec_info = m.get('specInfo')

        return self

class ListInstanceResponseBodyResultElasticDataNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        # The number of nodes.
        self.amount = amount
        # The storage size of the node. Unit: GB.
        self.disk = disk
        # Indicates whether disk encryption is enabled for the node. Valid values:
        # 
        # - true: Disk encryption is enabled.
        # 
        # - false: Disk encryption is not enabled.
        self.disk_encryption = disk_encryption
        # The storage type of the node. Valid values:
        # 
        # - cloud_ssd: standard SSD
        # 
        # - cloud_essd: enhanced SSD (ESSD)
        # 
        # - cloud_efficiency: ultra disk
        self.disk_type = disk_type
        # The node specifications. For more information about the specifications, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
        self.spec = spec
        # The description of node specifications.
        self.spec_info = spec_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_info is not None:
            result['specInfo'] = self.spec_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specInfo') is not None:
            self.spec_info = m.get('specInfo')

        return self

class ListInstanceResponseBodyResultClientNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        # The number of nodes.
        self.amount = amount
        # The storage size of the node. Unit: GB.
        self.disk = disk
        # The storage type of the node. Only ultra disks (cloud_efficiency) are supported.
        self.disk_type = disk_type
        # The node specifications. For more information about the specifications, see [Product specifications](https://help.aliyun.com/document_detail/271718.html).
        self.spec = spec
        # The description of node specifications.
        self.spec_info = spec_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_info is not None:
            result['specInfo'] = self.spec_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specInfo') is not None:
            self.spec_info = m.get('specInfo')

        return self

class ListInstanceResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The total number of instances.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

