# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GenerateK8sAccessInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GenerateK8sAccessInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GenerateK8sAccessInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateK8sAccessInfoResponseBodyData(DaraModel):
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
        install_key: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The Simple Log Service Logstore that is used to store the audit logs.
        self.audit_log_store = audit_log_store
        # The Simple Log Service project that is used to store the audit logs.
        self.audit_project = audit_project
        # The ID of the region in which the server is deployed.
        self.audit_region_id = audit_region_id
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # CPU architectures are divided into ARM architecture and x86 architecture.
        self.cpu_arch = cpu_arch
        # The expiration time. Unit: milliseconds.
        self.expire_date = expire_date
        # The server group ID.
        self.group_id = group_id
        # The installation key of the server.
        self.install_key = install_key

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

        if self.install_key is not None:
            result['InstallKey'] = self.install_key

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

        if m.get('InstallKey') is not None:
            self.install_key = m.get('InstallKey')

        return self

