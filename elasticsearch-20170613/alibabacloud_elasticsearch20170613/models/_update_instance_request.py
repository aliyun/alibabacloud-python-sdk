# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        client_node_configuration: main_models.ClientNodeConfiguration = None,
        elastic_data_node_configuration: main_models.ElasticDataNodeConfiguration = None,
        instance_category: str = None,
        kibana_configuration: main_models.KibanaNodeConfiguration = None,
        master_configuration: main_models.MasterNodeConfiguration = None,
        node_amount: int = None,
        node_spec: main_models.NodeSpec = None,
        update_type: str = None,
        warm_node_configuration: main_models.WarmNodeConfiguration = None,
        client_token: str = None,
        force: bool = None,
        order_action_type: str = None,
    ):
        self.client_node_configuration = client_node_configuration
        self.elastic_data_node_configuration = elastic_data_node_configuration
        self.instance_category = instance_category
        self.kibana_configuration = kibana_configuration
        self.master_configuration = master_configuration
        self.node_amount = node_amount
        self.node_spec = node_spec
        self.update_type = update_type
        self.warm_node_configuration = warm_node_configuration
        # The result of the request.
        self.client_token = client_token
        self.force = force
        # The number of data nodes.
        self.order_action_type = order_action_type

    def validate(self):
        if self.client_node_configuration:
            self.client_node_configuration.validate()
        if self.elastic_data_node_configuration:
            self.elastic_data_node_configuration.validate()
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.node_spec:
            self.node_spec.validate()
        if self.warm_node_configuration:
            self.warm_node_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_node_configuration is not None:
            result['clientNodeConfiguration'] = self.client_node_configuration.to_map()

        if self.elastic_data_node_configuration is not None:
            result['elasticDataNodeConfiguration'] = self.elastic_data_node_configuration.to_map()

        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category

        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()

        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.update_type is not None:
            result['updateType'] = self.update_type

        if self.warm_node_configuration is not None:
            result['warmNodeConfiguration'] = self.warm_node_configuration.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.force is not None:
            result['force'] = self.force

        if self.order_action_type is not None:
            result['orderActionType'] = self.order_action_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientNodeConfiguration') is not None:
            temp_model = main_models.ClientNodeConfiguration()
            self.client_node_configuration = temp_model.from_map(m.get('clientNodeConfiguration'))

        if m.get('elasticDataNodeConfiguration') is not None:
            temp_model = main_models.ElasticDataNodeConfiguration()
            self.elastic_data_node_configuration = temp_model.from_map(m.get('elasticDataNodeConfiguration'))

        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.KibanaNodeConfiguration()
            self.kibana_configuration = temp_model.from_map(m.get('kibanaConfiguration'))

        if m.get('masterConfiguration') is not None:
            temp_model = main_models.MasterNodeConfiguration()
            self.master_configuration = temp_model.from_map(m.get('masterConfiguration'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.NodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('updateType') is not None:
            self.update_type = m.get('updateType')

        if m.get('warmNodeConfiguration') is not None:
            temp_model = main_models.WarmNodeConfiguration()
            self.warm_node_configuration = temp_model.from_map(m.get('warmNodeConfiguration'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('force') is not None:
            self.force = m.get('force')

        if m.get('orderActionType') is not None:
            self.order_action_type = m.get('orderActionType')

        return self

