# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceUsageResponseBody(DaraModel):
    def __init__(
        self,
        chart_namespace_quota: str = None,
        chart_namespace_usage: str = None,
        chart_repo_quota: str = None,
        chart_repo_usage: str = None,
        code: str = None,
        is_success: bool = None,
        namespace_quota: str = None,
        namespace_usage: str = None,
        repo_quota: str = None,
        repo_usage: str = None,
        request_id: str = None,
        vpc_quota: str = None,
        vpc_usage: str = None,
    ):
        # The quota of chart namespaces.
        self.chart_namespace_quota = chart_namespace_quota
        # The number of chart namespaces that are created in the instance.
        self.chart_namespace_usage = chart_namespace_usage
        # The quota of chart repositories for the instance.
        self.chart_repo_quota = chart_repo_quota
        # The number of chart repositories that are created.
        self.chart_repo_usage = chart_repo_usage
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The quota of image namespaces for the instance.
        self.namespace_quota = namespace_quota
        # The number of image namespaces that are created in the instance.
        self.namespace_usage = namespace_usage
        # The quota of image repositories for the instance.
        self.repo_quota = repo_quota
        # The number of image repositories that are created in the instance.
        self.repo_usage = repo_usage
        # The ID of the request.
        self.request_id = request_id
        # VPC quota
        self.vpc_quota = vpc_quota
        # Number of bound VPCs
        self.vpc_usage = vpc_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart_namespace_quota is not None:
            result['ChartNamespaceQuota'] = self.chart_namespace_quota

        if self.chart_namespace_usage is not None:
            result['ChartNamespaceUsage'] = self.chart_namespace_usage

        if self.chart_repo_quota is not None:
            result['ChartRepoQuota'] = self.chart_repo_quota

        if self.chart_repo_usage is not None:
            result['ChartRepoUsage'] = self.chart_repo_usage

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.namespace_quota is not None:
            result['NamespaceQuota'] = self.namespace_quota

        if self.namespace_usage is not None:
            result['NamespaceUsage'] = self.namespace_usage

        if self.repo_quota is not None:
            result['RepoQuota'] = self.repo_quota

        if self.repo_usage is not None:
            result['RepoUsage'] = self.repo_usage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpc_quota is not None:
            result['VpcQuota'] = self.vpc_quota

        if self.vpc_usage is not None:
            result['VpcUsage'] = self.vpc_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChartNamespaceQuota') is not None:
            self.chart_namespace_quota = m.get('ChartNamespaceQuota')

        if m.get('ChartNamespaceUsage') is not None:
            self.chart_namespace_usage = m.get('ChartNamespaceUsage')

        if m.get('ChartRepoQuota') is not None:
            self.chart_repo_quota = m.get('ChartRepoQuota')

        if m.get('ChartRepoUsage') is not None:
            self.chart_repo_usage = m.get('ChartRepoUsage')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('NamespaceQuota') is not None:
            self.namespace_quota = m.get('NamespaceQuota')

        if m.get('NamespaceUsage') is not None:
            self.namespace_usage = m.get('NamespaceUsage')

        if m.get('RepoQuota') is not None:
            self.repo_quota = m.get('RepoQuota')

        if m.get('RepoUsage') is not None:
            self.repo_usage = m.get('RepoUsage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpcQuota') is not None:
            self.vpc_quota = m.get('VpcQuota')

        if m.get('VpcUsage') is not None:
            self.vpc_usage = m.get('VpcUsage')

        return self

