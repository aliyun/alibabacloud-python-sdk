# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policies: List[main_models.ListIntegrationPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Page size
        # Default value:
        # 	50
        # Maximum value:
        # 	50
        self.max_results = max_results
        # Pagination token
        self.next_token = next_token
        # Access policy list
        self.policies = policies
        # ID of the request
        self.request_id = request_id
        # Total number of entries
        self.total_count = total_count

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.policies = []
        if m.get('policies') is not None:
            for k1 in m.get('policies'):
                temp_model = main_models.ListIntegrationPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListIntegrationPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        bind_resource: main_models.ListIntegrationPoliciesResponseBodyPoliciesBindResource = None,
        cs_umodel_status: bool = None,
        entity_group: main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroup = None,
        fee_package: str = None,
        managed_info: main_models.ListIntegrationPoliciesResponseBodyPoliciesManagedInfo = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sub_addon_release: main_models.ListIntegrationPoliciesResponseBodyPoliciesSubAddonRelease = None,
        tags: List[main_models.ListIntegrationPoliciesResponseBodyPoliciesTags] = None,
        user_id: str = None,
        workspace: str = None,
    ):
        # Bound resource information
        self.bind_resource = bind_resource
        # Container environment umodel installation status.
        self.cs_umodel_status = cs_umodel_status
        # Entity group
        self.entity_group = entity_group
        # Billing type.
        self.fee_package = fee_package
        # Policy network management information.
        self.managed_info = managed_info
        # Policy ID.
        self.policy_id = policy_id
        # Rule name.
        self.policy_name = policy_name
        # Access center policy type
        self.policy_type = policy_type
        # Region ID.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Number of sub-releases
        self.sub_addon_release = sub_addon_release
        # Resource tag key values.
        self.tags = tags
        # User ID
        self.user_id = user_id
        # Workspace.
        self.workspace = workspace

    def validate(self):
        if self.bind_resource:
            self.bind_resource.validate()
        if self.entity_group:
            self.entity_group.validate()
        if self.managed_info:
            self.managed_info.validate()
        if self.sub_addon_release:
            self.sub_addon_release.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_resource is not None:
            result['bindResource'] = self.bind_resource.to_map()

        if self.cs_umodel_status is not None:
            result['csUmodelStatus'] = self.cs_umodel_status

        if self.entity_group is not None:
            result['entityGroup'] = self.entity_group.to_map()

        if self.fee_package is not None:
            result['feePackage'] = self.fee_package

        if self.managed_info is not None:
            result['managedInfo'] = self.managed_info.to_map()

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.sub_addon_release is not None:
            result['subAddonRelease'] = self.sub_addon_release.to_map()

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindResource') is not None:
            temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesBindResource()
            self.bind_resource = temp_model.from_map(m.get('bindResource'))

        if m.get('csUmodelStatus') is not None:
            self.cs_umodel_status = m.get('csUmodelStatus')

        if m.get('entityGroup') is not None:
            temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroup()
            self.entity_group = temp_model.from_map(m.get('entityGroup'))

        if m.get('feePackage') is not None:
            self.fee_package = m.get('feePackage')

        if m.get('managedInfo') is not None:
            temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesManagedInfo()
            self.managed_info = temp_model.from_map(m.get('managedInfo'))

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('subAddonRelease') is not None:
            temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesSubAddonRelease()
            self.sub_addon_release = temp_model.from_map(m.get('subAddonRelease'))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key
        self.key = key
        # Match value.
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

