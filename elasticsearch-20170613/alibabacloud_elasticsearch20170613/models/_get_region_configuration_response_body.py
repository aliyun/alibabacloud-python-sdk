# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetRegionConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetRegionConfigurationResponseBodyResult = None,
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
            temp_model = main_models.GetRegionConfigurationResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetRegionConfigurationResponseBodyResult(DaraModel):
    def __init__(
        self,
        client_node_amount_range: main_models.GetRegionConfigurationResponseBodyResultClientNodeAmountRange = None,
        client_node_disk_list: List[main_models.GetRegionConfigurationResponseBodyResultClientNodeDiskList] = None,
        client_node_spec: List[str] = None,
        create_url: str = None,
        data_disk_list: List[main_models.GetRegionConfigurationResponseBodyResultDataDiskList] = None,
        elastic_node_properties: main_models.GetRegionConfigurationResponseBodyResultElasticNodeProperties = None,
        env: str = None,
        es_versions: List[str] = None,
        es_versions_latest_list: List[main_models.GetRegionConfigurationResponseBodyResultEsVersionsLatestList] = None,
        instance_support_nodes: List[str] = None,
        jvm_confine: main_models.GetRegionConfigurationResponseBodyResultJvmConfine = None,
        kibana_node_properties: main_models.GetRegionConfigurationResponseBodyResultKibanaNodeProperties = None,
        logstash_zones: List[str] = None,
        master_disk_list: List[main_models.GetRegionConfigurationResponseBodyResultMasterDiskList] = None,
        master_spec: List[str] = None,
        node: main_models.GetRegionConfigurationResponseBodyResultNode = None,
        node_spec_list: List[main_models.GetRegionConfigurationResponseBodyResultNodeSpecList] = None,
        region_id: str = None,
        support_versions: List[main_models.GetRegionConfigurationResponseBodyResultSupportVersions] = None,
        warm_node_properties: main_models.GetRegionConfigurationResponseBodyResultWarmNodeProperties = None,
        zones: List[str] = None,
    ):
        self.client_node_amount_range = client_node_amount_range
        self.client_node_disk_list = client_node_disk_list
        self.client_node_spec = client_node_spec
        self.create_url = create_url
        self.data_disk_list = data_disk_list
        self.elastic_node_properties = elastic_node_properties
        self.env = env
        self.es_versions = es_versions
        self.es_versions_latest_list = es_versions_latest_list
        self.instance_support_nodes = instance_support_nodes
        self.jvm_confine = jvm_confine
        self.kibana_node_properties = kibana_node_properties
        self.logstash_zones = logstash_zones
        self.master_disk_list = master_disk_list
        self.master_spec = master_spec
        self.node = node
        self.node_spec_list = node_spec_list
        self.region_id = region_id
        self.support_versions = support_versions
        self.warm_node_properties = warm_node_properties
        self.zones = zones

    def validate(self):
        if self.client_node_amount_range:
            self.client_node_amount_range.validate()
        if self.client_node_disk_list:
            for v1 in self.client_node_disk_list:
                 if v1:
                    v1.validate()
        if self.data_disk_list:
            for v1 in self.data_disk_list:
                 if v1:
                    v1.validate()
        if self.elastic_node_properties:
            self.elastic_node_properties.validate()
        if self.es_versions_latest_list:
            for v1 in self.es_versions_latest_list:
                 if v1:
                    v1.validate()
        if self.jvm_confine:
            self.jvm_confine.validate()
        if self.kibana_node_properties:
            self.kibana_node_properties.validate()
        if self.master_disk_list:
            for v1 in self.master_disk_list:
                 if v1:
                    v1.validate()
        if self.node:
            self.node.validate()
        if self.node_spec_list:
            for v1 in self.node_spec_list:
                 if v1:
                    v1.validate()
        if self.support_versions:
            for v1 in self.support_versions:
                 if v1:
                    v1.validate()
        if self.warm_node_properties:
            self.warm_node_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_node_amount_range is not None:
            result['clientNodeAmountRange'] = self.client_node_amount_range.to_map()

        result['clientNodeDiskList'] = []
        if self.client_node_disk_list is not None:
            for k1 in self.client_node_disk_list:
                result['clientNodeDiskList'].append(k1.to_map() if k1 else None)

        if self.client_node_spec is not None:
            result['clientNodeSpec'] = self.client_node_spec

        if self.create_url is not None:
            result['createUrl'] = self.create_url

        result['dataDiskList'] = []
        if self.data_disk_list is not None:
            for k1 in self.data_disk_list:
                result['dataDiskList'].append(k1.to_map() if k1 else None)

        if self.elastic_node_properties is not None:
            result['elasticNodeProperties'] = self.elastic_node_properties.to_map()

        if self.env is not None:
            result['env'] = self.env

        if self.es_versions is not None:
            result['esVersions'] = self.es_versions

        result['esVersionsLatestList'] = []
        if self.es_versions_latest_list is not None:
            for k1 in self.es_versions_latest_list:
                result['esVersionsLatestList'].append(k1.to_map() if k1 else None)

        if self.instance_support_nodes is not None:
            result['instanceSupportNodes'] = self.instance_support_nodes

        if self.jvm_confine is not None:
            result['jvmConfine'] = self.jvm_confine.to_map()

        if self.kibana_node_properties is not None:
            result['kibanaNodeProperties'] = self.kibana_node_properties.to_map()

        if self.logstash_zones is not None:
            result['logstashZones'] = self.logstash_zones

        result['masterDiskList'] = []
        if self.master_disk_list is not None:
            for k1 in self.master_disk_list:
                result['masterDiskList'].append(k1.to_map() if k1 else None)

        if self.master_spec is not None:
            result['masterSpec'] = self.master_spec

        if self.node is not None:
            result['node'] = self.node.to_map()

        result['nodeSpecList'] = []
        if self.node_spec_list is not None:
            for k1 in self.node_spec_list:
                result['nodeSpecList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['regionId'] = self.region_id

        result['supportVersions'] = []
        if self.support_versions is not None:
            for k1 in self.support_versions:
                result['supportVersions'].append(k1.to_map() if k1 else None)

        if self.warm_node_properties is not None:
            result['warmNodeProperties'] = self.warm_node_properties.to_map()

        if self.zones is not None:
            result['zones'] = self.zones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientNodeAmountRange') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultClientNodeAmountRange()
            self.client_node_amount_range = temp_model.from_map(m.get('clientNodeAmountRange'))

        self.client_node_disk_list = []
        if m.get('clientNodeDiskList') is not None:
            for k1 in m.get('clientNodeDiskList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultClientNodeDiskList()
                self.client_node_disk_list.append(temp_model.from_map(k1))

        if m.get('clientNodeSpec') is not None:
            self.client_node_spec = m.get('clientNodeSpec')

        if m.get('createUrl') is not None:
            self.create_url = m.get('createUrl')

        self.data_disk_list = []
        if m.get('dataDiskList') is not None:
            for k1 in m.get('dataDiskList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultDataDiskList()
                self.data_disk_list.append(temp_model.from_map(k1))

        if m.get('elasticNodeProperties') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultElasticNodeProperties()
            self.elastic_node_properties = temp_model.from_map(m.get('elasticNodeProperties'))

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('esVersions') is not None:
            self.es_versions = m.get('esVersions')

        self.es_versions_latest_list = []
        if m.get('esVersionsLatestList') is not None:
            for k1 in m.get('esVersionsLatestList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultEsVersionsLatestList()
                self.es_versions_latest_list.append(temp_model.from_map(k1))

        if m.get('instanceSupportNodes') is not None:
            self.instance_support_nodes = m.get('instanceSupportNodes')

        if m.get('jvmConfine') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultJvmConfine()
            self.jvm_confine = temp_model.from_map(m.get('jvmConfine'))

        if m.get('kibanaNodeProperties') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultKibanaNodeProperties()
            self.kibana_node_properties = temp_model.from_map(m.get('kibanaNodeProperties'))

        if m.get('logstashZones') is not None:
            self.logstash_zones = m.get('logstashZones')

        self.master_disk_list = []
        if m.get('masterDiskList') is not None:
            for k1 in m.get('masterDiskList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultMasterDiskList()
                self.master_disk_list.append(temp_model.from_map(k1))

        if m.get('masterSpec') is not None:
            self.master_spec = m.get('masterSpec')

        if m.get('node') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultNode()
            self.node = temp_model.from_map(m.get('node'))

        self.node_spec_list = []
        if m.get('nodeSpecList') is not None:
            for k1 in m.get('nodeSpecList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultNodeSpecList()
                self.node_spec_list.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        self.support_versions = []
        if m.get('supportVersions') is not None:
            for k1 in m.get('supportVersions'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultSupportVersions()
                self.support_versions.append(temp_model.from_map(k1))

        if m.get('warmNodeProperties') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultWarmNodeProperties()
            self.warm_node_properties = temp_model.from_map(m.get('warmNodeProperties'))

        if m.get('zones') is not None:
            self.zones = m.get('zones')

        return self

class GetRegionConfigurationResponseBodyResultWarmNodeProperties(DaraModel):
    def __init__(
        self,
        amount_range: main_models.GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange = None,
        disk_list: List[main_models.GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList] = None,
        spec: List[str] = None,
    ):
        self.amount_range = amount_range
        self.disk_list = disk_list
        self.spec = spec

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()
        if self.disk_list:
            for v1 in self.disk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()

        result['diskList'] = []
        if self.disk_list is not None:
            for k1 in self.disk_list:
                result['diskList'].append(k1.to_map() if k1 else None)

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amountRange') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m.get('amountRange'))

        self.disk_list = []
        if m.get('diskList') is not None:
            for k1 in m.get('diskList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList()
                self.disk_list.append(temp_model.from_map(k1))

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class GetRegionConfigurationResponseBodyResultWarmNodePropertiesDiskList(DaraModel):
    def __init__(
        self,
        disk_encryption: bool = None,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        value_limit_set: List[str] = None,
    ):
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.value_limit_set = value_limit_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')

        return self

class GetRegionConfigurationResponseBodyResultWarmNodePropertiesAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

class GetRegionConfigurationResponseBodyResultSupportVersions(DaraModel):
    def __init__(
        self,
        instance_category: str = None,
        support_version_list: List[main_models.GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList] = None,
    ):
        self.instance_category = instance_category
        self.support_version_list = support_version_list

    def validate(self):
        if self.support_version_list:
            for v1 in self.support_version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_category is not None:
            result['instanceCategory'] = self.instance_category

        result['supportVersionList'] = []
        if self.support_version_list is not None:
            for k1 in self.support_version_list:
                result['supportVersionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceCategory') is not None:
            self.instance_category = m.get('instanceCategory')

        self.support_version_list = []
        if m.get('supportVersionList') is not None:
            for k1 in m.get('supportVersionList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList()
                self.support_version_list.append(temp_model.from_map(k1))

        return self

class GetRegionConfigurationResponseBodyResultSupportVersionsSupportVersionList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetRegionConfigurationResponseBodyResultNodeSpecList(DaraModel):
    def __init__(
        self,
        cpu_count: int = None,
        disk: int = None,
        disk_type: str = None,
        enable: bool = None,
        memory_size: int = None,
        spec: str = None,
        spec_group_type: str = None,
    ):
        self.cpu_count = cpu_count
        self.disk = disk
        self.disk_type = disk_type
        self.enable = enable
        self.memory_size = memory_size
        self.spec = spec
        self.spec_group_type = spec_group_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.enable is not None:
            result['enable'] = self.enable

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_group_type is not None:
            result['specGroupType'] = self.spec_group_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specGroupType') is not None:
            self.spec_group_type = m.get('specGroupType')

        return self

class GetRegionConfigurationResponseBodyResultNode(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

class GetRegionConfigurationResponseBodyResultMasterDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        return self

class GetRegionConfigurationResponseBodyResultKibanaNodeProperties(DaraModel):
    def __init__(
        self,
        amount_range: main_models.GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange = None,
        spec: List[str] = None,
    ):
        self.amount_range = amount_range
        self.spec = spec

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amountRange') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m.get('amountRange'))

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class GetRegionConfigurationResponseBodyResultKibanaNodePropertiesAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

class GetRegionConfigurationResponseBodyResultJvmConfine(DaraModel):
    def __init__(
        self,
        memory: int = None,
        support_es_versions: List[str] = None,
        support_gcs: List[str] = None,
    ):
        self.memory = memory
        self.support_es_versions = support_es_versions
        self.support_gcs = support_gcs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory is not None:
            result['memory'] = self.memory

        if self.support_es_versions is not None:
            result['supportEsVersions'] = self.support_es_versions

        if self.support_gcs is not None:
            result['supportGcs'] = self.support_gcs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('supportEsVersions') is not None:
            self.support_es_versions = m.get('supportEsVersions')

        if m.get('supportGcs') is not None:
            self.support_gcs = m.get('supportGcs')

        return self

class GetRegionConfigurationResponseBodyResultEsVersionsLatestList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetRegionConfigurationResponseBodyResultElasticNodeProperties(DaraModel):
    def __init__(
        self,
        amount_range: main_models.GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange = None,
        disk_list: List[main_models.GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList] = None,
        spec: List[str] = None,
    ):
        self.amount_range = amount_range
        self.disk_list = disk_list
        self.spec = spec

    def validate(self):
        if self.amount_range:
            self.amount_range.validate()
        if self.disk_list:
            for v1 in self.disk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount_range is not None:
            result['amountRange'] = self.amount_range.to_map()

        result['diskList'] = []
        if self.disk_list is not None:
            for k1 in self.disk_list:
                result['diskList'].append(k1.to_map() if k1 else None)

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amountRange') is not None:
            temp_model = main_models.GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange()
            self.amount_range = temp_model.from_map(m.get('amountRange'))

        self.disk_list = []
        if m.get('diskList') is not None:
            for k1 in m.get('diskList'):
                temp_model = main_models.GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList()
                self.disk_list.append(temp_model.from_map(k1))

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class GetRegionConfigurationResponseBodyResultElasticNodePropertiesDiskList(DaraModel):
    def __init__(
        self,
        disk_encryption: bool = None,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        value_limit_set: List[str] = None,
    ):
        self.disk_encryption = disk_encryption
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.value_limit_set = value_limit_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_encryption is not None:
            result['diskEncryption'] = self.disk_encryption

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskEncryption') is not None:
            self.disk_encryption = m.get('diskEncryption')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')

        return self

class GetRegionConfigurationResponseBodyResultElasticNodePropertiesAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

class GetRegionConfigurationResponseBodyResultDataDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
        value_limit_set: List[str] = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit
        self.value_limit_set = value_limit_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        if self.value_limit_set is not None:
            result['valueLimitSet'] = self.value_limit_set

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        if m.get('valueLimitSet') is not None:
            self.value_limit_set = m.get('valueLimitSet')

        return self

class GetRegionConfigurationResponseBodyResultClientNodeDiskList(DaraModel):
    def __init__(
        self,
        disk_type: str = None,
        max_size: int = None,
        min_size: int = None,
        scale_limit: int = None,
    ):
        self.disk_type = disk_type
        self.max_size = max_size
        self.min_size = min_size
        self.scale_limit = scale_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.min_size is not None:
            result['minSize'] = self.min_size

        if self.scale_limit is not None:
            result['scaleLimit'] = self.scale_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('minSize') is not None:
            self.min_size = m.get('minSize')

        if m.get('scaleLimit') is not None:
            self.scale_limit = m.get('scaleLimit')

        return self

class GetRegionConfigurationResponseBodyResultClientNodeAmountRange(DaraModel):
    def __init__(
        self,
        max_amount: int = None,
        min_amount: int = None,
    ):
        self.max_amount = max_amount
        self.min_amount = min_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_amount is not None:
            result['maxAmount'] = self.max_amount

        if self.min_amount is not None:
            result['minAmount'] = self.min_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxAmount') is not None:
            self.max_amount = m.get('maxAmount')

        if m.get('minAmount') is not None:
            self.min_amount = m.get('minAmount')

        return self

