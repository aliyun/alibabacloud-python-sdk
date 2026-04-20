# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAIDBClusterTaskRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_class: str = None,
        dataset_path: str = None,
        eval_dataset_path: str = None,
        kube_type: str = None,
        model_name: str = None,
        model_source: str = None,
        model_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        running_parameter: str = None,
        security_group_id: str = None,
        task_name: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dbinstance_class = dbinstance_class
        self.dataset_path = dataset_path
        self.eval_dataset_path = eval_dataset_path
        # This parameter is required.
        self.kube_type = kube_type
        # This parameter is required.
        self.model_name = model_name
        # This parameter is required.
        self.model_source = model_source
        self.model_type = model_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.running_parameter = running_parameter
        self.security_group_id = security_group_id
        self.task_name = task_name
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dataset_path is not None:
            result['DatasetPath'] = self.dataset_path

        if self.eval_dataset_path is not None:
            result['EvalDatasetPath'] = self.eval_dataset_path

        if self.kube_type is not None:
            result['KubeType'] = self.kube_type

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_source is not None:
            result['ModelSource'] = self.model_source

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.running_parameter is not None:
            result['RunningParameter'] = self.running_parameter

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DatasetPath') is not None:
            self.dataset_path = m.get('DatasetPath')

        if m.get('EvalDatasetPath') is not None:
            self.eval_dataset_path = m.get('EvalDatasetPath')

        if m.get('KubeType') is not None:
            self.kube_type = m.get('KubeType')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RunningParameter') is not None:
            self.running_parameter = m.get('RunningParameter')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

