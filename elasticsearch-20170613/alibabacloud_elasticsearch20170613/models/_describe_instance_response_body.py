# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeInstanceResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        advanced_dedicate_master: bool = None,
        advanced_setting: main_models.DescribeInstanceResponseBodyResultAdvancedSetting = None,
        aliws_dicts: List[main_models.DescribeInstanceResponseBodyResultAliwsDicts] = None,
        arch_type: str = None,
        client_node_configuration: main_models.DescribeInstanceResponseBodyResultClientNodeConfiguration = None,
        created_at: str = None,
        dedicate_master: bool = None,
        description: str = None,
        dict_list: List[main_models.DescribeInstanceResponseBodyResultDictList] = None,
        domain: str = None,
        elastic_data_node_configuration: main_models.DescribeInstanceResponseBodyResultElasticDataNodeConfiguration = None,
        enable_kibana_private_network: bool = None,
        enable_kibana_public_network: bool = None,
        enable_public: bool = None,
        end_time: int = None,
        endpoints: List[main_models.DescribeInstanceResponseBodyResultEndpoints] = None,
        es_config: Dict[str, Any] = None,
        es_ipblacklist: List[str] = None,
        es_ipwhitelist: List[str] = None,
        es_version: str = None,
        extend_configs: List[Dict[str, Any]] = None,
        have_client_node: bool = None,
        have_kibana: bool = None,
        ik_hot_dicts: List[main_models.DescribeInstanceResponseBodyResultIkHotDicts] = None,
        instance_category: str = None,
        instance_id: str = None,
        is_new_deployment: bool = None,
        kibana_configuration: main_models.DescribeInstanceResponseBodyResultKibanaConfiguration = None,
        kibana_domain: str = None,
        kibana_ipwhitelist: List[str] = None,
        kibana_port: int = None,
        kibana_private_domain: str = None,
        kibana_private_ipwhitelist: List[str] = None,
        kibana_private_port: str = None,
        master_configuration: main_models.DescribeInstanceResponseBodyResultMasterConfiguration = None,
        network_config: main_models.DescribeInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.DescribeInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        port: int = None,
        postpaid_service_status: str = None,
        private_network_ip_white_list: List[str] = None,
        protocol: str = None,
        public_domain: str = None,
        public_ip_whitelist: List[str] = None,
        public_port: int = None,
        resource_group_id: str = None,
        service_vpc: bool = None,
        status: str = None,
        synonyms_dicts: List[main_models.DescribeInstanceResponseBodyResultSynonymsDicts] = None,
        tags: List[main_models.DescribeInstanceResponseBodyResultTags] = None,
        updated_at: str = None,
        vpc_instance_id: str = None,
        warm_node: bool = None,
        warm_node_configuration: main_models.DescribeInstanceResponseBodyResultWarmNodeConfiguration = None,
        zone_count: int = None,
        zone_infos: List[main_models.DescribeInstanceResponseBodyResultZoneInfos] = None,
    ):
        self.advanced_dedicate_master = advanced_dedicate_master
        self.advanced_setting = advanced_setting
        self.aliws_dicts = aliws_dicts
        self.arch_type = arch_type
        self.client_node_configuration = client_node_configuration
        self.created_at = created_at
        self.dedicate_master = dedicate_master
        self.description = description
        self.dict_list = dict_list
        self.domain = domain
        self.elastic_data_node_configuration = elastic_data_node_configuration
        self.enable_kibana_private_network = enable_kibana_private_network
        self.enable_kibana_public_network = enable_kibana_public_network
        self.enable_public = enable_public
        self.end_time = end_time
        self.endpoints = endpoints
        self.es_config = es_config
        self.es_ipblacklist = es_ipblacklist
        self.es_ipwhitelist = es_ipwhitelist
        self.es_version = es_version
        self.extend_configs = extend_configs
        self.have_client_node = have_client_node
        self.have_kibana = have_kibana
        self.ik_hot_dicts = ik_hot_dicts
        self.instance_category = instance_category
        self.instance_id = instance_id
        self.is_new_deployment = is_new_deployment
        self.kibana_configuration = kibana_configuration
        self.kibana_domain = kibana_domain
        self.kibana_ipwhitelist = kibana_ipwhitelist
        self.kibana_port = kibana_port
        self.kibana_private_domain = kibana_private_domain
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist
        self.kibana_private_port = kibana_private_port
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.port = port
        self.postpaid_service_status = postpaid_service_status
        self.private_network_ip_white_list = private_network_ip_white_list
        self.protocol = protocol
        self.public_domain = public_domain
        self.public_ip_whitelist = public_ip_whitelist
        self.public_port = public_port
        self.resource_group_id = resource_group_id
        self.service_vpc = service_vpc
        self.status = status
        self.synonyms_dicts = synonyms_dicts
        self.tags = tags
        self.updated_at = updated_at
        self.vpc_instance_id = vpc_instance_id
        self.warm_node = warm_node
        self.warm_node_configuration = warm_node_configuration
        self.zone_count = zone_count
        self.zone_infos = zone_infos

    def validate(self):
        if self.advanced_setting:
            self.advanced_setting.validate()
        if self.aliws_dicts:
            for v1 in self.aliws_dicts:
                 if v1:
                    v1.validate()
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.dict_list:
            for v1 in self.dict_list:
                 if v1:
                    v1.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()
        if self.ik_hot_dicts:
            for v1 in self.ik_hot_dicts:
                 if v1:
                    v1.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.network_config:
            self.network_config.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.synonyms_dicts:
            for v1 in self.synonyms_dicts:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.warm_node_configuration:
            self.warm_node_configuration.validate()
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

        if self.advanced_setting is not None:
            result['advancedSetting'] = self.advanced_setting.to_map()

        result['aliwsDicts'] = []
        if self.aliws_dicts is not None:
            for k1 in self.aliws_dicts:
                result['aliwsDicts'].append(k1.to_map() if k1 else None)

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

        result['dictList'] = []
        if self.dict_list is not None:
            for k1 in self.dict_list:
                result['dictList'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['domain'] = self.domain

        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()

        if self.enable_kibana_private_network is not None:
            result['enableKibanaPrivateNetwork'] = self.enable_kibana_private_network

        if self.enable_kibana_public_network is not None:
            result['enableKibanaPublicNetwork'] = self.enable_kibana_public_network

        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public

        if self.end_time is not None:
            result['endTime'] = self.end_time

        result['endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['endpoints'].append(k1.to_map() if k1 else None)

        if self.es_config is not None:
            result['esConfig'] = self.es_config

        if self.es_ipblacklist is not None:
            result['esIPBlacklist'] = self.es_ipblacklist

        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs

        if self.have_client_node is not None:
            result['haveClientNode'] = self.have_client_node

        if self.have_kibana is not None:
            result['haveKibana'] = self.have_kibana

        result['ikHotDicts'] = []
        if self.ik_hot_dicts is not None:
            for k1 in self.ik_hot_dicts:
                result['ikHotDicts'].append(k1.to_map() if k1 else None)

        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.is_new_deployment is not None:
            result['isNewDeployment'] = self.is_new_deployment

        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()

        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain

        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist

        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port

        if self.kibana_private_domain is not None:
            result['kibanaPrivateDomain'] = self.kibana_private_domain

        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist

        if self.kibana_private_port is not None:
            result['kibanaPrivatePort'] = self.kibana_private_port

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

        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain

        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist

        if self.public_port is not None:
            result['publicPort'] = self.public_port

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.service_vpc is not None:
            result['serviceVpc'] = self.service_vpc

        if self.status is not None:
            result['status'] = self.status

        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k1 in self.synonyms_dicts:
                result['synonymsDicts'].append(k1.to_map() if k1 else None)

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.vpc_instance_id is not None:
            result['vpcInstanceId'] = self.vpc_instance_id

        if self.warm_node is not None:
            result['warmNode'] = self.warm_node

        if self.warm_node_configuration is not None:
            result['warmNodeConfiguration'] = self.warm_node_configuration.to_map()

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

        if m.get('advancedSetting') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultAdvancedSetting()
            self.advanced_setting = temp_model.from_map(m.get('advancedSetting'))

        self.aliws_dicts = []
        if m.get('aliwsDicts') is not None:
            for k1 in m.get('aliwsDicts'):
                temp_model = main_models.DescribeInstanceResponseBodyResultAliwsDicts()
                self.aliws_dicts.append(temp_model.from_map(k1))

        if m.get('archType') is not None:
            self.arch_type = m.get('archType')

        if m.get('clientNodeConfiguration') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m.get('clientNodeConfiguration'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.dict_list = []
        if m.get('dictList') is not None:
            for k1 in m.get('dictList'):
                temp_model = main_models.DescribeInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k1))

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m.get('elasticDataNodeConfiguration'))

        if m.get('enableKibanaPrivateNetwork') is not None:
            self.enable_kibana_private_network = m.get('enableKibanaPrivateNetwork')

        if m.get('enableKibanaPublicNetwork') is not None:
            self.enable_kibana_public_network = m.get('enableKibanaPublicNetwork')

        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        self.endpoints = []
        if m.get('endpoints') is not None:
            for k1 in m.get('endpoints'):
                temp_model = main_models.DescribeInstanceResponseBodyResultEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('esConfig') is not None:
            self.es_config = m.get('esConfig')

        if m.get('esIPBlacklist') is not None:
            self.es_ipblacklist = m.get('esIPBlacklist')

        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')

        if m.get('haveClientNode') is not None:
            self.have_client_node = m.get('haveClientNode')

        if m.get('haveKibana') is not None:
            self.have_kibana = m.get('haveKibana')

        self.ik_hot_dicts = []
        if m.get('ikHotDicts') is not None:
            for k1 in m.get('ikHotDicts'):
                temp_model = main_models.DescribeInstanceResponseBodyResultIkHotDicts()
                self.ik_hot_dicts.append(temp_model.from_map(k1))

        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('isNewDeployment') is not None:
            self.is_new_deployment = m.get('isNewDeployment')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m.get('kibanaConfiguration'))

        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')

        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')

        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')

        if m.get('kibanaPrivateDomain') is not None:
            self.kibana_private_domain = m.get('kibanaPrivateDomain')

        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')

        if m.get('kibanaPrivatePort') is not None:
            self.kibana_private_port = m.get('kibanaPrivatePort')

        if m.get('masterConfiguration') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m.get('masterConfiguration'))

        if m.get('networkConfig') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultNodeSpec()
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

        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')

        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')

        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k1 in m.get('synonymsDicts'):
                temp_model = main_models.DescribeInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.DescribeInstanceResponseBodyResultTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('vpcInstanceId') is not None:
            self.vpc_instance_id = m.get('vpcInstanceId')

        if m.get('warmNode') is not None:
            self.warm_node = m.get('warmNode')

        if m.get('warmNodeConfiguration') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyResultWarmNodeConfiguration()
            self.warm_node_configuration = temp_model.from_map(m.get('warmNodeConfiguration'))

        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')

        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k1 in m.get('zoneInfos'):
                temp_model = main_models.DescribeInstanceResponseBodyResultZoneInfos()
                self.zone_infos.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyResultZoneInfos(DaraModel):
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

class DescribeInstanceResponseBodyResultWarmNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec
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

class DescribeInstanceResponseBodyResultTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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

class DescribeInstanceResponseBodyResultSynonymsDicts(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeInstanceResponseBodyResultNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        performance_level: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.performance_level = performance_level
        self.spec = spec
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

class DescribeInstanceResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
        white_ip_group_list: List[main_models.DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList] = None,
    ):
        self.type = type
        self.vpc_id = vpc_id
        self.vs_area = vs_area
        self.vswitch_id = vswitch_id
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
                temp_model = main_models.DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyResultNetworkConfigWhiteIpGroupList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        self.group_name = group_name
        self.ips = ips
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

class DescribeInstanceResponseBodyResultMasterConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec
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

class DescribeInstanceResponseBodyResultKibanaConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        spec: str = None,
        spec_info: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.spec = spec
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

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specInfo') is not None:
            self.spec_info = m.get('specInfo')

        return self

class DescribeInstanceResponseBodyResultIkHotDicts(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeInstanceResponseBodyResultEndpoints(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.endpoint = endpoint
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class DescribeInstanceResponseBodyResultElasticDataNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_encryption: bool = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.spec = spec
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

class DescribeInstanceResponseBodyResultDictList(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeInstanceResponseBodyResultClientNodeConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
        spec_info: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        self.spec = spec
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

class DescribeInstanceResponseBodyResultAliwsDicts(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        self.file_size = file_size
        self.name = name
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeInstanceResponseBodyResultAdvancedSetting(DaraModel):
    def __init__(
        self,
        gc_name: str = None,
    ):
        self.gc_name = gc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gc_name is not None:
            result['gcName'] = self.gc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gcName') is not None:
            self.gc_name = m.get('gcName')

        return self