class ListIntegrationPoliciesResponseBodyPoliciesSubAddonRelease(DaraModel):
    def __init__(
        self,
        ready: int = None,
        total: int = None,
    ):
        # Number of ready sub-releases
        self.ready = ready
        # Number of rules.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ready is not None:
            result['ready'] = self.ready

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ready') is not None:
            self.ready = m.get('ready')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesManagedInfo(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        security_group_id: str = None,
        vswitch_id: str = None,
    ):
        # ENI card ID of the managed probe. For example: eni-xxxx.
        self.eni_id = eni_id
        # Security group ID
        self.security_group_id = security_group_id
        # VSwitch ID.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['eniId'] = self.eni_id

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroup(DaraModel):
    def __init__(
        self,
        description: str = None,
        entity_group_id: str = None,
        entity_group_name: str = None,
        entity_rules: main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRules = None,
        query: str = None,
        region_id: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        # Description.
        self.description = description
        # Entity group ID
        self.entity_group_id = entity_group_id
        # Entity group name
        self.entity_group_name = entity_group_name
        # Entity group
        self.entity_rules = entity_rules
        # Search keywords, supporting document library name and description
        self.query = query
        # Region ID.
        self.region_id = region_id
        # User ID
        self.user_id = user_id
        # Workspace.
        self.workspace = workspace

    def validate(self):
        if self.entity_rules:
            self.entity_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.entity_group_id is not None:
            result['entityGroupId'] = self.entity_group_id

        if self.entity_group_name is not None:
            result['entityGroupName'] = self.entity_group_name

        if self.entity_rules is not None:
            result['entityRules'] = self.entity_rules.to_map()

        if self.query is not None:
            result['query'] = self.query

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('entityGroupId') is not None:
            self.entity_group_id = m.get('entityGroupId')

        if m.get('entityGroupName') is not None:
            self.entity_group_name = m.get('entityGroupName')

        if m.get('entityRules') is not None:
            temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRules()
            self.entity_rules = temp_model.from_map(m.get('entityRules'))

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRules(DaraModel):
    def __init__(
        self,
        annotations: List[main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesAnnotations] = None,
        entity_types: List[str] = None,
        field_rules: List[main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesFieldRules] = None,
        instance_ids: List[str] = None,
        ip_match_rule: main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesIpMatchRule = None,
        labels: List[main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesLabels] = None,
        region_ids: List[str] = None,
        resource_group_id: str = None,
        tags: List[main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesTags] = None,
    ):
        # Annotations
        self.annotations = annotations
        # List of entity types
        self.entity_types = entity_types
        # Field rules
        self.field_rules = field_rules
        # Instance IDs.
        self.instance_ids = instance_ids
        # IP match rule
        self.ip_match_rule = ip_match_rule
        # Labels
        self.labels = labels
        # List of region IDs.
        self.region_ids = region_ids
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Instance tag information.
        self.tags = tags

    def validate(self):
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()
        if self.field_rules:
            for v1 in self.field_rules:
                 if v1:
                    v1.validate()
        if self.ip_match_rule:
            self.ip_match_rule.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['annotations'].append(k1.to_map() if k1 else None)

        if self.entity_types is not None:
            result['entityTypes'] = self.entity_types

        result['fieldRules'] = []
        if self.field_rules is not None:
            for k1 in self.field_rules:
                result['fieldRules'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        if self.ip_match_rule is not None:
            result['ipMatchRule'] = self.ip_match_rule.to_map()

        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

        if self.region_ids is not None:
            result['regionIds'] = self.region_ids

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('annotations') is not None:
            for k1 in m.get('annotations'):
                temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('entityTypes') is not None:
            self.entity_types = m.get('entityTypes')

        self.field_rules = []
        if m.get('fieldRules') is not None:
            for k1 in m.get('fieldRules'):
                temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesFieldRules()
                self.field_rules.append(temp_model.from_map(k1))

        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        if m.get('ipMatchRule') is not None:
            temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesIpMatchRule()
            self.ip_match_rule = temp_model.from_map(m.get('ipMatchRule'))

        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesTags(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # Operation to be performed.
        self.op = op
        # Tag key.
        self.tag_key = tag_key
        # Tag value.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_values is not None:
            result['tagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesLabels(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # Operation to be performed.
        self.op = op
        # Tag key.
        self.tag_key = tag_key
        # Tag values
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_values is not None:
            result['tagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesIpMatchRule(DaraModel):
    def __init__(
        self,
        ip_cidr: str = None,
        ip_field_key: str = None,
    ):
        # IP segment
        self.ip_cidr = ip_cidr
        # Key of the IP field
        self.ip_field_key = ip_field_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_cidr is not None:
            result['ipCidr'] = self.ip_cidr

        if self.ip_field_key is not None:
            result['ipFieldKey'] = self.ip_field_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipCidr') is not None:
            self.ip_cidr = m.get('ipCidr')

        if m.get('ipFieldKey') is not None:
            self.ip_field_key = m.get('ipFieldKey')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesFieldRules(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        field_values: List[str] = None,
        op: str = None,
    ):
        # Unique identifier for the field.
        self.field_key = field_key
        # Field content, multiple values separated by English commas.
        self.field_values = field_values
        # Operation to be performed.
        self.op = op

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.field_values is not None:
            result['fieldValues'] = self.field_values

        if self.op is not None:
            result['op'] = self.op

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('fieldValues') is not None:
            self.field_values = m.get('fieldValues')

        if m.get('op') is not None:
            self.op = m.get('op')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesEntityGroupEntityRulesAnnotations(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # Operation to be performed.
        self.op = op
        # Tag key.
        self.tag_key = tag_key
        # Tag values
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_values is not None:
            result['tagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')

        return self

class ListIntegrationPoliciesResponseBodyPoliciesBindResource(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        vpc_cidr: str = None,
        vpc_id: str = None,
    ):
        # Cluster ID.
        self.cluster_id = cluster_id
        # Cluster type.
        self.cluster_type = cluster_type
        # VPC CIDR
        self.vpc_cidr = vpc_cidr
        # Virtual Private Cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type

        if self.vpc_cidr is not None:
            result['vpcCidr'] = self.vpc_cidr

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')

        if m.get('vpcCidr') is not None:
            self.vpc_cidr = m.get('vpcCidr')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

