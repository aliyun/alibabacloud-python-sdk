# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class RestartInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.RestartInstanceResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return results.
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
            temp_model = main_models.RestartInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class RestartInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        dict_list: List[main_models.RestartInstanceResponseBodyResultDictList] = None,
        domain: str = None,
        es_version: str = None,
        instance_id: str = None,
        kibana_configuration: main_models.RestartInstanceResponseBodyResultKibanaConfiguration = None,
        kibana_domain: str = None,
        kibana_port: int = None,
        master_configuration: main_models.RestartInstanceResponseBodyResultMasterConfiguration = None,
        network_config: main_models.RestartInstanceResponseBodyResultNetworkConfig = None,
        node_amount: int = None,
        node_spec: main_models.RestartInstanceResponseBodyResultNodeSpec = None,
        payment_type: str = None,
        public_domain: str = None,
        public_port: int = None,
        status: str = None,
        synonyms_dicts: List[main_models.RestartInstanceResponseBodyResultSynonymsDicts] = None,
        updated_at: str = None,
    ):
        # The time when the instance was created.
        self.created_at = created_at
        # The name of the instance.
        self.description = description
        # The configuration of the IK dictionaries.
        self.dict_list = dict_list
        # The intranet access address of the instance.
        self.domain = domain
        # The version of the instance.
        self.es_version = es_version
        # The ID of the instance.
        self.instance_id = instance_id
        # The configuration of Kibana nodes.
        self.kibana_configuration = kibana_configuration
        # The public network access address of Kibana.
        self.kibana_domain = kibana_domain
        # The public port of the Kibana network.
        self.kibana_port = kibana_port
        # The configuration of dedicated master nodes.
        self.master_configuration = master_configuration
        # The network configuration.
        self.network_config = network_config
        # The number of data nodes.
        self.node_amount = node_amount
        # The configuration of data nodes.
        self.node_spec = node_spec
        # The billing method of the created ECS instance.
        # 
        # Valid values: prepaid and postpaid.
        self.payment_type = payment_type
        # The public network access address.
        self.public_domain = public_domain
        # The public network port.
        self.public_port = public_port
        # The state of the cluster.
        # 
        # Supported: active (normal), activating (initializing), inactive (blocked), and invalid (expired).
        self.status = status
        # The configuration of the synonym dictionaries.
        self.synonyms_dicts = synonyms_dicts
        # The time when the instance was last updated.
        self.updated_at = updated_at

    def validate(self):
        if self.dict_list:
            for v1 in self.dict_list:
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

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        result['dictList'] = []
        if self.dict_list is not None:
            for k1 in self.dict_list:
                result['dictList'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['domain'] = self.domain

        if self.es_version is not None:
            result['esVersion'] = self.es_version

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.kibana_configuration is not None:
            result['kibanaConfiguration'] = self.kibana_configuration.to_map()

        if self.kibana_domain is not None:
            result['kibanaDomain'] = self.kibana_domain

        if self.kibana_port is not None:
            result['kibanaPort'] = self.kibana_port

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

        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain

        if self.public_port is not None:
            result['publicPort'] = self.public_port

        if self.status is not None:
            result['status'] = self.status

        result['synonymsDicts'] = []
        if self.synonyms_dicts is not None:
            for k1 in self.synonyms_dicts:
                result['synonymsDicts'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.dict_list = []
        if m.get('dictList') is not None:
            for k1 in m.get('dictList'):
                temp_model = main_models.RestartInstanceResponseBodyResultDictList()
                self.dict_list.append(temp_model.from_map(k1))

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('esVersion') is not None:
            self.es_version = m.get('esVersion')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('kibanaConfiguration') is not None:
            temp_model = main_models.RestartInstanceResponseBodyResultKibanaConfiguration()
            self.kibana_configuration = temp_model.from_map(m.get('kibanaConfiguration'))

        if m.get('kibanaDomain') is not None:
            self.kibana_domain = m.get('kibanaDomain')

        if m.get('kibanaPort') is not None:
            self.kibana_port = m.get('kibanaPort')

        if m.get('masterConfiguration') is not None:
            temp_model = main_models.RestartInstanceResponseBodyResultMasterConfiguration()
            self.master_configuration = temp_model.from_map(m.get('masterConfiguration'))

        if m.get('networkConfig') is not None:
            temp_model = main_models.RestartInstanceResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        if m.get('nodeAmount') is not None:
            self.node_amount = m.get('nodeAmount')

        if m.get('nodeSpec') is not None:
            temp_model = main_models.RestartInstanceResponseBodyResultNodeSpec()
            self.node_spec = temp_model.from_map(m.get('nodeSpec'))

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')

        if m.get('publicPort') is not None:
            self.public_port = m.get('publicPort')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.synonyms_dicts = []
        if m.get('synonymsDicts') is not None:
            for k1 in m.get('synonymsDicts'):
                temp_model = main_models.RestartInstanceResponseBodyResultSynonymsDicts()
                self.synonyms_dicts.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class RestartInstanceResponseBodyResultSynonymsDicts(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        # The size of the Dictionary File. Unit: bytes.
        self.file_size = file_size
        # The name of the dictionary file.
        self.name = name
        # The source type. Valid values:
        # 
        # *   OSS:OSS open storage (the OSS storage space must be publicly readable.)
        # *   ORIGIN: open-source Elasticsearch
        # *   UPLOAD
        self.source_type = source_type
        # The type of the dictionary. Valid values:
        # 
        # *   STOP: The STOP word.
        # *   MAIN: MAIN Dictionary
        # *   SYNONYMS: SYNONYMS
        # *   ALI_WS: an Alibaba Dictionary.
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

class RestartInstanceResponseBodyResultNodeSpec(DaraModel):
    def __init__(
        self,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The storage space size per data node. Unit: GB.
        self.disk = disk
        # The storage type of the node. Valid values: cloud_ssd and cloud_efficiency.
        self.disk_type = disk_type
        # The specification of data nodes.
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

class RestartInstanceResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
    ):
        # The network type. Only Virtual Private Cloud (VPC) is supported.
        self.type = type
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone where the instance is deployed.
        self.vs_area = vs_area
        # The ID of the vSwitch associated with the specified VPC.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

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

        return self

class RestartInstanceResponseBodyResultMasterConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The number of nodes in the cluster.
        self.amount = amount
        # The size of the node storage space. Unit: GB.
        self.disk = disk
        # The storage type of the node. This tool only supports cloud_ssd (cloud SSD) disks.
        self.disk_type = disk_type
        # The node specifications of the cluster.
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

class RestartInstanceResponseBodyResultKibanaConfiguration(DaraModel):
    def __init__(
        self,
        amount: int = None,
        disk: int = None,
        disk_type: str = None,
        spec: str = None,
    ):
        # The number of performance metrics.
        self.amount = amount
        # The size of the node storage space. Unit: GB.
        self.disk = disk
        # The storage type of the node.
        self.disk_type = disk_type
        # The specification of data nodes.
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

class RestartInstanceResponseBodyResultDictList(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        # The size of the Dictionary File. Unit: bytes.
        self.file_size = file_size
        # The name of the dictionary file.
        self.name = name
        # The source type. Valid values:
        # 
        # *   OSS: OSS open storage (need to ensure that OSS storage space is public readable.)
        # *   ORIGIN: Open source Elasticsearch
        # *   UPLOAD: Uploaded files
        self.source_type = source_type
        # The type of the dictionary. Valid values:
        # 
        # *   STOP: The STOP word.
        # *   MAIN: MAIN Dictionary
        # *   SYNONYMS: SYNONYMS
        # *   ALI_WS: an Alibaba Dictionary.
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

