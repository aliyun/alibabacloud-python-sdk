# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GrafanaWorkspace(DaraModel):
    def __init__(
        self,
        commercial: bool = None,
        deploy_type: str = None,
        description: str = None,
        end_time: float = None,
        gmt_create: float = None,
        grafana_version: str = None,
        grafana_workspace_domain: str = None,
        grafana_workspace_domain_status: str = None,
        grafana_workspace_edition: str = None,
        grafana_workspace_id: str = None,
        grafana_workspace_ip: str = None,
        grafana_workspace_name: str = None,
        max_account: str = None,
        ntm_id: str = None,
        personal_domain: str = None,
        personal_domain_prefix: str = None,
        private_domain: str = None,
        private_ip: str = None,
        protocol: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_synced: bool = None,
        snat_ip: str = None,
        status: str = None,
        tags: List[main_models.GrafanaWorkspaceTags] = None,
        upgrade_version: List[str] = None,
        user_id: str = None,
    ):
        self.commercial = commercial
        self.deploy_type = deploy_type
        self.description = description
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.grafana_version = grafana_version
        self.grafana_workspace_domain = grafana_workspace_domain
        self.grafana_workspace_domain_status = grafana_workspace_domain_status
        self.grafana_workspace_edition = grafana_workspace_edition
        self.grafana_workspace_id = grafana_workspace_id
        self.grafana_workspace_ip = grafana_workspace_ip
        self.grafana_workspace_name = grafana_workspace_name
        self.max_account = max_account
        self.ntm_id = ntm_id
        self.personal_domain = personal_domain
        self.personal_domain_prefix = personal_domain_prefix
        self.private_domain = private_domain
        self.private_ip = private_ip
        self.protocol = protocol
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.share_synced = share_synced
        self.snat_ip = snat_ip
        self.status = status
        self.tags = tags
        self.upgrade_version = upgrade_version
        self.user_id = user_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commercial is not None:
            result['commercial'] = self.commercial

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.grafana_version is not None:
            result['grafanaVersion'] = self.grafana_version

        if self.grafana_workspace_domain is not None:
            result['grafanaWorkspaceDomain'] = self.grafana_workspace_domain

        if self.grafana_workspace_domain_status is not None:
            result['grafanaWorkspaceDomainStatus'] = self.grafana_workspace_domain_status

        if self.grafana_workspace_edition is not None:
            result['grafanaWorkspaceEdition'] = self.grafana_workspace_edition

        if self.grafana_workspace_id is not None:
            result['grafanaWorkspaceId'] = self.grafana_workspace_id

        if self.grafana_workspace_ip is not None:
            result['grafanaWorkspaceIp'] = self.grafana_workspace_ip

        if self.grafana_workspace_name is not None:
            result['grafanaWorkspaceName'] = self.grafana_workspace_name

        if self.max_account is not None:
            result['maxAccount'] = self.max_account

        if self.ntm_id is not None:
            result['ntmId'] = self.ntm_id

        if self.personal_domain is not None:
            result['personalDomain'] = self.personal_domain

        if self.personal_domain_prefix is not None:
            result['personalDomainPrefix'] = self.personal_domain_prefix

        if self.private_domain is not None:
            result['privateDomain'] = self.private_domain

        if self.private_ip is not None:
            result['privateIp'] = self.private_ip

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.share_synced is not None:
            result['shareSynced'] = self.share_synced

        if self.snat_ip is not None:
            result['snatIp'] = self.snat_ip

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.upgrade_version is not None:
            result['upgradeVersion'] = self.upgrade_version

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commercial') is not None:
            self.commercial = m.get('commercial')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('grafanaVersion') is not None:
            self.grafana_version = m.get('grafanaVersion')

        if m.get('grafanaWorkspaceDomain') is not None:
            self.grafana_workspace_domain = m.get('grafanaWorkspaceDomain')

        if m.get('grafanaWorkspaceDomainStatus') is not None:
            self.grafana_workspace_domain_status = m.get('grafanaWorkspaceDomainStatus')

        if m.get('grafanaWorkspaceEdition') is not None:
            self.grafana_workspace_edition = m.get('grafanaWorkspaceEdition')

        if m.get('grafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('grafanaWorkspaceId')

        if m.get('grafanaWorkspaceIp') is not None:
            self.grafana_workspace_ip = m.get('grafanaWorkspaceIp')

        if m.get('grafanaWorkspaceName') is not None:
            self.grafana_workspace_name = m.get('grafanaWorkspaceName')

        if m.get('maxAccount') is not None:
            self.max_account = m.get('maxAccount')

        if m.get('ntmId') is not None:
            self.ntm_id = m.get('ntmId')

        if m.get('personalDomain') is not None:
            self.personal_domain = m.get('personalDomain')

        if m.get('personalDomainPrefix') is not None:
            self.personal_domain_prefix = m.get('personalDomainPrefix')

        if m.get('privateDomain') is not None:
            self.private_domain = m.get('privateDomain')

        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('shareSynced') is not None:
            self.share_synced = m.get('shareSynced')

        if m.get('snatIp') is not None:
            self.snat_ip = m.get('snatIp')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GrafanaWorkspaceTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('upgradeVersion') is not None:
            self.upgrade_version = m.get('upgradeVersion')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self



class GrafanaWorkspaceTags(DaraModel):
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

