# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListK8sAccessInfoResponseBody(DaraModel):
    def __init__(
        self,
        k_8s_access_infos: List[main_models.ListK8sAccessInfoResponseBodyK8sAccessInfos] = None,
        request_id: str = None,
    ):
        # The information about the Kubernetes clusters.
        self.k_8s_access_infos = k_8s_access_infos
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.k_8s_access_infos:
            for v1 in self.k_8s_access_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['K8sAccessInfos'] = []
        if self.k_8s_access_infos is not None:
            for k1 in self.k_8s_access_infos:
                result['K8sAccessInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.k_8s_access_infos = []
        if m.get('K8sAccessInfos') is not None:
            for k1 in m.get('K8sAccessInfos'):
                temp_model = main_models.ListK8sAccessInfoResponseBodyK8sAccessInfos()
                self.k_8s_access_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListK8sAccessInfoResponseBodyK8sAccessInfos(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        audit_log_store: str = None,
        audit_project: str = None,
        audit_region_id: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cpu_arch: str = None,
        expire_date: int = None,
        group_id: str = None,
        group_name: str = None,
        id: int = None,
        install_key: str = None,
        vendor: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The Simple Log Service Logstore that is used to store the audit logs.
        self.audit_log_store = audit_log_store
        # The Simple Log Service project that is used to store the audit logs.
        self.audit_project = audit_project
        # The ID of the region in which the server is deployed.
        self.audit_region_id = audit_region_id
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # CPU architecture, divided into ARM and x86 architectures.
        self.cpu_arch = cpu_arch
        # The expiration time.
        self.expire_date = expire_date
        # The ID of the server group.
        self.group_id = group_id
        # The name of the server group.
        self.group_name = group_name
        # The UUID of the access information.
        self.id = id
        # The installation key of the Kubernetes cluster.
        self.install_key = install_key
        # The service provider.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.audit_log_store is not None:
            result['AuditLogStore'] = self.audit_log_store

        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project

        if self.audit_region_id is not None:
            result['AuditRegionId'] = self.audit_region_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cpu_arch is not None:
            result['CpuArch'] = self.cpu_arch

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.install_key is not None:
            result['InstallKey'] = self.install_key

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AuditLogStore') is not None:
            self.audit_log_store = m.get('AuditLogStore')

        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')

        if m.get('AuditRegionId') is not None:
            self.audit_region_id = m.get('AuditRegionId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CpuArch') is not None:
            self.cpu_arch = m.get('CpuArch')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstallKey') is not None:
            self.install_key = m.get('InstallKey')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

