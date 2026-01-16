# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class Elasticsearch(DaraModel):
    def __init__(
        self,
        advanced_dedicate_master: bool = None,
        advanced_setting: main_models.ElasticsearchAdvancedSetting = None,
        aliws_dicts: List[main_models.DictInfo] = None,
        client_node_configuration: main_models.ClientNodeConfiguration = None,
        created_at: str = None,
        data_node: bool = None,
        dedicate_master: bool = None,
        description: str = None,
        dict_list: List[main_models.DictInfo] = None,
        domain: str = None,
        elastic_data_node_configuration: main_models.ElasticDataNodeConfiguration = None,
        enable_kibana_private_network: bool = None,
        enable_kibana_public_network: bool = None,
        enable_public: bool = None,
        end_time: int = None,
        es_config: Dict[str, str] = None,
        es_ipwhitelist: List[str] = None,
        es_version: str = None,
        extend_configs: List[Dict[str, Any]] = None,
        have_client_node: bool = None,
        have_elastic_data_node: bool = None,
        have_kibana: bool = None,
        ik_hot_dicts: List[main_models.DictInfo] = None,
        instance_id: str = None,
        kibana_configuration: main_models.KibanaNodeConfiguration = None,
        kibana_domain: str = None,
        kibana_ipwhitelist: List[str] = None,
        kibana_port: int = None,
        kibana_private_domain: str = None,
        kibana_private_ipwhitelist: List[str] = None,
        kibana_private_port: int = None,
        kibana_protocol: str = None,
        master_configuration: main_models.MasterNodeConfiguration = None,
        network_config: main_models.NetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.NodeSpec = None,
        payment_type: str = None,
        port: int = None,
        private_network_ip_white_list: List[str] = None,
        product_type: str = None,
        protocol: str = None,
        public_domain: str = None,
        public_ip_whitelist: List[str] = None,
        public_port: int = None,
        read_write_policy: main_models.ReadWritePolicy = None,
        resource_group_id: str = None,
        service_vpc: bool = None,
        status: str = None,
        synonyms_dicts: List[main_models.DictInfo] = None,
        tags: List[main_models.Tag] = None,
        updated_at: str = None,
        warm_node: bool = None,
        warm_node_configuration: main_models.WarmNodeConfiguration = None,
        zone_count: int = None,
        zone_infos: List[main_models.ZoneInfo] = None,
    ):
        self.advanced_dedicate_master = advanced_dedicate_master
        self.advanced_setting = advanced_setting
        self.aliws_dicts = aliws_dicts
        self.client_node_configuration = client_node_configuration
        self.created_at = created_at
        self.data_node = data_node
        self.dedicate_master = dedicate_master
        self.description = description
        self.dict_list = dict_list
        self.domain = domain
        self.elastic_data_node_configuration = elastic_data_node_configuration
        self.enable_kibana_private_network = enable_kibana_private_network
        self.enable_kibana_public_network = enable_kibana_public_network
        self.enable_public = enable_public
        self.end_time = end_time
        self.es_config = es_config
        self.es_ipwhitelist = es_ipwhitelist
        self.es_version = es_version
        self.extend_configs = extend_configs
        self.have_client_node = have_client_node
        self.have_elastic_data_node = have_elastic_data_node
        self.have_kibana = have_kibana
        self.ik_hot_dicts = ik_hot_dicts
        self.instance_id = instance_id
        self.kibana_configuration = kibana_configuration
        self.kibana_domain = kibana_domain
        self.kibana_ipwhitelist = kibana_ipwhitelist
        self.kibana_port = kibana_port
        self.kibana_private_domain = kibana_private_domain
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist
        self.kibana_private_port = kibana_private_port
        self.kibana_protocol = kibana_protocol
        self.master_configuration = master_configuration
        self.network_config = network_config
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_type = payment_type
        self.port = port
        self.private_network_ip_white_list = private_network_ip_white_list
        self.product_type = product_type
        self.protocol = protocol
        self.public_domain = public_domain
        self.public_ip_whitelist = public_ip_whitelist
        self.public_port = public_port
        self.read_write_policy = read_write_policy
        self.resource_group_id = resource_group_id
        self.service_vpc = service_vpc
        self.status = status
        self.synonyms_dicts = synonyms_dicts
        self.tags = tags
        self.updated_at = updated_at
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
        if self.read_write_policy:
            self.read_write_policy.validate()
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

        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.data_node is not None:
            result['dataNode'] = self.data_node

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

        if self.es_config is not None:
            result['esConfig'] = self.es_config

        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.extend_configs is not None:
            result['extendConfigs'] = self.extend_configs

        if self.have_client_node is not None:
            result['haveClientNode'] = self.have_client_node

        if self.have_elastic_data_node is not None:
            result['haveElasticDataNode'] = self.have_elastic_data_node

        if self.have_kibana is not None:
            result['haveKibana'] = self.have_kibana

        result['ikHotDicts'] = []
        if self.ik_hot_dicts is not None:
            for k1 in self.ik_hot_dicts:
                result['ikHotDicts'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

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

        if self.kibana_protocol is not None:
            result['kibanaProtocol'] = self.kibana_protocol

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

        if self.private_network_ip_white_list is not None:
            result['privateNetworkIpWhiteList'] = self.private_network_ip_white_list

        if self.product_type is not None:
            result['productType'] = self.product_type

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain

        if self.public_ip_whitelist is not None:
            result['publicIpWhitelist'] = self.public_ip_whitelist

        if self.public_port is not None:
            result['publicPort'] = self.public_port

        if self.read_write_policy is not None:
            result['readWritePolicy'] = self.read_write_policy.to_map()

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
            temp_model = main_models.ElasticsearchAdvancedSetting()
            self.advanced_setting = temp_model.from_map(m.get('advancedSetting'))

        self.aliws_dicts = []
        if m.get('aliwsDicts') is not None:
            for k1 in m.get('aliwsDicts'):
                temp_model = main_models.DictInfo()
                self.aliws_dicts.append(temp_model.from_map(k1))

        if m.get('clientNodeConfiguration') is not None:
            temp_model = main_models.ClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m.get('clientNodeConfiguration'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dataNode') is not None:
            self.data_node = m.get('dataNode')

        if m.get('dedicateMaster') is not None:
            self.dedicate_master = m.get('dedicateMaster')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.dict_list = []
        if m.get('dictList') is not None:
            for k1 in m.get('dictList'):
                temp_model = main_models.DictInfo()
                self.dict_list.append(temp_model.from_map(k1))

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = main_models.ElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m.get('elasticDataNodeConfiguration'))

        if m.get('enableKibanaPrivateNetwork') is not None:
            self.enable_kibana_private_network = m.get('enableKibanaPrivateNetwork')

        if m.get('enableKibanaPublicNetwork') is not None:
            self.enable_kibana_public_network = m.get('enableKibanaPublicNetwork')

        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('esConfig') is not None:
            self.es_config = m.get('esConfig')

        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('extendConfigs') is not None:
            self.extend_configs = m.get('extendConfigs')

        if m.get('haveClientNode') is not None:
            self.have_client_node = m.get('haveClientNode')

        if m.get('haveElasticDataNode') is not None:
            self.have_elastic_data_node = m.get('haveElasticDataNode')

        if m.get('haveKibana') is not None:
            self.have_kibana = m.get('haveKibana')

        self.ik_hot_dicts = []
        if m.get('ikHotDicts') is not None:
            for k1 in m.get('ikHotDicts'):
                temp_model = main_models.DictInfo()
                self.ik_hot_dicts.append(temp_model.from_map(k1))

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.KibanaNodeConfiguration()
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

        if m.get('kibanaProtocol') is not None:
            self.kibana_protocol = m.get('kibanaProtocol')

        if m.get('masterConfiguration') is not None:
            temp_model = main_models.MasterNodeConfiguration()
            self.master_configuration = temp_model.from_map(m.get('masterConfiguration'))

        if m.get('networkConfig') is not None:
            temp_model = main_models.NetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.NodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('privateNetworkIpWhiteList') is not None:
            self.private_network_ip_white_list = m.get('privateNetworkIpWhiteList')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')

        if m.get('publicIpWhitelist') is not None:
            self.public_ip_whitelist = m.get('publicIpWhitelist')

        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')

        if m.get('readWritePolicy') is not None:
            temp_model = main_models.ReadWritePolicy()
            self.read_write_policy = temp_model.from_map(m.get('readWritePolicy'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('serviceVpc') is not None:
            self.service_vpc = m.get('serviceVpc')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k1 in m.get('synonymsDicts'):
                temp_model = main_models.DictInfo()
                self.synonyms_dicts.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('warmNode') is not None:
            self.warm_node = m.get('warmNode')

        if m.get('warmNodeConfiguration') is not None:
            temp_model = main_models.WarmNodeConfiguration()
            self.warm_node_configuration = temp_model.from_map(m.get('warmNodeConfiguration'))

        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')

        self.zone_infos = []
        if m.get('zoneInfos') is not None:
            for k1 in m.get('zoneInfos'):
                temp_model = main_models.ZoneInfo()
                self.zone_infos.append(temp_model.from_map(k1))

        return self

class ElasticsearchAdvancedSetting(DaraModel):
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

