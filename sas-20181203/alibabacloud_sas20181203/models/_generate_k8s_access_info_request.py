# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateK8sAccessInfoRequest(DaraModel):
    def __init__(
        self,
        aliyun_yundun_gateway_api_name: str = None,
        aliyun_yundun_gateway_pop_name: str = None,
        aliyun_yundun_gateway_project_name: str = None,
        audit_log_store: str = None,
        audit_project: str = None,
        audit_region_id: str = None,
        cluster_name: str = None,
        cpu_arch: str = None,
        expire_date: int = None,
        group_id: int = None,
        vendor: str = None,
    ):
        # This parameter is deprecated and does not need to be specified.
        self.aliyun_yundun_gateway_api_name = aliyun_yundun_gateway_api_name
        # This parameter is deprecated and does not need to be specified.
        self.aliyun_yundun_gateway_pop_name = aliyun_yundun_gateway_pop_name
        # This parameter is deprecated and does not need to be specified.
        self.aliyun_yundun_gateway_project_name = aliyun_yundun_gateway_project_name
        # The SLS Logstore of the audit log.
        self.audit_log_store = audit_log_store
        # The SLS project of the audit log.
        self.audit_project = audit_project
        # The region of the audit log.
        self.audit_region_id = audit_region_id
        # The name of the Kubernetes cluster.
        # 
        # This parameter is required.
        self.cluster_name = cluster_name
        # The CPU architecture, which can be ARM or x86.
        self.cpu_arch = cpu_arch
        # The expiration time for container access.
        # 
        # This parameter is required.
        self.expire_date = expire_date
        # The queried group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The cloud asset vendor. Valid values:
        # - **Tencent**
        # - **HUAWEICLOUD**
        # - **Azure**
        # - **AWS** 
        # - **Other cloud assets**
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_yundun_gateway_api_name is not None:
            result['AliyunYundunGatewayApiName'] = self.aliyun_yundun_gateway_api_name

        if self.aliyun_yundun_gateway_pop_name is not None:
            result['AliyunYundunGatewayPopName'] = self.aliyun_yundun_gateway_pop_name

        if self.aliyun_yundun_gateway_project_name is not None:
            result['AliyunYundunGatewayProjectName'] = self.aliyun_yundun_gateway_project_name

        if self.audit_log_store is not None:
            result['AuditLogStore'] = self.audit_log_store

        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project

        if self.audit_region_id is not None:
            result['AuditRegionId'] = self.audit_region_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cpu_arch is not None:
            result['CpuArch'] = self.cpu_arch

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunYundunGatewayApiName') is not None:
            self.aliyun_yundun_gateway_api_name = m.get('AliyunYundunGatewayApiName')

        if m.get('AliyunYundunGatewayPopName') is not None:
            self.aliyun_yundun_gateway_pop_name = m.get('AliyunYundunGatewayPopName')

        if m.get('AliyunYundunGatewayProjectName') is not None:
            self.aliyun_yundun_gateway_project_name = m.get('AliyunYundunGatewayProjectName')

        if m.get('AuditLogStore') is not None:
            self.audit_log_store = m.get('AuditLogStore')

        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')

        if m.get('AuditRegionId') is not None:
            self.audit_region_id = m.get('AuditRegionId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CpuArch') is not None:
            self.cpu_arch = m.get('CpuArch')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

