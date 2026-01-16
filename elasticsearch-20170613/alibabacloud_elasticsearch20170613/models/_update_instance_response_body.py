# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.UpdateInstanceResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # The time when the instance was created.
        self.request_id = request_id
        # The state of the instance. Valid values:
        # 
        # *   active: normal
        # *   activating: taking effect
        # *   inactive: frozen
        # *   invalid: invalid
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpdateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class UpdateInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        domain: str = None,
        es_version: str = None,
        instance_id: str = None,
        kibana_configuration: main_models.UpdateInstanceResponseBodyResultKibanaConfiguration = None,
        master_configuration: main_models.UpdateInstanceResponseBodyResultMasterConfiguration = None,
        node_amount: int = None,
        node_spec: main_models.UpdateInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        status: str = None,
    ):
        # The private domain name of the instance.
        self.created_at = created_at
        # The configuration of data nodes.
        self.description = description
        # The ID of the instance.
        self.domain = domain
        # The node specifications.
        self.es_version = es_version
        # The storage space of the node. Unit: GB.
        self.instance_id = instance_id
        # The size of the node storage space.
        self.kibana_configuration = kibana_configuration
        # The storage space of the node. Unit: GB.
        self.master_configuration = master_configuration
        # The billing method of the instance. Valid values:
        # 
        # *   prepaid: subscription
        # *   postpaid: pay-as-you-go
        self.node_amount = node_amount
        # The storage type of the node. Valid values:
        # 
        # *   cloud_ssd: standard SSD
        # *   cloud_efficiency: ultra disk
        self.node_spec = node_spec
        # The edition of the dedicated KMS instance.
        self.payment_type = payment_type
        # The name of the instance.
        self.status = status

    def validate(self):
        if self.kibana_configuration:
            self.kibana_configuration.validate()
        if self.master_configuration:
            self.master_configuration.validate()
        if self.node_spec:
            self.node_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.domain is not None:
            result['domain'] = self.domain

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()

        if self.master_configuration is not None:
            result['masterConfiguration'] = self.master_configuration.to_map()

        if self.node_amount is not None:
            result['nodeAmount'] = self.node_amount

        if self.node_spec is not None:
            result['nodeSpec'] = self.node_spec.to_map()

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.UpdateInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m.get('kibanaConfiguration'))

        if m.get('masterConfiguration') is not None:
            temp_model = main_models.UpdateInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m.get('masterConfiguration'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.UpdateInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class UpdateInstanceResponseBodyResultNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The node specifications.
        self.disk = disk
        # The number of nodes.
        self.disk_type = disk_type
        # The configuration of Kibana nodes.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class UpdateInstanceResponseBodyResultMasterConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        self.amount = amount
        self.disk = disk
        self.disk_type = disk_type
        # The storage type of the node. Only cloud_ssd(SSD cloud disk) is supported.
        self.spec = spec

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

        return self

class UpdateInstanceResponseBodyResultKibanaConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The configuration of dedicated master nodes.
        self.amount = amount
        # The node specifications.
        self.disk = disk
        # The number of nodes.
        self.disk_type = disk_type
        # The storage type of the node. This parameter can be ignored.
        self.spec = spec

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

        return self

