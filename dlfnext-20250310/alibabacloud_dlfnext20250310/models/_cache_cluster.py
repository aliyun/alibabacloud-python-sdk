# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class CacheCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        created_at: int = None,
        created_by: str = None,
        deploy_instance_version: str = None,
        deploy_options_version: int = None,
        instance_version: str = None,
        options: Dict[str, str] = None,
        options_version: int = None,
        status: str = None,
        updated_at: int = None,
        updated_by: str = None,
        v_switches: List[main_models.CacheClusterVSwitches] = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.created_at = created_at
        self.created_by = created_by
        self.deploy_instance_version = deploy_instance_version
        self.deploy_options_version = deploy_options_version
        self.instance_version = instance_version
        self.options = options
        self.options_version = options_version
        self.status = status
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.v_switches = v_switches
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.deploy_instance_version is not None:
            result['deployInstanceVersion'] = self.deploy_instance_version

        if self.deploy_options_version is not None:
            result['deployOptionsVersion'] = self.deploy_options_version

        if self.instance_version is not None:
            result['instanceVersion'] = self.instance_version

        if self.options is not None:
            result['options'] = self.options

        if self.options_version is not None:
            result['optionsVersion'] = self.options_version

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        result['vSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['vSwitches'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('deployInstanceVersion') is not None:
            self.deploy_instance_version = m.get('deployInstanceVersion')

        if m.get('deployOptionsVersion') is not None:
            self.deploy_options_version = m.get('deployOptionsVersion')

        if m.get('instanceVersion') is not None:
            self.instance_version = m.get('instanceVersion')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('optionsVersion') is not None:
            self.options_version = m.get('optionsVersion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        self.v_switches = []
        if m.get('vSwitches') is not None:
            for k1 in m.get('vSwitches'):
                temp_model = main_models.CacheClusterVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self



class CacheClusterVSwitches(DaraModel):
    def __init__(
        self,
        v_switch_id: str = None,
        zone: str = None,
    ):
        self.v_switch_id = v_switch_id
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.zone is not None:
            result['zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('zone') is not None:
            self.zone = m.get('zone')

        return self

