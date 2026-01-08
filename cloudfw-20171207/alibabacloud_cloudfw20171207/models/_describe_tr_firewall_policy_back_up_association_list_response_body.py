# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrFirewallPolicyBackUpAssociationListResponseBody(DaraModel):
    def __init__(
        self,
        policy_association_backup_configs: List[main_models.DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs] = None,
        request_id: str = None,
    ):
        # The route tables.
        self.policy_association_backup_configs = policy_association_backup_configs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy_association_backup_configs:
            for v1 in self.policy_association_backup_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolicyAssociationBackupConfigs'] = []
        if self.policy_association_backup_configs is not None:
            for k1 in self.policy_association_backup_configs:
                result['PolicyAssociationBackupConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_association_backup_configs = []
        if m.get('PolicyAssociationBackupConfigs') is not None:
            for k1 in m.get('PolicyAssociationBackupConfigs'):
                temp_model = main_models.DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs()
                self.policy_association_backup_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTrFirewallPolicyBackUpAssociationListResponseBodyPolicyAssociationBackupConfigs(DaraModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_name: str = None,
        candidate_type: str = None,
        current_route_table_id: str = None,
        original_route_table_id: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The name of the traffic redirection instance.
        self.candidate_name = candidate_name
        # The type of the traffic redirection instance.
        self.candidate_type = candidate_type
        # The route table that is used after traffic redirection.
        self.current_route_table_id = current_route_table_id
        # The ID of the route table.
        self.original_route_table_id = original_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id

        if self.candidate_name is not None:
            result['CandidateName'] = self.candidate_name

        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type

        if self.current_route_table_id is not None:
            result['CurrentRouteTableId'] = self.current_route_table_id

        if self.original_route_table_id is not None:
            result['OriginalRouteTableId'] = self.original_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')

        if m.get('CandidateName') is not None:
            self.candidate_name = m.get('CandidateName')

        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')

        if m.get('CurrentRouteTableId') is not None:
            self.current_route_table_id = m.get('CurrentRouteTableId')

        if m.get('OriginalRouteTableId') is not None:
            self.original_route_table_id = m.get('OriginalRouteTableId')

        return self

