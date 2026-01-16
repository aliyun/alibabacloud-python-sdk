# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        client_node_configuration: main_models.ClientNodeConfiguration = None,
        description: str = None,
        elastic_data_node_configuration: main_models.ElasticDataNodeConfiguration = None,
        es_admin_password: str = None,
        es_version: str = None,
        instance_category: str = None,
        kibana_configuration: main_models.KibanaNodeConfiguration = None,
        master_configuration: main_models.MasterNodeConfiguration = None,
        network_config: main_models.NetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.NodeSpec = None,
        payment_info: main_models.PaymentInfo = None,
        payment_type: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateInstanceRequestTags] = None,
        warm_node_configuration: main_models.WarmNodeConfiguration = None,
        zone_count: int = None,
        client_token: str = None,
    ):
        self.client_node_configuration = client_node_configuration
        self.description = description
        self.elastic_data_node_configuration = elastic_data_node_configuration
        # This parameter is required.
        self.es_admin_password = es_admin_password
        # This parameter is required.
        self.es_version = es_version
        self.instance_category = instance_category
        self.kibana_configuration = kibana_configuration
        self.master_configuration = master_configuration
        # This parameter is required.
        self.network_config = network_config
        # This parameter is required.
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.payment_info = payment_info
        self.payment_type = payment_type
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.warm_node_configuration = warm_node_configuration
        self.zone_count = zone_count
        self.client_token = client_token

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
        if self.payment_info:
            self.payment_info.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.warm_node_configuration:
            self.warm_node_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()

        if self.es_admin_password is not None:
            result['esAdminPassword'] = self.es_admin_password

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category

        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()

        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.payment_info is not None:
            result['paymentInfo'] = self.payment_info.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.warm_node_configuration is not None:
            result['warmNodeConfiguration'] = self.warm_node_configuration.to_map()

        if self.zone_count is not None:
            result['zoneCount'] = self.zone_count

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientNodeConfiguration') is not None:
            temp_model = main_models.ClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m.get('clientNodeConfiguration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = main_models.ElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m.get('elasticDataNodeConfiguration'))

        if m.get('esAdminPassword') is not None:
            self.es_admin_password = m.get('esAdminPassword')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.KibanaNodeConfiguration()
            self.kibana_configuration = temp_model.from_map(m.get('kibanaConfiguration'))

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

        if m.get('paymentInfo') is not None:
            temp_model = main_models.PaymentInfo()
            self.payment_info = temp_model.from_map(m.get('paymentInfo'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('warmNodeConfiguration') is not None:
            temp_model = main_models.WarmNodeConfiguration()
            self.warm_node_configuration = temp_model.from_map(m.get('warmNodeConfiguration'))

        if m.get('zoneCount') is not None:
            self.zone_count = m.get('zoneCount')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateInstanceRequestTags(DaraModel):
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

