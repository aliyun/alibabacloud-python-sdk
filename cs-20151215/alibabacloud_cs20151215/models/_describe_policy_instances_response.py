# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribePolicyInstancesResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribePolicyInstancesResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribePolicyInstancesResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribePolicyInstancesResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        cluster_id: str = None,
        instance_name: str = None,
        policy_name: str = None,
        policy_category: str = None,
        policy_description: str = None,
        policy_parameters: str = None,
        policy_severity: str = None,
        policy_scope: str = None,
        policy_action: str = None,
        created: str = None,
        updated: str = None,
        resource_id: str = None,
        total_violations: int = None,
        is_deleted: int = None,
    ):
        # The UID of the Alibaba Cloud account that is used to deploy the policy instance.
        self.ali_uid = ali_uid
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the policy instance.
        self.instance_name = instance_name
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy.
        self.policy_category = policy_category
        # The description of the policy template.
        self.policy_description = policy_description
        # The parameters of the policy instance.
        self.policy_parameters = policy_parameters
        # The severity level of the policy instance.
        self.policy_severity = policy_severity
        # The applicable scope of the policy instance.
        # 
        # A value of \\* indicates all namespaces in the cluster. This is the default value.
        # 
        # Multiple namespaces are separated by commas (,).
        self.policy_scope = policy_scope
        # The action of the policy. Valid values:
        # 
        # *   `deny`: Deployments that match the policy are denied.
        # *   `warn`: Alerts are generated for deployments that match the policy.
        self.policy_action = policy_action
        # The creation time of the instance. This parameter is deprecated.
        self.created = created
        # The update time of the instance. This parameter is deprecated.
        self.updated = updated
        # The ID of the resource. This parameter is deprecated.
        self.resource_id = resource_id
        # The number of violations processed in the cluster. This parameter is deprecated.
        self.total_violations = total_violations
        # The status of the deletion. This parameter is deprecated.
        self.is_deleted = is_deleted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['ali_uid'] = self.ali_uid

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.instance_name is not None:
            result['instance_name'] = self.instance_name

        if self.policy_name is not None:
            result['policy_name'] = self.policy_name

        if self.policy_category is not None:
            result['policy_category'] = self.policy_category

        if self.policy_description is not None:
            result['policy_description'] = self.policy_description

        if self.policy_parameters is not None:
            result['policy_parameters'] = self.policy_parameters

        if self.policy_severity is not None:
            result['policy_severity'] = self.policy_severity

        if self.policy_scope is not None:
            result['policy_scope'] = self.policy_scope

        if self.policy_action is not None:
            result['policy_action'] = self.policy_action

        if self.created is not None:
            result['Created'] = self.created

        if self.updated is not None:
            result['Updated'] = self.updated

        if self.resource_id is not None:
            result['resource_id'] = self.resource_id

        if self.total_violations is not None:
            result['total_violations'] = self.total_violations

        if self.is_deleted is not None:
            result['is_deleted'] = self.is_deleted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ali_uid') is not None:
            self.ali_uid = m.get('ali_uid')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')

        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')

        if m.get('policy_category') is not None:
            self.policy_category = m.get('policy_category')

        if m.get('policy_description') is not None:
            self.policy_description = m.get('policy_description')

        if m.get('policy_parameters') is not None:
            self.policy_parameters = m.get('policy_parameters')

        if m.get('policy_severity') is not None:
            self.policy_severity = m.get('policy_severity')

        if m.get('policy_scope') is not None:
            self.policy_scope = m.get('policy_scope')

        if m.get('policy_action') is not None:
            self.policy_action = m.get('policy_action')

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Updated') is not None:
            self.updated = m.get('Updated')

        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')

        if m.get('total_violations') is not None:
            self.total_violations = m.get('total_violations')

        if m.get('is_deleted') is not None:
            self.is_deleted = m.get('is_deleted')

        return self

