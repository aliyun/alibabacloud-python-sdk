# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SmartCluster(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        create_time: str = None,
        dataset_name: str = None,
        description: str = None,
        name: str = None,
        object_id: str = None,
        object_status: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        reason: str = None,
        rule: main_models.SmartClusterRule = None,
        rules: List[main_models.SmartClusterRule] = None,
        update_time: str = None,
    ):
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.create_time = create_time
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The description of the cluster.
        self.description = description
        # The name of the cluster.
        self.name = name
        # The ID of the cluster.
        self.object_id = object_id
        # The status of the cluster.
        self.object_status = object_status
        # The type of the cluster.
        self.object_type = object_type
        # The user ID.
        self.owner_id = owner_id
        # The name of the project.
        self.project_name = project_name
        self.reason = reason
        # The clustering rule.
        self.rule = rule
        self.rules = rules
        # The time when the cluster was updated.
        self.update_time = update_time

    def validate(self):
        if self.rule:
            self.rule.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_status is not None:
            result['ObjectStatus'] = self.object_status

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectStatus') is not None:
            self.object_status = m.get('ObjectStatus')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Rule') is not None:
            temp_model = main_models.SmartClusterRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.SmartClusterRule()
                self.rules.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

